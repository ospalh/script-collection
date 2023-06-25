#!/bin/bash

# Absolutely ad-hoc. I got a file with one output filename and start end end times. I want this to calculate the duration.

inf="../inf.flac"
of=$1
st_hms=$2
et_hms=$3

st_s=$(date -d  $st_hms "+(%S+%M*60+%H*3600)" | bc)
et_s=$(date -d  $et_hms "+(%S+%M*60+%H*3600)" | bc)
dur=$(echo $et_s - $st_s | bc)

sox $inf "$of" trim $st_s $dur
