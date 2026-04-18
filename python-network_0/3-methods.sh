#!/bin/bash
# hi
curl -s -X OPTIONS "$1" | grep -i "Allow:"
