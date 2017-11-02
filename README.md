# Introduction

This repository contains the code for a Pomodoro web application.

This application allows you to run a pomodoro timer for custom contexts e.g. work, home.

Everytime you complete a pomodoro it gets stored in the database and you will be able to view your pomodoro history for the past few days as a bar graph.

# Launching the application

## Prerequisites

Make sure you have the following installed:

* bower
* docker
* docker-compose

## Steps to launch the application

```
git clone https://github.com/sirrah23/Pomodoro-App.git
cd Pomodoro-App
bower install
docker-compose build
docker-compose up
```
