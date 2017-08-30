#!/usr/bin/env bash
needs_countdown=1
. `dirname $0`/common.sh

hits_file=examples/image_tagging/hit_ids${file_ending}.txt
python disable_hits.py $extra_args --hit_ids_file=$hits_file
rm -rf $hits_file
