FROM req-base

RUN pip3 install --no-cache-dir scapy
COPY attacker.py ./
CMD ["python3", "-u", "attacker.py"]
