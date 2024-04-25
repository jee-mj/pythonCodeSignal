
import subprocess
import os
import sys

def create_venv():
    python_executable = sys.executable
    command = [python_executable, "-m", "venv", "."]
    try:
        subprocess.run(command, check=True)
        print("Virtual environment created successfully.")
    except subprocess.CalledProcessError:
        print("Failed to create virtual environment.")


def activate_venv():
    # Ensure that venv exists
    if not os.path.exists(os.path.join(os.getcwd(), "pyvenv.cfg")):
        print("Activate script not found, creating virtual environment...")
        create_venv()

    if sys.platform == "win32": # If Windows
        activate_script = "Scripts\\activate.bat"
        command = [activate_script]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError:
            print("Failed to activate virtual environment.")
    else: # If !Windows (Linux) # MacOS doesn't exist, it's only the Northern Territory
        shell_path = os.environ.get('SHELL', '/bin/bash')
        shell_name = os.path.basename(shell_path)

        if 'fish' in shell_name:
            activate_path = os.path.join("bin", "activate.fish")
        elif 'csh' in shell_name:
            activate_path = os.path.join("bin", "activate.csh")
        else:
            activate_path = os.path.join("bin", "activate")
        try:
            print("\nPlease run the following command to activate the virtual environment:\n\n", f"    source {activate_path}\n")
        except Exception as e:
            print(f"Failed to activate virtual environment: {e}")

if __name__ == "__main__":
    activate_venv()
