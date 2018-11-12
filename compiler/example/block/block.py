import sys,logging
import frenetic
from frenetic.packet import *
from frenetic.syntax import *

class NIB(object):
	def __init__(self):
		self.s1 = False
		self.s2 = False
		self.s3 = False
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
		if(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",492
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1372
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",657
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s3 and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
			print "case",1193
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",517
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",200
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",104
		elif(( self.nib.Port == 0 ) and self.nib.s3 and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1117
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",54
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",899
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",884
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1340
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",95
		elif(( self.nib.ip4Dst == 4 ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",758
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",848
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",536
		elif(self.nib.block and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 3 )):
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = True 
			print "case",8
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",729
		elif((not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1012
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",553
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.block) and ( self.nib.ip4Src == 1 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",258
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",494
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",447
		elif(( self.nib.ip4Dst == 4 ) and (not self.nib.s3) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1)):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1171
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",643
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",886
		elif(self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",983
		elif(self.nib.s3 and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
			print "case",921
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1311
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",770
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
			print "case",253
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",465
		elif(self.nib.block and (not self.nib.s2) and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = True 
			print "case",347
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",806
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",139
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",661
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",1094
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",574
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",232
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 0 or self.nib.Port == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",581
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",169
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",438
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",1141
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",269
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",454
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",107
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1342
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s1 and self.nib.s3 and self.nib.block):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",835
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",479
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",582
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",920
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",56
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",124
		elif((not self.nib.s3) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",272
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",988
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",268
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1194
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.s3 = True 
			print "case",698
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",9
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",186
		elif(( self.nib.Port == 0 ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",1115
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",446
		elif(( self.nib.ip4Dst == 4 ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1270
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",172
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",51
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1203
		elif(( self.nib.ip4Dst == 4 ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",756
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s1 and self.nib.s3 and self.nib.block):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",816
		elif(( self.nib.Port == 0 ) and self.nib.s3 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2) and ( (pkt.ip4Dst == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",935
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",760
		elif(( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = True 
			print "case",259
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1049
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",968
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",772
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.block and self.nib.s3 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",885
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",79
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",427
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1202
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",254
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1337
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",390
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1215
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",307
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1314
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",504
		elif(( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",550
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and self.nib.s3 and self.nib.block and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 3 )):
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = True 
			print "case",256
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",763
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",1190
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1214
		elif(self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1065
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",117
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",898
		elif(( self.nib.ip4Dst == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Dst == "10.0.0.2") )):
			self.nib.s1 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s3 = True 
			print "case",1143
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1309
		elif(self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1016
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",603
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",727
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",84
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",458
		elif(( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and (not self.nib.s2)):
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1010
		elif(( self.nib.ip4Dst == 4 ) and (not self.nib.s3) and ( (pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1)):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1173
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1189
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",148
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",441
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",668
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			self.nib.s3 = True 
			print "case",695
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1308
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",39
		elif((not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",451
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",666
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",173
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",792
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",106
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1140
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",818
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.block = False 
			self.nib.s2 = False 
			print "case",563
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",231
		elif(( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",354
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",579
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",774
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",267
		elif(self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",981
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",201
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",665
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",105
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",275
		elif((not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",422
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",531
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",312
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",239
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",654
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",790
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",73
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 0 ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",768
		elif(( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",368
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1200
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",865
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",814
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",401
		elif((not self.nib.s3) and ( self.nib.ip4Src == 1 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",313
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",992
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",1331
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",16
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",74
		elif(( self.nib.ip4Dst == 4 ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.2") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",1282
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1303
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",904
		elif((not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",369
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1345
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",211
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1316
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",480
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",751
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",352
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",371
		elif(self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1060
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",86
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",403
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",1368
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			print "case",943
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1334
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",122
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1195
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",18
		elif(( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = True 
			print "case",270
		elif(self.nib.s3 and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",977
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1148
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 0 or self.nib.Port == 2 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",203
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",153
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",523
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1234
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1275
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",273
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",87
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",588
		elif((not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",485
		elif(( self.nib.ip4Dst == 4 ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1284
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",1362
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3 and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",782
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 3 )):
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = True 
			print "case",311
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",78
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 1 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",57
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",516
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",711
		elif((not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",103
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",658
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
			print "case",292
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",396
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1332
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",486
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",225
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.Port == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",622
		elif(self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s1 and ( self.nib.ip4Src == 2 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",626
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",902
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1)):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1170
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",464
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",350
		elif((not self.nib.s3) and ( self.nib.Port == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",620
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",26
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",262
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",150
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",1333
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",896
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",893
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",510
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",25
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",923
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1050
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",364
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1339
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",125
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",77
		elif(self.nib.s3 and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s1 and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",11
		elif(( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",271
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1019
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",713
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1039
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",182
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1051
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",689
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and ( self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and (not self.nib.s2) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1022
		elif(( self.nib.ip4Dst == 4 ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1149
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",234
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1018
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
			print "case",391
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",534
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",524
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1056
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",974
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",710
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",76
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.Port == 0 ) and self.nib.s3 and (not self.nib.s1) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1043
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",737
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1164
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",181
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",224
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",308
		elif(self.nib.block and ( self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s1 and (not self.nib.s2) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",604
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",303
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",821
		elif(( self.nib.Port == 0 ) and self.nib.s3 and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1075
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",909
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",738
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",43
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			print "case",434
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",357
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",633
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",726
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",85
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",147
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1030
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1172
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",143
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",667
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",463
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",356
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",906
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",24
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",405
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1123
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",612
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1070
		elif(self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and (not self.nib.s2)):
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1142
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1136
		elif((not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",515
		elif(( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",266
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",120
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",742
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.Port == 0 ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1041
		elif(self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",628
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Dst == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1144
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",918
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.2") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
			print "case",1163
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",507
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s3 and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",305
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",220
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1017
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",376
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",195
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1178
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",402
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and self.nib.s3 and (not self.nib.s1) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",721
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",324
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3 and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",15
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1180
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",993
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",636
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",208
		elif(( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			self.nib.s1 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s3 = True 
			print "case",1021
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 3 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",96
		elif((not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",587
		elif(( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",387
		elif(( self.nib.Port == 0 ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",985
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1181
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1064
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",856
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1207
		elif(self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",112
		elif((not self.nib.s2) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",1134
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",455
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",52
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",598
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",589
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",170
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",651
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",60
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",442
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1150
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",374
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			print "case",1233
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",197
		elif(self.nib.s3 and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1067
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 0 ) and (not self.nib.s2)):
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1052
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",823
		elif(self.nib.s3 and ( self.nib.Port == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",621
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",931
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",719
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",99
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",487
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",493
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1317
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",849
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 3 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",526
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",199
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",822
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",496
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",435
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",425
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s3 and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",316
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",134
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",488
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1062
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",80
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1209
		elif(self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",110
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",696
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.block = False 
			self.nib.s2 = False 
			print "case",1364
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",771
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1296
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",596
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1246
		elif(self.nib.s3 and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1054
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",136
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s3 and self.nib.block):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1174
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1124
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",291
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",372
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",189
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1251
		elif(self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",972
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",44
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1146
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",857
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",309
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",854
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",880
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",525
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and ( self.nib.ip4Src == 1 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",10
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",187
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",743
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",498
		elif((not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",300
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",310
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",145
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3 and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",6
		elif(self.nib.block and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 )):
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = True 
			print "case",330
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",707
		elif(( self.nib.ip4Dst == 4 ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( (pkt.ip4Dst == "10.0.0.2") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1268
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",397
		elif(( self.nib.ip4Dst == 4 ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1286
		elif(self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 0 ) and (not self.nib.s2)):
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",634
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",1082
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",393
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s3 and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",820
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",34
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",42
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1125
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 2 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1044
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",1087
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s1 and self.nib.s3 and self.nib.block and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1196
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",859
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",704
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1244
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",572
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1310
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",700
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.2") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",805
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",167
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1336
		elif(( self.nib.ip4Dst == 4 ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",1289
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1096
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",35
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",907
		elif(self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s1 and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",88
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",926
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",23
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 0 ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1294
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",807
		elif(( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",440
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",19
		elif(self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1122
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",836
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",546
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",584
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1061
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1212
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",990
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1)):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",804
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",699
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",327
		elif(( self.nib.ip4Dst == 4 ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1267
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",399
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",219
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",520
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",341
		elif(( self.nib.Port == 0 ) and self.nib.s3 and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",937
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",529
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 1 ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.block = False 
			self.nib.s2 = False 
			print "case",569
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",250
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",929
		elif((not self.nib.s3) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",423
		elif(self.nib.s3 and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",2
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1179
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",971
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1204
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1046
		elif(( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and (not self.nib.s2)):
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1020
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			self.nib.s1 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s3 = True 
			print "case",745
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",49
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",506
		elif(( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",249
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",927
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",388
		elif(self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",959
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1120
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",924
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s1 and self.nib.s3 and self.nib.block and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",1326
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",21
		elif(( self.nib.ip4Dst == 4 ) and (not self.nib.s3) and ( (pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1)):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",1162
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",780
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",460
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			self.nib.s1 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s3 = True 
			print "case",755
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1210
		elif((not self.nib.s2) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1118
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",840
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1347
		elif(self.nib.s3 and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",966
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1024
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1165
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",443
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",198
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",808
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s2) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",501
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",339
		elif(( self.nib.ip4Dst == 4 ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1151
		elif(( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",522
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",976
		elif(( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",343
		elif((not self.nib.s2) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1014
		elif(self.nib.s3 and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s1 and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",0
		elif(( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",484
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1266
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1245
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1168
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",5
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1264
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",922
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",932
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",686
		elif(self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1071
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",417
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",47
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",678
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",344
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",879
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1346
		elif((not self.nib.s3) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.s3 = False 
			print "case",261
		elif((not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",428
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1297
		elif(self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
			print "case",958
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",133
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",611
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1354
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",222
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",901
		elif((not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",289
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",866
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",252
		elif(( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = True 
			print "case",260
		elif(self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1088
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1029
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s1 and self.nib.s3 and self.nib.block and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",838
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",842
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and (not self.nib.s2) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",610
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1301
		elif(( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",288
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",444
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",844
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",188
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",329
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",294
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.block = False 
			self.nib.s2 = False 
			print "case",1370
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",302
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and self.nib.s3 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",669
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",845
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",535
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s2) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",509
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
			print "case",426
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and (not self.nib.block) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1295
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",328
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",837
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			print "case",416
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1239
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",784
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",677
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",642
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",301
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s3) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1273
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s3 and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",831
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s1 and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1312
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",740
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and (not self.nib.s2)):
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",744
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = True 
			print "case",45
		elif(( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",299
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1318
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",295
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",1352
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",98
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",345
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1272
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",394
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",832
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",40
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",890
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 1 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.s3 = False 
			print "case",46
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",453
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1344
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",1242
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1290
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",476
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s2) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and ( self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",632
		elif(( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 )):
			self.nib.s1 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s3 = True 
			print "case",1011
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",38
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1319
		elif((not self.nib.block) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 2 )):
			self.nib.s1 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s3 = True 
			print "case",635
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",705
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",687
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",908
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1)):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",801
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",609
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and self.nib.s3 and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",671
		elif(( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s3) and ( self.nib.ip4Src == 1 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",332
		elif(( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",473
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",891
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
			print "case",477
		elif(( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.block and (not self.nib.s1)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",766
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",366
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",810
		elif(self.nib.s3 and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",13
		elif(( self.nib.Port == 0 ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",625
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",297
		elif(( self.nib.Port == 0 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			print "case",964
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",722
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",1240
		elif(( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",326
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",184
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",762
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",379
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1198
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",888
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",512
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",236
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s3 and self.nib.block and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1292
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",602
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",499
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1258
		elif(self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",970
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1252
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",482
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1033
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",180
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1274
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",377
		elif((not self.nib.s3) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",1004
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",944
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3 and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",114
		elif(( self.nib.ip4Dst == 2 ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",606
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",775
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",63
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1256
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1300
		elif((not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",601
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",230
		elif(( self.nib.Port == 0 ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",623
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",900
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",478
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",748
		elif(self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1003
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",115
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1249
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",777
		elif(( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s1 and self.nib.block):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",764
		elif(( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",586
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",142
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1032
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",537
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",697
		elif(( self.nib.Port == 0 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",965
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",724
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",933
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",660
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1306
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",293
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1260
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",641
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",318
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1166
		elif(self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1109
		elif((not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",539
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",4
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1254
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",118
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1059
		elif(self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1111
		elif(( self.nib.ip4Dst == 4 ) and (not self.nib.s3) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1)):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",1160
		elif(( self.nib.ip4Dst == 4 ) and (not self.nib.s3) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1265
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",240
		elif(self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1138
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",264
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1298
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",228
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",277
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",1112
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",894
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",631
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",717
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",404
		elif((not self.nib.block) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( self.nib.ip4Dst == 2 )):
			self.nib.s1 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s3 = True 
			print "case",1053
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1248
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",193
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",241
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and (not self.nib.s1)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1262
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",123
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",746
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3 and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",17
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and self.nib.s3):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1026
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",1139
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",552
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",1089
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",255
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",140
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",752
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",973
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",843
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",783
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1216
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",1006
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and (not self.nib.s1)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",788
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1304
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1257
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",753
		elif((not self.nib.s3) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",955
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",392
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 3 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",561
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",708
		elif((not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 0 or self.nib.Port == 2 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",457
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1037
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",957
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 3 )):
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = True 
			print "case",55
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1)):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1159
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",785
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",834
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",151
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",223
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1027
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",58
		elif(( self.nib.ip4Src == 1 ) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = True 
			print "case",348
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",94
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
			print "case",1007
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",226
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1038
		elif(self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",960
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and (not self.nib.block) and ( self.nib.ip4Src == 1 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",257
		elif(self.nib.s3 and ( self.nib.Port == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",619
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",984
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",149
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",495
		elif(self.nib.s3 and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",979
		elif((not self.nib.s2) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",101
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",346
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",982
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",204
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1330
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",37
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",791
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",851
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",7
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",279
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1259
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",706
		elif(self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",1105
		elif((not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",573
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",233
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",314
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 3 )):
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = True 
			print "case",41
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",174
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and (not self.nib.s2) and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",786
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",407
		elif(( self.nib.Port == 1 or self.nib.Port == 3 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",614
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",82
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",280
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",320
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1)):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",882
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and self.nib.s2 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1)):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",802
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and self.nib.s3):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",608
		elif((not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",474
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.s3 and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",741
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",1373
		elif(( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",331
		elif(self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1086
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",166
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1176
		elif((not self.nib.s3) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",321
		elif((not self.nib.s2) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1008
		elif(self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1058
		elif(self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",617
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 3 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",190
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",1375
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1048
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",761
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",934
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",715
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",378
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",322
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",852
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",206
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",65
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.block and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",638
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",92
		elif((not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",533
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1040
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") )):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = False 
			print "case",1192
		elif((not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1072
		elif(self.nib.s3 and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1107
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",716
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and self.nib.s2 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",503
		elif((not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",551
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",116
		elif(( self.nib.Port == 0 ) and self.nib.s3 and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",987
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			print "case",1223
		elif(self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and (not self.nib.s2)):
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1126
		elif((not self.nib.s3) and ( self.nib.ip4Src == 1 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = True 
			self.nib.s3 = False 
			print "case",349
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",64
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and ( self.nib.ip4Src == 3 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",93
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",462
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.block and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",656
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",62
		elif(( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",600
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1084
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and ( self.nib.Port == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",505
		elif(( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 0 ) and ( (pkt.ip4Dst == "10.0.0.2") )):
			self.nib.s1 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s3 = True 
			print "case",1127
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",171
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",514
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1)):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",793
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",452
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.s3 and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1035
		elif(self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.4") ) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",615
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",192
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.s2 = False 
			print "case",1243
		elif(self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",917
		elif((not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",355
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1)):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",815
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",702
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",640
		elif(self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",90
		elif((not self.nib.s3) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1217
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",728
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",138
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s1 = False 
			self.nib.block = True 
			self.nib.s2 = False 
			self.nib.s3 = True 
			print "case",887
		elif((not self.nib.s3) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Dst == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",319
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and ( self.nib.ip4Src == 3 ) and ( self.nib.ip4Dst == 2 ) and (not self.nib.block) and (not self.nib.s1) and (not self.nib.s2) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",1028
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",548
		elif((not self.nib.s2) and ( self.nib.Port == 3 ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",528
		elif((not self.nib.s3) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",1110
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s3 and self.nib.s2):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",238
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",858
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s2 and ( self.nib.ip4Dst == 1 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",209
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1224
		elif(( (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4") ) and self.nib.block and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and self.nib.s3):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",490
		elif(( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1328
		elif((not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1201
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s3) and ( self.nib.ip4Dst == 0 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 1 or self.nib.ip4Src == 3 )):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",769
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.Port == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",883
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1374
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 0 ) and (not self.nib.s2)):
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",754
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and ( self.nib.ip4Dst == 2 ) and self.nib.block and self.nib.s3 and self.nib.s1):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",655
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and self.nib.s3 and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 ) and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",846
		elif(( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.s3 and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",630
		elif((not self.nib.s2) and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 1 ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.s1 = True 
			self.nib.block = True 
			self.nib.s2 = False 
			print "case",567
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.s2):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",278
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and self.nib.s2 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1)):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",812
		elif((not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 1 ) and ( self.nib.ip4Src == 1 ) and self.nib.s3 and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",571
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",718
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",518
		elif((not self.nib.s2) and (not self.nib.s1) and ( self.nib.ip4Dst == 1 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.Port == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",449
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",994
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Src == 2 )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",750
		elif(( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and ( self.nib.Port == 1 or self.nib.Port == 3 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",1206
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and self.nib.s3 and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",210
		elif((not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",370
		elif(( self.nib.ip4Dst == 4 ) and (not self.nib.s3) and self.nib.s2 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",1287
		elif(( self.nib.ip4Dst == 4 ) and (not self.nib.s2) and self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1288
		elif(( self.nib.ip4Dst == 4 ) and ( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and self.nib.s2 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and (not self.nib.s1)):
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",813
		elif(self.nib.s3 and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.2") ) and ( self.nib.Port == 2 ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2 and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") )):
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",1069
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s3) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			actions += [SetPort (1)]
			self.nib.Port = 1
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			self.nib.s3 = False 
			print "case",652
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s3 and (not self.nib.s1) and ( self.nib.Port == 2 ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",663
		elif((not self.nib.s3) and ( (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and (not self.nib.s2) and (not self.nib.block) and (not self.nib.s1) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			self.nib.s2 = False 
			self.nib.s3 = False 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",995
		elif(( self.nib.Port == 0 ) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.2") ) and self.nib.block and ( self.nib.ip4Dst == 2 ) and ( (pkt.ip4Src == "10.0.0.2") or (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3") ) and self.nib.s1 and ( self.nib.ip4Src == 1 ) and (not self.nib.s2)):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",1073
		elif((not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",436
		elif((not self.nib.s2) and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and self.nib.s3 and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Dst == 2 ) and ( self.nib.ip4Src == 2 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s1 = False 
			self.nib.s2 = False 
			print "case",1009
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and ( (pkt.ip4Src == "10.0.0.2") ) and self.nib.block and self.nib.s3 and self.nib.s1 and ( self.nib.ip4Dst == 1 )):
			actions += [SetPort (2)]
			self.nib.Port = 0
			self.nib.block = True 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.s1 = True 
			print "case",137
		elif((not self.nib.s2) and ( (pkt.ip4Dst == "10.0.0.4") ) and (not self.nib.s1) and self.nib.block and self.nib.s3 and ( self.nib.ip4Src == 1 ) and ( self.nib.Port == 0 or self.nib.Port == 2 ) and ( self.nib.ip4Dst == 1 )):
			self.nib.s1 = False 
			self.nib.s3 = True 
			self.nib.s2 = False 
			self.nib.block = False 
			print "case",109
		elif(( (pkt.ip4Dst == "10.0.0.1") ) and (not self.nib.s2) and ( self.nib.ip4Src == 3 ) and (not self.nib.block) and (not self.nib.s1) and ( self.nib.ip4Dst == 3 ) and self.nib.s3 and ( (pkt.ip4Src == "10.0.0.1") or (pkt.ip4Src == "10.0.0.3") )):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s1 = False 
			print "case",53
		elif(( self.nib.Port == 0 ) and ( self.nib.ip4Dst == 0 ) and (not self.nib.s2) and ( self.nib.ip4Src == 0 or self.nib.ip4Src == 2 ) and ( (pkt.ip4Dst == "10.0.0.4") ) and self.nib.block and self.nib.s3 and self.nib.s1):
			self.nib.s2 = False 
			self.nib.s3 = True 
			self.nib.block = True 
			self.nib.s1 = True 
			print "case",778
		elif(self.nib.s3 and (not self.nib.block) and ( (pkt.ip4Src == "10.0.0.2") ) and (not self.nib.s1) and ( self.nib.Port == 2 ) and ( (pkt.ip4Dst == "10.0.0.3") ) and ( self.nib.ip4Src == 1 ) and ( self.nib.ip4Dst == 2 ) and self.nib.s2):
			actions += [SetPort (3)]
			self.nib.Port = 2
			self.nib.s3 = True 
			self.nib.block = False 
			self.nib.s2 = True 
			self.nib.s1 = False 
			print "case",954
		if ((pkt.ip4Dst == "10.0.0.2")):
			self.nib.ip4Dst = 0
		elif ((pkt.ip4Dst == "10.0.0.1")):
			self.nib.ip4Dst = 1
		elif ((pkt.ip4Dst == "10.0.0.3")):
			self.nib.ip4Dst = 2
		elif ((pkt.ip4Dst == "10.0.0.4")):
			self.nib.ip4Dst = 3
		elif ((pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4")):
			self.nib.ip4Dst = 4
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
