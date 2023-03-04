import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='django-helpdeskeddy',
    version='0.1.3',
    packages=find_packages(),
    include_package_data=True,
    author='devxplorer',
    author_email='devxplorer@gmail.com',
    description='Django HelpDeskEddy Helper',
    long_description=README,
    install_requires=[
        'Django>=2.2,<4.0',
        'django-jsonfield-backport>=1.0.5,<2.0',
        'helpdeskeddy-api-client @ git+https://github.com/Keyintegrity/helpdeskeddy-api-client.git@v0.0.2',
        'mysqlclient>=2.0.0,<3.0',
    ],
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
