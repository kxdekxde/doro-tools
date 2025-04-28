import os
import requests
import subprocess
from tqdm import tqdm

# Define the download URL and the filename
url = "https://mega.nz/MEGAcmdSetup64.exe"
filename = "MEGAcmdSetup64.exe"

# Step 1: Check if the installer already exists in the directory
if os.path.exists(filename):
    print(f"{filename} already exists. Proceeding with installation...")
else:
    # If the installer doesn't exist, download it
    print("Downloading MEGAcmd...")
    response = requests.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        with open(filename, "wb") as file:
            # Create a progress bar using tqdm
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as pbar:
                for data in response.iter_content(chunk_size=1024):
                    file.write(data)
                    pbar.update(len(data))  # Update the progress bar
        print("Download complete!")
    else:
        print("Failed to download the file.")
        exit(1)

# Step 2: Install MEGAcmd silently
print("Installing MEGAcmd...")
subprocess.run([filename, "/S"], check=True)

# Step 3: Delete the installer file after installation
print("Deleting the installer file...")
os.remove(filename)
print("Installation complete and installer removed.")
