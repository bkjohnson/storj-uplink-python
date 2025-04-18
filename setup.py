"""
    Setup file for storj-uplink.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.6.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""

from setuptools import setup
from setuptools.dist import Distribution


# TODO: Consider re-enabling the distclass and/or looking into cibuildwheel
# in order to make sure that package works on the right platform
#
# class BinaryDistribution(Distribution):
#     """Distribution which always forces a binary package with platform name"""
#     def has_ext_modules(foo):
#         return True


if __name__ == "__main__":
    try:
        setup(
            include_package_data=True,
            use_scm_version={"version_scheme": "no-guess-dev"},
            package_data={
                '':['libuplink.so', 'py.typed']
            },
            # distclass=BinaryDistribution
        )
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
