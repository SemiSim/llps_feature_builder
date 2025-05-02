import re
import numpy as np
from itertools import groupby

def parse_pondr(filepath):
    scores = []
    with open(filepath, 'r') as f:
        for line in f:
            if re.match(r'^\d+\s+\w\s+[\d\.]+', line):
                parts = line.strip().split()
                scores.append(float(parts[2]))
    if not scores:
        return {}
    return {
        'pond_mean_disorder': np.mean(scores),
        'pond_max_disorder': np.max(scores),
        'pond_disordered_frac': sum(s > 0.5 for s in scores) / len(scores),
        'pond_longest_disordered': max(
            (len(list(g)) for k, g in groupby(scores, lambda x: x > 0.5) if k),
            default=0
        )
    }
