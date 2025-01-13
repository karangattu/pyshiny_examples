#!/bin/bash

# python script to loop through each dir and delete all folders named "comprehensive"

for dir in $(ls -d */); do
    echo "Processing $dir"
    find $dir -type d -name "comprehensive" -exec rm -rf {} \;
done
