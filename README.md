# ABM: Agent-Based Model

## Overview
ABM is a simplified simulation tool designed to model the South African cannabis and hemp industry dynamics using an agent-based approach in Streamlit. The model features two agent types: Farmers (both formal and informal) with attributes like production capacity and compliance status, and Regulators, influencing the market by policies. This simulation aims to help understand how these entities interact over a fixed period.

## User Guide
Users interact with the ABM simulation through a Streamlit interface to:
* Input market demand and regulatory conditions.
* Control the simulation with start, stop, and reset functionalities.
* Observe the outcomes through visualizations of production and compliance levels.

- Regulatory Conditions: Choose between 'Lenient', 'Strict', or 'Custom' to determine the stringency of regulations in the simulation. 'Custom' allows setting a specific compliance factor that affects farmer production.

## Installation & Running the Simulation
1. Clone the repository.
2. Install the required libraries: Streamlit, Python, Pandas, numpy, matplotlib, and altair.
3. Run the `streamlit run streamlit_app.py` command in your terminal to initiate the interface.

## Features
* Interactive Streamlit UI for input parameter configuration.
* Start, stop, and reset controls for the simulation.
* Graphical representations for viewing simulation outputs.

## Development and Contribution
The codebase adheres to clean-coding principles and is well-documented to facilitate contributions. Developers should refer to in-code comments and docstrings for guidance. Contributions towards expanding the ABM's features and scalability are welcome.

For developers, please ensure you:
* Maintain the coding standards as per the documentation.
* Update the README.md and CHANGELOG.md as appropriate for new features or bug fixes.
* Add unit tests for new code to ensure reliability.

## Technical Architecture
ABM runs a Streamlit application (`streamlit_app.py`) that includes user input collection, control buttons, and output placeholders separated into modular Python files. The simulation logic is encapsulated in `simulation_engine.py`, iterating over the various agent classes such as `farmer.py` and `regulator.py`.

## Project Structure
The project comprises several modules:
* `/streamlit_app.py`: The entry point for the Streamlit application.
* `/interface`: Modules for the user input, control buttons, and outputs display.
* `/simulation`: Core modules for the agent-based model, including agent definitions and the simulation engine.

## License
This project is released under the XYZ License. For more details, see the `LICENSE` file included in the repository.

## Contact
For questions, suggestions, or contributions, please open an issue in the repository, and a maintainer will get back to you.

### Disclaimer
This simulation is a basic model and may not account for all real-world dynamics of the South African cannabis and hemp industry. It is intended for educational and research purposes only.
