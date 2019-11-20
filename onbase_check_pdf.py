class lookup_files:
    def __init__(self,lines_list):
        self.lookup_pdf.append(lines_list)
        self.lookup_length = len(lines_list)

    def dict_files(self):
        for i in range(self.lookup_length):
            dict