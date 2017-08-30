#!/usr/bin/env bash
needs_countdown=1
. `dirname $0`/common.sh

python launch_hits.py $extra_args \
  --html_template=image_tagging.html \
  --hit_properties_file=hit_properties/image_tagging.json \
  --input_json_file=examples/image_tagging/hit_inputs${file_ending}.json \
  --hit_ids_file=examples/image_tagging/hit_ids${file_ending}.txt
