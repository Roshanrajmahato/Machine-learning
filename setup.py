from setuptools import setup ,find_packages
from typing import List

#declaring variable for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Roshan raj mahato"
DESCRIPTION="This is a first batch Machine learning Project"
REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT="-e ."


def get_requirements_list() -> List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

    """
    Description :This function is going to return list of requirement mention 
    in  requirements.txt file
    return this function is going to return a list which contain name 
    of libraries mention in requirement.txt file 
    """

setup (
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), 
install_requires=get_requirements_list()

)


















