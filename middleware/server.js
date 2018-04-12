'use strict';
var express = require('express');
var port = process.env.PORT || 8080;
var rest = require('node-rest-client').Client;
var fs = require('fs');
var path = require('path');
var jsyaml = require('js-yaml');
var swaggerTools = require('swagger-tools');

class NHCServer {
    constructor(runPort) {
        let thisNHCServer = this;
        this.MerakiDevices = {};
        this.UnityClients = {};
        this.expressApp = express();
        this.expressWs = require('express-ws')(this.expressApp);
        this.AddSwagger();
        this.AddUnityWSRoute();
        this.expressApp.listen(runPort, function () {
            console.log('Express server listening on port ' + runPort + ' in ' + thisNHCServer.expressApp.get('env') + ' mode');
        });
    }

    AddSwagger() {
        let thisNHCServer = this;

        let swaggerPath = path.resolve(__dirname, "swagger");

        let options = {
            swaggerUi: path.join(swaggerPath, 'swagger.json'),
            controllers: path.join(swaggerPath, 'controllers')
        };

        var spec = fs.readFileSync(path.join(swaggerPath, 'api/swagger.yaml'), 'utf8');
        var swaggerDoc = jsyaml.safeLoad(spec);

        swaggerTools.initializeMiddleware(swaggerDoc, function (middleware) {

            // Interpret Swagger resources and attach metadata to request - must be first in swagger-tools middleware chain
            thisNHCServer.expressApp.use(middleware.swaggerMetadata());

            // Validate Swagger requests
            thisNHCServer.expressApp.use(middleware.swaggerValidator());

            // Route validated requests to appropriate controller
            thisNHCServer.expressApp.use(middleware.swaggerRouter(options));

            // Serve the Swagger documents and Swagger UI
            thisNHCServer.expressApp.use(middleware.swaggerUi());

        });
    }

    AddUnityWSRoute() {
        let thisNHCServer = this;

        thisNHCServer.expressApp.ws('/unity', function (conn, req) {
            console.log("WS - new Unity connection from ip (" + conn._socket.remoteAddress + ")");
            let thisUnityClient = new UnityClient(thisNHCServer, conn, null);
            thisNHCServer.UnityClients[thisUnityClient.ClientID] = thisUnityClient;
        });
    }

    async GetMerakiDevices(apiKey, orgID) {
        let thisNHCServer = this;
        thisNHCServer.merakiHeaderArgs = {
            headers: {
                'x-cisco-meraki-api-key': apiKey,
                'Content-Type': 'application/json'
            }
        };
        thisNHCServer.merakiRestClient = new rest();
        let myNetworks = await thisNHCServer.GetNetworks(orgID);
        for (let i = 0; i < myNetworks.length; i++) {
            let networkObj = myNetworks[i];
            let myDevices = await thisNHCServer.GetDevicesByNetwork(myNetworks[i].id);
            for (let j = 0; j < myDevices.length; j++) {
                //let deviceKey = 
                thisNHCServer.MerakiDevices[myDevices[j].serial] = myDevices[j];
            }
        }
    }

    GetOrgs() {
        let thisNHCServer = this;

        return new Promise(function (resolve, reject) {
            thisNHCServer.merakiRestClient.get("https://api.meraki.com/api/v0/organizations", thisNHCServer.merakiHeaderArgs, function (data, response) {
                var error = null;
                var returnObj = null;
                resolve(data);
            });
        });
    }

    GetNetworks(orgID) {
        let thisNHCServer = this;

        return new Promise(function (resolve, reject) {
            thisNHCServer.merakiRestClient.get("https://api.meraki.com/api/v0/organizations/" + orgID + "/networks", thisNHCServer.merakiHeaderArgs, function (data, response) {
                var error = null;
                var returnObj = null;
                resolve(data);
            });
        });
    }

    GetDevicesByNetwork(networkID) {
        let thisNHCServer = this;

        return new Promise(function (resolve, reject) {
            thisNHCServer.merakiRestClient.get("https://api.meraki.com/api/v0/networks/" + networkID + "/devices", thisNHCServer.merakiHeaderArgs, function (data, response) {
                var error = null;
                var returnObj = null;
                resolve(data);
            });
        });
    }

