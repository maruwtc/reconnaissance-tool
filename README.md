# Penetration Testing Project

For windows please install perl first:
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
stream run home.py
```