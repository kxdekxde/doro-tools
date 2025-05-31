import subprocess
import time
import sys
from pathlib import Path

def run_megacmd_command():
    # Path to MEGAclient.exe using pathlib
    megacmd_path = Path.home() / "AppData" / "Local" / "MEGAcmd" / "MEGAclient.exe"
    
    # List of Mega folder URLs (including the original one and new ones)
    mega_urls = [
        "https://mega.nz/folder/ELEmEDyK#U0iobhXNez5nuWALOrYdzg"  # Doro_Tools folder
    ]
    
    # Get script directory and create DORO_Tools path using pathlib
    script_dir = Path(__file__).parent.absolute()
    download_path = script_dir / "DORO_Tools"
    
    if not megacmd_path.exists():
        print(f"❌ Error: MEGAclient not found at {megacmd_path}")
        return
    
    try:
        print("🚀 Starting downloads...")
        print(f"📁 Download location: {download_path}")
        # Create DORO_Tools directory if it doesn't exist
        download_path.mkdir(exist_ok=True)

        # Loop through all Mega URLs and start download
        for mega_url in mega_urls:
            print("\n📥 Downloading content...")  # Removed URL from output
            print("=" * 50)
            
            # Run MEGAclient command for each URL with proxy and show real-time output
            process = subprocess.Popen(
                [str(megacmd_path), "get", mega_url, str(download_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # Merge stderr into stdout
                text=True,
                bufsize=1,  # Line buffered
                universal_newlines=True
            )

            # Real-time output display
            print("📡 MEGAcmd output:")
            print("-" * 30)
            
            # Read output line by line in real-time
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    # Filter out any lines that might contain the URL
                    if mega_url not in output:
                        print(output.strip())
                    sys.stdout.flush()

            # Get return code
            return_code = process.poll()
            
            print("-" * 30)
            if return_code == 0:
                print("✅ Download completed successfully!")
            else:
                print(f"⚠️ Download finished with return code: {return_code}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    run_megacmd_command()