    GetDeviceStatus(networkID, deviceSerial) {
        let thisNHCServer = this;

        return new Promise(function (resolve, reject) {
            thisNHCServer.merakiRestClient.get("https://api.meraki.com/api/v0/networks/" + networkID + "/devices/" + deviceSerial + "/uplink", thisNHCServer.merakiHeaderArgs, function (data, response) {
                var error = null;
                var returnObj = null;
                resolve(data);
            });
        });
    }

    GetConnectedClients(deviceSerial) {
        let thisNHCServer = this;

        return new Promise(function (resolve, reject) {
            thisNHCServer.merakiRestClient.get("https://api.meraki.com/api/v0/devices/" + deviceSerial + "/clients?timespan=84000", thisNHCServer.merakiHeaderArgs, function (data, response) {
                var error = null;
                var returnObj = null;
                resolve(data);
            });
        });
    }
}

// A Unity client connection
class UnityClient {
    constructor(nhcServer, wsConn, wsTarget) {
        var thisConnClient = this;
        this.NHCServer = nhcServer;
        this.wsConn = wsConn;
        this.connType = null;
        this.wsTarget = wsTarget;

        thisConnClient.wsConn.on('message', function incoming(data, flags) {
            // flags.binary will be set if a binary data is received.
            // flags.masked will be set if the data was masked.
            thisConnClient.ReceiveJSONCmd(data);
        });

        thisConnClient.wsConn.on('close', function (msg) {
            // Client session closed
            console.log("WS client disconnected");
        });

        thisConnClient.wsConn.on('error', function (error) {
            // Client session error
            console.log("Error connecting to Unity client [", wsTarget, "] - ", error);
        });
    }

    SendJSONCmd(cmd, data, token, stream) {
        var thisConnClient = this;
        thisConnClient.wsConn.send(JSON.stringify({
            'cmd': cmd,
            'data': data,
            'token': token,
            'stream': stream
        }));
    };

    SendJSONCmd_Promise(cmd, data) {
        var thisConnClient = this;
        return new Promise(function (resolve, reject) {
            var token = thisConnClient.NHCServer.Cortex.GenerateID();
            thisConnClient.ReturnCmdQueue[token] = function (message) {
                resolve(message);
            };
            thisConnClient.SendJSONCmd(cmd, data, token);
        });
    }

    async ReceiveJSONCmd(jsonMessage) {
        var thisUnityClient = this;
        var thisNHCServer = thisUnityClient.NHCServer;
        var message;
        try {
            message = JSON.parse(jsonMessage);
        } catch (e) {
            console.log("Received non-JSON message, disconnecting client... %s", thisUnityClient.wsConn._socket.remoteAddress);
            thisUnityClient.wsConn.close();
            return;
        }
        // Add logic to see if conn has been authorized
        if (message.cmd) {
            if (message.data && message.data['collectorID']) {
                //console.log("WS - Received cmd '" + message.cmd + "' from [" + message.data['collectorID'] + "]");
            } else {
                //console.log("WS - Received cmd '" + message.cmd + "'");
            }
            //console.dir(message.data);
            if (typeof (message.token) !== "undefined" && message.token !== null && thisUnityClient.ReturnCmdQueue.hasOwnProperty(message.token)) {
                // This is a response to a command we sent out
                thisUnityClient.ReturnCmdQueue[message.token](message);
                delete thisUnityClient.ReturnCmdQueue[message.token];
            } else {
                try {
                    switch (message.cmd) {
                        case 'GetMerakiDevices':
                            thisUnityClient.SendJSONCmd('MerakiDevices', thisNHCServer.MerakiDevices, null, null);
                            break;
                        default:
                            break;
                    }
                } catch (e) {
                    //console.log("Error processing command.  Here's the JSON data..." + jsonMessage);
                    console.log("Error processing command.");
                    DumpError(e);
                }
            }
        } else {
            console.log("Bad command.  Here's the JSON data..." + jsonMessage);
            thisUnityClient.wsConn.send("Bad command.  Here's the JSON data..." + jsonMessage);
        }
    }
}

let merakiAPIKey = "093b24e85df15a3e66f1fc359f4c48493eaa1b73";
let merakiOrgId = "549236";

let myNHCServer = new NHCServer(port);
myNHCServer.GetMerakiDevices(merakiAPIKey, merakiOrgId);