#!/bin/sh

# 1.sh  input

cat "$1" | awk 'BEGIN { prev = 99999 } { if ($0 > prev) { count ++ }; prev = $0; } END { print count }' 
cat "$1" | awk '{ print a + b + $0 } { a = b; b = $0; }' | tail -n +3 | awk 'BEGIN { prev = 99999 } { if ($0 > prev) { count ++ }; prev = $0; } END { print count }' 
