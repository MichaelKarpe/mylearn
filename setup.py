
import setuptools

setuptools.setup(
    name='mylearn',
    version='0.0.1',
    url='https://github.com/MichaelKarpe/mylearn',
    author='Michaël Karpe',
    author_email='michael.karpe@berkeley.edu',
    description='mylearn: my Machine Learning toolkit',
    long_description='mylearn: my Machine Learning toolkit',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    
    install_requires=[
        'matplotlib==3.4.1',
        'numpy==1.20.2',
        'pandas==1.2.3',
        'scikit-learn==0.24.1',
        'seaborn==0.11.1',
    ],
)

