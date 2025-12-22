#!/bin/bash

# audible notification utility using espeak
# Usage: ./speak.sh "Your message here"

message="$1"

if [ -z "$message" ]; then
  echo "Usage: ./speak.sh \"Your message here\""
  exit 1
fi

espeak -s 150 -p 50 -a 200 "$message"
