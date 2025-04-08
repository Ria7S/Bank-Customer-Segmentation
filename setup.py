from setuptools import setup, find_packages   

def get_requirements(file_path):
    """
    This function returns a list of requirements from the given file path.
    """
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    
        if "-e" in requirements:
            requirements.remove("-e")
    return requirements




setup(
    name='mlproject',
    version='0.0.1',
    author='Riya',
    author_email='riya.saroj2002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)