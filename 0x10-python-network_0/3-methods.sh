#!/bin/bash
# show all allowed
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
