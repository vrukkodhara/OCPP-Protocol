# OCPP-Protocol
Working of Versi charger using OCPP protocol
Overview
This project simulates the operation of multiple EV chargers. It provides a graphical user interface (GUI) for real-time monitoring and control of chargers, along with a command-line interface (CLI) for advanced configurations. Each charger can be controlled independently, with features such as starting/stopping charging, setting current limits, and monitoring active power.

Features
GUI Features:

Displays charger information: Current, Status, Active Power, Setpoint Current.
Real-time charging status indicator (green for active, red for stopped).
User-friendly interface to monitor and manage multiple chargers.
CLI Features:

Issue commands to control chargers directly.
Perform operations like starting/stopping charging, setting current, and defining setpoint current.
Simulation:

Simulates dynamic charging behavior with random current values and corresponding active power.
How to Run
Prerequisites
Python 3.x
Required libraries: tkinter, PIL (Pillow)
A charger image file (versicharge.png) for the GUI representation.
Installation
Clone or download this repository.

Install dependencies:

bash
Copy code
pip install pillow
Ensure the charger image file path is correct in the code ("D:\\Siemens Internship\\OCPP Versi Charger\\versicharge.png"). Update the path as needed.

Running the Application
Open a terminal and navigate to the project directory.

Run the script:

bash
Copy code
python ev_charger_simulation.py
The startup UI will prompt you to select the number of chargers. Choose a value and click "Start."

Usage Instructions
Graphical User Interface (GUI)
Charger Information:
Current (A): The current amperage being drawn by the charger.
Status: Indicates whether charging is active (3 for charging, 4 for stopped).
Active Power (W): Real-time power consumption calculated as Setpoint Current × 230V.
Setpoint Current (A): Desired current set by the user.
Charging Indicator:
Green: Active charging.
Red: Charging stopped.
Command-Line Interface (CLI)
Use the CLI to issue commands for charger operations. Format:

css
Copy code
charger_id action [value]
Commands:
Command	Description	Example
charger_id start	Start charging for the specified charger	1 start
charger_id stop	Stop charging for the specified charger	2 stop
charger_id set value	Set the current for the charger	1 set 20
charger_id setpoint value	Set the setpoint current for the charger	1 setpoint 30
Code Structure
Key Classes
EVCharger:

Manages charger-specific operations like setting current, calculating active power, and simulating charging.
EVChargerGUI:

Provides a graphical interface for monitoring and controlling EV chargers.
StartupUI:

Handles the initial setup for selecting the number of chargers and launching the simulation.
File Structure
ev_charger_simulation.py: Main script to run the simulation.
versicharge.png: Charger image used in the GUI (ensure the file is in the specified path).
Troubleshooting
GUI not displaying the charger image:

Check the image file path and update it if necessary.
Ensure the image file exists and is in the correct format (PNG).
CLI commands not working:

Ensure the correct format is used: charger_id action [value].
Verify that charger_id matches the initialized chargers.
Dependencies missing:

Run the following command to install missing dependencies:
bash
Copy code
pip install -r requirements.txt
Future Enhancements
Add more detailed charging statistics and analytics.
Integrate a database for charger logs.
Expand CLI commands to include more complex configurations.
Author
This project was developed as part of an internship at Siemens.
