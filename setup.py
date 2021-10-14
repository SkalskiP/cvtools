import pathlib
import setuptools

from typing import List

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding="utf-8")


def load_install_requirements(path: pathlib.Path) -> List[str]:
    with open(path) as f:
        return f.read().splitlines()


setuptools.setup(
    name="cvtools",
    version='1.0.0',
    python_requires=">=3.7",
    description="Useful Computer Vision utils.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SkalskiP/cvtools",
    author="Piotr Skalski",
    author_email="piotr.skalski92@gmail.com",
    license='MIT',
    packages=['cvtools'],
    include_package_data=True,
    install_requires=load_install_requirements(HERE / "requirements.txt"),
    extras_require={
        'test': [
            'pytest==6.2.3',
        ],
        'dev': [
            'notebook==6.4.0'
        ]
    },
    setup_requires=[],
    tests_require=[
        'pytest==6.2.3'
    ],
)
