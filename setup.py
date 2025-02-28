'''
The setup.py is an essential part of packaging and distributing Python projects. It
is used by setuptools(or distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more

'''
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This will return list of requirements
    
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileExistsError:
        print("requirements.txt file not found!")
        
    return requirement_lst

# print(get_requirements()) 

setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author="Anjali Kakde",
    author_email="anjalikakde48@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)