#! /usr/bin/env python

# Copyright 2011 Aj00200 <aj00200@aj00200.org> - All rights reserved.
# Please contact me before using this code, I will probably say yes!

import libs.organisms
import libs.operators
import libs.objects
import libs.goals

goal = libs.goals.Goal({3:-1, 4:0, 5:1, 100:0, 101:-1})
pool = libs.operators.get_basic_pool()
sequence = pool.generate_sequence()

organism = libs.organisms.Organism(goal, sequence, pool, maxlength = 5)
organism.loop()
