import json
import zmq

from AbortException import AbortException

class zmq_obj_function:

    def __init__(self, socket):
        self.socket = socket

    def __call__(self, x):
        return self.request_evaluation(x)
        
    def request_evaluation(self, x):
        """Objective function to send parameters to a remote socket and receive the result value"""

        print("Sending parameters: {}".format(x))

        self.socket.send(json.dumps(x.tolist()).encode('utf-8'))

        reply = self.socket.recv()
        print("Received reply: {}".format(reply))
        
        if (reply == b"abort"):
            raise AbortException()
        
        return float(reply)
        
