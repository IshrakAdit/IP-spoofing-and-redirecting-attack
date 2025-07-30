#!/bin/bash

echo "[*] Setting up attacker-vm (192.168.56.10)..."

sudo bash -c 'cat > /etc/netplan/00-installer-config.yaml <<EOF
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: true          # NAT interface to reach internet
    enp0s8:
      dhcp4: no
      addresses: [192.168.56.10/24]
EOF'

sudo netplan apply
sleep 2

# Enable IP forwarding
sudo sysctl -w net.ipv4.ip_forward=1

# Enable NAT (Masquerading)
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE

# Allow forwarding: LAN <--> WAN
sudo iptables -A FORWARD -i enp0s8 -o enp0s3 -j ACCEPT
sudo iptables -A FORWARD -i enp0s3 -o enp0s8 -m state --state ESTABLISHED,RELATED -j ACCEPT

# Send ICMP redirect
echo "[*] Sending ICMP Redirect to victim..."
sudo python3 ~/Desktop/icmp_redirect.py
