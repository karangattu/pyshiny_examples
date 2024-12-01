#!/bin/bash

# Set directory path (change to desired path)
root_dir=/Users/karangathani/Documents/GitHub/pyshiny_examples

# Loop through each directory
for dir in "$root_dir"/*; do
  if [ -d "$dir" ]; then
    # Check if app.py exists in the directory
    if [ ! -f "$dir/app.py" ]; then
      echo "Deleting directory: $dir"
      rm -rf "$dir"
    fi
  fi
done