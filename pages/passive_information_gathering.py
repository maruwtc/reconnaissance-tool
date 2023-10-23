import streamlit as st
from subprocess import run
from osoperator import operator
import platform
import subprocess
import whois
import pandas as pd

st.subheader('Domian Analysis')
whois_url = st.text_input('Enter domain name')
show_results = st.empty()
if st.button('Whois'):
    whois_data = whois.whois(whois_url)
    st.write("Domain Name: "+whois_data.get("domain_name", None))
    st.write("Registrar: "+whois_data.get("registrar", None))
    st.write("Whois Server: "+whois_data.get("whois_server", None))
    updated_date = whois_data.get("updated_date", None)
    if isinstance(updated_date, list):
        updated_date = ", ".join(str(date) for date in updated_date)
    st.write("Updated Date: " + str(updated_date))
    st.write("Creation Date: " + str(whois_data.get("creation_date", None)))
    st.write("Expiration Date: " + str(whois_data.get("expiration_date", None)))
    name_servers = whois_data.get("name_servers", None)
    if name_servers:
        lowercase_name_servers = [server.lower() for server in name_servers]
        unique_name_servers = sorted(list(set(lowercase_name_servers)))
        name_servers_df = pd.DataFrame(unique_name_servers, columns=["Name Servers"])
        st.dataframe(name_servers_df, hide_index=True)
    else:
        st.write("No name servers found.")

    st.subheader('DNS records')

if st.button('DNS Reconn'):
    result = subprocess.run(f'dnsrecon -d {whois_url}', capture_output=True, shell=True, text=True)
    if result.stderr != '':
        st.code(result.stderr)
    else:
        st.code(result.stdout)

st.divider()

st.subheader('HTTP Vulnerability Scan')

target = st.text_input('Enter IP address or URL')

if st.button('Scan Vulnerabilities'):
    with st.spinner('Scanning...'):
        if platform.system() == "Linux" or platform.system() == "Darwin":
            result = subprocess.run(f'./nikto/program/nikto.pl -h {target}', capture_output=True, shell=True, text=True)
        elif platform.system() == "Windows":
            result = subprocess.run(f'attrib +x nikto\\program\\nikto.pl ; perl nikto\\program\\nikto.pl -h {target}', capture_output=True, shell=True, text=True)
        if result.stderr != '':
            st.code(result.stderr)
        else:
            st.code(result.stdout)