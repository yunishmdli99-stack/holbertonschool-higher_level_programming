#!/bin/bash
# hi
curl -s -X OPTIONS "$1" | GREP -i "Allow:"
