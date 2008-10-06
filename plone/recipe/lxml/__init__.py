import os, sys, shutil, tempfile, urllib2, urlparse
import setuptools.archive_util
import zc.buildout
import zc.recipe.egg

WIN32 = False
if sys.platform[:3].lower() == "win":
    WIN32 = True


def system(c):
    if os.system(c):
        raise SystemError("Failed", c)


class Recipe:
    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options

        self.libxml2_url = options.get(
            'libxml2-url', 'http://xmlsoft.org/sources/libxml2-2.6.32.tar.gz')
        self.libxslt_url = options.get(
            'libxslt-url', 'http://xmlsoft.org/sources/libxslt-1.1.24.tar.gz')

        options['location'] = os.path.join(
            buildout['buildout']['parts-directory'],
            self.name
            )
        location = options['location']

        options.setdefault('include-dirs', 'lxml')
        options.setdefault('egg', 'lxml == 2.1.2')
        options.setdefault('include-dirs', location + '/include')
        options.setdefault('rpath', location + '/lib')

        self.egg = zc.recipe.egg.Custom(buildout, name, options)

    def install(self):
        options = self.options
        location = options['location']

        if not os.path.exists(location):
            os.mkdir(location)

        here = os.getcwd()

        old_path = os.getenv('PATH')
        try:
            os.chdir(location)

            # Build libxml2 and libxslt, unless buildout.cfg specifically
            # set those to a false value

            if not WIN32 and self.libxml2_url:
                self.cmmi(self.libxml2_url, '--without-python', location)

            if not WIN32 and self.libxslt_url:
                 self.cmmi(
                     self.libxslt_url,
                     '--without-python --with-libxml-prefix=%s' % location,
                     location)

            os.environ['PATH'] = location + '/bin:' + old_path
            self.egg.install()

        finally:
            os.environ['PATH'] = old_path
            os.chdir(here)

        return location

    def update(self):
        pass

    def cmmi(self, url, extra_options, location):

        # Code largely borrowed from zc.recipe.cmmi

        _, _, urlpath, _, _, _ = urlparse.urlparse(url)
        tmp = tempfile.mkdtemp('buildout-'+self.name)
        tmp2 = tempfile.mkdtemp('buildout-'+self.name)
        try:
            fname = os.path.join(tmp2, urlpath.split('/')[-1])
            open(fname, 'w').write(urllib2.urlopen(url).read())
            setuptools.archive_util.unpack_archive(fname, tmp)

            here = os.getcwd()
            os.chdir(tmp)
            try:
                if not os.path.exists('configure'):
                    entries = os.listdir(tmp)
                    if len(entries) == 1:
                        os.chdir(entries[0])
                    else:
                        raise ValueError("Couldn't find configure")

                system("sh ./configure --prefix=%s %s" % (location, extra_options))
                system("make")
                system("make install")

            finally:
                os.chdir(here)

        finally:
            shutil.rmtree(tmp)
            shutil.rmtree(tmp2)
