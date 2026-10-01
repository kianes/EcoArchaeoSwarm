# EcoArchaeoSwarm — Minimum Viable Prototype
 
## 1. MVP Definition
 
The Minimum Viable Prototype of EcoArchaeoSwarm is a small multi-robot system designed to demonstrate the core decision-making loop of the project in a controlled environment.
 
The MVP does not attempt to perform real-world ecosystem restoration at full scale.
 
Instead, it demonstrates that a small swarm can:
 
1. Observe environmental conditions
2. Build a shared representation of the environment
3. Identify areas requiring attention
4. Prioritize tasks
5. Allocate tasks between robots
6. Respect protected zones
7. Execute a controlled action
8. Monitor the result
9. Update future decisions

 
The MVP therefore focuses on proving the system architecture rather than maximizing hardware complexity.
 
***
 
## 2. MVP Objective
 
The primary objective is to demonstrate the following closed-loop process:
 
```text
Observe
   ↓
Map
   ↓
Analyze
   ↓
Prioritize
   ↓
Allocate
   ↓
Act
   ↓
Monitor
   ↓
Adapt
```
 
The prototype should demonstrate that these stages can operate together as one system.
 
***
 
## 3. MVP Scenario
 
The initial test environment represents a simplified degraded landscape.
 
The environment contains several different areas:
 
```text
┌────┬────┬────┬────┬────┬────┐
│    │    │ P  │ P  │    │    │
├────┼────┼────┼────┼────┼────┤
│ D  │ D  │ B  │ B  │ R  │ R  │
├────┼────┼────┼────┼────┼────┤
│ D  │ D  │ B  │ R  │ R  │ R  │
├────┼────┼────┼────┼────┼────┤
│    │    │    │ R  │ D  │ D  │
├────┼────┼────┼────┼────┼────┤
│    │    │    │    │    │    │
└────┴────┴────┴────┴────┴────┘

D = Degraded Area
R = Restoration Zone
B = Buffer Zone
P = Protected Zone
```
 
The robots must explore the environment, collect observations, identify high-priority areas, and perform approved tasks without entering protected zones.
 
***
 
## 4. Number of Robots
 
The first physical prototype will use two robots.
 
### Robot A
 
Primary capability:
 
Environmental sensing
 
Potential tasks:
 
- Environmental mapping
- Soil measurement
- Temperature measurement
- Light measurement
- Visual observation

 
### Robot B
 
Primary capability:
 
Intervention
 
Potential tasks:
 
- Seed placement
- Micro-watering
- Follow-up environmental measurement

 
The two robots should still remain capable of performing basic common tasks.
 
This prevents the architecture from becoming dependent on fixed robot identities.
 
A third robot can be introduced after the two-robot system is stable.
 
***
 
## 5. Robot Design Philosophy
 
The robots should be modular.
 
Each robot consists of a common base platform with optional payload modules.
 
```text
             COMMON ROBOT BASE
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
    Sensors      Controller    Mobility
       │
       ▼
   Payload Bay
       │
   ┌───┴───────────┐
   │               │
   ▼               ▼
Seed Module    Water Module
```
 
This allows the same robot platform to be reused for different experiments.
 
***
 
## 6. Hardware Requirements
 
The initial physical prototype may use the following components.
 
### Main Controller
 
ESP32-class microcontroller.
 
Responsibilities:
 
- Sensor acquisition
- Motor control
- Wireless communication
- Local state management
- Task execution

 
### Mobility
 
- Two DC geared motors
- Motor driver
- Two-wheel differential-drive chassis
- Caster wheel
- Wheel encoders if available

 
### Environmental Sensors
 
Initial sensors:
 
- Soil moisture
- Temperature
- Humidity
- Light

 
### Motion Sensors
 
- IMU
- Wheel encoders

 
### Visual Sensor
 
A small camera may be added after the basic robot platform is operational.
 
Computer vision should not be required for the first successful MVP demonstration.
 
***
 
## 7. Communication
 
The robots must exchange information wirelessly.
 
The initial prototype can use a lightweight communication mechanism such as:
 
- ESP-NOW
- Wi-Fi
- Bluetooth

 
The first implementation should prioritize reliability and simplicity rather than long-range communication.
 
