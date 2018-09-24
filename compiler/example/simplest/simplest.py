import sys,logging
import frenetic
from frenetic.packet import *
from frenetic.syntax import *


class NIB(object):
    def __init__(self):
		self.i1 = False
		self.i3 = False
		self.o2 = False
		self.o4 = False




class MyApp(frenetic.App):
    
    client_id = "quick_start"
    
    def __init__(self):
        frenetic.App.__init__(self)
        self.nib = NIB()

    def connected(self):
        self.update (id >> SendToController("qq"))

    #def packet_in(self,dpid,port_id,payload):
    #    pkt = Packet.from_payload(dpid,port_id,payload)
        actions = []

	def packet_in(self,dpid,port_id,payload):
		pkt = Packet.from_payload(dpid,port_id,payload)
		actions = []

		if ( self.nib.i1 and self.nib.i3 and self.nib.o2 and self.nib.o4 and ( not self.nib._jx_b0 ) ):
			if ( pkt.ip4Src == "10.0.0.1" and pkt.ip4Src == "10.0.0.2" ):
				self.nib.i1= True
				self.nib.i3= True
				actions += SetPort(2)
				self.nib.o2= True
				actions += SetPort(1)
				self.nib.o4= True

		elif ( self.nib.i1 and self.nib.i3 and self.nib.o2 and self.nib.o4 and ( not self.nib._jx_b0 ) ):
			if ( pkt.ip4Src == "10.0.0.1" and ( not pkt.ip4Src == "10.0.0.2" ) ):
				self.nib.i1= True
				self.nib.i3= False
				actions += SetPort(2)
				self.nib.o2= True

		elif ( self.nib.i1 and ( not self.nib.i3 ) and self.nib.o2 and ( not self.nib._jx_b0 ) ):
			if ( pkt.ip4Src == "10.0.0.1" and pkt.ip4Src == "10.0.0.2" ):
				self.nib.i1= True
				self.nib.i3= True
				actions += SetPort(2)
				self.nib.o2= True
				actions += SetPort(1)
				self.nib.o4= True

		elif ( self.nib.i1 and ( not self.nib.i3 ) and self.nib.o2 and ( not self.nib._jx_b0 ) ):
			if ( pkt.ip4Src == "10.0.0.1" and ( not pkt.ip4Src == "10.0.0.2" ) ):
				self.nib.i1= True
				self.nib.i3= False
				actions += SetPort(2)
				self.nib.o2= True

		elif ( self.nib.i1 and self.nib.i3 and self.nib.o2 and self.nib.o4 and ( not self.nib._jx_b0 ) ):
			if ( ( not pkt.ip4Src == "10.0.0.1" ) and pkt.ip4Src == "10.0.0.2" ):
				self.nib.i1= False
				self.nib.i3= True
				actions += SetPort(1)
				self.nib.o4= True

		elif ( self.nib.i1 and self.nib.i3 and self.nib.o2 and self.nib.o4 and ( not self.nib._jx_b0 ) ):
			if ( ( not pkt.ip4Src == "10.0.0.1" ) and ( not pkt.ip4Src == "10.0.0.2" ) ):
				self.nib.i1= False
				self.nib.i3= False

		elif ( self.nib.i1 and ( not self.nib.i3 ) and self.nib.o2 and ( not self.nib._jx_b0 ) ):
			if ( ( not pkt.ip4Src == "10.0.0.1" ) and pkt.ip4Src == "10.0.0.2" ):
				self.nib.i1= False
				self.nib.i3= True
				actions += SetPort(1)
				self.nib.o4= True

		elif ( self.nib.i1 and ( not self.nib.i3 ) and self.nib.o2 and ( not self.nib._jx_b0 ) ):
			if ( ( not pkt.ip4Src == "10.0.0.1" ) and ( not pkt.ip4Src == "10.0.0.2" ) ):
				self.nib.i1= False
				self.nib.i3= False

		elif ( ( not self.nib.i1 ) and self.nib.i3 and self.nib.o4 and ( not self.nib._jx_b0 ) ):
			if ( pkt.ip4Src == "10.0.0.1" and pkt.ip4Src == "10.0.0.2" ):
				self.nib.i1= True
				self.nib.i3= True
				actions += SetPort(2)
				self.nib.o2= True
				actions += SetPort(1)
				self.nib.o4= True

		elif ( ( not self.nib.i1 ) and self.nib.i3 and self.nib.o4 and ( not self.nib._jx_b0 ) ):
			if ( pkt.ip4Src == "10.0.0.1" and ( not pkt.ip4Src == "10.0.0.2" ) ):
				self.nib.i1= True
				self.nib.i3= False
				actions += SetPort(2)
				self.nib.o2= True

		elif ( ( not self.nib.i1 ) and ( not self.nib.i3 ) and ( not self.nib._jx_b0 ) ):
			if ( pkt.ip4Src == "10.0.0.1" and pkt.ip4Src == "10.0.0.2" ):
				self.nib.i1= True
				self.nib.i3= True
				actions += SetPort(2)
				self.nib.o2= True
				actions += SetPort(1)
				self.nib.o4= True

		elif ( ( not self.nib.i1 ) and ( not self.nib.i3 ) and ( not self.nib._jx_b0 ) ):
			if ( pkt.ip4Src == "10.0.0.1" and ( not pkt.ip4Src == "10.0.0.2" ) ):
				self.nib.i1= True
				self.nib.i3= False
				actions += SetPort(2)
				self.nib.o2= True

		elif ( ( not self.nib.i1 ) and self.nib.i3 and self.nib.o4 and ( not self.nib._jx_b0 ) ):
			if ( ( not pkt.ip4Src == "10.0.0.1" ) and pkt.ip4Src == "10.0.0.2" ):
				self.nib.i1= False
				self.nib.i3= True
				actions += SetPort(1)
				self.nib.o4= True

		elif ( ( not self.nib.i1 ) and self.nib.i3 and self.nib.o4 and ( not self.nib._jx_b0 ) ):
			if ( ( not pkt.ip4Src == "10.0.0.1" ) and ( not pkt.ip4Src == "10.0.0.2" ) ):
				self.nib.i1= False
				self.nib.i3= False

		elif ( ( not self.nib.i1 ) and ( not self.nib.i3 ) and ( not self.nib._jx_b0 ) ):
			if ( ( not pkt.ip4Src == "10.0.0.1" ) and pkt.ip4Src == "10.0.0.2" ):
				self.nib.i1= False
				self.nib.i3= True
				actions += SetPort(1)
				self.nib.o4= True

		elif ( ( not self.nib.i1 ) and ( not self.nib.i3 ) and ( not self.nib._jx_b0 ) ):
			if ( ( not pkt.ip4Src == "10.0.0.1" ) and ( not pkt.ip4Src == "10.0.0.2" ) ):
				self.nib.i1= False
				self.nib.i3= False

		#Updating Internal State Variables 
		print pkt
		self.pkt_out( dpid, payload , actions) 


app = MyApp()
app.start_event_loop()
