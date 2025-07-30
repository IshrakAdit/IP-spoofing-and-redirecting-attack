import os
import time

print("[*] Enabling ICMP redirect acceptance and disabling security filters...")

# Accepting ICMP redirects
os.system("sysctl -w net.ipv4.conf.all.accept_redirects=1")
os.system("sysctl -w net.ipv4.conf.default.accept_redirects=1")
os.system("sysctl -w net.ipv4.conf.eth0.accept_redirects=1")

# Disabling secure redirect filtering
os.system("sysctl -w net.ipv4.conf.all.secure_redirects=0")
os.system("sysctl -w net.ipv4.conf.default.secure_redirects=0")
os.system("sysctl -w net.ipv4.conf.eth0.secure_redirects=0")

# Disabling reverse path filtering (can block redirected routes)
os.system("sysctl -w net.ipv4.conf.all.rp_filter=0")
os.system("sysctl -w net.ipv4.conf.default.rp_filter=0")
os.system("sysctl -w net.ipv4.conf.eth0.rp_filter=0")

print("[*] Configuring default gateway to router...")
os.system("ip route del default || true")
os.system("ip route add default via 172.28.0.30")

print("[*] Initial routing table:")
os.system("ip route show")

counter = 0
while True:
    os.system("ping -c 1 172.28.0.100")
    counter += 1
    if counter % 5 == 0:
        print(f"[*] Routing table after {counter} pings:")
        os.system("ip route show")
    time.sleep(2)
