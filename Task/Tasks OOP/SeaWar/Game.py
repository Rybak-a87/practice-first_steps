class Game:
    def display(self, map, width, height):
        for i in range(height):
            for j in range(width):
                print(map[j + i*height], end="\t")
            print()
