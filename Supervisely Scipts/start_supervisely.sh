#!/usr/bin/env bash

echo 'Starting supervisely agent'
docker start $(docker ps -q -f "name=supervisely-agent")
