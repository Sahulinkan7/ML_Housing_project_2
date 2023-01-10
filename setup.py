from setuptools import setup,find_packages
from typing import List

#Variables for setup function
PROJECT_NAME="Housing-Price-Predictor"
VERSION="0.0.2"
AUTHOR="Linkan Kumar Sahu"
DESCRIPTION="A Machine Learning Project on Housing Price prediction"

REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT="-e ."


def get_requirement_list() -> List[str]:

    """
    Description : This function will return the list of requirements
    or libraries mentioned in requirements.txt file.
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
        requirement_list=[requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirement_list()
)