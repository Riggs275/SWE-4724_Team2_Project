#!/bin/bash
cd /Users/evanv/owlEye/SWE-4724_Team2_Project
export PYTHONPATH=$(pwd)/TroubleMakerApp
echo 'Running scheduled_1_test.sh at $(date)' >> ~/troublemaker_log.txt
python3 -c "from CPUOverload import CPUOverload; from Intensity import Intensity; import datetime; CPUOverload(Intensity(3), datetime.datetime.now()).triggerEvent()"
