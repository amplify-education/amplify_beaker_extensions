from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='beaker_extensions',
      version=version,
      description="Beaker extensions for additional back-end stores.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Didip Kerabat',
      author_email='didpk@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [beaker.backends]
      dynomite = beaker_extensions.dynomite_:DynomiteManager
      redis = beaker_extensions.redis_:RedisManager
      ringo = beaker_extensions.ringo:RingoManager
      tyrant = beaker_extensions.tyrant_:TokyoTyrantManager      
      """,
      )
