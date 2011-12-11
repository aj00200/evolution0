class Goal(object):
    '''Holds various types of goals including dictionaries, lists, and single
    goals. This provides abundant flexibility for finding functions or just
    a simple way to reach a set goal.
    '''
    def __init__(self, goal):
        if isinstance(goal, list):
            self.goaltype = 'list'
        elif isinstance(goal, dict):
            self.goaltype = 'dict'
        else:
            self.goaltype = 'single'
        self.goal = goal
        
    def match(self, value, result):
        '''Returns true if `result` matches the goal. `value` should be
        the value that was provided to the sequence to get this goal.'''
        if self.goaltype == 'list':
            if result in self.goal:
                return True
            
        elif self.goaltype == 'dict':
            if value in self.goal:
                if self.goal[value] == result:
                    return True
            else:
                return True
                
        elif self.goaltype == 'single':
            if result == self.goal:
                return True
            
        else:
            raise GoalError('Unknown goal type')
        
        return False
    
class GoalError(Exception):
    pass