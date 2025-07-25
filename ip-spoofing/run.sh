docker build -f Dockerfile.scapy -t scapy-base .
docker compose up --build -d
docker logs -f spoofing-attacker-1
docker logs -f spoofing-receiver-1
docker logs -f spoofing-victim-1
# docker compose down -v
# docker system prune -a --volumes -f