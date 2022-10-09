def generate(path):
    path1 = path + '\\file'
    kBytes = 120

    for i in range(800):
        f = open(f"{path1}{i}", "wb")
        size = kBytes * 1024
        f.write(b"\0" * size)
