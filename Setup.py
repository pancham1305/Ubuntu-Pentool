import subprocess
import sys
import os

# List of tools to install (available in default repositories)
tools = [
    # Reconnaissance Tools
    "nmap",                # Nmap
    "theharvester",         # theHarvester
    "nikto",               # Nikto

    # Vulnerability Scanners
    "openvas",             # OpenVAS
    "nessus",              # Nessus (requires manual setup)

    # Exploitation Tools
    "metasploit-framework", # Metasploit Framework
    "sqlmap",              # SQLmap

    # Password Cracking Tools
    "john",                # John the Ripper
    "hydra",               # Hydra

    # Wireless Network Tools
    "aircrack-ng",         # Aircrack-ng
    "kismet",              # Kismet

    # Web Application Tools
    "zaproxy",             # OWASP ZAP
    "wfuzz",               # Wfuzz

    # Network Sniffing and Spoofing
    "wireshark",           # Wireshark
    "ettercap-graphical",  # Ettercap

    # Bonus Tools
    "dirb",                # Dirb
    "gobuster",            # Gobuster
]

def install_tools():
    print("Starting installation of tools...\n")
    
    # Update package list
    print("Updating package list...")
    subprocess.run(["sudo", "apt", "update"], check=True)
    
    # Install each tool
    for tool in tools:
        print(f"Installing {tool}...")
        try:
            subprocess.run(["sudo", "apt", "install", "-y", tool], check=True)
            print(f"{tool} installed successfully!\n")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {tool}. Error: {e}\n")
    
    print("Tools available in the default repositories have been installed.")
    print("\nAdditional steps for tools not in the default repositories:")

    # Install Recon-ng (via git and pip)
    print("\n1. Installing Recon-ng...")
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "git", "python3-pip"], check=True)
        subprocess.run(["git", "clone", "https://github.com/lanmaster53/recon-ng.git"], check=True)
        os.chdir("recon-ng")
        subprocess.run(["pip3", "install", "-r", "requirements.txt"], check=True)
        print("Recon-ng installed successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Recon-ng. Error: {e}\n")

    # Install Nessus (manual download)
    print("\n2. Nessus is not in the default repositories.")
    print("   Download it from https://www.tenable.com/downloads/nessus and install manually.")

    # Install Burp Suite (manual download)
    print("\n3. Burp Suite is not in the default repositories.")
    print("   Download it from https://portswigger.net/burp/releases and install manually.")

    # Install Hashcat (manual download for latest version)
    print("\n4. Hashcat is not in the default repositories.")
    print("   Download it from https://hashcat.net/hashcat/ and install manually.")

    # Install Cobalt Strike (manual download)
    print("\n5. Cobalt Strike is a commercial tool.")
    print("   Purchase and download it from https://www.cobaltstrike.com/.")

    # Install Empire (via git)
    print("\n6. Installing Empire...")
    try:
        subprocess.run(["git", "clone", "https://github.com/BC-SECURITY/Empire.git"], check=True)
        os.chdir("Empire")
        subprocess.run(["sudo", "./setup/install.sh"], check=True)
        print("Empire installed successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Empire. Error: {e}\n")

    # Install Shodan (via pip)
    print("\n7. Installing Shodan...")
    try:
        subprocess.run(["pip3", "install", "shodan"], check=True)
        print("Shodan installed successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Shodan. Error: {e}\n")

    print("\nAll tools installed or instructions provided!")

if __name__ == "__main__":
    # Check if the script is running with sudo privileges
    if not 'SUDO_UID' in os.environ.keys():
        print("Please run this script with sudo.")
        sys.exit(1)
    
    install_tools()