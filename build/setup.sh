#!/bin/bash

# cd to the directory of the script
cd "$(dirname "$0")"

cd ../deps
git clone 'https://github.com/omarr45/Atheer.git'

cd ..
npm install