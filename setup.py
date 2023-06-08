from setuptools import setup, find_packages
from typing import List

HYPHEN_E = '-e .'


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as obj:
        for line in obj:
            req = line.strip()
            if req != HYPHEN_E:
                requirements.append(req)
    return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='AYUSH',
    author_email='joshiayush339@gmail.com',
    install_requires=get_requirements('./requirements.txt'),
    packages=find_packages()
)
