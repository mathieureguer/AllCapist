# -*- coding: utf-8 -*-

from setuptools import setup


def readme():
  with open("README.md") as f:
    return f.read()


setup(name="AllCapist",
      version="0.3",
      description="a little tool to inject unicode mapping in font files",
      long_description=readme(),
      classifiers=[
          "Development Status :: 4 - Beta",
          "License :: Other/Proprietary License",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Build Tools",
      ],
      author="Mathieu Reguer",
      author_email="mathieu.reguer@gmail.com",
      license="All rights reserved",
      packages=[
          "AllCapist",
      ],
      entry_points="""
        [console_scripts]
        AllCapist=AllCapist.AllCapist:double_encode_uc
        """,
      install_requires=[
          "fonttools",
          "click",
      ],
      include_package_data=True,
      zip_safe=False)
