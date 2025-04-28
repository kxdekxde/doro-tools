import os
import subprocess
import time
import sys  # Added this import
from tqdm import tqdm

def spinning_wheel():
    """Simple spinner animation for indeterminate progress."""
    spinner = ['-', '\\', '|', '/']
    for i in range(20):  # Adjust duration as needed
        sys.stdout.write(f"\rDownloading... {spinner[i % 4]}")
        sys.stdout.flush()
        time.sleep(0.1)

def run_megacmd_command():
    # Path to MEGAclient.exe
    megacmd_path = os.path.expandvars("%USERPROFILE%\\AppData\\Local\\MEGAcmd\\MEGAclient.exe")
    
    # List of Mega folder URLs (including the original one and new ones)
    mega_urls = [
        "https://mega.nz/folder/EG1kDRYL#qoj4PIfzukfK-OXd0J_HpA",  # Original link
        "https://mega.nz/folder/ZCckyBja#GNr0XzRR1wmVoEbBZiq5IA",  # New link 1
        "https://mega.nz/folder/kfdFwCpb#XhvGFo75mX_SeLAAn4TuzQ",  # New link 2
        "https://mega.nz/folder/pfNCyZyQ#gLefHjXOQ_kxSMiGGL6Qng",  # New link 3
        "https://mega.nz/folder/wDUXiDDQ#PpvESE30Y5q8ecmo9ywhEg",  # New link 4
        "https://mega.nz/folder/RLN1kBKQ#O9nB6gtpYycQYuPuBvTHWQ",  # New link 5
        "https://mega.nz/folder/pHV3ALaJ#nx-XPxPvkXFn2gQsqZ3XgA",  # New link 6
        "https://mega.nz/folder/IOUX2K7K#tJjVroQD3pdA8vT6MoBRhg",  # New link 7
        "https://mega.nz/folder/IT0xySZJ#eYi5p8-1SPUUSwumfp1Cew"   # New link 8
    ]
    
    # Get script directory and create DORO_Tools path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.join(script_dir, "DORO_Tools")
    
    if not os.path.exists(megacmd_path):
        print(f"❌ Error: MEGAclient not found at {megacmd_path}")
        return
    
    try:
        print("🚀 Starting downloads...")
        print(f"📁 Download location: {download_path}")

        # Create DORO_Tools directory if it doesn't exist
        os.makedirs(download_path, exist_ok=True)

        # Loop through all Mega URLs and start download
        for mega_url in mega_urls:
            print(f"\n📥 Downloading from: {mega_url}")
            
            # Run MEGAclient command for each URL
            process = subprocess.Popen(
                [megacmd_path, "get", mega_url, download_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True
            )

            # Show progress
            spinning_wheel()

            # Simulated progress bar
            print("\n⌛ Download in progress...")
            with tqdm(total=100, desc=f"📦 Downloading {mega_url}", unit="%") as pbar:
                for i in range(10):  # Simulate progress updates
                    time.sleep(1)
                    pbar.update(10)  # Increment by 10% each step

            # Wait for process to finish
            stdout, stderr = process.communicate()

            print("\n✅ Download complete!")
            if stdout:
                print("Output:", stdout.strip())
            if stderr:
                print("Completed:", stderr.strip())

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    run_megacmd_command()
