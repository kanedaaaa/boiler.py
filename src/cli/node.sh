#!/bin/bash
mkdir "$1"
cd "$1"
npm init -y
git init
touch .gitignore
echo "node_modules" >> .gitignore
mkdir src
cd src
touch index.js
echo "console.log('Hey there')" >> index.js
