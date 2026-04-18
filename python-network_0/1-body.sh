#!/bin/bash
# Sends a GET request and displays the response body only if status code is 200
curl -s -L -o body.txt -w "%{http_code}" -X GET "$1" | grep -q "^200$" && cat body.txt
