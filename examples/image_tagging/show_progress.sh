#!/usr/bin/env bash
. `dirname $0`/common.sh
python show_hit_progress.py $extra_args --hit_ids_file=examples/image_tagging/hit_ids${file_ending}.txt
