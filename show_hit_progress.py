import argparse
from collections import Counter
from progressbar import ProgressBar

import simpleamt


if __name__ == '__main__':
  parser = argparse.ArgumentParser(parents=[simpleamt.get_parent_parser()])
  args = parser.parse_args()

  mtc = simpleamt.get_mturk_connection_from_args(args)

  if args.hit_ids_file is None:
    parser.error('Must specify hit_ids_file')

  with open(args.hit_ids_file, 'r') as f:
    hit_ids = [line.strip() for line in f]

  counter = Counter()

  pbar = ProgressBar(max_value=len(hit_ids))
  missing_hits = []
  for idx, hit_id in pbar(enumerate(hit_ids)):
    # print 'Checking HIT %3d of %d' % (idx + 1, len(hit_ids))
    try:
      hit = mtc.get_hit(hit_id)[0]
    except:
      missing_hits.append(hit_id)
      # print 'Can\'t find hit id: %d' % (hit_id)
      continue
    total = int(hit.MaxAssignments)
    completed = 0
    for a in mtc.get_assignments(hit_id):
      s = a.AssignmentStatus
      if s == 'Submitted' or s == 'Approved' or s == 'Rejected':
        completed += 1
    counter.update([(completed, total)])

  if len(missing_hits) > 0:
    print "Could not find %d hits. Here's a sample of them:"
    print ' '.join(missing_hits[:10])

  for (completed, total), count in counter.most_common():
    print '%d / %d: %d' % (completed, total, count)

