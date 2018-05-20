from udp_com import ReceiverUDP

ins_receiver = ReceiverUDP(127.0.0.1, 5505)
gps_receiver = ReceiverUDP(127.0.0.1, 5506)
truth_receiver = ReceiverUDP(127.0.0.1, 5507)

if __name__ == "__main__":
    
    while True:
        print("INS message:")
        print(ins_receiver.get_msg())
