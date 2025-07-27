FROM ubuntu:20.04

# Use a more stable mirror
RUN sed -i 's|http://archive.ubuntu.com/ubuntu|http://mirror.math.princeton.edu/pub/ubuntu|g' /etc/apt/sources.list

# Install basic network tools
RUN apt-get update --fix-missing && \
    apt-get install -y iputils-ping iproute2 tcpdump

# Enable IP forwarding
RUN echo 'net.ipv4.ip_forward = 1' >> /etc/sysctl.conf
