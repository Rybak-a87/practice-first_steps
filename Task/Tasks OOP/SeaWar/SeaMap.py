class SeaMap:
    def __init__(self, size_map):
        self.width = size_map
        self.height = size_map
        self.map = [i+1 for i in range(self.width*self.height)]

