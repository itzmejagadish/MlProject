from setuptools import setup, find_packages

def get_requirements(file_path):
    with open(file_path) as file:
        requirements = file.readlines()
    return [req.strip() for req in requirements if req.strip() and not req.startswith("#") and not req.startswith("-e")]
setup(
    name="MLProject",
    version="0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirement.text")
)