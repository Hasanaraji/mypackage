from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='My first example python package',
    long_description=open('readme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/hasanaraji/mypackage',
    author='Hasan A-Raji',
    author_email='hasanaraji9@gmail.com'
)