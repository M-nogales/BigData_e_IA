rs.initiate({
    _id: "rs-config-server",
    configsvr: true,
    members: [
      { _id: 0, host: "configsvr1:27020" },
      { _id: 1, host: "configsvr2:27020" },
      { _id: 2, host: "configsvr3:27020" }
    ]
  });