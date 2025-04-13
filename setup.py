"""
    Setup file for storj-uplink.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.6.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""

from setuptools import Extension, setup
from setuptools.dist import Distribution
import os

class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(foo):
        return True


if __name__ == "__main__":
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        setup(
            include_package_data=True,
            use_scm_version={"version_scheme": "no-guess-dev"},
            package_data={
                'storj_uplink':['py.typed']
            },
            ext_modules = [
                Extension(
                    name="m_uplink",
                    sources = [],
                    extra_objects=[f"{dir_path}/src/storj_uplink/libuplink.so"]
                )
            ],
            distclass=BinaryDistribution
        )
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
