import pandas as pd
import numpy as np
from itertools import groupby

def parse_plaac(filepath):
    df = pd.read_csv(filepath, sep='\t', comment='#')
    probs = df['HMM.PrD-like']
    mask  = probs > 0.5

    # Global stats
    stats = {
        'plaac_mean': df['PLAAC'].mean(),
        'plaac_max' : df['PLAAC'].max(),
        'prd_frac'  : mask.mean(),
        'prd_mean_prob': probs.mean(),
        'prd_max_prob' : probs.max(),
    }

    # Longest region
    regions = []
    start = None
    for i, val in enumerate(mask):
        if val and start is None:
            start = i
        if not val and start is not None:
            regions.append((start, i))
            start = None
    if start is not None:
        regions.append((start, len(mask)))

    if regions:
        a, b = max(regions, key=lambda x: x[1]-x[0])
        sub = df.iloc[a:b]
        stats.update({
            'prd_longest': b - a,
            'prd_region_charge_mean': sub['CHARGE'].mean(),
            'prd_region_hydro_mean' : sub['HYDRO'].mean()
        })
    else:
        stats.update({
            'prd_longest': 0,
            'prd_region_charge_mean': np.nan,
            'prd_region_hydro_mean' : np.nan
        })

    return stats
