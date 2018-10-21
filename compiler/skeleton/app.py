class MyApp(frenetic.App):
    
    client_id = "quick_start"
    
    def __init__(self):
        frenetic.App.__init__(self)
        self.nib = NIB()

    def connected(self):
        self.update (id >> SendToController("qq"))

    #def packet_in(self,dpid,port_id,payload):
    #    pkt = Packet.from_payload(dpid,port_id,payload)

