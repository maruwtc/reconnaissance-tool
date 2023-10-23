from get_int import interfaces_arr, ip_addresses_arr, subnet_mask_arr, gateways_arr, dns_result, winmac
from nmap import nmap_quick_scan, nmap_ver_scan, nmap_ping_scan
from cidr import subnet_cidr
import streamlit as st
import pandas as pd 

st.subheader('Network Information')
data = {'Interface': interfaces_arr, 'IP Address': ip_addresses_arr, 'Subnet Mask': subnet_mask_arr, 'Gateway': gateways_arr, 'DNS Server': dns_result}
df = pd.DataFrame(data)
st.dataframe(df, hide_index=True, use_container_width=True)

st.divider()

ethernet_df = df[df['Interface'] == 'Ethernet']
if not ethernet_df.empty:
    host_ip = ethernet_df.iloc[0]['IP Address']
else:
    gateway_subnet = df.iloc[0]['Subnet Mask']
    subnet_df = df[df['Subnet Mask'] == gateway_subnet]
    if not subnet_df.empty:
        host_ip = subnet_df.iloc[0]['IP Address']

st.subheader('Host information')
quick_scan_result = nmap_quick_scan(host_ip)
sysinfo_scan_result = []
port_scan_results = []
for hostname in quick_scan_result.get(host_ip, {}).get('hostname', []):
    st.write('Hostname: '+hostname.get('name', ''))
if quick_scan_result.get(host_ip, {}).get('macaddress', ''):
    st.write('MAC Address: ' + quick_scan_result.get(host_ip, {}).get('macaddress', ''))
    st.write('MB Vendor: '+quick_scan_result.get(host_ip, {}).get('macaddress', {}).get('vendor', ''))
else:
    st.write('MAC Address: '+winmac)
    st.write('MB Vendor: Unknown')
st.write('Up reason: '+quick_scan_result.get(host_ip, {}).get('state', {}).get('reason', ''))

st.divider()

st.subheader('Subnet active host')
if st.button('Ping'):
    ping_result = nmap_ping_scan(subnet_cidr)
    filtered_data = pd.DataFrame({
        'IP Address': [ip for ip, data in ping_result.items() if 'state' in data and data['state'].get('state') == 'up'],
        'State': ['up' for ip, data in ping_result.items() if 'state' in data and data['state'].get('state') == 'up']
    })
    st.subheader('Subnet active host where state is up')
    st.dataframe(filtered_data, hide_index=True, use_container_width=True)

st.divider()

st.subheader('Usual Port Scan')
ups_ip = st.text_input('To scan usual port, enter IP address or click leave blank to scan current host')

if st.button('Start'):
    with st.spinner('Scanning...'):
        st.subheader('Usual Ports (Enter IP): ' if ups_ip != "" else 'Usual Ports (Host): ')
        quick_scan_result = nmap_quick_scan(ups_ip) if ups_ip != "" else nmap_quick_scan(host_ip)
        port_scan_results = []
        for portinfo in quick_scan_result.get(ups_ip if ups_ip != "" else host_ip, {}).get('ports', []):
            scan_results = {
                "service": portinfo.get('service', {}).get('name', ''),
                "port": portinfo.get('portid', ''),
                "protocol": portinfo.get('protocol', ''),
                "state": portinfo.get('state', ''),
            }
            port_scan_results.append(scan_results)
        
        portinfo = pd.DataFrame(port_scan_results)
        st.dataframe(portinfo, hide_index=True)

st.divider()

st.subheader('Ports with version')
ver_ip = st.text_input('To scan port with version, Enter IP address or Click leave blank to scan current host')
if st.button('Services Version Scan'):
    with st.spinner('Scanning...'):
        if ver_ip != '':
            ver_scan_result = nmap_ver_scan(ver_ip)
            host = ver_ip
        else:
            ver_scan_result = nmap_ver_scan(host_ip)
            host = host_ip

        sysinfo_scan_result = []
        for portinfo in ver_scan_result.get(host, {}).get('ports', []):
            scan_results = {
                "protocol": portinfo.get('protocol', 'unknown'),
                "port": portinfo.get('portid', 'unknown'),
                "state": portinfo.get('state', 'unknown'),
                "service name": portinfo.get('service', {}).get('name', 'unknown'),
                "service product": portinfo.get('service', {}).get('product', 'unknown'),
                "service extrainfo": portinfo.get('service', {}).get('extrainfo', 'unknown'),
            }
            sysinfo_scan_result.append(scan_results)
        portinfo = pd.DataFrame(sysinfo_scan_result)
        st.write(host + "'s scanning result")
        st.dataframe(portinfo, hide_index=True, use_container_width=True)