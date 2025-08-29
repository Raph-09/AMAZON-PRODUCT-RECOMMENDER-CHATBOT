from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AMAZON RECOMMENDER",
    version="0.1",
    author="raphael",
    packages=find_packages(),
    install_requires = requirements,
)