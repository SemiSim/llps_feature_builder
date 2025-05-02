import os
import yaml

REQUIRED_DATA_SUBFOLDERS = ['pondr', 'plaac', 'saps', 'biogrid', 'string']

def ensure_dir(path):
    if not os.path.exists(path):
        print(f"Creating missing directory: {path}")
        os.makedirs(path, exist_ok=True)

def scan_project_structure(project_root='.'):
    config = {}

    # === Set up DATA directory ===
    data_dir = os.path.join(project_root, 'data')
    ensure_dir(data_dir)
    config['data_dir'] = 'data'

    # Ensure required subfolders exist in data/
    for subfolder in REQUIRED_DATA_SUBFOLDERS:
        subfolder_path = os.path.join(data_dir, subfolder)
        ensure_dir(subfolder_path)

    # Look for llpsdb.csv in data/
    llpsdb_path = os.path.join(data_dir, 'llpsdb.csv')
    print(f"Checking for llpsdb.csv at: {os.path.abspath(llpsdb_path)}")
    if os.path.isfile(llpsdb_path):
        config['llpsdb_csv'] = os.path.join('data', 'llpsdb.csv')
    else:
        print(f"llpsdb.csv not found at top level of {data_dir}. Searching recursively...")
        found = False
        for root, dirs, files in os.walk(data_dir):
        	print(f"Scanning {root} with files: {files}")
        	for fname in files:
        		if fname.strip().lower() == 'llpsdb.csv':
        			rel_path = os.path.relpath(os.path.join(root, fname)).replace("\\", "/")
        			config['llpsdb_csv'] = rel_path
        			print(f"Found llpsdb.csv at: {config['llpsdb_csv']}")
        			found = True
        			break
        	if found:
        		break
        if not found:
        	print("WARNING: llpsdb.csv not found anywhere in data/. Using fallback path.")
        	config['llpsdb_csv'] = os.path.join('data', 'llpsdb.csv')
        		
    # === Set up FASTA directory ===
    fasta_dir = os.path.join(project_root, 'fasta')
    ensure_dir(fasta_dir)
    config['fasta_dir'] = 'fasta'

    # === Set up output locations ===
    config['output_csv'] = 'features.csv'
    config['missing_log'] = 'missing_files.log'
    config['origin_log'] = 'feature_origins.log'

    # === Set up split output ===
    split_output_dir = os.path.join(project_root, 'split_data')
    ensure_dir(split_output_dir)
    config['split_output_dir'] = 'split_data'
    config['label_column'] = 'llps_label'
    config['test_size'] = 0.2
    config['random_state'] = 42

    return config

def write_config_yaml(config, output_path='config.yaml'):
    with open(output_path, 'w') as f:
        yaml.dump(config, f, sort_keys=False)
    print(f"\nGenerated config.yaml:")
    for k, v in config.items():
        print(f"  {k}: {v}")

if __name__ == '__main__':
    config = scan_project_structure()
    write_config_yaml(config)
