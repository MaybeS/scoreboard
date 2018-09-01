import glob
from os.path import dirname, basename, isfile

files = glob.glob(dirname(__file__) + "/*.py")
modules = filter(lambda f: not f.startswith('__'), map(basename, filter(isfile, files)))
__all__ = list(map(lambda f: f.split('.')[0], modules))

from app import Base
from app.lib.moduletools import import_subclass
__all__ = list(import_subclass(__path__, Base, locals()))
