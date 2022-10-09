from tqdm import tqdm
from pathlib import Path


def generate(path: Path):
    path1 = path / 'file'
    kBytes = 120
    length = 800

    for i in tqdm(range(length), desc='Generating'):
        f = open(f"{path1}{i}", "wb")
        size = kBytes * 1024
        f.write(b"\0" * size)

        f.close()
