# main.py
import subprocess
import os
import sys
from videoEditor.trim_or_delete_02 import remove_first_25_seconds


# Example usage of the combibe_images function
# def main():
#     print("--- Video Automation Tool ---")
    
#     # Path to the script inside the videoEditor folder
#     script_path = os.path.join("videoEditor", "combine_images_01.py")
    
#     if not os.path.exists(script_path):
#         print(f"Error: Cannot find {script_path}")
#         return

#     print(f"Executing {script_path}...")

#     # Run the script using the current virtual environment's python
#     try:
#         result = subprocess.run(
#             [sys.executable, script_path],
#             check=True,
#             capture_output=True,
#             text=True
#         )
#         print(result.stdout)
#     except subprocess.CalledProcessError as e:
#         print("An error occurred while running the script:")
#         print(e.stderr)


# Example usage of the trim_or_delete function 
def main():
    print("🎧 Media Tool")
    print("1. Remove first 25 seconds from audio")
    
    choice = input("Enter choice: ")

    if choice == "1":
        input_file = input("Enter input file path: ").strip() 
        output_file = input("Enter output file path: ").strip()

        if not input_file or not output_file:
            print("❌ Please provide valid paths")
            return

        result = remove_first_25_seconds(input_file, output_file)
        print(result)
#  upload/audios/Never_Be_The_Same.mp3
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()