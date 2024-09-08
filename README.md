```bash
sudo docker build -t traffic_server .
```

# 6002 UDP ??

```bash
sudo docker run -dit -p 7000:7000 -p 7001:7001 -p 7002:7002 --name traffic_server traffic_server
```

# kein Zugriff auf 5001, 5002? oder nur kein output?
