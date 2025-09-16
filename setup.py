from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return the list of requirements
    """
    requirement_lst: List[str] = []
    try:
      with open('requirements.txt','r') as file:
          # read lines from the file
          lines = file.readlines()
          # proces each line
          for line in lines:
              requirement = line.strip()
              # ignore empty lines and -e
              if requirement and not requirement.startswith('-e'):
                  requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    
    return requirement_lst
  
setup(
  name='NetworkSecurity_DataScience',
  version='0.0.1',
  author='Rahul Raj',
  author_email='rahulrajpr06@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements(),
)