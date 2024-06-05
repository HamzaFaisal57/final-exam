class PDF:
    def __init__(self, file_name, file_size, content):
        self.name = file_name
        self.size = file_size
        self.content = content

    def open_file(self):
        print("opening file")

    def read_file(self):
        print("reading file")

    def save_file(self):
        print("saving file")
