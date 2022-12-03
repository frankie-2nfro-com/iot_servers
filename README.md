# IoT and A.I. Servers Docker Setup
IoT devices trigger and send data to MQTT server and other clients subscribed to MQTT can get the data and process. 

(diagram of the servers)


## 1. Clone repository
```
> cd <root directory of the project workspace>
> git clone https://github.com/frankie-2nfro-com/iot_servers.git
```

## 2. Create a .env file to store credential information
```
INFLUXDB_USERNAME=admin
INFLUXDB_PASSWORD=<admin password of influxdb>
INFLUXDB_ORG=<organization name>
INFLUXDB_BUCKET=<bucket name>

WATCHTOWER_TOKEN_FOR_MODEL_SERVER=<watchtower token for accessing docker hub>
```

## 3. run the services
```
> docker compose --env-file ../docker_workspace.env up -d
```
(to check if all services is up normally, you can open the docker desktop to make sure all are up and running)
