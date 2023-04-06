#!/bin/bash
# make request to server that causes the server to respiond with a message contains you have got me
curl -sX PUT -L -d "user_id=98" -H "Origin: HolbertoonSchool" 0.0.0.0:5000/catch_me
