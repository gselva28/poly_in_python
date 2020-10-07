#two classes -- Rectangle, Square
#Rectangle instance variable -- self.width, self.length
#Square instance variable -- self.s1

#common method for both classes -- calculate_perimeter
#create Rectangle and square objects and call the method in both of it

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

class Square():
    def __init__(self, s1, new):
        self.s1 = s1
        self.new = new

    def calculate_perimeter(self):
        perimeter = 4 * s1
        return perimeter

    def change_size(self):
        self.s1 = self.s1 + self.new
        perimeter = 4 * self.s1
        return perimeter 

rect = Rectangle(4, 5)
sq = Square(3, 5)

print(rect.calculate_perimeter())
print(sq.change_size())
