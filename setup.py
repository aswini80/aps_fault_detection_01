from setuptools import find_packages, setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHON_E_DOT = "-e ."

setup(
    name = "sensor",
    version = "0.0.1",
    author= "aswini",
    author_email= "aswinikk@gmail.com",
    packages=find_packages(),
    install_reqires = get_requirements()
)

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requiremnt_file:
        requirement_list = requiremnt_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requiremet_name in requirement_list]
    if HYPHON_E_DOT in requirement_list:
        requirement_list.remove(HYPHON_E_DOT)
    return requirement_list
    