The communication system should support messages such as:
 
```text
ROBOT_STATUS
SENSOR_DATA
TASK_ASSIGNMENT
TASK_COMPLETE
TASK_FAILED
MAP_UPDATE
RESOURCE_STATUS
EMERGENCY_STOP
```
 
***
 
## 8. Robot State Model
 
Each robot should maintain a structured state.
 
Example:
 
```text
RobotState
│
├── robot_id
├── position
├── orientation
├── battery
├── current_task
├── sensor_status
├── payload_type
├── payload_level
├── communication_status
└── fault_status
```
 
The state is periodically transmitted to the swarm coordination layer.
 
***
 
## 9. Environmental Data Model
 
Each environmental observation should contain at least:
 
```text
Observation
│
├── position
├── timestamp
├── soil_moisture
├── temperature
├── humidity
├── light
└── confidence
```
 
If a camera is available, visual observations can later be added.
 
The system should preserve timestamps so that environmental conditions can be compared over time.
 
***
 
## 10. Shared Map
 
The first MVP will use a grid-based map.
 
Each grid cell can contain:
 
```text
Cell
│
├── zone_type
├── soil_moisture
├── temperature
├── humidity
├── light
├── vegetation_score
├── restoration_priority
├── observation_count
└── confidence
```
 
The map should be updated whenever a robot contributes new information.
 
This allows the swarm to gradually improve its understanding of the environment.
 
***
 
## 11. Restoration Priority
 
The first MVP should not rely on a complex Machine Learning model to determine restoration priority.
 
Instead, an explainable scoring system will be used.
 
A simplified priority model may consider:
 
```text
Restoration Priority =
Environmental Need
+
Restoration Suitability
+
Resource Feasibility
-
Operational Risk
```
 
For example, a location may receive a higher priority when:
 
- Soil moisture is low
- Vegetation condition is poor
- The area is inside an allowed restoration zone
- A suitable robot is nearby
- Required resources are available

 
A protected archaeological zone should result in an intervention priority of zero.
 
***
 
## 12. Task Model
 
The swarm operates using explicit tasks.
 
Example:
 
```text
Task
│
├── task_id
├── task_type
├── target_position
├── priority
├── required_capabilities
├── required_payload
├── estimated_energy
├── estimated_duration
└── status
```
 
Possible task types include:
 
- SURVEY
- SOIL_MEASUREMENT
- VISUAL_INSPECTION
- SEED_PLACEMENT
- MICRO_WATERING
- REASSESSMENT

 
***
 
## 13. Task Allocation
 
Task allocation is one of the core demonstrations of the MVP.
 
Suppose the system creates three tasks:
 
```text
Task 1 → Environmental Survey
Task 2 → Seed Placement
Task 3 → Reassessment
```
 
The system evaluates:
 
```text
Robot Position
+
Battery
+
Current Workload
+
Required Capability
+
Payload Availability
+
Distance
+
Zone Constraints
```
 
The task is then assigned to an appropriate robot.
 
This demonstrates that the swarm is making decisions based on system state rather than following a fixed sequence.
 
***
 
## 14. Protected-Zone Handling
 
Protected zones are represented as hard constraints.
 
For example:
 
```text
Protected Zone
       │
       ▼
Navigation Constraint
       │
       ├── No Entry
       ├── No Intervention
       └── No Task Assignment
```
 
If a planned path crosses a protected zone, the navigation system must reject or modify the path.
 
If a task target is located inside a protected zone, the task must not be generated as an intervention task.
 
***
 
## 15. Resource Model
 
The MVP will simulate limited resources.
 
The initial resource types are:
 
### Water
 
Example:
 
```text
Initial Water = 100 units
```
 
Each micro-watering operation consumes a defined amount.
 
### Seeds
 
Example:
 
```text
Initial Seeds = 50 units
```
 
Each seed-placement operation consumes a defined amount.
 
### Battery
 
Each robot has a finite energy level.
 
### Time
 
Each task has an estimated duration.
 
The AI planning layer should consider resource availability before assigning an intervention.
 
***
 
## 16. Intervention Mechanism
 
The first physical intervention mechanism should remain simple.
 
Two possible modules are:
 
