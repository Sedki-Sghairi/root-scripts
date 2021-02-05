#!/bin/bash

for file in images*; do cwebp -q 70 "$file" -o "${file%.*}.webp";done
