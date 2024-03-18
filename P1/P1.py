import numpy as np
import sys
import random
import math
import tkinter as tk

class Board:
    
    block_counter = 1
    def __init__(self, n, special_square_i, special_square_j):
        if(n < 0):
            print("Board size minor than 0")
        if((special_square_i >= n) or (special_square_j >= n)):
            print("Wrong position for special square")
        
        self.board = np.zeros((n,n))
        self.special_square_i = special_square_i
        self.special_square_j = special_square_j
        self.put_special_square(special_square_i, special_square_j)
        
        self.subsquares_stack = []
        self.subsquares_stack.append([ [(len(self.board) - 1, 0), (0, len(self.board) - 1)]
                                 , [special_square_i, special_square_j]])
        
        
    def solve_all(self):
        count = 0
        while(self.next_step()):
            continue
        
    def print(self):
        print(str(self.board))
        return
    
    def to_string(self):
        return str(self.board)
    def get_matrix_state(self):
        return self.board
    
    def next_step(self):
        if (self.subsquares_stack == []):
            return False
        
        [[sub_left_lower_corner, sub_right_upper_corner], [sub_special_square_i, sub_special_square_j]] = self.subsquares_stack.pop()
        
        if((sub_left_lower_corner[0] - sub_right_upper_corner[0]) == 0):
            return True
        if((sub_left_lower_corner[0] - sub_right_upper_corner[0]) == 1):
            self.put_block( sub_left_lower_corner
                        , sub_right_upper_corner
                        , sub_special_square_i
                        , sub_special_square_j)
            return True
        vertical_mid = ((((sub_left_lower_corner[0]) - sub_right_upper_corner[0] )>>1) )
        horizontal_mid = ((((sub_right_upper_corner[1]) - sub_left_lower_corner[1] )>>1) )
        subsquare_middle = [sub_left_lower_corner[0] - vertical_mid, sub_right_upper_corner[1] - horizontal_mid]
        
        center_blank = [0, 0]
        center_blank[0] = subsquare_middle[0] + (0 if (sub_special_square_i >= subsquare_middle[0]) else -1)
        center_blank[1] = subsquare_middle[1] + (0 if (sub_special_square_j >= subsquare_middle[1]) else -1)
        
        # # put_block in the middle
        self.put_block([subsquare_middle[0], subsquare_middle[1] - 1]
                        , [subsquare_middle[0] - 1, subsquare_middle[1]]
                        , center_blank[0]
                        , center_blank[1])

        self.subsquares_stack.append([([[sub_left_lower_corner[0] - vertical_mid - 1, sub_left_lower_corner[1]]
                                        , [sub_right_upper_corner[0], sub_right_upper_corner[1] - horizontal_mid]])
                                        , (np.add(subsquare_middle, [-1, -1])) if ((self.board[(np.add(subsquare_middle, [-1, -1]))[0], (np.add(subsquare_middle, [-1, -1]))[1]]) != 0) else ([sub_special_square_i, sub_special_square_j])])
        self.subsquares_stack.append([[[subsquare_middle[0] - 1, subsquare_middle[1]]
                                        , sub_right_upper_corner]
                                        , (np.add(subsquare_middle, [-1, 0])) if (self.board[(np.add(subsquare_middle, [-1, 0]))[0], (np.add(subsquare_middle, [-1, 0]))[1]] != 0) else ([sub_special_square_i, sub_special_square_j])])
        self.subsquares_stack.append([[sub_left_lower_corner
                                        , [subsquare_middle[0], subsquare_middle[1] - 1]]
                                        , (np.add(subsquare_middle, [0, -1])) if (self.board[(np.add(subsquare_middle, [0, -1]))[0], (np.add(subsquare_middle, [0, -1]))[1]] != 0) else ([sub_special_square_i, sub_special_square_j])])
        self.subsquares_stack.append([[[sub_left_lower_corner[0], sub_right_upper_corner[1] - horizontal_mid]
                                        , [sub_left_lower_corner[0] - vertical_mid, sub_right_upper_corner[1]]]
                                        , (np.add(subsquare_middle, [0, 0])) if ((self.board[(np.add(subsquare_middle, [0, 0]))[0], (np.add(subsquare_middle, [0, 0]))[1]]) != 0) else ([sub_special_square_i, sub_special_square_j])])
        return True    
    def put_block(self, left_lower_corner, right_upper_corner, blank_i, blank_j):
        # Pending checking of left anr rigth corners
        if((blank_i < 0) or (blank_i > (len(self.board) + 1))):
            print("Index of blank out of horizontal board range")
        if((blank_j < 0) or (blank_j > (len(self.board[0]) + 1))):
            print("Index of blank out of vertical board range")
        previous_hole = self.board[blank_i][blank_j]
        self.board[left_lower_corner[0] - 1][left_lower_corner[1]] = self.block_counter
        self.board[left_lower_corner[0]][left_lower_corner[1]] = self.block_counter
        self.board[left_lower_corner[0] - 1][left_lower_corner[1] + 1] = self.block_counter
        self.board[left_lower_corner[0]][left_lower_corner[1] + 1] = self.block_counter
        self.board[blank_i][blank_j] = previous_hole
        self.block_counter += 1
        return
    def put_special_square(self, square_i, square_j):
        self.board[square_i, square_j] = -1
        return

