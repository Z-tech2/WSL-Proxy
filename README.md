WSL PROXY

-------
REQUIREMENTS:
Kali Linux installed with WSL.
Python installed.
A windows computer with WSL installed.
-------
STARTUP GUIDE:
Go to WSL and make sure openssh-server is installed. To check, type "sudo service ssh"
Go to WSL and find the inet ipv4 of your wsl machine. Copy this value.
Go to ip.txt and change the inside value of this to the ipv4 you recently copied.
Go to WSL and use "whoami". Copy this value.
Go to start.bat and replace all instances of the word "default" with what you copied.
Go to changeip.bat and replace all isntances of the word "default" with what you copied.
-------
USAGE GUIDE:
Use changeip.py to change the proxy's IP address.
Use start.bat to start up the proxy server.
If you're using firefox, go to settings > proxy settings > manual proxy configuration >  SOCKS Host > localhost > port 2432 > SOCKS v5

If you want to route ALL of your traffic through this proxy and you're using windows, go to settings, Network & Internet > Proxy > Use a proxy server > Setup > Use a proxy server ON > localhost port 2432
-------
TURNING OFF PROXY:
Go to start.bat
When prompted to press Ctrl+C to stop proxy, proceed to press Ctrl+C followed by N.
When prompted to type in your WSL machine's password, do it.