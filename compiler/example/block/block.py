import sys,logging
import frenetic
from frenetic.packet import *
from frenetic.syntax import *

class NIB(object):
	def __init__(self):
		self.s1 = False
		self.s2 = False
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
		if(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.block and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
		elif(self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and self.nib.block and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 2 ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( self.nib.ip4Src == 2 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( self.nib.Port == 2 ) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(self.nib.s1 and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif(( self.nib.Port == 2 ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(self.nib.s1 and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.block and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = True 
			self.nib.s2 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = True 
		elif((not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 2 ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif((not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Src == 1 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 3 ) and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 2 ) and self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s1 and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 2 ) and self.nib.s1 and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 2 ) and self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif((not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.block and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( self.nib.ip4Src == 1 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and ( self.nib.Port == 3 ) and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif((not self.nib.s2) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif((not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(self.nib.s1 and ( self.nib.ip4Dst == 3 ) and self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = True 
			self.nib.s2 = True 
		elif(self.nib.s1 and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( self.nib.ip4Src == 1 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.block) and ( self.nib.Port == 1 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 0 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.s1 and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif((not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif((not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif(self.nib.s1 and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif((not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(self.nib.s1 and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif((not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = True 
			self.nib.s2 = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( self.nib.Port == 2 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.block and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and (not self.nib.s2) and self.nib.block and ( self.nib.ip4Src == 2 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif((not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 2 ) and ( self.nib.Port == 0 ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 2 ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif((not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.block and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( self.nib.ip4Dst == 2 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s1 and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and self.nib.block and ( self.nib.ip4Src == 2 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s1) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif((not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s1 and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(self.nib.s1 and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 3 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and (not self.nib.s2) and self.nib.block and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( self.nib.ip4Dst == 2 ) and self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 2 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( self.nib.ip4Dst == 2 ) and self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.block and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.block and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif((not self.nib.block) and (not self.nib.s1) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(self.nib.s1 and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and ( self.nib.Port == 3 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s1 and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( self.nib.ip4Src == 1 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.block and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( self.nib.Port == 2 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.block and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.block and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.block and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 0 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.block and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.block and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( self.nib.Port == 2 ) and self.nib.s1 and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( self.nib.ip4Dst == 2 ) and ( self.nib.Port == 0 ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif((not self.nib.s2) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(self.nib.block and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s2 and self.nib.s1 and ( self.nib.ip4Src == 2 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s2 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s1 and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and self.nib.block and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s2 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.block = True 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.block = True 
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.s1 = False 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and ( self.nib.Port == 0 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
		elif(( (pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = True 
			self.nib.s2 = False 
			self.nib.block = True 
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3") ) and self.nib.block and self.nib.s2):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.block = True 
		if ((pkt.ip4Dst == "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3")):
			self.nib.ip4Dst = "10.0.0.2"
		elif ((pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst == "10.0.0.1" and pkt.ip4Dst != "10.0.0.3")):
			self.nib.ip4Dst = "10.0.0.1"
		elif ((pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst == "10.0.0.3")):
			self.nib.ip4Dst = "10.0.0.3"
		elif ((pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3")):
			self.nib.ip4Dst = "10.0.0.4"
		if ((pkt.ip4Src == "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3")):
			self.nib.ip4Src = "10.0.0.1"
		elif ((pkt.ip4Src != "10.0.0.1" and pkt.ip4Src == "10.0.0.2" and pkt.ip4Src != "10.0.0.3")):
			self.nib.ip4Src = "10.0.0.2"
		elif ((pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src == "10.0.0.3")):
			self.nib.ip4Src = "10.0.0.3"
		elif ((pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3")):
			self.nib.ip4Src = "10.0.0.4"
		print pkt
		print actions
		self.pkt_out( dpid, payload , actions) 
app = MyApp()
app.start_event_loop()
