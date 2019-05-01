import setuptools

with open("README.md") as f:
  long_description = f.read()

setuptools.setup(
  name="PyCon2019",
  version="0.0.2",
  description="My first package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  license="Apache 2.0",
  packages=setuptools.find_packages(),
  url="https://github.com/crwilcox/mypackage",
  author="Chris Wilcox",
  author_email="pypi@crwilcox.com",
  classifiers=[
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Operating System :: OS Independent",
    "Topic :: Utilities",
  ],
  install_requires=[
    "urllib3",
    "requests",
  ],
)
