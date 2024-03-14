@echo off
set /p ip=<ip.txt
kali run "sudo service ssh start"
title wsl proxy
cls
title "wsl proxy | starting"
echo "RUNNING PROXY AT localhost:2432 PRESS CTRL+C FOLLOWED BY N TO SHUTOFF PROXY"
ssh -D 2432 -N -C default@%ip%
kali run "sudo service ssh stop"
title "wsl proxy | shut off"
cls
