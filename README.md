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
