#!/bin/bash
# show the body
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
