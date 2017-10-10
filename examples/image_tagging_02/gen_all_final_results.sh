#!/usr/bin/env bash

for lab in `cat labels.txt `; do
  echo $lab
  python gen_final_results.py results/results_${lab}.json > final_results/final_results_${lab}.txt
done
