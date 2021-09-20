#!/bin/bash
result=$(ls)
echo $result
for x in $result
do
echo "hello $x"
done
