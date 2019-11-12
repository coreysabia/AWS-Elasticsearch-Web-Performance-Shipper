# endpoint_web_speed
 Visualize how long it takes for endpoints on your network to load the web with this dynamic, lightweight data shipper.

This project is currently under Development. Please check back later.

Every 5 min
Selenium boots, and tries to fully load 5 different

Flow of Performance Timings on Web Browsers:

navigationStart -> redirectStart -> redirectEnd -> fetchStart -> domainLookupStart -> domainLookupEnd 
-> connectStart -> connectEnd -> requestStart -> responseStart -> responseEnd 
-> domLoading -> domInteractive -> domContentLoaded -> domComplete -> loadEventStart -> loadEventEnd



TO DO:
3. Automate operation to run every 5 minutes?? NOTES: CRON NOT WORKING IN DOCKER

