import numpy as np


class Board:
    
    def __init__(self, n, special_square_i, special_square_j):
        if(n < 0):
            print("Board size minor than 0")
        if((special_square_i >= n) or (special_square_j >= n)):
            print("Wrong position for special square")
        
        self.board = np.zeros((n,n))

        self.special_square_i = special_square_i
        self.special_square_j = special_square_j
        self.subsquares_stack = []
        subsquares_stack.append( ((len(self.board), 0), (len(self.board), 0))
                                 , (special_square_i, special_square_j) )

    def solve_all(self):
        while(self.next_step()):
            self.print()
        
    def print(self):
        return
    
    def next_step(self):
        if (self.subsquares_stack == []):
            return False
        
        ((left_lower_corner, right_upper_corner), (special_square_i, special_square_j)) = self.subsquares_stack.popleft()
        
        if((left_lower_corner[0] == 1) or (left_lower_corner[1] == 1)):
            print("Solved Subsquare")
            return False
        if((left_lower_corner[0] == 2) and (left_lower_corner[1] == 2)):
            # put_block
            return False
        
        # put_block in the middle

        vertical_mid = left_lower_corner[0]>>1
        horizontal_mid = right_upper_corner[1]>>1

        
        
        # Push to stack the four new squares for next steps
        # [(left_lower, right_upper), (left_lower, right_upper)]
        # [(left_lower, right_upper), (left_lower, right_upper)]
        subsquares_stack.append( (left_lower_corner[0] - vertical_mid, left_lower_corner[1])
                                ,(right_upper_corner[0], right_upper_corner[1] - horizontal_mid)  )
        subsquares_stack.append( (left_lower_corner[0] - vertical_mid, left_lower_corner[1] + horizontal_mid)
                                , right_upper_corner)
        subsquares_stack.append( left_lower_corner
                                ,(right_upper_corner[0] + vertical_mid, right_upper_corner[1] - horizontal_mid)  )
        subsquares_stack.append( (left_lower_corner[0], left_lower_corner[1] + horizontal_mid)
                                ,(right_upper_corner[0] + vertical_mid, right_upper_corner[1])  )
        
        return True    
    def put_block(self, left_lower_corner, right_upper_corner, blank_i, blank_j):
        return
    def put_square(self, square_i, square_j):
        return

