# OCPP-Protocol
Working of Versi charger using OCPP protocol
# EV Charger Simulation Application

## Overview
This project simulates the operation of multiple EV chargers. It provides a graphical user interface (GUI) for real-time monitoring and control of chargers, along with a command-line interface (CLI) for advanced configurations. Each charger can be controlled independently, with features such as starting/stopping charging, setting current limits, and monitoring active power.

---

## Features
1. **GUI Features**:
   - Displays charger information: Current, Status, Active Power, Setpoint Current.
   - Real-time charging status indicator (green for active, red for stopped).
   - User-friendly interface to monitor and manage multiple chargers.

2. **CLI Features**:
   - Issue commands to control chargers directly.
   - Perform operations like starting/stopping charging, setting current, and defining setpoint current.

3. **Simulation**:
   - Simulates dynamic charging behavior with random current values and corresponding active power.

---

## Prerequisites
- Python 3.x
- Required libraries: `tkinter`, `Pillow`
- A charger image file (`versicharge.png`) for the GUI representation.

---

## Installation
1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install pillow


## Usage Instructions
- Graphical User Interface (GUI)
1. Charger Information:

Current (A): The current amperage being drawn by the charger.
Status: Indicates whether charging is active (3 for charging, 4 for stopped).
Active Power (W): Real-time power consumption calculated as Setpoint Current × 230V.
Setpoint Current (A): Desired current set by the user.
Charging Indicator:

Green: Active charging.
Red: Charging stopped.

## Command-Line Interface (CLI)
Use the CLI to issue commands for charger operations. 
Format:
```css
charger_id action [value]
```


## Commands:
Command	                           Description	                           Example
charger_id start	         Start charging for the specified charger	       1 start
charger_id stop	         Stop charging for the specified charger	       2 stop
charger_id set value	      Set the current for the charger	                1 set 20
charger_id setpoint value	Set the setpoint current for the charger	       1 setpoint 30
