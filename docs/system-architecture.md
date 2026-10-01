# EcoArchaeoSwarm — System Architecture
 
## 1. Architecture Overview
 
EcoArchaeoSwarm is designed as a layered cyber-physical system combining environmental sensing, autonomous mobile robots, swarm coordination, AI-assisted planning, and human-defined ecological and archaeological constraints.
 
The system is divided into five primary layers:
 
1. Environmental Layer
2. Robot Layer
3. Swarm Layer
4. AI Layer
5. Human / Expert Layer

 
The layers interact continuously through environmental observations, robot state information, planning decisions, and operational feedback.
 
The overall architecture follows this loop:
 
**Observe → Analyze → Prioritize → Allocate → Act → Monitor → Adapt**
 
***
 
## 2. High-Level Architecture
 
```text
                    HUMAN / EXPERT LAYER
                            │
                            │
                  Ecological Constraints
                  Heritage Constraints
                  Safety Rules
                  Restoration Objectives
                            │
                            ▼
                     ┌─────────────┐
                     │  AI AGENT   │
                     │             │
                     │ Assessment  │
                     │ Priority    │
                     │ Allocation  │
                     │ Planning    │
                     └──────┬──────┘
                            │
                     Planning Decisions
                            │
                            ▼
                    ┌───────────────┐
                    │ SWARM LAYER   │
                    │               │
                    │ Coordination  │
                    │ Task Allocation│
                    │ Shared Map    │
                    │ Communication │
                    └───────┬───────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
         ┌─────────┐   ┌─────────┐   ┌─────────┐
         │ Robot A │   │ Robot B │   │ Robot C │
         │         │   │         │   │         │
         │ Sensors │   │ Sensors │   │ Sensors │
         │ Motors  │   │ Motors  │   │ Motors  │
         │ Payload │   │ Payload │   │ Payload │
         └────┬────┘   └────┬────┘   └────┬────┘
              │             │             │
              └─────────────┼─────────────┘
                            │
                            ▼
                  ENVIRONMENTAL LAYER
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
         Soil / Water   Vegetation      Terrain
         Conditions     Conditions      Conditions
```
 
***
 
## 3. Environmental Layer
 
The Environmental Layer represents the physical world in which the swarm operates.
 
It contains both measurable environmental variables and operational constraints.
 
### Environmental Variables
 
Potential variables include:
 
- Soil moisture
- Temperature
- Relative humidity
- Light intensity
- Vegetation density
- Vegetation condition
- Terrain characteristics
- Robot-accessible areas

 
### Operational Zones
 
The environment also contains spatial constraints:
 
- Protected Zones
- Buffer Zones
- Restoration Zones
- General Navigation Zones

 
These zones influence how robots are allowed to move and operate.
 
***
 
## 4. Environmental Representation
 
The initial MVP will represent the environment as a spatial grid.
 
Each cell may contain information such as:
 
```text
Cell
│
├── Position
├── Soil Moisture
├── Temperature
├── Light Level
├── Vegetation Estimate
├── Restoration Priority
├── Zone Type
└── Confidence
```
 
For example:
 
```text
┌────┬────┬────┬────┬────┐
│ R  │ R  │ B  │ P  │ P  │
├────┼────┼────┼────┼────┤
│ R  │ D  │ D  │ B  │ P  │
├────┼────┼────┼────┼────┤
│ R  │ D  │ D  │ R  │ R  │
├────┼────┼────┼────┼────┤
│ R  │ R  │ R  │ R  │ R  │
└────┴────┴────┴────┴────┘

R = Restoration Zone
D = Degraded Area
B = Buffer Zone
P = Protected Zone
```
 
The grid-based representation is intentionally simple for the MVP.
 
More advanced geographic representations can be introduced later.
 
***
 
## 5. Robot Layer
 
Each robot is an autonomous embedded system.
 
A robot contains five major subsystems:
 
1. Embedded Controller
2. Sensors
3. Mobility System
4. Communication
5. Modular Payload

 
### Robot Architecture
 
