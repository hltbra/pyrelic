# #!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
from setuptools import setup, find_packages


def parse_requirements():
    """
    Rudimentary parser for the `requirements.txt` file

    We just want to separate regular packages from links to pass them to the
    `install_requires` and `dependency_links` params of the `setup()`
    function properly.
    """
    try:
        requirements = \
            map(str.strip, local_file('requirements.txt'))
    except IOError:
        raise RuntimeError("Couldn't find the `requirements.txt' file :(")

    links = []
    pkgs = []
    for req in requirements:
        if not req:
            continue
        if 'http:' in req or 'https:' in req:
            links.append(req)
            name, version = re.findall("\#egg=([^\-]+)-(.+$)", req)[0]
            pkgs.append('{0}=={1}'.format(name, version))
        else:
            pkgs.append(req)

    return pkgs, links

local_file = lambda f: \
    open(os.path.join(os.path.dirname(__file__), f)).readlines()

#install_requires, dependency_links = parse_requirements()

if __name__ == '__main__':

    packages = find_packages(exclude=['*tests*'])

    setup(
        name="pyrelic",
        license="GPL",
        version='0.7.0',
        description=u'Python API Wrapper for NewRelic API',
        author=u'Andrew Gross',
        author_email=u'andrew.w.gross@gmail.com',
        include_package_data=True,
        url='https://github.com/andrewgross/pyrelic',
        packages=packages,
        classifiers=(
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Natural Language :: English',
            'Operating System :: Microsoft',
            'Operating System :: POSIX',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
        )
    )
