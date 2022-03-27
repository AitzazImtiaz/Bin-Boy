from setuptools import setup

setup(
    name = "binboy",
    version = "0.1.0",
    description = "A beautiful binary code printer",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/aitbin",
    packages = ["binboy"],
    entry_points = {
        'console_scripts': [
            'binboy = binboy.__main__:main'
        ]
    },
)
