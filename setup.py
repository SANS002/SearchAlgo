from setuptools import setup, find_packages

setup(
    name="my_search_library",
    version="0.1.0",
    packages=find_packages(),
    description="A library for various search algorithms and graph traversal",
    author="Santhosh",
    author_email="santhoshkanagaraj66@gmail.com",
    url="https://github.com/SANS002/SearchAlgo.git",  # Optional
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
