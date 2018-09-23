import sys,logging
import frenetic
from frenetic.packet import *
from frenetic.syntax import *


class NIB(object):
    def __init__(self):
		self.i1 = False
		self.i2 = False
		self.i3 = False




class MyApp(frenetic.App):
    
    client_id = "quick_start"
    
    def __init__(self):
        frenetic.App.__init__(self)
        self.nib = NIB()

    def connected(self):
        self.update (id >> SendToController("qq"))

    #def packet_in(self,dpid,port_id,payload):
    #    pkt = Packet.from_payload(dpid,port_id,payload)
    #    actions = []

	def packet_in(self,dpid,port_id,payload):
		pkt = Packet.from_payload(dpid,port_id,payload)
		actions = []

		if ( self.nib.i1 and self.nib.i2 and self.nib.i3 ):
			if ( pkt.ipProto == 3 ):
				self.nib.i1= True
				self.nib.occurred == True
				self.nib.i2= True
				actions += []
				self.nib.i3= False

		elif ( self.nib.i1 and self.nib.i2 and self.nib.i3 ):
			if ( ( not pkt.ipProto == 3 ) ):
				self.nib.i1= False
				actions += []
				self.nib.i3= False

		elif ( ( not self.nib.i1 ) and self.nib.i2 and self.nib.i3 ):
			if ( pkt.ipProto == 3 ):
				self.nib.i1= True
				self.nib.occurred == True
				self.nib.i2= True
				actions += []
				self.nib.i3= False

		elif ( ( not self.nib.i1 ) and self.nib.i2 and self.nib.i3 ):
			if ( ( not pkt.ipProto == 3 ) ):
				self.nib.i1= False
				actions += []
				self.nib.i3= False

		elif ( ( not self.nib.i1 ) and ( not self.nib.i2 ) ):
			if ( ( not pkt.ipProto == 3 ) ):
				self.nib.i1= False
				actions += []
				self.nib.i3= False

		#Updating Internal State Variables 
		print pkt
		self.pkt_out( dpid, payload , actions) 


app = MyApp()
app.start_event_loop()
