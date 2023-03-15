# Introduction

A telegram bot that allows users to save and view bus timings for their favourite bus stops.

# Accomplishments

- Created a telegram bot with a UI that allows users to add, remove, and view bus stop data
- Created a script to scrapes all bus stop data from LTA's API with [LTA's permission](https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html)

# Non-project accomplishments

- Create a cron job on a linux server, hosted on DigitalOcean
- Schedule custom messages to be sent by a telegram bot on a given group chat on push to this repo with Github Actions
- Use a Protocol class to structurally define telegram menus

# Perfect is the enemy of the good

- To implement database methods/functions that maps user id and saved bus stops for CRUD functions. Current implementation stores user data in session
- To implement cron job that runs `scripts.py` to update `bus_stop_data.json` file
- To move `bus_stop_data.json` file into a database to standardize storage of data within project

# Learning points

- To move faster, write code first and refactor later. Refactoring first typically leads to overabstraction and overengineering
- Use ChatGPT to illustrate and elucidate poorly worded concepts in poorly written documentation
