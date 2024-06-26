from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
#This string is commonly used in Python requirements.txt files to indicate 
#that the package in the current directory should be installed in editable mode.
# Test123
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements 
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #list expression 
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
name="globalWeatherInsight",
version="0.0.1",
author="Ed Chiu",
author_email="tungwu.chiu@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')   



)

