#!/bin/bash
# Display size of the body response:; Usage ./0-body_size.sh 0.0.0.0:5000
echo $(curl -s -w "%{size_download}" -o /dev/null "$1")
