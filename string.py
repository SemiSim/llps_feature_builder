import pandas as pd

def parse_string(filepath):
    df = pd.read_csv(filepath, sep='\t')
    scores = pd.to_numeric(df['Score'], errors='coerce')
    return {
        'string_ppi_count': len(df),
        'string_mean_score': scores.mean(),
        'string_high_conf_interactors': (scores > 700).sum()
    }
