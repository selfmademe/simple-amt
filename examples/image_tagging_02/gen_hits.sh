for lab in `cat labels.txt`; do
  echo $lab
  python gen_hits.py $lab hit_inputs/hit_inputs_${lab}.json
  python gen_hits.py $lab hit_inputs/hit_inputs_${lab}_SANDBOX.json 3
done
