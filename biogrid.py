import pandas as pd

def parse_biogrid(filepath):
    df = pd.read_csv(filepath, sep='\t', comment='#', low_memory=False)
    col_pairs = [
        ('Official Symbol Interactor A', 'Official Symbol Interactor B'),
        ('Systematic Name Interactor A', 'Systematic Name Interactor B')
    ]

    bait_col = partner_col = None
    for A, B in col_pairs:
        if A in df.columns and df[A].nunique(dropna=True)==1:
            bait_col, partner_col = A, B
            break
        if B in df.columns and df[B].nunique(dropna=True)==1:
            bait_col, partner_col = B, A
            break
    if bait_col is None:
        raise ValueError(f"Could not detect bait column in {filepath}")

    bait = df[bait_col].iloc[0]
    partners = set(df[partner_col].dropna().astype(str))
    scores = pd.to_numeric(df['Score'], errors='coerce')
    mods   = df.get('Modification', pd.Series([], dtype=str)).dropna().astype(str)

    features = {
        'biogrid_bait': bait,
        'biogrid_num_partners': len(partners),
        'biogrid_partners_list': ';'.join(sorted(partners)),
        'biogrid_row_count': len(df),
        'biogrid_mean_score': scores.mean(),
        'biogrid_high_score_count': (scores>700).sum()
    }
    for mtype, cnt in mods.value_counts().items():
        features[f'biogrid_ptm_type_{mtype}'] = cnt

    return features
