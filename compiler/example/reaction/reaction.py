import sys,logging
import frenetic
from frenetic.packet import *
from frenetic.syntax import *

class NIB(object):
	def __init__(self):
		self.block = False
		self.ip4Dst = 0
		self.Port = 0
		self.ip4Src = 0
		self.counter = 0



class MyApp(frenetic.App):
	
	client_id = "quick_start"
	
	def __init__(self):
		frenetic.App.__init__(self)
		self.nib = NIB()

	def connected(self):
		self.update (id >> SendToController("qq"))

	#def packet_in(self,dpid,port_id,payload):
	#	pkt = Packet.from_payload(dpid,port_id,payload)

	def packet_in(self,dpid,port_id,payload):
		pkt = Packet.from_payload(dpid,port_id,payload)
		actions = []
		if(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src == "10.0.0.2") )):
			actions += [SetPort (1)]
			self.nib.Port = 1
		elif(( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.2") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
		elif(( (pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src == "10.0.0.2") )):
			actions += [SetPort (3)]
			self.nib.Port = 2
		if ((pkt.ip4Dst == "10.0.0.2")):
			self.nib.ip4Dst = 0
		elif ((pkt.ip4Dst == "10.0.0.1")):
			self.nib.ip4Dst = 1
		elif ((pkt.ip4Dst == "10.0.0.3")):
			self.nib.ip4Dst = 2
		elif ((pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3")):
			self.nib.ip4Dst = 3
		if ((pkt.ip4Src == "10.0.0.1")):
			self.nib.ip4Src = 0
		elif ((pkt.ip4Src == "10.0.0.2")):
			self.nib.ip4Src = 1
		elif ((pkt.ip4Src == "10.0.0.3")):
			self.nib.ip4Src = 2
		elif ((pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3")):
			self.nib.ip4Src = 3
		print pkt
		print actions
		self.pkt_out( dpid, payload , actions) 
app = MyApp()
app.start_event_loop()
