from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(filepath:str)->List[str]:
    '''
    This function will return the list of requirements
    :param filepath: path to file to read requirements
    :return: return the libraries in the file.
    '''

    requirements = []
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Uma',
    author_email='itsmineee@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)