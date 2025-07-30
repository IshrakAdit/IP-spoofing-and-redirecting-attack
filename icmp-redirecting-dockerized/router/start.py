import os
import subprocess

def enable_ip_forwarding():
    res = subprocess.run(['sysctl', '-w', 'net.ipv4.ip_forward=1'], capture_output=True, text=True)
    print(res.stdout)
    print(res.stderr)

def main():
    print("[Router] Starting ICMP Redirecting Router...")
    enable_ip_forwarding()

    os.system('tail -f /dev/null')

if __name__ == "__main__":
    main()
