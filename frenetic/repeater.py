import frenetic
from frenetic.syntax import *
from frenetic.packet import *
from nib import *

class RepeaterApp(frenetic.App):

    client_id = "quick_start"

    def __init__(self):
        frenetic.App.__init__(self)
        self.NIB = nib()

    def connected(self):
        print "hahaha"
        self.update(id >> SendToController("repeater_app"))
    
    def packet_in(self,dpid,port_id,payload):
        out_port_id = 2 if port_id == 1 else 1
        pkt = Packet.from_payload(dpid,port_id,payload) 
        if (pkt.ip4Src == "10.0.0.1"):
            print "from 1"
        print dpid,port_id,pkt
        
         
        self.pkt_out(dpid,payload,[SetPort(1,2,3,4,5)])
        """ 
        if(self.NIB.allow):
            print "allow"
            self.pkt_out(dpid,payload,SetPort(od (port_id)),port_id)
        else:
            print "deny"
            self.pkt_out(dpid,payload,SetPort(3),port_id)

        self.NIB.flip()
        """
        
app = RepeaterApp()
app.start_event_loop()
