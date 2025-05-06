#!/bin/bash
cd /home/EValenc6/SWE-4724_Team2_Project/Troublemaker App
python3 -c "from MemorySpike import MemorySpike; from Intensity import Intensity; import datetime; MemorySpike(Intensity.Medium, datetime.datetime.now()).triggerEvent()"
