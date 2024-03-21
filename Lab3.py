#task1
squares = [x**2 for x in range(1, 11)]
print(squares)

#task2
def generate_squares(start, end):
    squares = [x**2 for x in range(start, end+1)]
    return squares

start = 1
end = 10
print(generate_squares(start, end))

#task3
class SquareGenerator:
    def generate_squares(self, start, end):
        squares = [x**2 for x in range(start, end+1)]
        return squares

# Example usage:
generator = SquareGenerator()
print(generator.generate_squares(1, 10))

#task4
import math

class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end+1)]

    def calculate_square_roots(self, numbers):
        return [math.sqrt(num) for num in numbers]

# Usage
sg = SquareGenerator()
squares = sg.generate_squares(1, 10)
square_roots = sg.calculate_square_roots(squares)

print("Generated squares:", squares)
print("Square roots:", square_roots)

#task5
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range cannot be less than start")
        return [x**2 for x in range(start, end+1)]

