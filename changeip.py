import os
import random

path = "D:\proxy\ip.txt"

with open(path, 'r') as file:
 currentip = file.read()
 newip = random.randrange(2,254)
 while newip == currentip:
  newip = random.randrange(2,254)

newip = str(newip)

with open(path, 'w') as writefile:
 writefile.write("172.17.131.%s" % newip)

os.system('kali run sudo ifconfig eth0 172.17.131.%s' % newip)
input()