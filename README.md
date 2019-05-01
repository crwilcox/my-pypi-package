`mypackage` is a sample package made to demonstrate how to create a package of your own

# Quick Start

## Supported Python Versions

Python >= 3.5

## Mac/Linux

```
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install google-cloud-firestore
```

## Windows

```
pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install google-cloud-firestore
```

# Example Usage

```
import mypackage
mypackage.MyPackage().spam()
```