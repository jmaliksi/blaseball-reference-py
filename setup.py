import setuptools


with open('README.md', 'r') as f:
    long_desc = f.read()


setuptools.setup(
    name='blaseball-reference',
    version='0.0.2',
    author='Joe Maliksi',
    author_email='joe.maliksi@gmail.com',
    url='https://github.com/jmaliksi/blaseball-reference-py',
    description='Python wrapper around blaseball-reference API',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
)
