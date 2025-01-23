// ./shard-init/shard3-init.js
rs.initiate({
    _id: "shard3",
    members: [
      { _id: 0, host: "shard3a:27030" },
      { _id: 1, host: "shard3b:27030" },
      { _id: 2, host: "shard3c:27030" }
    ]
  });