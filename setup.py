from setuptools import find_packages, setup

setup(
    name='healthcare_cost_prediction',
    version='0.0.1',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'pandas==2.0.3',
        'numpy==1.24.3',
        'scikit-learn==1.3.0',
        'Flask==2.3.3',
        'werkzeug==2.3.7',
        'seaborn==0.12.2',
        'matplotlib==3.7.2',
        'xgboost==1.7.6',
        'joblib==1.3.2'
    ]
)