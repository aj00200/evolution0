'''Basic objects which are used a lot in the program.'''
import random

class Sequence(list):
    '''A sequences of operations which can be run in a sequence'''
    def run(self, value):
        '''Run each element in a sequence and return the final output.'''
        current = value
        for item in self:
            current = item.operate(current)
        return current
    
class Operation(object):
    '''Preforms an operation. Often times simple operations like division
    need to be preformed but other times a complex sequence of operations
    needs to be preformed. All desired operations can be placed into a pool
    to be used at random by the organism.
    '''
    def operate(self, value):
        '''Preform the operation.'''
        return value
    
class Pool(list):
    '''A collection of all operations which can be used. In other words,
    a gene pool.
    '''
    def get_random(self):
        '''Get a random operator from the pool.'''
        return self[random.randint(0, len(self) - 1)]
    
    def generate_sequence(self, maxlength = 25):
        '''Returns a random sequence of operations'''
        sequence = Sequence()
        rand_len = random.randint(1, maxlength)
        for each in range(0, rand_len):
            sequence.append(self.get_random())
        return sequence