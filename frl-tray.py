import os
import subprocess
import glob
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import sys

# Path to the bundled CLI app
# Path to the bundled CLI app
CLI_APP = next(iter(glob.glob("frltoggle*.exe")), "frltoggle.exe")

if not os.path.exists(CLI_APP):
    print(f"Error: No matching CLI app found for 'frltoggle*.exe'")
    sys.exit(1)

def run_cli_app(param):
    """Run the CLI app with the selected parameter."""
    try:
        subprocess.run(
            [CLI_APP, str(param)], 
            check=True, 
            creationflags=subprocess.CREATE_NO_WINDOW  # Suppress console window
        )
    except Exception as e:
        print(f"Error running {CLI_APP}: {e}")

def get_initial_status():
    """Run the CLI app with 'status' and return the output."""
    try:
        result = subprocess.run(
            [CLI_APP, "status"], 
            check=True, 
            creationflags=subprocess.CREATE_NO_WINDOW, 
            text=True, 
            capture_output=True
        )
        return int(result.stdout.strip())
    except Exception as e:
        print(f"Error getting initial status from {CLI_APP}: {e}")
        return None

# Variable to track the selected option
selected_option = get_initial_status()  # Initialize based on CLI app output

def set_option(icon, item, param):
    """Set the selected option and run the CLI app."""
    global selected_option
    selected_option = param
    run_cli_app(param)
    # Update the menu to reflect the selected option
    icon.update_menu()
    icon.icon = Image.open(f'./icons/{param}.png')  # Update icon image dynamically

# Define the tray menu with radio items
menu = Menu(
    MenuItem("Unlimited", lambda icon, item: set_option(icon, item, 0), checked=lambda item: selected_option == 0),
    MenuItem("120", lambda icon, item: set_option(icon, item, 120), checked=lambda item: selected_option == 120),
    MenuItem("90", lambda icon, item: set_option(icon, item, 90), checked=lambda item: selected_option == 90),
    MenuItem("60", lambda icon, item: set_option(icon, item, 60), checked=lambda item: selected_option == 60),
    MenuItem("30", lambda icon, item: set_option(icon, item, 30), checked=lambda item: selected_option == 30),
    Menu.SEPARATOR,
    MenuItem("Exit", lambda icon, item: icon.stop())
)

# Create and run the tray icon
im = Image.open(f'./icons/{selected_option}.png')
icon = Icon("frl-tray", im, menu=menu)  # Use dynamically created image
icon.run()
