#!/bin/bash

# Aritmatic & Logical
read n

if [ $((n%2)) -ne 0 ] || [ $((n%3)) -ne 0 ]
then
    echo "Not divisible by 6"
else
    echo "Divisible by 6"

fi

# String

read f

if [ -z "$f" ]
then
    echo "File name not provided"
else
    echo "$f"

fi

# Assignment operators


n=2
echo "$((n+=1))"