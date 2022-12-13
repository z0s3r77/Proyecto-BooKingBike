#!/bin/bash

#Se crea el entorno virtual, se activa y se instalan los requirements.txt de Python


python3 -m venv venv

. ./venv/bin/activate

pip3 install -r requirements.txt

