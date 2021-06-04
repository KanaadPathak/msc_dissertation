#!/usr/bin/env bash
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`
echo "${red}Stopping supervise.ly agent.${reset}"
docker stop $(docker ps -q -f "name=supervisely-agent")
echo "${green}Agent was stopped successfully.${reset}"