### Micro-Watering
 
A small pump delivers a controlled amount of water.
 
### Seed Dispensing
 
A simple mechanism releases a controlled number of seeds.
 
Only one intervention mechanism is required for the first physical demonstration.
 
The choice should be based on:
 
- Mechanical complexity
- Cost
- Reliability
- Safety
- Ease of measurement

 
***
 
## 17. Outcome Monitoring
 
The system should not stop after performing an intervention.
 
The robot returns to the target area later and collects another observation.
 
The system then compares:
 
```text
Before Intervention
        │
        ▼
Environmental State
        │
        │
   Intervention
        │
        ▼
After Intervention
        │
        ▼
Environmental Comparison
```
 
The purpose of the first MVP is not to prove long-term ecological success.
 
Instead, it demonstrates the technical capability to measure environmental change and feed that information back into the planning system.
 
***
 
## 18. AI Agent in the MVP
 
The AI Agent should initially perform a limited set of responsibilities.
 
### Input
 
```text
Environmental Map
Robot States
Available Resources
Protected Zones
Task History
Expert Rules
```
 
### Processing
 
```text
Assess Environment
       ↓
Estimate Priority
       ↓
Generate Tasks
       ↓
Evaluate Robot Candidates
       ↓
Allocate Resources
       ↓
Recommend Actions
```
 
### Output
 
```text
Task Plan
+
Robot Assignments
+
Resource Allocation
+
Reason for Decision
```
 
The explanation associated with each decision is important.
 
For example:
 
```text
Target: Cell (7,4)

Priority: HIGH

Reason:
Low soil moisture
+
High degradation score
+
Allowed restoration zone
+
Suitable robot available
```
 
***
 
## 19. AI Implementation Strategy
 
The MVP will use a hybrid approach.
 
### Rule-Based Logic
 
Used for:
 
- Safety constraints
- Protected zones
- Hard resource limits
- Basic environmental thresholds

 
### Optimization
 
Used for:
 
- Task allocation
- Resource allocation
- Route selection

 
### Machine Learning
 
Introduced only where sufficient data exists and where it provides measurable value.
 
Potential future applications include:
 
- Vegetation classification
- Environmental prediction
- Restoration outcome prediction
- Adaptive task allocation

 
This prevents the project from using AI simply for the sake of adding AI.
 
***
 
## 20. Dashboard
 
The MVP should include a simple monitoring dashboard.
 
The dashboard may display:
 
```text
┌─────────────────────────────────┐
│        EcoArchaeoSwarm          │
├─────────────────────────────────┤
│                                 │
│          ENVIRONMENT MAP        │
│                                 │
│      🤖A          🏺            │
│              🤖B                │
│                                 │
├─────────────────────────────────┤
│ Robot A   Battery: 82%          │
│ Robot B   Battery: 67%          │
│                                 │
│ Water: 64%                      │
│ Seeds: 38                       │
│                                 │
│ Active Task: Robot B → Watering│
└─────────────────────────────────┘
```
 
The dashboard is primarily intended for system observation and debugging during development.
 
***
 
## 21. Simulation Before Hardware
 
The first implementation should be developed in simulation.
 
The simulation will contain:
 
- Virtual environment
- Multiple robots
- Environmental variables
- Protected zones
- Resources
- Tasks
- Robot states
- Task allocation
- Navigation
- AI planning

 
The simulation allows the core algorithms to be tested before physical hardware is introduced.
 
***
 
## 22. Hardware-in-the-Loop
 
After simulation, real Embedded hardware can be connected to the software system.
 
For example:
 
```text
Simulation Environment
        │
        ▼
   AI / Swarm Logic
        │
        ▼
      ESP32
        │
        ▼
   Real Motors
   Real Sensors
```
 
This stage allows firmware and higher-level algorithms to be tested together.
 
***
 
## 23. Physical MVP
 
The first physical demonstration should contain:
 
### Two Robots
 
Each robot should have:
 
- ESP32
- Differential-drive chassis
- Motor driver
- Environmental sensors
- Wireless communication
- Battery

 
### One Intervention Module
 
Either:
 
- Micro-watering

 
or:
 
- Seed dispensing

 
### One Controlled Environment
 
