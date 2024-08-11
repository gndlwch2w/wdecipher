from setuptools import setup, find_packages
import wdecipher
from wdecipher.utils import read_file

requirements = [
    "setuptools",
    "pycryptodomex",
    "loguru"
]

setup(
    name="wdecipher",
    version=wdecipher.__version__,
    python_requires=">=3.8",
    author="Chisheng Chen",
    author_email="chishengchen@126.com",
    url="https://github.com/gndlwch2w/wdecipher",
    description="WDecipher is a third-party extension tool for WeChat that can decrypt WeChat SQLite databases and export and merge databases.",
    long_description_content_type="text/markdown",
    long_description=read_file(path="README.md", encoding="utf-8"),
    license="MIT-0",
    packages=find_packages(),
    zip_safe=True,
    install_requires=requirements,
)
