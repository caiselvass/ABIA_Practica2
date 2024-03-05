# AI Planning with PDDL: Python Execution Guide for Book Reading Planning

## Project Overview
This project leverages Planning Domain Definition Language (PDDL) for AI planning to optimize the reading schedule of books over a year. The objective is to balance the number of pages read each month, not exceeding 800 pages, while adhering to constraints related to book reading order. Some books have predecessors that must be read before others, and there are parallel reads that should be completed within a month of each other, adding complexity to the planning process.

## Directory Structure and Requirements
The proper functioning of Python scripts depends on the unaltered structure of the `ABIA_Practica2_Roger_Cai_Pau` directory. Modifying any files or directories within it may affect the execution of the Python scripts.

### Execution Instructions

1. **generate_test_cases.py**: Generates and executes test cases through terminal prompts. For additional command information, type "HELP" in response to the prompts. This script is tailored for Windows and MacOS, with manual execution required on Linux.

2. **generate_plots_experiments.py**: This script generates plots from the data in `ABIA_Practica2_Roger_Cai_Pau/experiments/data`. The plots are already available in `ABIA_Practica2_Roger_Cai_Pau/experiments/plots` and do not require script execution to view.

### Recommendations

- Run Python scripts from within the `ABIA_Practica2_Roger_Cai_Pau` directory using Visual Studio Code to mirror the development environment.
- If using a terminal for script execution, ensure that `ABIA_Practica2_Roger_Cai_Pau` is the current working directory.

## About AI Planning and PDDL
This project demonstrates the application of AI planning and PDDL in solving complex logistical problems like scheduling book readings. It showcases the capability of AI planning to navigate intricate constraints, such as book predecessors and parallel reading timelines, to achieve a balanced and feasible reading plan.
