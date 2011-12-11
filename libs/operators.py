from __future__ import division
import math

import libs.objects

# Math Operators
class Add1(libs.objects.Operation):
    def operate(self, value):
        return value + 1
    
class Sub1(libs.objects.Operation):
    def operate(self, value):
        return value - 1

class Mult2(libs.objects.Operation):
    def operate(self, value):
        return value * 2
    
class Div2(libs.objects.Operation):
    def operate(self, value):
        return value / 2
    
class Pow2(libs.objects.Operation):
    def operate(self, value):
        return math.pow(value, 2)
    
class Pow3(libs.objects.Operation):
    def operate(self, value):
        return math.pow(value, 3)
    
class Mod2(libs.objects.Operation):
    def operate(self, value):
        return value % 2
    
class Mod3(libs.objects.Operation):
    def operate(self, value):
        return value % 3
    
def get_basic_pool():
    return libs.objects.Pool([
            Add1(),
            Sub1(),
            Mult2(),
            Div2(),
            Pow2(),
            Pow3(),
            Mod2(),
            Mod3()
    ])
    
# Crypto Operators
class Translate(libs.objects.Operation):
    def operate(self, value):
        return value