#!/bin/bash
# Scrpt that sends DELETE request to the URL Passed as the first argeument and display
curl -sL -X DELETE "$1"
