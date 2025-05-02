from setuptools import setup, find_packages

setup(
    name='llps_feature_builder',
    version='0.9.2',
    description='LLPS Feature Builder: modular bioinformatics feature matrix generator',
    author='Rylie Pecha',
    author_email='ry.labwork@gmail.com',
    url='https://github.com/semisim/llps_feature_builder',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'pyyaml',
        'requests',
        'biopython',
        'tqdm'            
    ],
    entry_points={
        'console_scripts': [
            'llps-feature-builder=llps_feature_builder.main:main',
        ],
    },
    python_requires='>=3.7',
)
