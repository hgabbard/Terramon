#!/bin/bash

time=$(lalapps_tconvert now)
t_date=$(lalapps_tconvert "$time")
echo "$time"
echo "$t_date"
t_new_date=$(echo "$t_date" | tr " " "_")

cp /home/hunter.gabbard/Seismon_folders/seismon/bin/ihope.html /home/hunter.gabbard/Seismon_folders/seismon/bin/$t_new_date.html
#cp /home/hunter.gabbard/Seismon_folders/seismon/bin/ihope.html /home/hunter.gabbard/$t_date.html
