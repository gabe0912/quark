# Setup file for package builtin_codec

from setuptools import setup

setup(name="builtin_codec",
      version="0.0.1",
      install_requires=["datawire-quark-core==0.4.2", "builtin==0.0.1"],
      py_modules=['builtin_codec'],
      packages=['builtin_codec_md'])