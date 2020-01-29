# endpoint_web_speed
Programatically ship endpoint web browser preformance data to an AWS Elasticsearch Service endpoint.

This project is currently under Development. Please check back soon.

Selenium boots, and tries to fully load different websites, collects Preformance Timings listed below and shipps them to an AWS Elasticsearch Service.

Flow of Performance Timings on Web Browsers:

navigationStart -> redirectStart -> redirectEnd -> fetchStart -> domainLookupStart -> domainLookupEnd 
-> connectStart -> connectEnd -> requestStart -> responseStart -> responseEnd 
-> domLoading -> domInteractive -> domContentLoaded -> domComplete -> loadEventStart -> loadEventEnd



# Installation
1. Install the chromedriver by using the command `brew cask install chromedriver`
    - If you have already installed the chromedriver once and need to update it:
        - First try `brew cask install chromedriver`
        - If that errors try `brew cask reinstall chromedriver`
        - If that also errors run `rm /usr/local/bin/chromedriver` and then rerun `brew cask install chromedriver`
2. 
