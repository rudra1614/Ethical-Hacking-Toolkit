import os
import socket
import subprocess
import webbrowser

from core import HackingTool, HackingToolsCollection, clear_screen

class NMAP(HackingTool):
    TITLE = "NMAP - Network Discovery and Security Auditing"
    DESCRIPTION = "Free and open source utility for network discovery and security auditing."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nmap/nmap.git",
        "cd nmap && sudo chmod -R 755 . && sudo ./configure && make && sudo make install"
    ]
    PROJECT_URL = "https://github.com/nmap/nmap"

    def __init__(self):
        super().__init__(runnable=False)

class PhoneInfoga(HackingTool):
    TITLE = "PhoneInfoga - Advanced OSINT Framework for Phone Numbers"
    DESCRIPTION = "Advanced information gathering & OSINT framework for phone numbers."
    INSTALL_COMMANDS = [
        "curl -L https://github.com/sundowndev/phoneinfoga/releases/download/v2.0.8/phoneinfoga_$(uname -s)_$(uname -m).tar.gz -o phoneinfoga.tar.gz",
        "tar -xf phoneinfoga.tar.gz"
    ]
    RUN_COMMANDS = ["./phoneinfoga --help"]
    PROJECT_URL = "https://github.com/sundowndev/phoneinfoga"

class Dracnmap(HackingTool):
    TITLE = "Dracnmap - Exploit Networks with NMAP"
    DESCRIPTION = "Exploit the network and gather information with the help of nmap."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/Dracnmap.git",
        "cd Dracnmap && chmod +x dracnmap-v2.2*.sh"
    ]
    RUN_COMMANDS = ["cd Dracnmap && sudo ./dracnmap-v2.2.sh"]
    PROJECT_URL = "https://github.com/Screetsec/Dracnmap"

class PortScan(HackingTool):
    TITLE = "Port Scan - Port Scanning Target IP"

    def __init__(self):
        super().__init__(installable=False)

    def run(self):
        clear_screen()
        target = input("Enter Target IP: ")
        subprocess.run(["sudo", "nmap", "-O", "-Pn", target])

class Host2IP(HackingTool):
    TITLE = "Host to IP - Convert Host Name to IP"

    def __init__(self):
        super().__init__(installable=False)

    def run(self):
        clear_screen()
        host = input("Enter host name (e.g. www.google.com): ")
        ips = socket.gethostbyname(host)
        print("IP Address:", ips)

class XeroSploit(HackingTool):
    TITLE = "Xerosploit - Man-in-the-Middle Attack Testing Toolkit"
    DESCRIPTION = "A penetration testing toolkit aimed at performing Man-in-the-Middle attacks for testing purposes."
    INSTALL_COMMANDS = [
        "git clone https://github.com/LionSec/xerosploit.git",
        "cd xerosploit && sudo python install.py"
    ]
    RUN_COMMANDS = ["sudo xerosploit"]
    PROJECT_URL = "https://github.com/LionSec/xerosploit"

# Additional classes would be similarly updated...

class InformationGatheringTools(HackingToolsCollection):
    TITLE = "Information Gathering Tools"
    TOOLS = [
        NMAP(),
        PhoneInfoga(),
        Dracnmap(),
        PortScan(),
        Host2IP(),
        XeroSploit(),
    ]
