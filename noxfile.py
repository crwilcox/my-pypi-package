
from __future__ import absolute_import
import os

import nox

@nox.session(python=["3.5", "3.6", "3.7"])
def unit(session):
    """Run the unit test suite."""
    session.install("mock", "pytest", "pytest-cov")
    session.install("-e", ".")

    # Run py.test against the unit tests.
    session.run(
        "py.test",
        "--quiet",
        os.path.join("tests", "unit"),
        *session.posargs,
    )


@nox.session(python=["3.7"])
def docs(session):
    # verify we can build our docs. if this is running on a tagged release on master, it will publish the docs also
    pass
