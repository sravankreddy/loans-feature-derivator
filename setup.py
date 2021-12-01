# python setup.py bdist_egg

import os

from setuptools import setup, find_packages

superfast_src = os.path.join('loan_derivator', 'src', 'loan_derivator')
packages = find_packages('src') + ['loan_derivator'] + [f'loan_derivator.{p}' for p in find_packages(superfast_src)]
print(f'packages: {packages}')

setup(
    name='loan_derivator',
    version='0.0.0',
    description='loan_derivator',
    author='Shravan Kamidi',
    author_email='loan_derivator@credit.com',
    package_dir={'': 'src', 'loan_derivator': superfast_src},
    packages=packages,
)