```text
                 ROBOT
                   │
        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
     SENSORS    CONTROLLER   COMMUNICATION
        │          │          │
        │          │          │
        ▼          ▼          ▼
 Environmental   Firmware   Swarm Data
    Data         Logic       Exchange
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
       MOTORS             PAYLOAD
          │                 │
          ▼                 ▼
      Movement       Seed / Water /
                     Additional Sensors
```
 
***
 
## 6. Embedded Controller
 
The Embedded Controller is responsible for real-time robot operation.
 
The initial prototype may use an ESP32-class microcontroller.
 
Responsibilities include:
 
- Reading sensors
- Controlling motors
- Managing battery information
- Controlling payload mechanisms
- Maintaining robot state
- Communicating with other system components
- Executing local safety rules
- Receiving and executing assigned tasks

 
The Embedded Controller should not be responsible for the complete global intelligence of the swarm.
 
Instead, the robot performs local execution while higher-level planning can be performed by the Swarm and AI layers.
 
***
 
## 7. Sensor Subsystem
 
The initial robot may contain:
 
### Environmental Sensors
 
- Soil moisture
- Temperature
- Humidity
- Light

 
### Motion Sensors
 
- IMU
- Wheel encoders

 
### Visual Sensor
 
- Camera

 
The sensor architecture should remain modular so that additional sensors can be added without redesigning the entire robot.
 
***
 
## 8. Mobility Subsystem
 
The initial robot platform will use differential drive.
 
The system consists of:
 
- Left motor
- Right motor
- Motor driver
- Wheels
- Optional caster wheel
- Wheel encoders

 
Differential drive allows the robot to:
 
- Move forward
- Move backward
- Turn left
- Turn right
- Rotate approximately in place

 
This configuration is simple enough for the first prototype while providing sufficient mobility for swarm experiments.
 
***
 
## 9. Communication Subsystem
 
Communication allows robots and higher-level systems to exchange information.
 
The communication architecture may include:
 
```text
Robot A ─────┐
             │
Robot B ─────┼──── Communication Network
             │
Robot C ─────┘
             │
             ▼
       Shared System State
```
 
The initial prototype may use wireless communication suitable for short-range experiments.
 
Potential technologies include:
 
- Wi-Fi
- ESP-NOW
- Bluetooth
- Other lightweight wireless protocols

 
The final protocol will be selected according to range, power consumption, reliability, and system complexity.
 
***
 
## 10. Robot State
 
Each robot maintains a local state representation.
 
A simplified robot state may contain:
 
```text
Robot State
│
├── Robot ID
├── Position
├── Orientation
├── Battery Level
├── Current Task
├── Sensor Status
├── Payload Type
├── Payload Availability
├── Communication Status
└── Fault Status
```
 
The swarm uses this information when assigning tasks.
 
For example, a robot with low battery should not receive a distant intervention task if another suitable robot is available.
 
***
 
## 11. Swarm Layer
 
The Swarm Layer coordinates multiple robots.
 
Its primary responsibilities are:
 
- Shared environmental information
- Robot state management
- Task allocation
- Multi-robot coordination
- Collision avoidance
- Workload distribution
- Communication management

 
The swarm should avoid unnecessary duplication.
 
For example, if Robot A has already mapped an area, Robot B should not automatically repeat the same mapping task unless additional information is required.
 
***
 
## 12. Shared Map
 
The swarm maintains a shared representation of the environment.
 
Each robot contributes local observations.
 
```text
Robot A ──┐
          │
Robot B ──┼──► Shared Environmental Map
          │
Robot C ──┘
```
 
The map may contain:
 
- Environmental measurements
- Robot positions
- Restoration priorities
- Protected zones
- Buffer zones
- Completed tasks
- Unexplored areas
- Confidence levels

 
The shared map becomes one of the main information sources for the AI planning layer.
 
***
 
## 13. Task Allocation
 
Task allocation determines which robot should perform a particular task.
 
A task may include:
 
