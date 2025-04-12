<!-- These are examples of badges you might want to add to your README:
     please update the URLs accordingly

[![Built Status](https://api.cirrus-ci.com/github/<USER>/storj-uplink.svg?branch=main)](https://cirrus-ci.com/github/<USER>/storj-uplink)
[![ReadTheDocs](https://readthedocs.org/projects/storj-uplink/badge/?version=latest)](https://storj-uplink.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/<USER>/storj-uplink/main.svg)](https://coveralls.io/r/<USER>/storj-uplink)
[![PyPI-Server](https://img.shields.io/pypi/v/storj-uplink.svg)](https://pypi.org/project/storj-uplink/)
[![Monthly Downloads](https://pepy.tech/badge/storj-uplink/month)](https://pepy.tech/project/storj-uplink)
-->

[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)

# storj-uplink

> A python library for interacting with the [Storj][storj] network

This project is based on the [`uplink-python` repository][uplink-python]. Some key differences are:

1. This package uses the latest version of [uplink-c] rather than be locked to version 1.2.2
1. The binaries will be prebuilt and included with the distribution
   - This means that any downstream consumer won't have to have go and gcc installed

This is still in the early stages and under active development.

## Note

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.

[uplink-python]: https://github.com/storj-thirdparty/uplink-python
[storj]: https://www.storj.io/
