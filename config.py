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
N = 9

# Time a processor spends in the critical section (common for all threads) in milliseconds
cs_int = 1

# Time a processor stays in the (release state) in milliseconds
next_req = 1

# Total time to run hte program in seconds
tot_exec_time = 5

# size of voting set
k = 5

# 0 1 2
# 3 4 5
# 6 7 8
# Voting Sets
V0 = [0,1,2,3,6]
V1 = [0,1,2,4,7]
V2 = [0,1,2,5,8]
V3 = [3,4,5,0,6]
V4 = [3,4,5,1,7]
V5 = [3,4,5,2,8]
V6 = [6,7,8,0,3]
V7 = [6,7,8,1,6]
V8 = [6,7,8,2,5]

# Critical section is occupied or not
CS = 0