```text
Task
│
├── Task Type
├── Target Location
├── Priority
├── Required Capability
├── Required Payload
├── Estimated Energy
└── Deadline / Time Constraint
```
 
Example tasks include:
 
- Environmental scan
- Detailed soil measurement
- Visual inspection
- Seed placement
- Micro-watering
- Reassessment

 
The allocation system evaluates available robots and selects an appropriate assignment.
 
***
 
## 14. Task Allocation Example
 
Assume the system identifies a high-priority degraded location.
 
Three robots are available:
 
```text
Robot A
Distance: Short
Battery: High
Payload: Sensor

Robot B
Distance: Medium
Battery: High
Payload: Seed

Robot C
Distance: Long
Battery: Low
Payload: Water
```
 
The system may assign:
 
```text
Robot A → Detailed sensing

Robot B → Seed intervention

Robot C → No assignment
```
 
The decision is based on multiple constraints rather than distance alone.
 
***
 
## 15. AI Layer
 
The AI Layer operates above the basic swarm coordination mechanisms.
 
Its purpose is to convert environmental and robot-state information into higher-level planning decisions.
 
The AI Agent receives:
 
```text
Environmental Data
+
Robot States
+
Shared Map
+
Resource Availability
+
Ecological Rules
+
Archaeological Constraints
```
 
and produces:
 
```text
Priority Decisions
+
Task Recommendations
+
Resource Allocation
+
Planning Decisions
```
 
***
 
## 16. AI Agent Architecture
 
The AI Agent can be divided into several functional modules.
 
```text
                 AI AGENT
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
 Environmental   Restoration   Constraint
 Assessment      Priority      Handling
        │            │            │
        └────────────┼────────────┘
                     │
                     ▼
              Resource Planning
                     │
                     ▼
              Task Allocation
                     │
                     ▼
              Action Planning
                     │
                     ▼
             Outcome Evaluation
```
 
The first MVP should implement these functions using explainable logic and optimization before introducing complex Machine Learning models.
 
***
 
## 17. Human / Expert Layer
 
Human experts define the boundaries within which the autonomous system operates.
 
Potential expert inputs include:
 
- Protected archaeological zones
- Ecological restoration objectives
- Allowed intervention types
- Water limitations
- Seed restrictions
- Safety boundaries
- Operational rules

 
The Human / Expert Layer therefore establishes the system's constraints.
 
The AI Agent operates within these constraints.
 
***
 
## 18. Human-in-the-Loop Architecture
 
The system follows a Human-in-the-Loop model.
 
```text
Human / Expert
      │
      ▼
Rules + Constraints
      │
      ▼
AI Planning
      │
      ▼
Swarm Coordination
      │
      ▼
Robot Actions
      │
      ▼
Environmental Feedback
      │
      └──────────────► AI Planning
```
 
This creates a feedback loop while maintaining human authority over sensitive operational decisions.
 
***
 
## 19. Data Flow
 
The complete data flow can be summarized as:
 
```text
Environment
     │
     ▼
Robot Sensors
     │
     ▼
Local Robot Data
     │
     ▼
Communication
     │
     ▼
Shared Environmental Map
     │
     ├───────────────► Robot State
     │
     ▼
AI Agent
     │
     ├── Environmental Assessment
     ├── Priority Estimation
     ├── Resource Allocation
     └── Task Planning
     │
     ▼
Swarm Task Allocation
     │
     ▼
Individual Robots
     │
     ▼
Navigation + Intervention
     │
     ▼
New Environmental Observations
     │
     └──────────────────────► Shared Map
```
 
***
 
## 20. Decision Hierarchy
 
The architecture separates decision-making into three levels.
 
### Level 1 — Local Robot Decisions
 
Fast real-time decisions.
 
Examples:
 
- Motor control
- Sensor reading
- Obstacle response
- Local safety checks
- Task execution

 
### Level 2 — Swarm Decisions
 
Coordination between robots.
 
Examples:
 
- Task allocation
- Shared mapping
- Robot coordination
- Workload distribution

 
### Level 3 — AI Planning Decisions
 
Higher-level decisions.
 
