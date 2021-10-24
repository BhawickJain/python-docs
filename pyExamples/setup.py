from setuptools import setup, find_packages


with open('README.md') as f:
     readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

setup(
    name='pyExamples',
    version='0.1.0',
    description='example code snippets to demonstrate software patterns in python',
    long_description=readme,
    author='Bhawick',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=('tests', 'docs'))
)