class Interface:
    def start(self):
        if(len(sys.argv) < 2):
            print("Insert the fixed size for solving the Blocking Problem")

        board_size = 0
        try:
            board_size = self.validate_board_size(sys.argv[1])
        except Exception as e: 
            print(e)
            return 1
        
        (special_square_i, special_square_j) = (random.randint(0,board_size-1),  random.randint(0,board_size-1))
        self.board = Board(board_size, special_square_i, special_square_j)
        root = tk.Tk()
        root.title("Colored Frames")
        self.grid = Color_grid(root, board_size, board_size)
        self.grid.create_grid()
        self.grid.draw_matrix(self.board.get_matrix_state())
        boton = tk.Button(text="Siguiente Paso", command=self.next_board_step)
        boton.place(x=0, y=0)
        root.mainloop()

    def validate_board_size(self, size):
        int_size = 0
        
        try:
            int_size = int(size)
        except:
            raise Exception("Board size should be integer")
        
        if(int_size <= 0):
            raise Exception("Board size should be positive")
        if(((math.log2(int_size))%1) != 0):
            raise Exception("Board size should be 2^n shape")
        return int_size
        
    def next_board_step(self):
        self.board.next_step()
        self.grid.draw_matrix(self.board.get_matrix_state())
        
class Color_picker:
    def __init__(self, min_key, max_key):
        self.color_width_space = 16777214 #8-bit rgb max value
        
        self.step=(self.color_width_space/(max_key - min_key))
        self.min_key = min_key

    def get_colors(self):
        color = 0
        colors_array = []
        while(color <= self.color_width_space):
            colors_array.append('#'+ (str(hex(int(color))))[2:].zfill(6)) 
            color += self.step
        return colors_array

    def pick_color(self, key):
        if(key == -1):
            return '#ffffff'
        decimal_color = (key - self.min_key) * self.step
        return '#'+ (str(hex(int(decimal_color))))[2:].zfill(6)

class Color_grid:
    def __init__(self, root, length, width):
        self.square_size = 40
        self.length = length
        self.width = width
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=5, pady=5)
        self.squares = [None for i in range(self.width*self.length)]
    def create_grid(self):
        self.create_square()
        self.color_picker = Color_picker(0, (((self.length * self.width) - 1) / 3))
    
    def create_square(self):
        for i in range(self.length):
            for j in range(self.width):
                self.squares[(i*self.length)+j] = tk.Frame(self.main_frame, width=self.square_size, height=self.square_size, bg='#000000')
                self.squares[(i*self.length)+j].grid(row=i, column=j, padx=5, pady=5)
    def draw_matrix(self, matrix):
        for i in range(self.length):
            for j in range(self.width):
                self.color_square(self.color_picker.pick_color(matrix[i,j]), i, j)

    def color_square(self, color, i , j):
        self.squares[(i*self.width) + j]["bg"] = color


interface = Interface()
interface.start()