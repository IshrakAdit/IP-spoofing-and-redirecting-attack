FROM ubuntu:20.04

# Use a more stable mirror
RUN sed -i 's|http://archive.ubuntu.com/ubuntu|http://mirror.math.princeton.edu/pub/ubuntu|g' /etc/apt/sources.list

# Install required packages
RUN apt-get update --fix-missing && \
    apt-get install -y python3 python3-pip iputils-ping iproute2 tcpdump

# Install scapy
RUN pip3 install scapy

COPY attacker.py /attacker.py
CMD ["python3", "/attacker.py"]
