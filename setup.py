from setuptools import setup, find_packages

version = '0.3'

name = 'plone.recipe.lxml'

entry_points = """
[zc.buildout]
default = plone.recipe.lxml:Recipe
"""


setup(name=name, 
      version=version,
      description="Buildout recipe that creates a lxml egg",
      long_description="""\
        This buildout recipe creates a lxml egg and builds libxml2 
        and libxslt dependencies from source.
        
        You can use it with a part like this:

        [buildout]
        parts = lxml 
        eggs = 
            lxml == 2.1.2

        [lxml]
        recipe=plone.recipe.lxml    
        egg = lxml == 2.1.2

        The available options are:    

        egg -- The lxml version you want to use. The default setting ist 
               'lxml == 2.1.2'.

        libxml2-url -- A URL from which the libxml2 sources can be downloaded.
                       The default setting is
                       'http://xmlsoft.org/sources/libxml2-2.6.32.tar.gz'.

        libxslt-url -- A URL from which libxslt sources can be downloaded. 
                       The default setting is
                       'http://xmlsoft.org/sources/libxslt-1.1.24.tar.gz'.     

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
          "Topic :: Text Processing :: Markup :: XML",
         ], 
      keywords='lxml recipe',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://svn.plone.org/svn/collective/buildout/plone.recipe.lxml',
      license='ZPL 2.1',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'zc.buildout', 
        'setuptools', 
        'zc.recipe.egg',
      ],
      entry_points=entry_points,
    )



