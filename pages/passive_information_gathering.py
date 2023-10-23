import streamlit as st
from subprocess import run
from osoperator import operator
import platform
import subprocess

st.header('HTTP')

target = st.text_input('Enter IP address or URL')

if st.button('Scan Vulnerabilities'):
    with st.spinner('Scanning...'):
        if platform.system() == "Linux" or platform.system() == "Darwin":
            result = subprocess.run(f'cd nikto/program {operator()} ./nikto.pl -h {target}', capture_output=True, shell=True, text=True)
        elif platform.system() == "Windows":
            result = subprocess.run(f'attrib +x nikto\\program\\nikto.pl {operator()} perl nikto\\program\\nikto.pl -h {target}', capture_output=True, shell=True, text=True)
        if result.stderr != '':
            st.code(result.stderr)
        else:
            st.code(result.stdout)