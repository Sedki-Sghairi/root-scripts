#!/bin/bash

ext=HTM
newex=html
for f in *."$ext"; do
	name=$(basename "$file" ."$ext")
	mv "$file" "$name.$newex"
done	
