from setuptools import setup, find_packages

version = '0.1'

setup(name='quills.core',
      version=version,
      description="Core weblog interfaces and views for Quills.",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Weblog Plone',
      author='Tim Hicks',
      author_email='tim@sitefusion.co.uk',
      url='http://svn.plone.org/svn/collective/quills.core/',
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
