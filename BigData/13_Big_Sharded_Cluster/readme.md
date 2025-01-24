Create a complete sharded cluster with
3 shards:
- 1 replicaset:
 - 3 nodes
- 1 replciaset:
 - 3 nodes
- 1 replicaset:
 - 3 nodes
3 mongos(routers)
3 config nodes()
links:
https://medium.com/@yasasvi/mongodb-sharding-with-docker-c8b18bee32eb
https://phoenixnap.com/kb/mongodb-sharding


docker-compose -f big_sharded_cluster.yml up

docker exec configsvr1 sh -c "mongosh --port 27020 < /scripts/configserver-init.js"

docker exec shard1a sh -c "mongosh --port 27030 < /scripts/shard1-init.js"

docker exec shard2a sh -c "mongosh --port 27030 < /scripts/shard2-init.js"

docker exec shard3a sh -c "mongosh --port 27030 < /scripts/shard3-init.js"

docker exec mongos1 sh -c "mongosh --port 27017 < /scripts/router-init.js"

docker exec -it mongos1 mongosh --port 27017

sh.status()