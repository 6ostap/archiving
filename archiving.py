import os
import zipfile
from pathlib import Path

from tqdm import tqdm


def archive(path: Path):
    with zipfile.ZipFile(path / "archive.zip", mode="w") as fantasy_zip:
        for folder, subfolders, files in os.walk(path):

            for file in tqdm(files, desc='Archiving'):
                if not file.endswith('.zip'):
                    fantasy_zip.write(os.path.join(folder, file),
                                      os.path.relpath(os.path.join(folder, file), path),
                                      compress_type=zipfile.ZIP_DEFLATED)

