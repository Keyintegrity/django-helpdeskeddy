import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-helpdeskeddy',
    version='0.0.1',
    author='devxplorer',
    author_email='devxplorer@gmail.com',
    description='Django HelpDeskEddy Helper',
    long_description=long_description,
    install_requires=[
        "helpdeskeddy_api_client==0.0.1",
        "Django>=1.11.22",
        "mysqlclient>=1.3.13",
        "django-mysql>=3.2.0",
    ],
    dependency_links=[
        "git+https://github.com/Keyintegrity/helpdeskeddy-api-client.git@269ca4f23f9e9ef5056c230de4c13ea32fa15c23#egg=helpdeskeddy_api_client-0.0.1"
    ],
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
