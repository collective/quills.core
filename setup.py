from setuptools import setup, find_packages
import os

version = '1.7.0b3'

setup(name='quills.core',
      version=version,
      description="Core weblog interfaces and views for Quills.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone blogging',
      author='Quills Team',
      author_email='plone-quills@googlegroups.com',
      url='http://plone.org/products/quills',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['quills'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
