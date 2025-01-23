// ./shard-init/shard1-init.js
rs.initiate({
    _id: "shard1",
    members: [
      { _id: 0, host: "shard1a:27030" },
      { _id: 1, host: "shard1b:27030" },
      { _id: 2, host: "shard1c:27030" }
    ]
  });