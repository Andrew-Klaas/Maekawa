# Comments types
# @checklater
from config import *

class Maekawa_node(threading.Thread):
    """
        Implementing Maekawa mutal exclusion algorithm

    """

    def __init__(self, All_msg_qs, my_q, node_id):
        # Node params/variables
        super(Maekawa_node, self).__init__()
        self._stoprequest = threading.Event()
        self.node_id = node_id
        self.all_message_queues = All_msg_qs        # Each element is tuple - (dest, msg)
        self.received_message_queue = my_q
        self.message_lock = threading.Lock()        # Lock object to enforce synchronisation on send and receive message queues

        #initialization
        self.State = RELASED
        self.Voted = False
        self.Lamport_ts  = 0

        # Initialising the messaging layer for this node
        self.msg_layer = MessagingLayer(self.node_id, self.send_message_queue, self.all_message_queues, self.message_lock)
        self.msg_layer.start()

        # begin algorithm
        self.Maekawa_begin()


    def maekawa_begin(self):
        while 1:
           # request to enter critical section  
           self.m_request()

           # inside critical section
           time.sleep(cs_int/1000)

           # release critical section
           self.m_resease()

           # wait until next request
           time.sleep(next_req/1000)

    # Perform (enter) part of maekaw algo
    def m_request(self):
        self.State = WANTED
        self.Lamport_ts += 1
        self.send(REQUEST)
        while num_recv_msg != N:
            pass
        CS = 1
        self.print_log()

    def m_release(self):
        self.State = RELEASED
        self.send(RELEASE)


    def join(self, timeout=None):
        self._stoprequest.set()
        super(Maekawa_node, self).join(timeout)

    def send(self, dest_id, msg):
        #ask all nodes for access to critical section
        with self.message_lock:
            for i in range(N):
                self.all_message_queues[i].append((self.Lamport_ts, msg, self.node_id ))


    def run(self):
        while not self._stoprequest.isSet():
            msg_tuple = None

            with self.message_lock:
                if self.received_message_queue:
                    msg_tuple = self.received_message_queue.pop(0)
            if msg_tuple:
                (sender, msg) = msg_tuple
                if isinstance(msg, str):
                    msg_list = msg.split(' ')
                    cmd = msg_list[0]


                    if log_messages:
                        print("Run: " + msg + " from " + str(sender))
                    # Different commands/requests handled here
                    if cmd == "update_finger_table":
                        self.update_finger_table(int(msg_list[1]), int(msg_list[2]))

                    elif cmd == "update_finger_table_leave":
                        self.update_finger_table_leave(int(msg_list[1]), int(msg_list[2]), int(msg_list[3]))



class Coordinator(object):
    """
    The coordinator for the interfacing with the Maekawa network. 
    """

    def __init__(self, node_id):
        # Node params/variables
        self.node_id = node_id
        self.message_lock = threading.Lock()        # Lock object to enforce synchronisation on send and receive message queues

        All_msg_qs = list()
        for i in range(N):
           All_msg_qs[i].append([]) 

        nodes = [ Maekawa_node( all_qs = All_msg_qs, my_q = all_msg_qs[i], node_id = i) for i in range(N)

        for Node in Nodes
            Node.Start() 

        # total execution time
        sleep(tot_exec_time)

        for Node in nodes
            Node.join()

        # References maintained only to stop the thread. All the commands are send through network as messages



coord = None

if __name__ == "__main__":
    print sys.argv
    coord = Coordinator(coordinator_id)

    cs_int = sys.argv[1]
    next_req = sys.argv[2]
    tot_exec_time = sys.argv[3]
    option = sys.argv[4]

else:
    # Start a coordinator anyway
    coord = Coordinator(coordinator_id)



