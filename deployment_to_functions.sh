#!/bin/bash
echo Hello, starting deployment
echo enter hub_user 
read hubuser
echo enter repo-name
read reponame
echo building image
docker build -t $hubuser/$reponame:sentiment_demo .
echo DONE BUILD!!
echo pushing to dockerhub
docker push $hubuser/$reponame:sentiment_demo
echo Done!