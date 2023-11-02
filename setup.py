from setuptools import setup
from os import path

currrent_direct = path.abspath(path.dirname(__file__))
with open(path.join(currrent_direct, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PetfinderSDK',
    version='0.1.0',
    packages=['Pet'],
    url='https://github.com/tyler-tee/petfindersdk',
    license='MIT',
    author='Tyler Talaga',
    author_email='ttalaga@wgu.edu',
    description='Python wrapper designed to facilitate interaction with PetFinder\'s API.',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
