# Setup file for package org_example_foo

from setuptools import setup

setup(name="org_example_foo",
      version="0.1.0",
      install_requires=["quark==0.0.1"],
      py_modules=[],
      packages=['org', 'org.example', 'org.example.foo', 'org_example_foo_md'])
