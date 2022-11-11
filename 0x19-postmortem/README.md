# Server requests failure report
It was reported in the last week that all servers were returning status 500 error on all requests and call made. The root cause was established on server web-01
with the backup server web-02 having downtime as well.
## Timeline
The error on the server was recorder on October 21st 0900hrs East African Time. The master server was observerd to be lagging in speed.. The master server, web-01 was disconnected for detailed system analysis and all requests at the time channeled to server web-02. The error was resolved October 24th at 0900hrs EAT.
## Cause and resolution
The cause of outage was established to be memory outage. At the time, web-01 server was recieving all the incoming requests.The issue was fixed when the master server was temporarily disconnected for memory clean-up then later connected to the load balancer and the algorithm configured to serve client and the master servers with requests equally distributed between both servers.
## Prevention against such problem in the future
- Choose the most efficient load balancing algorithm
- Have back-up servers for downtime
- Constantly check on the running servers to ensure they are running properly.
