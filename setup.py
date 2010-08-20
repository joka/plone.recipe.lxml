from setuptools import setup, find_packages

version = '0.4'

name = 'plone.recipe.lxml'

entry_points = """
[zc.buildout]
default = plone.recipe.lxml:Recipe
"""


setup(name=name, 
      version=version,
      description="Recipe that builds lxml and dependencies (libxslt, libxml2).",
      long_description="""\
Notes
========

This recipe is only tested with Debian, Gentoo and minitage. The ``z3c.recipe.staticlxml`` 
recipe is better maintained.
 
Options
=================

**egg**
    The desired lxml egg version (like ``lxml==2.2.6``).

**libxslt-url**
    The URL to download the libxslt tarballe, the default value is:
    'http://xmlsoft.org/sources/libxslt-1.1.26.tar.gz'

**libxml2-url**
    The URL to download the libxml2 tarball, the default value is:
    'http://xmlsoft.org/sources/libxml2-2.7.7.tar.gz'


Example buildout configuration
===============================

    [buildout]
    parts = lxml 
    eggs = lxml == 2.2.6

    [lxml]
    recipe=plone.recipe.lxml    
    egg = lxml == 2.2.6

    
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
      author='Joscha Krutzki',
      author_email='joka at jokasis de',
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



