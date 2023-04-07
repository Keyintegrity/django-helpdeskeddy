import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='django-helpdeskeddy',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    author='devxplorer',
    author_email='devxplorer@gmail.com',
    description='Django HelpDeskEddy Helper',
    long_description=README,
    install_requires=[
        'Django>=3.1,<4.0',
        'helpdeskeddy-api-client @ git+https://github.com/Keyintegrity/helpdeskeddy-api-client.git@v0.0.2',
    ],
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
