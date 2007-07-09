from setuptools import setup, find_packages
import sys, os

version = '0.0'

name = 'plone.recipe.lxml'

entry_points = """
[zc.buildout]
default = plone.recipe.lxml:Recipe
"""


setup(name=name, 
      version=version,
      long_description="""\
        This recipe creates a lxml egg and builds libxml2 and libxslt dependencies from source.
        
        If you download it to directory 'src/lxml' you can use it with a part like this:

        [buildout]
        parts = lxml 
        develop =  src/lxml
        eggs = 
            lxml == 1.3

        [lxml]
        recipe=plone.recipe.lxml    
        egg = lxml == 1.3

        The available options are:    

        egg -- The lxml version you want to use. The default setting ist 'lxml == 1.3'.

        libxml2_url -- A URL from which the libxml2 sources can be downloaded. The default setting is
        'http://xmlsoft.org/sources/libxml2-2.6.29.tar.gz'.

        libxslt_url -- A URL from which libxslt sources can be downloaded. The default setting is
        'http://xmlsoft.org/sources/libxslt-1.1.21.tar.gz'.     

        Installation notes:

        The lxml egg is not build with buildout in offline mode.
        This recipe does not work with windows.

        """,
      classifiers=[
          "License :: OSI Approved :: Zope Public License",
          "Framework :: Buildout",
          "Framework :: Plone",
          "Framework :: Zope2",
          "Programming Language :: Python", 
          ], 
      keywords='',
      author='Joscha Krutzki',
      author_email='joka@jokasis.de',
      url='',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['plone.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'zc.buildout', 
        'setuptools', 
        'zc.recipe.egg',
      ],
      entry_points=entry_points,
    )



