import psutil, socket
import netifaces # pip install netifaces
import dns.resolver # pip install dnspython

def get_net():
    interfaces = []
    ip_addresses = []
    subnet_masks = []
    gateways = []

    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                iface = interface
                ip = addr.address

                if iface and ip:
                    first_octet = int(ip.split('.')[0])
                    if (first_octet == 10) or (first_octet == 172 and 16 <= int(ip.split('.')[1]) <= 31) or (first_octet == 192 and int(ip.split('.')[1]) == 168):
                        interfaces.append(iface)
                        ip_addresses.append(ip)
                        subnet_masks.append(socket.inet_ntoa(socket.inet_aton(addr.netmask)))
                        gateways.append(netifaces.gateways()['default'][netifaces.AF_INET][0])

    return interfaces, ip_addresses, subnet_masks, gateways

for interface in psutil.net_if_addrs():
    if psutil.net_if_addrs()[interface][0].address:
        winmac = (psutil.net_if_addrs()[interface][0].address)
        break

# Results in arrays
interfaces_arr, ip_addresses_arr, subnet_mask_arr, gateways_arr = get_net()

# Results in lines
interface_result = '\n'.join(interfaces_arr)
ip_address_result = '\n'.join(ip_addresses_arr)
subnet_mask_result = '\n'.join(subnet_mask_arr)
gatway_result = '\n'.join(gateways_arr)

# DNS
dns_resolver = dns.resolver.Resolver()
dns_result = ', '.join(str(ip) for ip in dns_resolver.nameservers)