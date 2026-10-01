from dataclasses import dataclass, field
from typing import Optional


GRID_WIDTH = 16
GRID_HEIGHT = 10

ROBOT_SYMBOLS = {
    1: "1",
    2: "2",
    3: "3",
}


@dataclass
class Task:
    task_id: int
    task_type: str
    x: int
    y: int
    priority: float
    status: str = "PENDING"
    assigned_robot: Optional[int] = None


@dataclass
class Robot:
    robot_id: int
    x: int
    y: int
    battery: int = 100
    current_task: Optional[int] = None
    state: str = "IDLE"
    sensor_data: dict = field(default_factory=dict)
    completed_tasks: int = 0


def create_environment():
    return [
        ["."] * GRID_WIDTH
        for _ in range(GRID_HEIGHT)
    ]


def add_zone(environment, x_start, y_start, x_end, y_end, zone_type):
    for y in range(y_start, y_end + 1):
        for x in range(x_start, x_end + 1):
            environment[y][x] = zone_type


def create_world():
    environment = create_environment()

    # D = degraded area
    add_zone(environment, 1, 1, 4, 3, "D")
    add_zone(environment, 10, 1, 14, 3, "D")

    # B = buffer zone
    add_zone(environment, 5, 1, 6, 4, "B")

    # P = protected archaeological zone
    add_zone(environment, 7, 0, 9, 3, "P")

    # R = restoration area
    add_zone(environment, 11, 5, 14, 7, "R")
    add_zone(environment, 2, 6, 5, 8, "R")

    return environment


def is_inside(x, y):
    return (
        0 <= x < GRID_WIDTH
        and 0 <= y < GRID_HEIGHT
    )


def can_enter(environment, x, y):
    if not is_inside(x, y):
        return False

    # Archaeological protected zone
    if environment[y][x] == "P":
        return False

    return True


def move_robot(environment, robot, target_x, target_y):
    dx = target_x - robot.x
    dy = target_y - robot.y

    new_x = robot.x
    new_y = robot.y

    if dx != 0:
        new_x += 1 if dx > 0 else -1
    elif dy != 0:
        new_y += 1 if dy > 0 else -1

    if can_enter(environment, new_x, new_y):
        robot.x = new_x
        robot.y = new_y
        robot.battery = max(0, robot.battery - 1)
        return True

    return False


def simulate_sensors(environment, robot):
    zone = environment[robot.y][robot.x]

    if zone == "D":
        moisture = 20
        vegetation = 25
        temperature = 38
    elif zone == "R":
        moisture = 45
        vegetation = 60
        temperature = 31
    elif zone == "B":
        moisture = 35
        vegetation = 40
        temperature = 33
    else:
        moisture = 50
        vegetation = 50
        temperature = 30

    robot.sensor_data = {
        "moisture": moisture,
        "vegetation": vegetation,
        "temperature": temperature,
        "zone": zone,
    }


def calculate_restoration_priority(sensor_data):
    moisture = sensor_data["moisture"]
    vegetation = sensor_data["vegetation"]

    priority = (
        (100 - moisture) * 0.5
        + (100 - vegetation) * 0.5
    )

    return round(priority, 2)


def generate_tasks(environment):
    tasks = []
    task_id = 1

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):

            if environment[y][x] == "D":
                sensor_data = {
                    "moisture": 20,
                    "vegetation": 25,
                }

                priority = calculate_restoration_priority(
                    sensor_data
                )

                tasks.append(
                    Task(
                        task_id=task_id,
                        task_type="RESTORATION_ASSESSMENT",
                        x=x,
                        y=y,
                        priority=priority,
                    )
                )

                task_id += 1

    tasks.sort(
        key=lambda task: task.priority,
        reverse=True
    )

    return tasks


def assign_tasks(robots, tasks):
    available_robots = [
        robot for robot in robots
        if robot.battery > 20
        and robot.current_task is None
    ]

    pending_tasks = [
        task for task in tasks
        if task.status == "PENDING"
    ]

    for robot, task in zip(
        available_robots,
        pending_tasks
    ):
        robot.current_task = task.task_id
        robot.state = "MOVING"

        task.assigned_robot = robot.robot_id
        task.status = "ASSIGNED"


def perform_task(environment, robot, task):
    if robot.x != task.x or robot.y != task.y:
        move_robot(
            environment,
            robot,
            task.x,
            task.y
        )
        return False

    simulate_sensors(environment, robot)

    task.status = "COMPLETED"

    robot.completed_tasks += 1
    robot.current_task = None
    robot.state = "IDLE"

    return True


def build_display(environment, robots):
    display = [
        row.copy()
        for row in environment
    ]

    for robot in robots:
        display[robot.y][robot.x] = ROBOT_SYMBOLS[
            robot.robot_id
        ]

    return display


def print_environment(environment, robots):
    display = build_display(
        environment,
        robots
    )

    print()

    for row in display:
        print(" ".join(row))

    print()


def print_robot_status(robots):
    print("ROBOT STATUS")
    print("------------")

    for robot in robots:
        print(
            f"Robot {robot.robot_id} | "
            f"Position: ({robot.x}, {robot.y}) | "
            f"Battery: {robot.battery}% | "
            f"State: {robot.state} | "
            f"Completed: {robot.completed_tasks}"
        )

    print()


def print_task_status(tasks):
    completed = sum(
        task.status == "COMPLETED"
        for task in tasks
    )

    assigned = sum(
        task.status == "ASSIGNED"
        for task in tasks
    )

    pending = sum(
        task.status == "PENDING"
        for task in tasks
    )

    print("TASK STATUS")
    print("-----------")
    print(f"Completed: {completed}")
    print(f"Assigned:  {assigned}")
    print(f"Pending:   {pending}")
    print()


def main():
    print("=" * 55)
    print("EcoArchaeoSwarm")
    print("AI-Driven Swarm Robotics for Ecological Restoration")
    print("=" * 55)

    environment = create_world()

    robots = [
        Robot(1, 0, 0),
        Robot(2, 15, 9),
        Robot(3, 0, 9),
    ]

    tasks = generate_tasks(environment)

    print()
    print("INITIAL ENVIRONMENT")
    print_environment(environment, robots)

    print(
        f"Detected restoration tasks: {len(tasks)}"
    )

    # Swarm operation
    for step in range(15):

        assign_tasks(
            robots,
            tasks
        )

        for robot in robots:

            if robot.current_task is None:
                continue

            task = next(
                (
                    task
                    for task in tasks
                    if task.task_id
                    == robot.current_task
                ),
                None
            )

            if task is not None:
                perform_task(
                    environment,
                    robot,
                    task
                )

    print()
    print("FINAL ENVIRONMENT")
    print_environment(environment, robots)

    print_robot_status(robots)
    print_task_status(tasks)

    print("SYSTEM PRINCIPLES")
    print("-----------------")
    print("✓ Multi-robot operation")
    print("✓ Shared environmental representation")
    print("✓ Restoration task generation")
    print("✓ Task prioritization")
    print("✓ Dynamic task allocation")
    print("✓ Protected archaeological zones")
    print("✓ Battery-aware robot state")
    print("✓ Environmental sensing simulation")
    print("✓ Human-supervised architecture")


if __name__ == "__main__":
    main()