#!/bin/bash
# Sends a DELETE request, follows redirects, and displays body only if final status is 200
curl -s -L -o body.txt -w "%{http_code}" -X DELETE "$1" | grep -q "^200$" && cat body.txt
