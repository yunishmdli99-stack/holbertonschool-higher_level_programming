#!/bin/bash
BODY=$(curl -s "$1")
echo ${#BODY}
