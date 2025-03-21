#!/bin/bash
cd /Users/evanv/owlEye/SWE-4724_Team2_Project
python3 -c "from CPUOverload import CPUOverload; from Intensity import Intensity; import datetime; CPUOverload(Intensity.High, datetime.datetime.now()).triggerEvent()"
