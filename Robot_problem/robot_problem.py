class Robot:
    def __init__(self, rows, cols):
        print("cols==", cols)
        print("rows==",rows)
        self.rows = rows
        self.cols = cols
        self.directions = ['N', 'E', 'S', 'W']
        self.row = 0
        self.col = 0
        self.direction = 'S'

    def move(self):
        if self.direction == 'N' and self.row > 0:
            self.row -= 1
        elif self.direction == 'E' and self.col < self.cols - 1:
            print("col==",self.col)
            print("cols==",self.cols)
            self.col += 1
        elif self.direction == 'S' and self.row < self.rows - 1:
            self.row += 1
        elif self.direction == 'W' and self.col > 0:
            self.col -= 1
#MSMMEMM
    def turn(self, instruction):
        if instruction == 'N':
            self.direction = 'N'
        elif instruction == 'E':
            self.direction = 'E'
        elif instruction == 'S':
            self.direction = 'S'
        elif instruction == 'W':
            self.direction = 'W'

    def execute_command(self, command):
        for instruction in command:
            if instruction == 'M':
                self.move()
            elif instruction in ['N', 'E', 'S', 'W']:
                self.turn(instruction)

    def get_position(self):
        return f'Robot Location: ({self.row},{self.col},{self.direction})'


def main():
    grid = Robot(4, 5)  # Create a 5x4 grid
    command = input("Enter the command: ")
    grid.execute_command(command)
    print(grid.get_position())  # Output the final position of the robot


if __name__ == '__main__':
    main()
