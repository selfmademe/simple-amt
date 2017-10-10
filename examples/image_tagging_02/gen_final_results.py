#!/usr/bin/env python

import json
import sys
# from os import path

counts = {}

for fname in sys.argv[1:]:
    for line in open(fname):
        data = json.loads(line)
        for item in data['output']:
            # print item

            im_url = item['image_url']

            if im_url not in counts:
                counts[im_url] = {'pos': 0, 'neg': 0}

            if item['is_checked']:
                counts[im_url]['pos'] += 1
            else:
                counts[im_url]['neg'] += 1

for im_url in counts:
    if '/pos/' in im_url: continue
    if '/neg/' in im_url: continue

    pos = counts[im_url]['pos']
    neg = counts[im_url]['neg']

    print '%4d %4d %5.1f %s' % (pos, neg, float(pos) / (neg + pos), im_url) #path.basename(im_url))
