// ./configserver-init.js
rs.initiate({
    _id: "rs-config-server",
    configsvr: true,
    members: [
      { _id: 0, host: "configsvr1:27018" },
      { _id: 1, host: "configsvr2:27018" },
      { _id: 2, host: "configsvr3:27018" }
    ]
  });