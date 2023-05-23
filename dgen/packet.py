import sys
from scapy.all import sr1, IP, ICMP

r = sr1(IP(dst='192.168.20.29')/ICMP()/'HelloWorld')
r.show()