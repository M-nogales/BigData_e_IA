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

[direct: mongos] bigdatabase> sh.enableSharding('bigdatabase')
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1738168584, i: 2 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1738168584, i: 2 })
}
[direct: mongos] bigdatabase> sh.shardCollection('bigdatabase.testCollection', { shardKey: 1 })
MongoServerError[InvalidOptions]: Please create an index that starts with the proposed shard key before sharding the collection. 
[direct: mongos] bigdatabase> db.testCollection.createIndex({ shardKey: 1 })
shardKey_1
[direct: mongos] bigdatabase> db.testCollection.getShardDistribution()
MongoshInvalidInputError: [SHAPI-10001] Collection testCollection is not sharded
[direct: mongos] bigdatabase> db.getShardDistribution()
TypeError: db.getShardDistribution is not a function
[direct: mongos] bigdatabase> sh.shardCollection('bigdatabase.testCollection', { shardKey: 1 })
{
  collectionsharded: 'bigdatabase.testCollection',
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1738168644, i: 41 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1738168644, i: 41 })
}
[direct: mongos] bigdatabase> db.testCollection.getShardDistribution()
Shard shard3 at shard3/shard3a:27030,shard3b:27030,shard3c:27030
{
  data: '1.54GiB',
  docs: 55000,
  chunks: 1,
  'estimated data per chunk': '1.54GiB',
  'estimated docs per chunk': 55000
}
---
Shard shard2 at shard2/shard2a:27030,shard2b:27030,shard2c:27030
{
  data: '255.92MiB',
  docs: 8902,
  chunks: 2,
  'estimated data per chunk': '127.96MiB',
  'estimated docs per chunk': 4451
}
---
Shard shard1 at shard1/shard1a:27030,shard1b:27030,shard1c:27030
{
  data: '127.96MiB',
  docs: 4451,
  chunks: 1,
  'estimated data per chunk': '127.96MiB',
  'estimated docs per chunk': 4451
}
---
Totals
{
  data: '1.91GiB',
  docs: 68353,
  chunks: 4,
  'Shard shard3': [
    '80.46 % data',
    '80.46 % docs in cluster',
    '29KiB avg obj size on shard'
  ],
  'Shard shard2': [
    '13.02 % data',
    '13.02 % docs in cluster',
    '29KiB avg obj size on shard'
  ],
  'Shard shard1': [
    '6.51 % data',
    '6.51 % docs in cluster',
    '29KiB avg obj size on shard'
  ]
}
[direct: mongos] bigdatabase> db.testCollection.getShardDistribution()
Shard shard3 at shard3/shard3a:27030,shard3b:27030,shard3c:27030
{
  data: '1.54GiB',
  docs: 55000,
  chunks: 1,
  'estimated data per chunk': '1.54GiB',
  'estimated docs per chunk': 55000
}
---
Shard shard2 at shard2/shard2a:27030,shard2b:27030,shard2c:27030
{
  data: '511.85MiB',
  docs: 17804,
  chunks: 4,
  'estimated data per chunk': '127.96MiB',
  'estimated docs per chunk': 4451
}
---
Shard shard1 at shard1/shard1a:27030,shard1b:27030,shard1c:27030
{
  data: '383.89MiB',
  docs: 13353,
  chunks: 3,
  'estimated data per chunk': '127.96MiB',
  'estimated docs per chunk': 4451
}
---
Totals
{
  data: '2.41GiB',
  docs: 86157,
  chunks: 8,
  'Shard shard3': [
    '63.83 % data',
    '63.83 % docs in cluster',
    '29KiB avg obj size on shard'
  ],
  'Shard shard2': [
    '20.66 % data',
    '20.66 % docs in cluster',
    '29KiB avg obj size on shard'
  ],
  'Shard shard1': [
    '15.49 % data',
    '15.49 % docs in cluster',
    '29KiB avg obj size on shard'
  ]
}
[direct: mongos] bigdatabase> db.testCollection.getShardDistribution()

--------------------------------------------------------------------------------------

alumno@A-325-PC13 MINGW64 ~/Desktop/Tarde_BigData/BigData_e_IA/BigData (main)
$ docker run -d --name shard4a --net big_sharded_cluster -p 27140:27030 mongo --replSet shard4 --shardsvr --port 27030 --bind_ip_all
13d114535aba4088db0d958f87f5ad3af6189e209940ad604cb7d47f6808eb80

alumno@A-325-PC13 MINGW64 ~/Desktop/Tarde_BigData/BigData_e_IA/BigData (main)
$ docker run -d --name shard4b --net big_sharded_cluster -p 27141:27030 mongo --replSet shard4 --shardsvr --port 27030 --bind_ip_all
99a65a6e8e3a1af8c6fc0590937c09643ab14987ff5fb54acf55b1cc871e30b0

alumno@A-325-PC13 MINGW64 ~/Desktop/Tarde_BigData/BigData_e_IA/BigData (main)
$ docker run -d --name shard4c --net big_sharded_cluster -p 27142:27030 mongo --replSet shard4 --shardsvr --port 27030 --bind_ip_all
d3f4786625778ddb8becd1c7039e7707f539ddfa15db33f553cfaae63c17eecd

alumno@A-325-PC13 MINGW64 ~/Desktop/Tarde_BigData/BigData_e_IA/BigData (main)
$ docker exec -it shard4a mongosh --port 27030
Current Mongosh Log ID: 679a5adb06a2ee5b24fe6910
Connecting to:          mongodb://127.0.0.1:27030/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.2
Using MongoDB:          8.0.1
Using Mongosh:          2.3.2

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

