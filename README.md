<!-- Headings -->
# **Camelot Fortune**

![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/teknofage/camelot-fortune?sort=date&style=for-the-badge)

![CircleCI](https://img.shields.io/circleci/build/github/teknofage/Camelot-Fortune?style=for-the-badge)

![Docker Build Status](https://img.shields.io/docker/build/teknofage/camelot-fortune?style=for-the-badge)

![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/teknofage/Camelot-Fortune?style=for-the-badge)

![Website](https://img.shields.io/website?down_color=light%20grey&down_message=offline&style=for-the-badge&up_color=green&up_message=online&url=https%3A%2F%2Fcamelot-fortune.dev.teknofage.com)

## Camelot Fortune is an API for nobles and commoners of Camelot and surrounding princedoms alike to learn their fortunes.

___

⚠️ ⚠️ Disclaimer: This web application is still in development. 
.⚠️ ⚠️ 
___


### Table of Contents

* [Rationale](#Rationale)
* [Benefits](#Benefits)
* [Getting Started](#Getting_Started)
* [Useful Links](#Useful_Links)
* [Developers](#Developers)


#### Rationale

This was an small API app which was then developed for deployment.


#### Description

Users can answer questions and discover their fortune.


Frameworks: Flask 

Languages: Python 3


#### Benefits

It's fun.


#### Getting Started

##Docker Installation Instructions

Make sure you have Docker Hub installed and running on your machine.

```bash
$ git clone https://github.com/teknofage/Camelot-Fortune.git
```

Run the following commands:

## Docker
Make sure Docker is running
### Build the image
```bash
docker build -t camelot-fortune .
```
### Build the container
```bash
docker run -p 5000:5000 camelot-fortune camelot-fortune
```
### To see what's running
```bash
docker ps
```
### Run
```bash
docker-compose up
```
### To stop, run
```bash
docker-compose down




#### Useful Links

Live App: 

http://camelot-fortune.dev.teknofage.com


#### Developers

Created by teknofage

