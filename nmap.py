import nmap3

def nmap_quick_scan(target):
    nmap = nmap3.Nmap()
    quick_result = nmap.scan_top_ports(target)
    return quick_result

def nmap_ver_scan(target):
    nmap = nmap3.Nmap()
    version_result = nmap.nmap_version_detection(target)
    return version_result

def nmap_ping_scan(target):
    nmap = nmap3.NmapScanTechniques()
    ping_result = nmap.nmap_ping_scan(target)
    return ping_result