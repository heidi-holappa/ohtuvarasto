#!/bin/bash
commitmsg=$1

git add -p
git commit -m "$commitmsg"
git push
