import os
import zipfile


def archive(path):
    with zipfile.ZipFile(path + "\\archive.zip", mode="w") as fantasy_zip:
        for folder, subfolders, files in os.walk(path):

            for file in files:
                if not file.endswith('.zip'):
                    fantasy_zip.write(os.path.join(folder, file),
                                      os.path.relpath(os.path.join(folder, file), path),
                                      compress_type=zipfile.ZIP_DEFLATED)


archive('E:\\task')
