import os
import zipfile
from pathlib import Path

from tqdm import tqdm


def archive(path: Path):
    with zipfile.ZipFile(path.parent / "archive.zip", mode="w") as fantasy_zip:

        for file in tqdm(list(path.iterdir()), desc='Archiving'):
            fantasy_zip.write(file, file.name, compress_type=zipfile.ZIP_DEFLATED)

