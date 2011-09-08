from distutils.core import setup

setup(
    name='solve',
    version='0.0.1',
    author='Orion Auld, Michael Sluyter',
    author_email='orion.auld@gmail.com',
    packages=['words', 'words.test'],
    scripts=[],
    #url='http://pypi.python.org/pypi/solve/',
    license='LICENSE.txt',
    description='Useful stuff to solve puzzles',
    long_description=open('README.txt').read(),
)
