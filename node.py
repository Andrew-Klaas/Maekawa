# Comments types
# @checklater
from config import *
from msglayer import *
from SendingLayer import *



######################################
# MAEKAWA NODE
######################################
class Maekawa_node(threading.Thread):
    """
        Implementing Maekawa mutal exclusion algorithm

    """

    def __init__(self, begin, All_msg_qs, my_q, node_id, message_lock):
        # Node params/variables
        super(Maekawa_node, self).__init__()
        self._stoprequest = threading.Event()
        self.node_id = node_id
        self.V = []
        self.all_message_queues = All_msg_qs      
        self.received_message_queue = my_q
        self.send_message_queue = list()
        self.message_lock = message_lock     
        self.num_recv_msg = list()    
        self.priority_q = list()    

        #initialization
        self.State = list()
        self.State.append("RELEASED")
        self.Lamport_ts = list()

        # Initialising the messaging layer for this node
        self.msg_layer = MessagingLayer(self.node_id, self.received_message_queue, self.send_message_queue, self.message_lock, self.num_recv_msg, self.State, self.Lamport_ts, self.priority_q)    
        self.msg_layer.start()
       
        self.send_layer = SendingLayer(self.node_id, self.all_message_queues, self.send_message_queue, self.message_lock, self.Lamport_ts)
        self.send_layer.start()
        
        self.total_recv_msg = 0
        self.begin = begin

        self.initiated = 0
        self.start_time = time.time()
        # begin algorithm
        #self.maekawa_begin()
        self.Request_num = 0

        #print "node: " + str(self.node_id) + " created \n" 


    def maekawa_begin(self):
        while 1:
           if ((time.time() - self.start_time)  > tot_exec_time):
               sys.exit(0)

           self.init_v()

           #request to enter critical section  

           print str(self.node_id) + " REQUESTING CRITICAL SECTION \n"

           self.m_request()

           # inside critical section
           time.sleep(cs_int/1000)
           print str(self.node_id) + " INSIDE CRITICAL SECTION \n"
           print "TIME:" + str(time.time()) + " NODE:" + str(self.node_id) + " NODE-LIST:" + str(self.V) + "\n"
           # release critical section
           self.m_release()

           # wait until next request
           time.sleep(next_req/1000)

    # Perform (enter) part of maekaw algo
    def m_request(self):
        self.State.append("WANTED")
        self.send("REQUEST")
        while self.total_recv_msg != M:
            #print "NODE:" + str(self.node_id) +  " " + str(self.total_recv_msg) + "\n"
            with self.message_lock:
                #print "NODE:" + str(self.node_id) + " YEHAW:" + str(self.num_recv_msg) + "\n"
                #print self.total_recv_msg
                if self.num_recv_msg:
                    value = self.num_recv_msg.pop() 
                    self.total_recv_msg = self.total_recv_msg + value
        #Critical section obtained 
        CS = 1
        self.State.append("HELD")
        #print str(time.time()) + " Node:" + self.node_id + " VotingSet: " str(self.V) 

    def m_release(self):
        self.total_recv_msg = 0
        self.State.append("RELEASED")
        self.send("RELEASE")

    def join(self, timeout=None):
        self._stoprequest.set()
        super(Maekawa_node, self).join(timeout)

    def send(self, msg):
        #ask all nodes for access to critical section
        with self.message_lock:
            self.Request_num = self.Request_num + 1
            self.Lamport_ts.append(1)
            for v in self.V  :
                self.send_message_queue.append((v, msg, self.Request_num)) 

    def init_v(self):
        if self.node_id == 0:
            self.V = V0
        elif self.node_id == 1:
            self.V = V1
        elif self.node_id == 2:
            self.V = V2
        elif self.node_id == 3:
            self.V = V3
        elif self.node_id == 4:
            self.V = V4
        elif self.node_id == 5:
            self.V = V5
        elif self.node_id == 6:
            self.V = V6
        elif self.node_id == 7:
            self.V = V7
        elif self.node_id == 8:
            self.V = V8
        else:
            print "wrong"

    def run(self):
        while not self._stoprequest.isSet():
            if self.begin:
                if self.initiated == 0:
                    self.maekawa_begin() 
                    self.initiated = 1


##############################


if __name__ == "__main__":
    #print sys.argv

    cs_int = int(sys.argv[1])
    next_req = int(sys.argv[2])
    tot_exec_time = float(sys.argv[3])
    option = int(sys.argv[4])

    begin = list()

    All_msg_qs = list()
    for i in range(N):
        # you may have a problem here
        All_msg_qs.append([]) 

    message_lock = threading.Lock()
    nodes = [ Maekawa_node( begin = begin, All_msg_qs = All_msg_qs, my_q = All_msg_qs[i], node_id = i, message_lock = message_lock) for i in range(N) ]

    for thread in nodes:
        print thread 
        thread.start() 
   

    begin.append(0)

    for thread in nodes:
        thread.join()





