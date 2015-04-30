'''
The configuration file for the ChordSystem
'''

import socket
import Queue
import threading
import random
import time
import sys
import pickle

RELEASED = 0
WANTED = 1
HELD = 2

REQUEST = 0
GRANTED = 1
FAILED = 2
YIELD = 3
INQUIRE = 4
RELEASE = 5
TOLATE = 6

NUM_IDENTIFIER_BITS = 8
MAX_NODES = 2**NUM_IDENTIFIER_BITS

# can be later changed to include unique random ids
node_ids = range(9) # number of nodes could be inferred from node_ids list

time_out = 12

log_messages = False

####################################
# MP3
####################################

# Number of fixed Nodes
N = 3

# Number of nodes in voting set
M = 2

# Time a processor spends in the critical section (common for all threads) in milliseconds
cs_int = 0

# Time a processor stays in the (release state) in milliseconds
next_req = 0

# Total time to run hte program in seconds
tot_exec_time =  0

# size of voting set
k = 2

# print option on received msg
option = 0

# 0 1 2
# 3 4 5
# 6 7 8
# Voting Sets
V0 = [0,1]
V1 = [1,2]
V2 = [2,0]

#V2 = [0,1,5,8]
V3 = [4,5,0,6]
V4 = [3,5,1,7]
V5 = [3,4,2,8]
V6 = [7,8,0,3]
V7 = [6,8,1,6]
V8 = [6,7,2,5]

# Critical section is occupied or not
CS = 0
