from search import *

class MissCannibalsVariant(Problem):
    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        """Define goal state and initialize the problem."""
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        self.boat_capacity = 3
        super().__init__(initial, goal)
    
    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False
    
    def result(self, state, action):
        m, c, on_left = state
        M = action.count('M')
        C = action.count('C')
        
        if on_left:
            new_m = m - M
            new_c = c - C
            new_side = False
        else:
            new_m = m + M
            new_c = c + C
            new_side = True
        
        return (new_m, new_c, new_side)
    
    def actions(self, state):
        m, c, on_left = state
        possible_actions = []
        
        for M in range(self.boat_capacity + 1):
            for C in range(self.boat_capacity + 1):
                if 1 <= M + C <= self.boat_capacity:
                    action = 'M' * M + 'C' * C
                    possible_actions.append(action)
        
        return possible_actions

if __name__ == '__main__':
    mc = MissCannibalsVariant(4,4)
    

    print(mc.goal_test((0, 0, False)))  
    print(mc.goal_test((3, 3, True)))   
    
 
    print(mc.actions((3, 3, True)))  
    
  
    print(mc.result((3, 3, True), 'MC'))  
