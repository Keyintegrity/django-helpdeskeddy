import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='django-helpdeskeddy',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    author='devxplorer',
    author_email='devxplorer@gmail.com',
    description='Django HelpDeskEddy Helper',
    long_description=README,
    install_requires=[
        "helpdeskeddy-api-client @ https://github.com/Keyintegrity/helpdeskeddy-api-client/archive/v0.0.2.zip#egg=helpdeskeddy-api-client-0.0.2",
        "Django>=1.11.22,<3.0",
        "mysqlclient>=1.3.13,<2.0",
        "django-mysql>=3.2.0,<4.0",
    ],
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
