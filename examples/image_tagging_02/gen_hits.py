#!/usr/bin/env python

from random import shuffle, sample, seed
from copy import copy
import math
import sys
import json
from os import path

seed(0)

category = sys.argv[1]
out_fname = sys.argv[2]
if len(sys.argv) == 4:
    max_jobs = int(sys.argv[3])
else:
    max_jobs = None

tmp = []
for line in open('/data/content_buckets_v2/test.txt'):
    line = line.split()
    tmp.append(line[0])

cat_ = category
if category == 'man_made_environments':
    cat_ = 'urban'
elif category == 'natural_environments':
    cat_ = 'landscape'
base_url = 'https://s3.amazonaws.com/selfmade-mturk/hit03/data/'
negs = list(set([path.join(base_url, path.basename(fn)) for fn in tmp if cat_ not in fn]))
pos = list(set([path.join(base_url, path.basename(fn)) for fn in tmp if cat_ in fn]))
shuffle(pos)
if len(pos) < len(negs):
    negs = sample(negs, len(pos))

# print len(pos), len(negs)
# sys.exit(1)

data = pos + negs
shuffle(data)

sentinels = open('sentinels.txt').read().strip().split()
sentinels = [fn for fn in sentinels if '/' + category + '/' in fn]
n_sentinels = [s for s in sentinels if ('_neg_' in s) or ('/neg/' in s)]
p_sentinels = [s for s in sentinels if '_pos_' in s or ('/pos/' in s)]
# data = open('data.txt').read().strip().split()
# shuffle(data)
data_ori = copy(data)

n_repeats_votes_per_img = 3
n_imgs_per_hit = 48
n_hits = int(math.ceil(1.0 * len(data) / (n_imgs_per_hit - 2)))
n_data_hit = n_imgs_per_hit - 2  # -2 because of sentinels (one positive and one negative)

print '# images to label: %6d' % (len(data))
print '  # pos sentinels: %6d' % (len(p_sentinels))
print '  # neg sentinels: %6d' % (len(n_sentinels))
print '        # of hits: %6d' % (n_hits * n_repeats_votes_per_img)

out_f = open(out_fname, 'w')

n_jobs = 0
for _ in range(n_repeats_votes_per_img):
    data = copy(data_ori)
    while len(data) > 0:
        # print len(data)
        hit_imgs = data[:n_data_hit]
        data = data[n_data_hit:]

        hit_imgs += sample(n_sentinels, 1)
        hit_imgs += sample(p_sentinels, 1)

        n_fill = n_imgs_per_hit - len(hit_imgs)
        if n_fill > 0:
            hit_imgs += sample(data_ori, n_fill)

        shuffle(hit_imgs)

        job = {'class': category, 'image_urls': hit_imgs}

        out_f.write(json.dumps(job) + '\n')
        n_jobs += 1

        if max_jobs is not None and n_jobs >= max_jobs:
            sys.exit(1)
