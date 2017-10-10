#!/usr/bin/env bash

aws s3 ls --recursive s3://selfmade-mturk/hit03/sentinels/ | awk '{print $4}' | awk '{print "https://s3.amazonaws.com/selfmade-mturk/" $1}' > sentinels.txt
aws s3 ls --recursive s3://selfmade-mturk/hit03/data/ | awk '{print $4}' | awk '{print "https://s3.amazonaws.com/selfmade-mturk/" $1}' > data.txt
