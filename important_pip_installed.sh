#!/bin/bash

pip install --upgrade pip

while IFS= read -r line; do
    echo "Installing $line..."
    pip install --no-cache-dir --force-reinstall --ignore-installed "$line" || echo "Failed to install $line"
done < requirements.txt

