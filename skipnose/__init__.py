# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals


__author__ = 'Miroslav Shubernetskiy'
__email__ = 'miroslav@miki725.com'
__version__ = '0.3.1'


try:
    from .skipnose import SkipNose  # noqa
except ImportError:
    pass  # probably during install
