import os
import zipfile

from generating import generate
from archiving import archive

path = 'E:\\task'

generate(path)
archive(path)
