LLPS Feature Builder

A modular Python package for building and splitting liquid–liquid phase separation (LLPS) feature matrices from various bioinformatics data sources, including PONDR, SAPS, PLAAC, STRING, BioGRID, the LLPSDB v2.0, and NetSurfP 2.0 predictions. The matrices generated and split with this package are ready for direct import to train the SemiSim model.


INSTALLATION
1. Clone the repository
[bash]
git clone https://github.com/SemiSim/llps_feature_builder.git
cd llps_feature_builder

2. Install in editable mode
[bash]
pip install -e .

3. Install/prepare system prerequisites
	3.1  Python 3.7+
	3.2  Python packages: Install via your virtual-env's pip (or requirements.txt)
	[bash]
	pip install pandas numpy scikit-learn pyyaml requests biopython tqdm
	3.3  Internet access for NetSurfP 2.0 API calls
	3.4  (Optional) mkdssp if you plan to integrate DSSP parsing ; Make sure mkdssp is on yuor PATH !


CONFIGURATION
<config.yaml> has been created and places at project root for directory as structured in this package

To generate a new <config.yaml> for custom directory structures, a helper script to automate generation of a new working <config.yaml> file has been written : llps_feature_builder/utils/generate_yaml_config_v4.py
	To run, move <generate_yaml_config_v4.py> to project root.  

To manually modify <config.yaml>, edit <llps_feature_builder/config.yaml> (or place one at your project root) to point at your data locations :

data_dir: data
fasta_dir: fasta
llpsdb_csv: data/llpsdb.csv
output_csv: features.csv
missing_log: missing_files.log
origin_log: feature_origins.log
split_output_dir: split_data
label_column: llps_label
test_size: 0.2
random_state: 42
data_dir & fasta_dir: paths to your input directories

llpsdb_csv: path to the CSV of LLPS labels

output_csv: where the full feature matrix will be written

split_output_dir: folder for train/test splits

USAGE: CLI
Once installed, run the pipeline with:
[bash]
llps-feature-builder

This will:
1. Load config.yaml
2. Parse all data files under data/
3. Call NetSurfP 2.0 API on your FASTAs
4. Merge everything into features.csv, features_X.csv, features_y.csv
5. Split into train/test and save under split_data/

USAGE: PYTHON API
You can also invoke components programmatically:
[python]
from llps_feature_builder.utils.config_loader import load_config
from llps_feature_builder.builder.matrix_builder import (
    build_full_feature_matrix,
    split_and_save_train_test
)

cfg = load_config()
df  = build_full_feature_matrix()
X_tr, X_te, y_tr, y_te = split_and_save_train_test(
    df,
    cfg['split_output_dir'],
    label_column=cfg['label_column'],
    test_size=cfg['test_size'],
    random_state=cfg['random_state']
)



OUTPUT FILES
1. features.csv = Full feature matrix (including llps_label).
2. features_X.csv / features_y.csv = Feature-only matrix and label vectors.
3. split_data/
	3.1  X_train.csv, X_test.csv
	3.2  y_train.csv, y_test.csv

4. missing_files.log = Records any parse failures or missing inputs.
5. feature_origins.log = Tracks which features were extracted from which data sources


CONTRIBUTING
1. File Issues: If you find a bug or have a feature request, please open an issue and describe:
	1.1  What you tried
	1.2  What happened (including error messages)
	1.3  What the expected outcome was

2. Fork & Branch 
[bash]
git clone https://github.com/SemiSim/llps_feature_builder.git
cd llps_feature_builder

3. Develop
	3.1  Follow the existing code style (PEP8)
	3.2  Add tests in the tests/ folder (if you set one up)
	3.3  Update documentation (README.md, docstrings)

4. Create a feature branch (git checkout -b feat/your-feature)

5. Commit & Push
[bash]
git add .
git commit -m "feat: describe your change"
git push origin feat/my-new-feature

6. Open a Pull Request
	6.1  Open a PR against <main> (or whatever your default branch is)
	6.2  Link the issue it fixes (if any)
	6.3  Describe what you've changed, and any attention needed

7. Review & Merge: We’ll review, request changes if needed, and merge once everything’s green.

LICENSE
This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.


ACKNOWLEDGEMENTS
PONDR, SAPS, PLAAC, STRING, BioGRID, LLPSDB v2.0, and NetSurfP 2.0 for their open APIs and data formats.

The open-source community for inspiration and best practices.

Dr. Woonghee Lee with the University of Colorado for challenging us in our education and the guidance necessary to make this project possible.


Happy SemiSimming!
