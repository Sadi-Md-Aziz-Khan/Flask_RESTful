from os import path
from setuptools import find_packages, setup

setup_dependencies = [
    "wheel",
    "setuptools-scm",
]

install_dependencies = [
    "flask-cors",
    "flask-restful",
    "python-dotenv",
]

setup(
    name="Flask_RESTful",
    url="https://github.com/Sadi-Md-Aziz-Khan/Flask_RESTful",
    license="MIT",
    author="Sadi",
    use_scm_version=True,
    setup_requires=setup_dependencies,
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    zip_safe=True,
    platforms=["posix"],
    install_requires=install_dependencies,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
