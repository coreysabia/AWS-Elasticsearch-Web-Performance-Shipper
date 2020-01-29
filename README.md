# AWS-Elasticsearch-Web-Speed-Shipper

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Made%20With-Python%203.7-blue.svg?style=for-the-badge" alt="Made with Python 3.7">
  </a>
</p>

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
