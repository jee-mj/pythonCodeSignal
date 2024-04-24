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

if __name__ == "__main__":
    create_venv()
