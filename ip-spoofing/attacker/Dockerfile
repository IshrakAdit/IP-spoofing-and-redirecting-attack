FROM scapy-base
COPY spoof.py sniff.py ./
CMD ["sh", "-c", "sleep 5 && python3 spoof.py 10.10.10.10 10.10.10.20 'Spoofed ping' && python3 sniff.py"]
