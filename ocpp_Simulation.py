import tkinter as tk
from PIL import Image, ImageTk
import random
import threading

class EVCharger:
    def __init__(self, charge_point_id):
        self.charge_point_id = charge_point_id
        self.start_charging = False
        self.current = 0
        self.setpoint_current = 0
        self.max_current = 40

    def set_current(self, current):
        if 0 <= current <= self.max_current:
            self.current = int(current)
        else:
            raise ValueError("Current should be between 0 and max_current")

    def calculate_active_power(self):
        return self.setpoint_current * 230 if self.start_charging else 0

    def simulate_charging(self):
        if self.start_charging:
            self.current = random.randint(1, self.max_current)
            status = 3  # Active Charging
        else:
            self.current = 0
            status = 4  # Stopped

        active_power = self.calculate_active_power()
        return self.current, status, active_power, self.setpoint_current

class EVChargerGUI:
    def __init__(self, root, ev_chargers, image_path):
        self.root = root
        self.ev_chargers = ev_chargers
        self.root.title("EV Charger Simulation")

        charger_image = Image.open(image_path)
        charger_image = charger_image.resize((200, 300))
        self.charger_photo = ImageTk.PhotoImage(charger_image)

        headers = ["Charger", "Current (A)", "Status", "Active Power (W)", "Setpoint Current (A)", "Charging"]
        for col, header in enumerate(headers):
            label = tk.Label(self.root, text=header)
            label.grid(row=0, column=col+1)

        charger_label = tk.Label(self.root, image=self.charger_photo)
        charger_label.grid(row=0, column=0, rowspan=len(ev_chargers) + 1, padx=10)

        self.labels_entries = {}
        self.charging_animations = {}

        for row, ev_charger in enumerate(self.ev_chargers):
            label_charger = tk.Label(self.root, text=f"Charger {row + 1}")
            label_charger.grid(row=row + 1, column=1)

            current_entry = tk.Entry(self.root)
            current_entry.grid(row=row + 1, column=2)

            status_entry = tk.Entry(self.root)
            status_entry.grid(row=row + 1, column=3)

            active_power_entry = tk.Entry(self.root)
            active_power_entry.grid(row=row + 1, column=4)

            setpoint_current_entry = tk.Entry(self.root)
            setpoint_current_entry.grid(row=row + 1, column=5)

            self.labels_entries[ev_charger] = {
                "current_entry": current_entry,
                "status_entry": status_entry,
                "active_power_entry": active_power_entry,
                "setpoint_current_entry": setpoint_current_entry
            }

            charging_animation = tk.Canvas(self.root, width=20, height=20)
            charging_animation.grid(row=row + 1, column=6)
            self.charging_animations[ev_charger] = {
                "canvas": charging_animation,
                "charging": False
            }

        self.update_values()

    def update_values(self):
        for ev_charger, entries in self.labels_entries.items():
            current, status, active_power, setpoint_current = ev_charger.simulate_charging()

            entries["current_entry"].delete(0, tk.END)
            entries["current_entry"].insert(0, current)
            entries["status_entry"].delete(0, tk.END)
            entries["status_entry"].insert(0, status)
            entries["active_power_entry"].delete(0, tk.END)
            entries["active_power_entry"].insert(0, active_power)
            entries["setpoint_current_entry"].delete(0, tk.END)
            entries["setpoint_current_entry"].insert(0, ev_charger.setpoint_current)

            self.update_charging_animation(ev_charger, status)

        self.root.after(1000, self.update_values)

    def update_charging_animation(self, ev_charger, status):
        charging_animation = self.charging_animations[ev_charger]["canvas"]

        if status == 3:
            charging_animation.delete("all")
            charging_animation.create_rectangle(2, 2, 18, 18, fill="green")
        elif status == 4:
            charging_animation.delete("all")
            charging_animation.create_rectangle(2, 2, 18, 18, fill="red")
        else:
            charging_animation.delete("all")

    def refresh_gui(self):
        self.update_values()

class StartupUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EV Charger Startup Configuration")

        label = tk.Label(root, text="Select the number of chargers:")
        label.pack(pady=10)

        self.selected_chargers = tk.StringVar(root)
        self.selected_chargers.set("5")
        options = [str(i) for i in range(5, 51, 5)]
        dropdown = tk.OptionMenu(root, self.selected_chargers, *options)
        dropdown.pack(pady=10)

        start_button = tk.Button(root, text="Start", command=self.start_simulation)
        start_button.pack(pady=10)

    def start_simulation(self):
        num_chargers = int(self.selected_chargers.get())
        self.root.destroy()
        self.run_simulation(num_chargers)

    def run_simulation(self, num_chargers):
        ev_chargers = [EVCharger(f"charger-{i}") for i in range(1, num_chargers + 1)]

        # Start the GUI in a separate thread
        self.simulation_root = tk.Tk()
        self.gui = EVChargerGUI(self.simulation_root, ev_chargers, "D:\\Siemens Internship\\OCPP Versi Charger\\versicharge.png")
        self.simulation_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(ev_chargers, self.simulation_root))

        # Start a separate thread for the CLI
        cli_thread = threading.Thread(target=self.handle_commands, args=(ev_chargers,))
        cli_thread.daemon = True  # Set as a daemon so it doesn't block the program from exiting
        cli_thread.start()

        # Start the GUI loop
        self.simulation_root.mainloop()

    def on_close(self, ev_chargers, root):
        for ev_charger in ev_chargers:
            ev_charger.start_charging = False
        root.destroy()

    def handle_commands(self, ev_chargers):
        while True:
            command = input("Enter command (format: charger_id action [value]): ")
            try:
                parts = command.split()
                charger_id = int(parts[0])
                action = parts[1]
                value = int(parts[2]) if len(parts) > 2 else None

                ev_charger = ev_chargers[charger_id - 1]

                if action == "set":
                    if value is not None:
                        ev_charger.set_current(value)
                elif action == "start":
                    ev_charger.start_charging = True
                elif action == "stop":
                    ev_charger.start_charging = False
                elif action == "setpoint":
                    if value is not None:
                        ev_charger.setpoint_current = value

                print(f"Updated Charger {charger_id} with action '{action}' and value '{value}'")

                # Refresh the GUI after command input
                self.gui.refresh_gui()

            except (IndexError, ValueError) as e:
                print(f"Invalid command: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StartupUI(root)
    root.mainloop()
