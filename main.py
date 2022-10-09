import os
import zipfile
import tqdm
import argparse
from pathlib import Path

from generating import generate
from archiving import archive

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=Path, help='')

    args = parser.parse_args()
    path = args.path / 'emptyFolder'

    path.mkdir(exist_ok=True, parents=True)

    generate(path)
    archive(path)
