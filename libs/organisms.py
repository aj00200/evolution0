'''Classes and functions used to create and control organisms.'''

class Organism(object):
    '''A virtual organism which can evolve'''
    def __init__(self, goal, sequence, pool, maxlength = 25):
        self.goal = goal
        self.sequence = sequence
        self.pool = pool
        self.maxlength = maxlength
        
        self.one_match = False        # Stop after one match
        self.running = True           # Loop is running
        self.testrange = range(0, 64) # TODO: Allow range detection
        
    def loop(self): 
        '''Have the organism run one cycle'''
        while self.running:
            if self.test_all():
                print('[*] Goal reached: %s' % self.sequence)
                if self.one_match:
                    self.running = False
                    break
                else:
                    self.sequence = self.pool.generate_sequence(self.maxlength)
            else: # Evolve - Get random operations
                self.sequence = self.pool.generate_sequence(self.maxlength)
                    
    def test_all(self):
        '''Test the current sequence with a wide range of values.'''
        all_work = True

        for each in self.testrange:
            current_result = self.sequence.run(each)
            if not self.goal.match(each, current_result): # Failed test
                all_work = False
        return all_work
