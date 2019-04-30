#!/usr/bin/python3
for i in range(ord('a'), ord('{')):
    print({:x}.format(chr(i)), end="")
