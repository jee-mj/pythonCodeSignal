import subprocess
import sys

def create_venv():
    # Determine the Python executable (useful for environments where the Python version matters)
    python_executable = sys.executable

    # Command to create a virtual environment
    command = [python_executable, "-m", "venv", "."]

    try:
        # Run the command
        subprocess.run(command, check=True)
        print("Virtual environment created successfully.")
    except subprocess.CalledProcessError:
        print("Failed to create virtual environment.")
        
def activate_venv():
        if sys.platform == "win32":
            activate_script = "Scripts\\activate.bat"
            command = [activate_script]
        else:
            activate_script = "bin/activate"
            command = ["source", activate_script]
        try:
            subprocess.run(command, shell=True, check=True)
            print("Virtual environment activated successfully.")
        except subprocess.CalledProcessError:
            print("Failed to activate virtual environment.")

if __name__ == "__main__":
    try:
        activate_venv()
    except:
        create_venv()
        activate_venv()
