#!/bin/bash

echo "[*] Setting up victim-vm (192.168.56.20)..."

sudo bash -c 'cat > /etc/netplan/00-installer-config.yaml <<EOF
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: no
    enp0s8:
      dhcp4: no
      addresses: [192.168.56.20/24]
      gateway4: 192.168.56.1
EOF'

sudo netplan apply
sleep 2

# Accept ICMP redirects
sudo sysctl -w net.ipv4.conf.all.accept_redirects=1
sudo sysctl -w net.ipv4.conf.enp0s8.accept_redirects=1

# Show route to 8.8.8.8 before attack
echo "[*] Route to 8.8.8.8 before attack:"
ip route get 8.8.8.8

# Try pinging
ping -c 4 8.8.8.8
