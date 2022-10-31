#!/bin/bash
files=$1
re=^[0-9]+$

if [ ${#*} -eq 0 ];
  then
    echo "Need an integer as a parameter. Aborting."
    exit
fi

for i in $(seq 1 $files)
  do
    touch file$i.txt
  done
