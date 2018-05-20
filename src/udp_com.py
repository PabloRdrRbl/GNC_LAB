import socket

class ReceiverUDP(object):
    
    def __init__(self, UDP_IP, UDP_PORT):
        """Return a new ReceiverUDP object."""
        
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT

        self.sock = socket.socket(socket.AF_INET,     # Internet
                                  socket.SOCK_DGRAM)  # UDP

        self.bind()


    def bind(self):
        """Bind receiver."""
        
        self.sock.bind((self.UDP_IP, self.UDP_PORT))


    def get_msg(self):
        """Get message."""
        
        data, addr = self.sock.recvfrom(1024)  # Buffer size is 1024 bytes

        return data
