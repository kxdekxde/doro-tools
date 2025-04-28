import subprocess
import os

# Get the current directory of the script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Define the path to the requirements.txt file in the same directory as the script
requirements_file = os.path.join(script_directory, "requirements.txt")

# Define the command to install dependencies
command = ["pip", "install", "-r", requirements_file]

try:
    # Run the command
    subprocess.run(command, check=True)
    print("Dependencies installed successfully.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while installing dependencies: {e}")
