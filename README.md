# Penetration Testing Project

Penetration Testing Project

### Functions
- Active Information Gathering [Done]
    - Network Information
    - Host information
    - Subnet active host
    - Usual Port Scan
    - Ports with version
- Passive Information Gathering [Done]
    - Whois
    - DNS information (linux only)
    - Web vulnerability information (linux only)
- Vulnerability Analysis
    - HTTP
        - SQL injection
        - NoSQL injection
        - Bypass file upload
    - Automated Vulnerability Scanners
- Exploiting
    - Reverse shell
- Post Exploitation
    - Privilege escalation - Linux
    - Privilege escalation - Windows
    - Bypass antivirus
    - Loot and enumerate
- Password Cracking
- Network traffic analysis
    - ARP spoofing
    - DNS spoofing
    - Wireshark
- Wireless
    - WEP
    - WPS

> For windows please install perl first:
[Link](https://platform.activestate.com/ActiveState-Projects/ActiveState-Perl-5.36.0)

``` powershell
sh <(curl -q https://platform.activestate.com/dl/cli/_pdli01/install.sh)
state checkout ActiveState-Projects/ActiveState-Perl-5.36.0 .
state use ActiveState-Perl-5.36.0
```

Require Package

``` shell 
pip3 install -r requirements.txt
```

Run
``` shell 
streamlit run home.py
```