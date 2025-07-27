import os
import time

# Enable ICMP redirects at runtime
os.system("echo 1 > /proc/sys/net/ipv4/conf/all/accept_redirects")
os.system("echo 1 > /proc/sys/net/ipv4/conf/default/accept_redirects")

# Add a default gateway via router
print("[*] Setting default gateway to router (192.168.56.1)")
os.system("ip route add default via 192.168.56.1")

print("[*] Initial routing table:")
os.system("ip route show")

# Ping continuously and check routes
print("[*] Pinging 192.168.56.100 repeatedly")
counter = 0
while True:
    os.system("ping -c 1 192.168.56.100")
    counter += 1
    
    # Check routing table every 5 pings
    if counter % 5 == 0:
        print(f"[*] Routing table after {counter} pings:")
        os.system("ip route show")
    
    time.sleep(2)
