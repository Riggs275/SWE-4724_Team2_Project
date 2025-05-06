#!/bin/bash
cd /home/EValenc6/SWE-4724_Team2_Project/Troublemaker App
python3 -c "from CPUOverload import CPUOverload; from Intensity import Intensity; import datetime; CPUOverload(Intensity.High, datetime.datetime.now()).triggerEvent()"
