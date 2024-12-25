from setuptools import setup, find_packages

setup(
    name='Exam-Success-Analytics-for-Scholarships',  #
    version='0.1.0',  # Initial version
    packages=find_packages(),  # Automatically discover and include all packages in project
    install_requires=[  # List of dependencies
        'scikit-learn==1.2.0',
        'xgboost==1.7.1',
        'imbalanced-learn==0.9.1',
        'joblib==1.2.0',
        'pandas==1.5.3',
        'numpy==1.23.5'
    ],
    classifiers=[  
        'Programming Language :: Python :: 3.12.0',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Ensure your project supports at least Python 3.6
    author='Minal Devikar',  # 
    author_email='meenal.madankar@gmail.com', 
    description='A machine learning model for predicting scholarship success based on exam performance',  # Short description of your project
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  #
    url='https://github.com/minalmmm/Exam-Success-Analytics-for-Scholarships.git',  

    
)
