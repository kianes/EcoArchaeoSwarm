# EcoArchaeoSwarm — Problem Definition
 
## 1. Background
 
Ecological degradation and desertification can make large landscapes difficult to monitor and restore.
 
Environmental conditions such as soil moisture, temperature, light availability, vegetation density, and terrain characteristics may vary significantly across relatively small areas.
 
At the same time, ecological restoration often operates under limited resources, including water, seeds, energy, time, and human access.
 
These challenges become more complex when degraded landscapes overlap with archaeologically sensitive areas.
 
In such environments, conventional vehicles or uncontrolled mechanical intervention may be unsuitable because archaeological structures, artifacts, or sensitive ground surfaces may require strict protection.
 
EcoArchaeoSwarm investigates whether a swarm of small autonomous robots can provide a low-impact platform for environmental monitoring and targeted assistance in ecological restoration while respecting archaeological and operational constraints.
 
***
 
## 2. Problem Statement
 
The central problem addressed by EcoArchaeoSwarm is:
 
> How can multiple low-cost autonomous robots collaboratively monitor degraded environments, identify areas suitable for ecological restoration, allocate limited resources, and assist controlled restoration actions while avoiding archaeologically protected areas?

 
This problem combines several engineering challenges:
 
- Environmental sensing
- Distributed data collection
- Multi-robot coordination
- Shared environmental mapping
- Task allocation
- Resource-constrained planning
- Autonomous navigation
- Computer vision
- Ecological restoration
- Archaeological protection
- Human-supervised decision-making

 
The system must therefore operate as an integrated cyber-physical system rather than as an isolated robot.
 
***
 
## 3. Core Engineering Challenge
 
The main engineering challenge is not simply building a mobile robot.
 
A single robot can collect environmental measurements and move through an environment.
 
The more difficult problem is determining how multiple robots should collaboratively decide:
 
1. What information needs to be collected
2. Where that information should be collected
3. Which robot should perform each task
4. How limited resources should be distributed
5. Which areas must be avoided
6. Which intervention is appropriate
7. How the result of an intervention should affect future decisions

 
Therefore, EcoArchaeoSwarm treats the robot swarm as a distributed decision-making system.
 
***
 
## 4. Environmental Problem
 
The target environment contains areas with different ecological conditions.
 
For example:
 
- Healthy vegetation
- Degraded vegetation
- Very dry soil
- Potential restoration areas
- Areas with insufficient environmental data
- Areas where intervention is restricted

 
A robot cannot assume that the entire environment requires the same action.
 
Instead, environmental observations must be converted into a spatial representation that allows the system to distinguish between different conditions.
 
The system should therefore be capable of constructing and updating a shared environmental map.
 
***
 
## 5. Resource Constraints
 
Ecological restoration is performed under limited resources.
 
The prototype considers at least four major resource categories:
 
### Water
 
Water should be delivered selectively rather than distributed uniformly.
 
### Seeds
 
Seeds should be allocated to locations where environmental conditions make their use appropriate.
 
### Energy
 
Each robot has a limited battery capacity and must account for energy consumption during navigation, sensing, communication, and intervention.
 
### Time
 
The system should avoid spending excessive time on low-priority areas when other locations require attention.
 
Resource allocation therefore becomes part of the swarm planning problem.
 
***
 
## 6. Archaeological Constraints
 
Archaeological protection is an explicit system constraint.
 
The environment may contain areas where robotic access or physical intervention is prohibited.
 
For the prototype, the environment is divided into three conceptual zones:
 
### Protected Zone
 
Robots must not enter or perform intervention inside this area.
 
### Buffer Zone
 
Robots may be required to maintain additional safety margins or operate under restricted conditions.
 
### Restoration Zone
 
Robots may perform approved monitoring and ecological operations.
 
These zones directly influence navigation, path planning, task allocation, and intervention decisions.
 
The system must treat archaeological protection as a hard operational constraint rather than as an optional consideration.
 
***
 
## 7. Swarm Robotics Problem
 
A swarm consists of multiple robots that operate toward a shared objective.
 
Each robot has:
 
- Position
- Battery state
- Sensor capabilities
- Payload capabilities
- Current task
- Local environmental observations

 
The robots must share relevant information and coordinate their actions.
 
For example:
 
Robot A may detect an area with very low soil moisture.
 
The observation is added to the shared environmental representation.
 
The planning layer then evaluates:
 
- Environmental priority
- Distance
- Robot battery levels
- Available payloads
- Protected zones
- Current robot workloads

 
The system may then assign another robot to perform detailed sensing or a controlled intervention.
 
This creates a dynamic task-allocation problem rather than a fixed sequence of robot commands.
 
***
 
## 8. AI Problem
 
The AI component is responsible for transforming distributed observations and system constraints into useful planning decisions.
 
The AI Agent should assist with:
 
### Environmental Assessment
 
Estimate environmental conditions from sensor and visual data.
 
### Restoration Prioritization
 
Determine which locations may require attention based on predefined ecological criteria.
 
### Resource Allocation
 
Determine how limited resources should be distributed.
 
### Task Allocation
 
Determine which robot should perform a particular task.
 
### Constraint Handling
 
Ensure that planned actions remain compatible with protected areas and operational restrictions.
 
### Outcome Evaluation
 
Compare environmental observations over time and evaluate whether previous actions produced measurable changes.
 
The AI Agent therefore functions primarily as a decision-support and planning system.
 
It is not intended to be a general conversational chatbot.
 
***
 
## 9. Research Question
 
The primary research question is:
 
> Can a small swarm of autonomous robots use shared environmental observations and AI-assisted task allocation to support resource-aware ecological restoration while respecting archaeological protection constraints?

 
Supporting questions include:
 
