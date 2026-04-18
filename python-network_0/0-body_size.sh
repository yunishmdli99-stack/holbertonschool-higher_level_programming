#!/bin/bash
# Fetches something that I have no axot to explain it
echo $(curl -s "$1" | wc -c)
