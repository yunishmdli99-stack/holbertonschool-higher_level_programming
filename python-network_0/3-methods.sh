#!/bin/bash
# hi
curl -s -X OPTIONS -I "$1" | grep -i "^Allow:" | cut -d' ' -f2-
