from setuptools import find_packages, setup

setup(
    name = "sensor",
    version = "0.0.1",
    author= "aswini",
    author_email= "aswinikk@gmail.com",
    packages=find_packages(),
    install_reqires = get_requirements()
)

def get_requirements():
    pass