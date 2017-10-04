#!/usr/bin/env python

from random import shuffle, sample
from copy import copy
import math
import sys
import json

out_fname = sys.argv[1]

sentinels = open('sentinels.txt').read().strip().split()
n_sentinels = [s for s in sentinels if ('_neg_' in s) or ('/neg/' in s)]
p_sentinels = [s for s in sentinels if '_pos_' in s or ('/pos/' in s)]
data = open('data.txt').read().strip().split()
shuffle(data)
data_ori = copy(data)

n_repeats_votes_per_img = 3
n_imgs_per_hit = 36
n_hits = int(math.ceil(1.0 * len(data) / (n_imgs_per_hit - 2)))
n_data_hit = n_imgs_per_hit - 2  # -2 because of sentinels (one positive and one negative)

print '# images to label: %6d' % (len(data))
print '  # pos sentinels: %6d' % (len(p_sentinels))
print '  # neg sentinels: %6d' % (len(n_sentinels))
print '        # of hits: %6d' % (n_hits * n_repeats_votes_per_img)

out_f = open(out_fname, 'w')

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

        out_f.write(json.dumps(hit_imgs) + '\n')
