#main.py
from llps_feature_builder.utils.config_loader import load_config
from llps_feature_builder.builder.matrix_builder import (
    build_full_feature_matrix,
    split_and_save_train_test
)

def main():
    config = load_config()
    df = build_full_feature_matrix()
    split_and_save_train_test(
        df,
        config['split_output_dir'],
        label_column=config['label_column'],
        test_size=config['test_size'],
        random_state=config['random_state']
    )

if __name__ == '__main__':
    main()
