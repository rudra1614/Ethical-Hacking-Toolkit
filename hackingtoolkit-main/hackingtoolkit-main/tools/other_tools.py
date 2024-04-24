# coding=utf-8
import os
import subprocess
import shlex

from core import HackingTool
from core import HackingToolsCollection
from tools.others.android_attack import AndroidAttackTools
from tools.others.email_verifier import EmailVerifyTools
from tools.others.hash_crack import HashCrackingTools
from tools.others.homograph_attacks import IDNHomographAttackTools
from tools.others.mix_tools import MixTools
from tools.others.payload_injection import PayloadInjectorTools
from tools.others.socialmedia import SocialMediaBruteforceTools
from tools.others.socialmedia_finder import SocialMediaFinderTools
from tools.others.web_crawling import WebCrawlingTools
from tools.others.wifi_jamming import WifiJammingTools

class HatCloud(HackingTool):
    TITLE = "HatCloud - Bypass CloudFlare to discover real IP"
    DESCRIPTION = "HatCloud, built in Ruby, bypasses CloudFlare to discover the real IP of a server."
    INSTALL_COMMANDS = ["git clone https://github.com/HatBashBR/HatCloud.git"]
    PROJECT_URL = "https://github.com/HatBashBR/HatCloud"

    def run(self):
        site = input("Enter Site >> ").strip()
        try:
            if not os.path.exists("HatCloud"):
                print("HatCloud directory not found. Please install it using the provided commands.")
                return
            os.chdir("HatCloud")
            subprocess.run(["sudo", "ruby", "hatcloud.rb", "-b", shlex.quote(site)], check=True)
        except FileNotFoundError:
            print("Ruby or HatCloud is not installed. Please check your installation.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing HatCloud: {e}")
        finally:
            os.chdir("..")  # Return to the original directory

class OtherTools(HackingToolsCollection):
    TITLE = "Other tools"
    TOOLS = [
        HatCloud(),
        SocialMediaFinderTools(),
        WebCrawlingTools(),
        AndroidAttackTools(),
        EmailVerifyTools(),
        HashCrackingTools(),
        IDNHomographAttackTools(),
        MixTools(),
        PayloadInjectorTools(),
        SocialMediaBruteforceTools(),
        WifiJammingTools()
    ]
