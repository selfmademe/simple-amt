while inotifywait -e close_write hit_templates/image_tagging_02.html; do
  bash ./examples/image_tagging_02/render_template.sh
done