------
   The server generated these startup warnings when booting
   2025-01-29T16:43:55.113+00:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
   2025-01-29T16:43:55.623+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2025-01-29T16:43:55.623+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-01-29T16:43:55.623+00:00: We suggest setting the contents of sysfsFile to 0.
   2025-01-29T16:43:55.623+00:00: Your system has glibc support for rseq built in, which is not yet supported by tcmalloc-google and has critical performance implications. Please set the environment variable GLIBC_TUNABLES=glibc.pthread.rseq=0
   2025-01-29T16:43:55.623+00:00: vm.max_map_count is too low
   2025-01-29T16:43:55.623+00:00: We suggest setting swappiness to 0 or 1, as swapping can cause performance problems.
------

test> rs.initiate({
t: "shard4b:27030" },
    { _id: 2, host: "shard4c:27030" }
  ]
})
...   _id: "shard4",
...   members: [
...     { _id: 0, host: "shard4a:27030" },
...     { _id: 1, host: "shard4b:27030" },
...     { _id: 2, host: "shard4c:27030" }
...   ]
... })
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1738169068, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1738169068, i: 1 })
}
shard4 [direct: secondary] test> rs.status()
{
  set: 'shard4',
  date: ISODate('2025-01-29T16:44:37.220Z'),
  myState: 2,
  term: Long('0'),
  syncSourceHost: '',
  syncSourceId: -1,
  heartbeatIntervalMillis: Long('2000'),
  majorityVoteCount: 2,
  writeMajorityCount: 2,
  votingMembersCount: 3,
  writableVotingMembersCount: 3,
  optimes: {
    lastCommittedOpTime: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
    lastCommittedWallTime: ISODate('2025-01-29T16:44:28.676Z'),
    readConcernMajorityOpTime: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
    appliedOpTime: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
    durableOpTime: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
    writtenOpTime: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
    lastAppliedWallTime: ISODate('2025-01-29T16:44:28.676Z'),
    lastDurableWallTime: ISODate('2025-01-29T16:44:28.676Z'),
    lastWrittenWallTime: ISODate('2025-01-29T16:44:28.676Z')
  },
  lastStableRecoveryTimestamp: Timestamp({ t: 1738169068, i: 1 }),
  members: [
    {
      _id: 0,
      name: 'shard4a:27030',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 42,
      optime: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
      optimeDate: ISODate('2025-01-29T16:44:28.000Z'),
      optimeWritten: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
      optimeWrittenDate: ISODate('2025-01-29T16:44:28.000Z'),
      lastAppliedWallTime: ISODate('2025-01-29T16:44:28.676Z'),
      lastDurableWallTime: ISODate('2025-01-29T16:44:28.676Z'),
      lastWrittenWallTime: ISODate('2025-01-29T16:44:28.676Z'),
      syncSourceHost: '',
      syncSourceId: -1,
      infoMessage: '',
      configVersion: 1,
      configTerm: 0,
      self: true,
      lastHeartbeatMessage: ''
    },
    {
      _id: 1,
      name: 'shard4b:27030',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 8,
      optime: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
      optimeDurable: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
      optimeWritten: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
      optimeDate: ISODate('2025-01-29T16:44:28.000Z'),
      optimeDurableDate: ISODate('2025-01-29T16:44:28.000Z'),
      optimeWrittenDate: ISODate('2025-01-29T16:44:28.000Z'),
      lastAppliedWallTime: ISODate('2025-01-29T16:44:28.676Z'),
      lastDurableWallTime: ISODate('2025-01-29T16:44:28.676Z'),
      lastWrittenWallTime: ISODate('2025-01-29T16:44:28.676Z'),
      lastHeartbeat: ISODate('2025-01-29T16:44:37.217Z'),
      lastHeartbeatRecv: ISODate('2025-01-29T16:44:36.750Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: '',
      syncSourceId: -1,
      infoMessage: '',
      configVersion: 1,
      configTerm: 0
    },
    {
      _id: 2,
      name: 'shard4c:27030',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 8,
      optime: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
      optimeDurable: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
      optimeWritten: { ts: Timestamp({ t: 1738169068, i: 1 }), t: Long('-1') },
      optimeDate: ISODate('2025-01-29T16:44:28.000Z'),
      optimeDurableDate: ISODate('2025-01-29T16:44:28.000Z'),
      optimeWrittenDate: ISODate('2025-01-29T16:44:28.000Z'),
      lastAppliedWallTime: ISODate('2025-01-29T16:44:28.676Z'),
      lastDurableWallTime: ISODate('2025-01-29T16:44:28.676Z'),
      lastWrittenWallTime: ISODate('2025-01-29T16:44:28.676Z'),
      lastHeartbeat: ISODate('2025-01-29T16:44:37.217Z'),
      lastHeartbeatRecv: ISODate('2025-01-29T16:44:36.759Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: '',
      syncSourceId: -1,
      infoMessage: '',
      configVersion: 1,
      configTerm: 0
    }
  ],
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1738169068, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1738169068, i: 1 })
}
shard4 [direct: secondary] test>

---------------------------------------------------------------------------
docker run -d --name shard4a --net big_sharded_cluster -p 27140:27030 mongo --replSet shard4 --shardsvr --port 27030 --bind_ip_all
docker run -d --name shard4b --net big_sharded_cluster -p 27141:27030 mongo --replSet shard4 --shardsvr --port 27030 --bind_ip_all
docker run -d --name shard4c --net big_sharded_cluster -p 27142:27030 mongo --replSet shard4 --shardsvr --port 27030 --bind_ip_all
----------------------------------------------------------------------------