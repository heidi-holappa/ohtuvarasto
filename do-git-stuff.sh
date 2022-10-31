#!/bin/bash
commitmsg=$1

git add .
git commit -m "$commitmsg"
git push