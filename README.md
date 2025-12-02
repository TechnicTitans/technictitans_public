# TechnicTitans FLL Team Repository

Welcome to the official repository of the **TechnicTitans FLL Team** from Lake Oswego.  
This space is dedicated to sharing our robot code development with the broader community.

## About
- All of our code is openly available for learning, experimentation, and inspiration.  
- Our learning can be your learning.  
- Our successes can be your successes.  

We believe in collaboration and knowledge-sharing, and we encourage others to build upon our work.

## Philosophy of Our Code
Our code is designed with a **modular architecture** to ensure clarity, scalability, and robustness:

- **Core Blocks (Bottom Row):**  
  Commonly used functions such as `GyroStraight` and `GyroTurn` are placed at the bottom of the code.  
  - These blocks are rarely edited.  
  - They contain only what has been extensively tested and proven to be extremely reliable.

- **Transit Blocks (Next Row):**  
  Each mission begins with a dedicated `transit_to_mission` block.  
  - These define the travel path to the point where missions are executed.  
  - This separation ensures smooth navigation and mission setup.

- **Mission Blocks (Above Transit):**  
  Each mission has its own `do_mission` block.  
  - This structure allows missions to be developed independently.  
  - It creates a fluid and scalable workflow for adding or refining missions.

- **Voyages (Above Mission Blocks):**   
  - A **Voyage** is a collection of missions assigned to a team member.  
  - Four Voyages were planned, each mapped to a memory position on the Spike Controller.  
  - Position 0 is reserved for Voyage development, enabling independent work without interference.  
  - Code comments clearly indicate which missions belong to which Voyage.

This modular approach allows every team member to contribute effectively while maintaining a clean, scalable, and collaborative codebase.

Our Start Block is positioned away from everything else and trash block acts as a garbage collector for any random code pieces we accidentally leave floating around. 

## Usage
Feel free to:
- Explore the codebase
- Adapt and extend the code for your own projects
- Use it as a foundation for developing your own solutions

## Contributing
If you find this repository useful, we’d love to hear from you!  
Please write to us in the **Issues** section to share your feedback, ideas, or experiences.

## Acknowledgments
Thank you for visiting our repository and supporting STEM learning through robotics.

---

**Team TechnicTitans**
