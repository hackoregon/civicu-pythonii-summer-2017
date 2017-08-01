class MyContext():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

files = []
for i in range(100):
    with MyContext(f'foo{i}.txt', 'w') as infile:
        infile.write('foo')
        files.append(infile)
