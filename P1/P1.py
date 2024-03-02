import numpy as np
import sys
import random
import math

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
        self.board[square_i, square_j] = 0
        return

class Interface:
    def start(self):
        if(len(sys.argv) < 2):
            print("Insert the fixed size for solving the Blocking Problem")

        board_size = 0
        try:
            board_size = self.validate_board_size(sys.argv[1])
        except Exception as e: print(e)
        
        (special_square_i, special_square_j) = (random.randint(0,board_size-1),  random.randint(0,board_size-1))
        board = Board(board_size, special_square_i, special_square_j)
        print(f"""Solution of the board with size {board_size} and
                    special unique square in (i,j) = ({special_square_i}, {special_square_i})
                    with special 0 number"""
            )
        
        count = 0
        while(board.next_step()):
            print("---------------------")
            count += 1
            print(count)
            print("---------------------")
            board.print()        

        
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
        

interface = Interface()
interface.start()