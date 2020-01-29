# AWS-Elasticsearch-Web-Performance-Shipper

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Made%20With-Python%203.7-blue.svg?style=for-the-badge" alt="Made with Python 3.7">
  </a>
</p>

<p align="center">
Programatically ship endpoint web browser preformance data to an AWS Elasticsearch Service endpoint.
This project is currently under Development. Please check back soon.
</p>

## Table of Contents

- [Web Performance Shipper](#web-performance-shipper)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Run This Yourself](#run-this-yourself)
    - [Local Development](#local-development)
      - [Without Docker](#without-docker)
      - [With Docker](#with-docker)
    - [Production](#production)
  - [Dependencies](#dependencies)
  - [Meet the Team](#meet-the-team)

## Overview
Selenium boots, and tries to fully load different websites, collects Preformance Timings listed below and shipps them to an AWS Elasticsearch Service.

Flow of Performance Timings on Web Browsers:

navigationStart -> redirectStart -> redirectEnd -> fetchStart -> domainLookupStart -> domainLookupEnd 
-> connectStart -> connectEnd -> requestStart -> responseStart -> responseEnd 
-> domLoading -> domInteractive -> domContentLoaded -> domComplete -> loadEventStart -> loadEventEnd

## Project Structure

See below for an explanation of the files in the tree.



## Run This Yourself

### Local Development

#### Without Docker

1. Clone this repository.
2. Run `pip install -r requirements.txt` to install the dependencies.
3. Generate some (AWS Elasticsearch Service) keys, and put them in a `src/config.py` file like so:

_Please use [`src/config_template.py`](src/config_template.py) file as a template._

```python
AWS_ES_ENDPOINT = {
    'aws_access_key_id': '',
    'aws_secret_access_key': '',
    'host': '',
    'region': '',
    'service': ''
}
```

4. To add the Elasticsearch index and source specific details look into the `src/config.py` you created, and put them in like so:

_Please use [`src/config_template.py`](src/config_template.py) as a reference._

``` python
ES_INDEX = {
    'index': '',
    'doc_type': '',
    'source': ''
}
```

5. To add websites (i.e. `https://www.google.com`) look into the `src/config.py` you created, and put them in like so:

_Please use [`src/config_template.py`](src/config_template.py) as a reference._

```python
webPage = ["https://www.google.com"]
```

6. Install the ChromeDriver by using the command specific to your OS:

  - On macOS: `brew cask install chromedriver`
    - Use Homebrew to install the chrome driver by running the command: `brew cask install chromedriver`
      - If you have already installed the ChromeDriver once and need to update it:
          - First try `brew cask install chromedriver`
          - If that errors try `brew cask reinstall chromedriver`
          - If that also errors run `rm /usr/local/bin/chromedriver` and then rerun `brew cask install chromedriver`
    - Confirm it installed by running: `chromedriver -version`

  - On Windows: `choco install chromedriver`
    - Start by installing the [Chocolatey](https://chocolatey.org/docs/installation) dependency manager using the [Install with CMD](https://chocolatey.org/docs/installation#install-with-cmdexe) method.
    - Then install the ChromeDriver by running: `choco install chromedriver`
    - Confirm it installed by running: `chromedriver -version`

7. 

#### With Docker

### Production

This data shipper is running on `Python 3.7`. We strongly advise the use of [Anaconda](https://www.anaconda.com/distribution/) to manage a virtual environment in which you can install the dependencies.

#### Without Docker

We strongly recommend that this data shipper be run on a docker instance (due to the ease of installation) on the host machine, however if you choose not to, the steps below outline the installation procedure.

1. Clone this repository.
2. Run `pip install -r requirements.txt` to install the dependencies.
3. Generate some (AWS Elasticsearch Service) keys, and put them in a `src/config.py` file like so:

_Please use [`src/config_template.py`](src/config_template.py) file as a template._

```python
AWS_ES_ENDPOINT = {
    'aws_access_key_id': '',
    'aws_secret_access_key': '',
    'host': '',
    'region': '',
    'service': ''
}
```

4. To add the Elasticsearch index and source specific details look into the `src/config.py` you created, and put them in like so:

_Please use [`src/config_template.py`](src/config_template.py) as a reference._

``` python
ES_INDEX = {
    'index': '',
    'doc_type': '',
    'source': ''
}
```

5. To add websites (i.e. `https://www.google.com`) look into the `src/config.py` you created, and put them in like so:

_Please use [`src/config_template.py`](src/config_template.py) as a reference._

```python
webPage = ["https://www.google.com"]
```

6. Install the ChromeDriver by using the command for your specific OS:

  - On macOS: `brew cask install chromedriver`
    - Use Homebrew to install the chrome driver by running the command: `brew cask install chromedriver`
      - If you have already installed the ChromeDriver once and need to update it:
          - First try `brew cask install chromedriver`
          - If that errors try `brew cask reinstall chromedriver`
          - If that also errors run `rm /usr/local/bin/chromedriver` and then rerun `brew cask install chromedriver`
    - Confirm it installed by running: `chromedriver -version`

  - On Windows: `choco install chromedriver`
    - Start by installing the [Chocolatey](https://chocolatey.org/docs/installation) dependency manager using the [Install with CMD](https://chocolatey.org/docs/installation#install-with-cmdexe) method.
    - Then install the ChromeDriver by running: `choco install chromedriver`
    - Confirm it installed by running: `chromedriver -version`

7. Run `./run.py` and you're off!

## Dependencies

## Meet the Team
<div>
  <p align="center">
    <a href="https://github.com/coreysabia">
      <img src="https://avatars1.githubusercontent.com/u/12410796?s=400&u=ee153e9c9496939767c01315212efb65936c01e8&v=4" height="100px" width="100px" alt="Version 1.0">
    </a>
    <p align="center"><strong>Corey Sabia</strong></p>
    <p align="center">Lead Developer</p>
    <p align="center"></p>
  </p>
</div>