A small test area containing:
 
- Degraded areas
- Restoration areas
- Protected areas
- Obstacles
- Limited resources

 
***
 
## 24. MVP Demonstration Scenario
 
The complete demonstration can follow this sequence:
 
### Step 1
 
Robots begin with incomplete knowledge of the environment.
 
### Step 2
 
Robots explore the environment.
 
### Step 3
 
Environmental observations are added to the shared map.
 
### Step 4
 
The AI planning layer identifies a high-priority restoration area.
 
### Step 5
 
The system checks:
 
- Protected zones
- Robot battery
- Robot capabilities
- Available resources
- Distance

 
### Step 6
 
A task is generated.
 
### Step 7
 
The appropriate robot receives the task.
 
### Step 8
 
The robot navigates to the target while respecting protected zones.
 
### Step 9
 
The robot performs the controlled intervention.
 
### Step 10
 
The intervention is recorded.
 
### Step 11
 
The robot later reassesses the location.
 
### Step 12
 
The new observation is added to the shared map.
 
### Step 13
 
The AI planning layer updates the environmental assessment.
 
This completes the first closed-loop demonstration.
 
***
 
## 25. MVP Success Criteria
 
The MVP will be considered technically successful if it can demonstrate:
 
### Multi-Robot Operation
 
At least two robots can operate within the same environment.
 
### Shared Information
 
Robots can contribute information to a common system state.
 
### Environmental Mapping
 
The system can construct and update a basic environmental map.
 
### Task Allocation
 
The system can assign tasks based on robot state and task requirements.
 
### Protected-Zone Avoidance
 
Robots can avoid defined protected areas.
 
### Resource Awareness
 
The system accounts for limited resources.
 
### Controlled Intervention
 
At least one physical or simulated intervention can be executed.
 
### Outcome Monitoring
 
The system can collect a second observation after intervention.
 
### Adaptive Planning
 
The updated observation can influence subsequent planning.
 
***
 
## 26. What the MVP Proves
 
The MVP is intended to prove the following concept:
 
> A small group of autonomous robots can collaboratively collect environmental information and use AI-assisted planning to coordinate resource-aware ecological restoration tasks while respecting spatial protection constraints.

 
The MVP does not claim to prove that autonomous robots can restore ecosystems.
 
It demonstrates the technical architecture required to investigate that larger problem.
 
***
 
## 27. Future Expansion
 
After the MVP, the system can be expanded with:
 
- More robots
- Better localization
- Advanced Computer Vision
- Vegetation classification
- Improved soil sensing
- Edge AI
- Machine Learning
- Reinforcement Learning
- Advanced Swarm Intelligence
- GIS integration
- Real archaeological datasets
- More sophisticated ecological models
- Multiple intervention modules
- Long-term environmental monitoring

 
The architecture is designed so these capabilities can be introduced incrementally.
 
***
 
## 28. MVP Development Sequence
 
The implementation will follow this sequence:
 
```text
1. Environment Simulation
        ↓
2. Single Robot Simulation
        ↓
3. Multi-Robot Simulation
        ↓
4. Shared Map
        ↓
5. Task Allocation
        ↓
6. Resource Constraints
        ↓
7. Protected Zones
        ↓
8. AI Planning Layer
        ↓
9. Single Physical Robot
        ↓
10. Two Physical Robots
        ↓
11. Intervention Module
        ↓
12. Closed-Loop Demonstration
```
 
Each stage should be tested before proceeding to the next.
 
***
 
## 29. Final MVP Definition
 
The EcoArchaeoSwarm MVP is a two-robot, resource-constrained, protected-zone-aware autonomous system capable of environmental observation, shared mapping, task allocation, controlled intervention, and outcome monitoring.
 
The system combines:
 
**Embedded Systems**
 
- 

 
**Mobile Robotics**
 
- 

 
**Swarm Coordination**
 
- 

 
**Artificial Intelligence**
 
- 

 
**Environmental Sensing**
 
- 

 
**Ecological Restoration**
 
- 

 
**Archaeological Protection**
 
into a single experimentally testable platform.
 
The MVP is intentionally limited in scope so that the core architecture can be implemented, measured, demonstrated, and iteratively improved.
