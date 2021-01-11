from setuptools import find_packages
from setuptools import setup
from glob import glob
from os.path import basename
from os.path import splitext

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cloud_demo",
    version="0.0.1",
    author="CrowdStrike",
    maintainer="Simon Lukasik",
    description="The CrowdStrike Demo Shell for Cloud Operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isimluk/cloud_demo",
    packages=find_packages("cloud_demo"),
    package_dir={"": "cloud_demo"},
    py_modules=[splitext(basename(path))[0] for path in glob("cloud_demo/*.py")],
    include_package_data=True,
    install_requires=[
        'crowdstrike-falconpy',
        'boto3',
        'gitpython',
        'IPython',
        'jedi==0.17.2',  # workaround https://github.com/ipython/ipython/issues/12742
    ],
    extras_require={
        'devel': [
            'flake8',
            'pylint',
            'pytest',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
