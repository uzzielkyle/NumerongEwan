from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="NumerongEwan",
    version="0.1.0",
    description="A simple number guessing game in Python",
    author="Uzziel Kyle Ynciong",
    author_email="uzzielynciong@gmail.com",
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'numerong-ewan=numerong_ewan.numerong_ewan:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
