#!/bin/bash
cd /Users/evanv/owlEye/SWE-4724_Team2_Project
export PYTHONPATH=$(pwd)/TroubleMakerApp
echo 'Running scheduled_3_test.sh at $(date)' >> ~/troublemaker_log.txt
python3 -c "from DirectoryOverflow import DirectoryOverflow; from Intensity import Intensity; import datetime; DirectoryOverflow(Intensity(2), datetime.datetime.now()).triggerEvent()"