Examples:
 
- Restoration prioritization
- Resource allocation
- Strategic task planning
- Outcome evaluation

 
This separation prevents the AI Agent from having to control every motor-level action.
 
***
 
## 21. Safety Architecture
 
Safety constraints exist at multiple levels.
 
### Robot Level
 
- Emergency stop
- Motor limits
- Battery protection
- Local obstacle avoidance

 
### Swarm Level
 
- Collision avoidance
- Communication failure handling
- Task reassignment
- Robot failure handling

 
### AI Level
 
- Protected-zone constraints
- Resource limits
- Intervention restrictions
- Human-defined rules

 
The system should fail toward a safe state whenever a critical constraint is violated.
 
***
 
## 22. Fault Handling
 
The swarm should be capable of handling partial failures.
 
Possible failures include:
 
- Robot communication loss
- Low battery
- Sensor failure
- Motor failure
- Payload failure
- Temporary network interruption

 
For example:
 
```text
Robot B
   │
   ├── Communication Lost
   │
   ▼
Swarm Detects Failure
   │
   ▼
Task Marked Unfinished
   │
   ▼
Available Robots Evaluated
   │
   ▼
Task Reassigned
```
 
This is an important advantage of a swarm architecture over relying on a single robot.
 
***
 
## 23. Scalability
 
The architecture should support increasing the number of robots without requiring a complete redesign.
 
The initial prototype may contain:
 
**2–3 robots**
 
Later experiments may expand to:
 
**5 → 10 → N robots**
 
The system should therefore avoid architectures where every robot requires direct coordination with every other robot for every decision.
 
As the swarm grows, distributed communication and hierarchical coordination may become increasingly important.
 
***
 
## 24. MVP Architecture
 
The first physical MVP will intentionally simplify the full architecture.
 
```text
                Laptop / Edge Computer
                         │
                         ▼
                    AI Planner
                         │
                    Task Allocation
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
           Robot A               Robot B
              │                     │
          ESP32 MCU              ESP32 MCU
              │                     │
       Sensors + Motors      Sensors + Motors
              │                     │
              └──────────┬──────────┘
                         │
                         ▼
                    Test Environment
```
 
Robot C can be introduced after the two-robot system is stable.
 
This staged architecture reduces implementation complexity.
 
***
 
## 25. Simulation Architecture
 
Before building multiple physical robots, the system will be tested in simulation.
 
The simulation should contain:
 
```text
Environment
│
├── Terrain
├── Environmental Conditions
├── Restoration Zones
├── Protected Zones
├── Resources
└── Obstacles

Robots
│
├── Position
├── Battery
├── Sensors
├── Capabilities
└── Tasks

AI / Swarm
│
├── Mapping
├── Prioritization
├── Allocation
├── Navigation
└── Evaluation
```
 
The simulation provides a safe environment for testing algorithms before hardware deployment.
 
***
 
## 26. Architecture Evolution
 
The architecture will evolve progressively.
 
### Stage 1
 
Simulation-only swarm.
 
### Stage 2
 
Single physical robot.
 
### Stage 3
 
Two physical robots.
 
### Stage 4
 
Multi-robot communication.
 
### Stage 5
 
AI-assisted task allocation.
 
### Stage 6
 
Controlled ecological intervention.
 
### Stage 7
 
Advanced environmental perception.
 
### Stage 8
 
Outdoor experimental testbed.
 
Each stage should be validated before moving to the next.
 
***
 
## 27. Core Architectural Principle
 
EcoArchaeoSwarm separates:
 
**Sensing**
 
from
 
**Coordination**
 
from
 
**Planning**
 
from
 
**Physical Action**
 
This separation makes the system easier to test, debug, scale, and improve.
 
The final architecture is therefore not simply:
 
**AI → Robot**
 
Instead, it is:
 
**Environment → Sensors → Shared Data → AI Planning → Swarm Coordination → Robot Action → Environmental Feedback**
 
This closed-loop architecture forms the technical foundation of EcoArchaeoSwarm.
