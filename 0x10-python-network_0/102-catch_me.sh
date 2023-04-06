#!/bin/bash
# make request to server that causes the server to respiond with a message contains you have got me
curl -sX PUT -L -d "user_id=98" -H "Origin: HolbertoonSchool" http://878f0b21f5f5.35f55309.alx-cod.online:5000/catch_me
