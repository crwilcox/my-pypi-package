
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
        "tests",
        *session.posargs,
    )
