#!/usr/bin/env bash
. `dirname $0`/common.sh

python get_results.py $extra_args \
  --hit_ids_file=examples/image_tagging/hit_ids${file_ending}.txt \
  > examples/image_tagging/results${file_ending}.txt
