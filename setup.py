import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dummylog",  # This is the name of the package
    version="0.0.4",  # The initial release version
    author="Tamil Selvan A V",  # Full name of the author
    description="dummylog is the open source python package to help the python module/plugin developers to "
                "create/update the log files in simple syntax and easy format",
    url="https://github.com/selva221724/dummylog",
    license="MIT",
    include_package_data=True,
    long_description=long_description,  # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),  # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Framework :: IPython",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Environment :: Console"
    ],  # Information to filter the project on PyPi website
    python_requires='>=3.6',  # Minimum version requirement of the package
    py_modules=["dummylog"],  # Name of the python package
    package_dir={'': 'dummylog/src'},  # Directory of the source code of the package

)
