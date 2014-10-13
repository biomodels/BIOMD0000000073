from setuptools import setup, find_packages

setup(name='BIOMD0000000073',
      version=20140916,
      description='BIOMD0000000073 from BioModels',
      url='http://www.ebi.ac.uk/biomodels-main/BIOMD0000000073',
      maintainer='Stanley Gu',
      maintainer_url='stanleygu@gmail.com',
      packages=find_packages(),
      package_data={'': ['*.xml', 'README.md']},
    )