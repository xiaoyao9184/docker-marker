import os
import subprocess

def install_pip_override():
    requirements_path = os.path.join('.', "requirements.override.txt")
    if os.path.exists(requirements_path):
        print("Installing override requirements...")
        subprocess.check_call(["pip", "install", "-r", requirements_path])
    else:
        print("No requirements.txt found.")
