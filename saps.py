import re

def parse_saps(filepath):
    features = {}
    comp_re   = re.compile(r'^([A-Z])\s*:\s*\d+\(\s*([\d\.]+)%\)')
    charge_re = re.compile(r'^(KRH|ED)\s*:\s*\d+\s*\(\s*([\d\.]+)%\)')
    hydro_re  = re.compile(r'Hydrophobicity.*?mean\)\s*:\s*([-+]?\d*\.\d+)')

    with open(filepath, 'r') as f:
        for line in f:
            m = comp_re.match(line)
            if m:
                aa, pct = m.groups()
                features[f'saps_aa_{aa}'] = float(pct) / 100.0
                continue

            m = charge_re.match(line)
            if m:
                grp, pct = m.groups()
                key = f"saps_pct_{'positively_charged' if grp=='KRH' else 'negatively_charged'}"
                features[key] = float(pct) / 100.0
                continue

            m = hydro_re.search(line)
            if m:
                features['saps_mean_hydropathy'] = float(m.group(1))
                continue

    return features
