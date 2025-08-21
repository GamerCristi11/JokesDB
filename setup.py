from setuptools import setup, find_packages

setup(
    name="JokesDB",
    version="0.1.0",
    description="A simple Python module to fetch jokes from my website.",
    author="Code2Craft",
    url="https://github.com/gamercristi11/JokesDB",
    project_urls={
        "Source": "https://github.com/gamercristi11/JokesDB",
        "Homepage": "https://code2craft.xyz"
    },
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "requests"
    ],
)