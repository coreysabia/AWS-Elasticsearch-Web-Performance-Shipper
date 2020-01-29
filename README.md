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


```
name: EWS Python

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v1
    - name: Set up Python 3.7
      uses: actions/setup-python@v1
      with:
        python-version: 3.7
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Lint with flake8
      run: |
        pip install flake8
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pip install pytest
        pytest src/test.py
```