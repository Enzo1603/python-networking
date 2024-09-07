sudo docker build -t traffic_server .

# 5002 UDP ??

sudo docker run -dit -p 5000:5000 -p 5001:5001 -p 5002:5002 --name traffic_server traffic_server

# kein Zugriff auf 5001, 5002? oder nur kein output?
