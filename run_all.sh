#!/bin/bash

screen -X -S relay_HUB quit
screen -X -S mouli_HUB quit

echo "Killed all screens"

screen -dmS relay_HUB
screen -S relay_HUB -X stuff 'cd proxy/my-epitech-relay\n'
screen -S relay_HUB -X stuff 'npm start\n'

echo "Relay starting..."

screen -dmS mouli_HUB
screen -S mouli_HUB -X stuff 'python src/main.py\n'

echo "Bot mouli is on"

echo -e "\033[1;32m\n================= Launch done ================="
echo -e "\033[0m"
