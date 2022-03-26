from setuptools import setup

setup(
    name = "aitbin",
    version = "0.1.0",
    description = "A beautiful binary code printer",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/aitbin",
    packages = ["aitbin"],
    entry_points = {
        'console_scripts': [
            'aitbin = aitbin.__main__:main'
        ]
    },
)
