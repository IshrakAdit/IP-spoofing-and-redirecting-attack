FROM ubuntu:20.04

# Use a more stable mirror
RUN sed -i 's|http://archive.ubuntu.com/ubuntu|http://mirror.math.princeton.edu/pub/ubuntu|g' /etc/apt/sources.list

# Install required packages
RUN apt-get update --fix-missing && \
    apt-get install -y iputils-ping iproute2 python3 tcpdump

# Enable ICMP redirect acceptance
RUN echo 'net.ipv4.conf.all.accept_redirects = 1' >> /etc/sysctl.conf && \
    echo 'net.ipv4.conf.default.accept_redirects = 1' >> /etc/sysctl.conf

COPY test_ping.py /test_ping.py
CMD ["python3", "/test_ping.py"]

