#!/usr/bin/env bash

rm -rf results_final.txt
cat results.json | jq '' | grep true -A 1 | grep image_url | awk '{gsub("\"", ""); print $2}' | grep -v "/pos/" | sort | uniq -c | sort -g | awk '{if($1 >= 3) {print "1 " $2}}' > results_final.txt
cat results.json | jq '' | grep false -A 1 | grep image_url | awk '{gsub("\"", ""); print $2}' | grep -v "/neg/" | sort | uniq -c | sort -g | awk '{if($1 >= 3) {print "0 " $2}}' >> results_final.txt
