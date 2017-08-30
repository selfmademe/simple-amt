#!/usr/bin/env bash
needs_countdown=1
. `dirname $0`/common.sh
python approve_hits.py $extra_args --hit_ids_file=examples/image_tagging/hit_ids${file_ending}.txt
