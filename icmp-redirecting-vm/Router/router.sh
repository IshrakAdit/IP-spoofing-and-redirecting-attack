#!/bin/bash

echo "[*] Setting up friend-vm (router - 192.168.56.1)..."

sudo bash -c 'cat > /etc/netplan/00-installer-config.yaml <<EOF
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: true
    enp0s8:
      dhcp4: no
      addresses: [192.168.56.1/24]
EOF'

sudo netplan apply
sleep 2

# Enable IP forwarding
sudo sysctl -w net.ipv4.ip_forward=1

# Enable NAT and forwarding
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
sudo iptables -A FORWARD -i enp0s8 -o enp0s3 -j ACCEPT
sudo iptables -A FORWARD -i enp0s3 -o enp0s8 -m state --state RELATED,ESTABLISHED -j ACCEPT

echo "[✓] Router setup complete"
