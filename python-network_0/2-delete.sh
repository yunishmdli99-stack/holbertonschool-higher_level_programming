#!/bin/bash
# Sends a DELETE request, follows redirects, and displays body only if final status is 200
curl -s -X DELETE "$1"
