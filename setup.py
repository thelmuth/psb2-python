from setuptools import setup

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    name='psb2',
    version='1.0.0',    
    description='Utilities for sampling the datasets of PSB2.',
    author='Thomas Helmuth',
    author_email='thelmuth@hamilton.edu',
    url='https://github.com/thelmuth/psb2-python',
    project_urls={
        "More information": "https://cs.hamilton.edu/~thelmuth/PSB2/PSB2.html",
        "Dataset archive": "https://zenodo.org/record/4678739",
    },
    long_description = readme,
    long_description_content_type = "text/markdown",
    license='Eclipse Public License 2.0 (EPL-2.0)',
    packages=["psb2"],
    install_requires=["requests"],
    classifiers=[  
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)'
    ],
)

