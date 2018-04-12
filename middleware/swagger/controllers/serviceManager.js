'use strict';

var url = require('url');

module.exports.cioStats = function resetVMpin (req, res, next) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({
    "error" : "0",
    "warning" : "2",
    "ok" : "4",
    "inactive" : "2"
  }));
};

module.exports.cioSlas = function resetVMpin (req, res, next) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({
    "device_availability" : "90%",
    "uptime" : "4 days, 6:20:17.57",
    "problem_detected" : 5,
    "critical_status" : "False"
  }));
};

module.exports.directorTicketStatus = function resetVMpin (req, res, next) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({
    "opened" : 30,
    "closed" : 70
  }));
};

module.exports.directorMttr = function resetVMpin (req, res, next) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({
    "router" : 3,
    "switches" : 10,
    "other" : 1
  }));
};

module.exports.managerAvailability = function resetVMpin (req, res, next) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({
    "total_time":200, 
    "up":190, 
    "down":10
  }));
};

module.exports.managerLatency = function resetVMpin (req, res, next) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({
    "avgLatencyByHour" : [
        "20",
        "30",
        "90",
        "50",
        "88",
        "77",
        "56",
        "33",
        "10",
        "40",
        "43",
        "45",
        "50",
        "49",
        "47",
        "40",
        "55",
        "60",
        "54",
        "51",
        "44",
        "40",
        "30",
        "28",
    ]
  }));
};

module.exports.cioStats = function resetVMpin (req, res, next) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({
    "error" : "0",
    "warning" : "2",
    "ok" : "4",
    "inactive" : "2"
  }));
};