- How should environmental observations be represented in a shared map?
- How should tasks be allocated between robots?
- How should battery, water, seed, and time constraints affect task allocation?
- How should protected archaeological zones influence navigation?
- How can restoration priorities be estimated from environmental data?
- How should the system evaluate the result of an intervention?
- How much intelligence should be centralized versus distributed between robots?

 
***
 
## 10. Project Objectives
 
The project has six primary objectives.
 
### Objective 1 — Environmental Monitoring
 
Develop a robotic platform capable of collecting distributed environmental observations.
 
### Objective 2 — Shared Environmental Mapping
 
Create a shared representation of environmental conditions that can be updated by multiple robots.
 
### Objective 3 — Swarm Coordination
 
Enable multiple robots to coordinate sensing and operational tasks.
 
### Objective 4 — Resource-Aware Planning
 
Develop planning mechanisms that account for limited water, seeds, battery energy, and time.
 
### Objective 5 — Archaeological Protection
 
Integrate protected zones and operational constraints directly into navigation and task allocation.
 
### Objective 6 — AI-Assisted Decision Making
 
Develop an AI planning layer capable of prioritizing restoration opportunities and coordinating robotic actions.
 
***
 
## 11. MVP Scope
 
The Minimum Viable Prototype will not attempt full-scale ecological restoration.
 
Instead, the MVP will demonstrate the complete decision-making loop in a controlled environment.
 
The MVP should include:
 
- Multiple simulated or physical robots
- Environmental sensing
- Shared environmental map
- Defined restoration-priority areas
- Protected zones
- Limited resources
- Task allocation
- Basic autonomous navigation
- AI-assisted planning
- Controlled intervention
- Outcome monitoring

 
The first implementation may use simulation before physical deployment.
 
***
 
## 12. Non-Goals
 
The initial project will explicitly avoid attempting to solve several problems.
 
The MVP will not attempt to:
 
- Restore an entire ecosystem autonomously
- Replace ecological experts
- Replace archaeological experts
- Perform archaeological excavation
- Disturb archaeological sites
- Independently select invasive or unsuitable plant species
- Perform unrestricted autonomous intervention
- Operate without human-defined safety constraints
- Deploy directly into sensitive archaeological sites without controlled validation

 
These limitations keep the initial project technically realistic and experimentally measurable.
 
***
 
## 13. Proposed System Boundary
 
The initial system boundary is:
 
Environmental Data
 
↓
 
Sensing
 
↓
 
Shared Environmental Representation
 
↓
 
AI-Assisted Assessment
 
↓
 
Restoration Prioritization
 
↓
 
Resource Allocation
 
↓
 
Swarm Task Allocation
 
↓
 
Navigation
 
↓
 
Controlled Intervention
 
↓
 
Outcome Monitoring
 
↓
 
Updated Environmental Data
 
The process forms a continuous feedback loop.
 
***
 
## 14. Human-in-the-Loop Requirement
 
The system is designed as a human-supervised autonomous platform.
 
Experts define:
 
- Ecological constraints
- Acceptable intervention types
- Protected areas
- Safety boundaries
- Restoration objectives
- Operational limits

 
The AI Agent operates within these predefined constraints.
 
This architecture prevents the AI system from independently redefining environmental or archaeological rules.
 
***
 
## 15. Technical Feasibility
 
The initial prototype can be constructed using relatively accessible technologies.
 
Potential hardware includes:
 
- ESP32-class microcontrollers
- Differential-drive robot platforms
- Low-cost environmental sensors
- Cameras
- IMUs
- Wireless communication
- Motor drivers
- Rechargeable batteries
- Modular seed or micro-watering mechanisms

 
The first software implementation can be developed using simulation and conventional algorithms before introducing more advanced Machine Learning.
 
This allows the project to validate its core architecture without requiring a complete autonomous field robot at the beginning.
 
***
 
## 16. Evaluation Criteria
 
The prototype should be evaluated using measurable technical criteria.
 
### Mapping
 
Can multiple robots contribute observations to a shared environmental representation?
 
### Coordination
 
Can robots avoid unnecessary duplication of tasks?
 
### Task Allocation
 
Can tasks be assigned according to robot position, battery state, capabilities, and workload?
 
### Resource Efficiency
 
Can the system account for limited resources?
 
### Constraint Compliance
 
Can robots reliably avoid protected zones?
 
### Adaptability
 
Can the system modify future tasks after receiving new observations?
 
### Intervention Evaluation
 
Can the system compare environmental conditions before and after an intervention?
 
***
 
## 17. Expected Outcome
 
The expected outcome is a working prototype architecture demonstrating how:
 
Environmental sensing
 
→
 
Swarm coordination
 
→
 
AI-assisted planning
 
→
 
Resource allocation
 
→
 
Protected-zone-aware navigation
 
→
 
Controlled ecological intervention
 
→
 
Outcome monitoring
 
can operate as one integrated system.
 
The project is intended to demonstrate the feasibility of using small collaborative robots as a tool for environmental monitoring and targeted ecological restoration assistance in complex and sensitive landscapes.
 
***
 
## 18. Final Problem Definition
 
EcoArchaeoSwarm addresses the intersection of ecological degradation, limited restoration resources, autonomous robotics, and archaeological landscape protection.
 
The project proposes a swarm of small autonomous robots that collaboratively collect environmental information, construct a shared representation of the environment, identify restoration priorities, allocate limited resources, and perform controlled interventions under explicit ecological and archaeological constraints.
 
The central engineering objective is to demonstrate that distributed robotic systems and AI-assisted planning can be combined into a measurable, modular, and human-supervised platform for low-impact ecological restoration support.
