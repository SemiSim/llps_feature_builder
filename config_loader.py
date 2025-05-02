import os
import yaml

def load_config(path=None):
    # 1) If caller passed an explicit path, use it:
    if path:
        cfg_path = path

    else:
        # 2) First try the package-local config.yaml
        here = os.path.dirname(__file__)                 # .../llps_feature_builder/utils
        pkg_root = os.path.abspath(os.path.join(here, os.pardir))
        candidate = os.path.join(pkg_root, 'config.yaml')
        if os.path.isfile(candidate):
            cfg_path = candidate
        else:
            # 3) Fallback to config.yaml in the CWD (project root)
            cfg_path = os.path.abspath('config.yaml')

    with open(cfg_path, 'r') as f:
        return yaml.safe_load(f)
