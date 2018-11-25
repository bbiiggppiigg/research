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
		nib=self.nib
		if (pkt.ip4Dst == "10.0.0.2"):
			ip4Dst = 0
		elif (pkt.ip4Dst == "10.0.0.1"):
			ip4Dst = 1
		elif (pkt.ip4Dst == "10.0.0.3"):
			ip4Dst = 2
		elif (pkt.ip4Dst == "10.0.0.4"):
			ip4Dst = 3
		elif (pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4"):
			ip4Dst = 4
		if (pkt.ip4Src == "10.0.0.1"):
			ip4Src = 0
		elif (pkt.ip4Src == "10.0.0.2"):
			ip4Src = 1
		elif (pkt.ip4Src == "10.0.0.3"):
			ip4Src = 2
		elif (pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3"):
			ip4Src = 3

		if((( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Src == 1 ) and ( ip4Dst == 2 ) and nib.s3)
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s2 and nib.s3)
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))
			or (( ip4Src == 3 ) and ( nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and nib.s3)
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.ip4Src == 1 ) and nib.s3)
			or (( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s2 and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Dst == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 0 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and nib.s3)
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and ( nib.ip4Dst == 4 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 0 ) and nib.s3)
			or (nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 3 ) and ( nib.Port == 0 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 3 ) and (not nib.block) and ( nib.ip4Src == 1 ) and ( ip4Dst == 2 ) and nib.s3)
			or (( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Dst == 4 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and nib.s2 and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and nib.s2 and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.Port == 0 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and nib.s3 and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Dst == 0 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1))
			or (( ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and nib.s2 and nib.s3)
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and (not nib.block) and (not nib.s1))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 4 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and nib.s2 and nib.s3)
			or (( ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and nib.s2 and nib.s3)
			or (( ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or ((not nib.block) and ( nib.ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and (not nib.s1) and nib.s2 and nib.s3)
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and (not nib.block) and (not nib.s1))
			or ((not nib.block) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Dst == 0 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1))
			or (( ip4Dst == 3 ) and ( nib.ip4Dst == 4 ) and (not nib.block) and (not nib.s1) and nib.s2 and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Src == 2 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and (not nib.s1) and nib.s2 and nib.s3)
			or (( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Dst == 4 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and nib.s2 and nib.s3)
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 4 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and nib.s2 and nib.s3)
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Dst == 3 ) and (not nib.block) and ( nib.ip4Src == 1 ) and nib.s3)
			or ((not nib.block) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and (not nib.s1) and nib.s2 and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Dst == 0 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1))
			or (( ip4Dst == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1))
			or (( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 0 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1))
			or (nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Dst == 3 ) and ( ip4Src == 1 or ip4Src == 3 ) and (not nib.s1) and (not nib.block) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3)
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.ip4Src == 1 ) and nib.s3)
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and nib.s2 and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( ip4Dst == 4 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 4 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and nib.s2 and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ))
			or ((not nib.block) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1))
			or (( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and nib.s2 and nib.s3)
			or (( nib.ip4Src == 2 ) and ( ip4Dst == 3 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and (not nib.s1) and nib.s2 and nib.s3)
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and (not nib.block) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.Port == 0 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Src == 2 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and nib.s2 and nib.s3)
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))):
			nib.s3 = True 
			nib.block = False 
			nib.s2 = True 
			nib.s1 = False 
		elif((( nib.ip4Dst == 3 ) and ( ip4Src == 1 or ip4Src == 3 ) and (not nib.s2) and nib.block and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3)
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.block and ( nib.ip4Src == 1 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 1 ) and ( ip4Dst == 2 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 3 ) and nib.block and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 3 ) and ( ip4Src == 3 ) and nib.block and ( nib.ip4Src == 1 ) and ( ip4Dst == 2 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 3 ) and nib.block and ( nib.ip4Src == 1 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 1 ) and (not nib.s2) and nib.s3)):
			nib.block = False 
			nib.s1 = False 
			nib.s3 = True 
			nib.s2 = True 
		elif((( ip4Src == 1 or ip4Src == 3 ) and nib.block and ( nib.ip4Dst == 2 ) and ( ip4Dst == 2 ) and ( nib.ip4Src == 0 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Src == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Dst == 2 ) and ( ip4Dst == 1 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Src == 0 ) and nib.block and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and (not nib.s2) and nib.s3)
			or (( ip4Src == 1 or ip4Src == 3 ) and (not nib.s2) and nib.block and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 0 ) and ( ip4Dst == 0 ) and nib.s3)
			or (( ip4Src == 1 or ip4Src == 3 ) and nib.block and ( nib.ip4Dst == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 0 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Src == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Dst == 2 ) and ( ip4Dst == 2 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Src == 0 ) and ( ip4Dst == 3 ) and nib.block and ( nib.ip4Dst == 2 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Src == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.s2) and nib.block and ( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and nib.s3)):
			nib.s3 = True 
			nib.s2 = False 
			nib.block = True 
			nib.s1 = True 
		elif((( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.ip4Src == 1 ) and nib.s3)):
			actions += [SetPort (1)]
			nib.Port = 1
			nib.s3 = True 
			nib.block = False 
			nib.s1 = False 
			nib.s2 = True 
		elif((( ip4Src == 0 or ip4Src == 2 ) and nib.s2 and ( nib.ip4Dst == 4 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 0 ) and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))
			or (nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))
			or (nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.s3 = True 
			nib.block = False 
			nib.s2 = True 
			nib.s1 = False 
		elif((( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Src == 1 ) and (not nib.s3) and ( ip4Dst == 0 ))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.block = False 
			nib.s1 = False 
			nib.s2 = True 
			nib.s3 = False 
		elif((( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and (not nib.s2))
			or (nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s2))
			or (( nib.Port == 0 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and ( nib.Port == 2 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (( ip4Src == 0 or ip4Src == 2 ) and (not nib.s2) and nib.block and ( nib.ip4Dst == 4 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( nib.Port == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.s3 = True 
			nib.s1 = True 
			nib.block = True 
			nib.s2 = False 
		elif((nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (nib.block and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or ((not nib.s1) and nib.block and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 4 ) and (not nib.s1) and ( ip4Src == 1 ) and nib.block and ( ip4Dst == 1 ) and (not nib.s2) and nib.s3)
			or ((not nib.s1) and ( nib.Port == 0 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.block and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( nib.Port == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (nib.block and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and nib.block and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (nib.block and ( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.block and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.block = True 
			nib.s1 = False 
			nib.s2 = False 
			nib.s3 = True 
		elif((( nib.ip4Dst == 2 ) and nib.block and nib.s1 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.block and nib.s1 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( nib.Port == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (nib.block and ( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.block and nib.s1 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s2))
			or (nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (nib.block and nib.s1 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (( nib.ip4Dst == 4 ) and ( ip4Src == 1 ) and nib.block and ( ip4Dst == 1 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (( nib.Port == 0 ) and nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.block = True 
			nib.s3 = True 
			nib.s2 = False 
			nib.s1 = True 
		elif((( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.s3 = True 
			nib.block = True 
			nib.s1 = False 
			nib.s2 = False 
		elif((( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3 and ( nib.Port == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and (not nib.s1) and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.s3 = True 
			nib.s1 = False 
			nib.block = False 
			nib.s2 = False 
		elif((nib.block and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.block = True 
			nib.s2 = False 
			nib.s1 = True 
			nib.s3 = True 
		elif((( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1))
			or (nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and ( ip4Src == 1 ) and nib.block and ( nib.ip4Src == 1 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or ((not nib.block) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1))
			or (( nib.ip4Dst == 4 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and nib.s2 and nib.s3)):
			actions += [SetPort (1)]
			nib.Port = 1
			nib.s3 = True 
			nib.block = False 
			nib.s2 = True 
			nib.s1 = False 
		elif((nib.block and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( nib.Port == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3 and nib.block and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 0 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 3 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or ((not nib.s1) and nib.block and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and (not nib.s1) and (not nib.s2))
			or (( ip4Dst == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and nib.block and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.block and nib.s3 and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.s3 and ( nib.Port == 3 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 3 ) and nib.s3 and ( nib.ip4Dst == 3 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Dst == 0 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and (not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.s3 and nib.block and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.s3 and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( nib.Port == 3 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 3 ) and nib.block and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (nib.block and ( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.block and nib.s3 and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Dst == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.block and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and (not nib.s1) and (not nib.s2))
			or (nib.block and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.s3 and ( nib.ip4Dst == 3 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Dst == 3 ) and ( nib.ip4Dst == 4 ) and nib.block and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s3 and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and nib.block and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (nib.block and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.s3 and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and (not nib.s2) and ( nib.ip4Dst == 4 ) and nib.block and (not nib.s1) and ( ip4Dst == 0 ) and nib.s3)
			or (nib.block and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Dst == 4 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.s3 and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 0 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.block and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or ((not nib.s1) and ( ip4Dst == 3 ) and nib.block and ( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.Port == 0 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or ((not nib.s1) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and nib.block and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( nib.Port == 3 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (nib.block and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 0 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or ((not nib.s1) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Dst == 4 ) and ( ip4Dst == 1 ) and nib.block and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and nib.block and (not nib.s1) and (not nib.s2))
			or ((not nib.s1) and nib.block and ( ip4Dst == 4 ) and ( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 1 ) and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and nib.block and (not nib.s1) and (not nib.s2))
			or (nib.block and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or ((not nib.s1) and nib.block and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 3 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and (not nib.s2) and nib.block and ( ip4Dst == 4 ) and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( nib.ip4Src == 2 ) and ( ip4Dst == 3 ) and nib.block and ( nib.ip4Dst == 2 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and nib.s3 and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.block and nib.s3 and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 4 ) and nib.block and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 0 ) and nib.block and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and (not nib.s2) and nib.block and ( ip4Dst == 4 ) and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (nib.block and ( ip4Src == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3 and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and (not nib.s2) and ( ip4Dst == 3 ) and nib.block and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( nib.Port == 3 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s3 and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 3 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or ((not nib.s1) and ( ip4Src == 3 ) and nib.block and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and ( ip4Dst == 1 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and (not nib.s2) and ( ip4Dst == 3 ) and nib.block and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 4 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (nib.block and ( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.block and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or ((not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 0 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( nib.Port == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and nib.s3 and nib.block and (not nib.s1) and (not nib.s2))
			or (( ip4Dst == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and nib.block and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or ((not nib.s1) and ( ip4Dst == 3 ) and nib.block and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 3 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( nib.Port == 3 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and (not nib.s1) and (not nib.s2))
			or ((not nib.s1) and ( ip4Src == 3 ) and ( nib.ip4Dst == 4 ) and ( ip4Dst == 1 ) and nib.block and (not nib.s2) and nib.s3)
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))):
			nib.s1 = False 
			nib.s3 = True 
			nib.s2 = False 
			nib.block = False 
		elif((nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.Port == 2 ) and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( nib.Port == 3 ) and ( ip4Src == 1 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.block = True 
			nib.s1 = True 
			nib.s3 = True 
			nib.s2 = False 
		elif((( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and ( ip4Dst == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 0 or ip4Src == 2 ) and (not nib.s2) and (not nib.block) and (not nib.s1) and (not nib.s3) and ( ip4Dst == 0 ) and ( nib.ip4Dst == 4 ))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Dst == 0 ) and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.block = False 
			nib.s1 = False 
			nib.s2 = False 
			nib.s3 = False 
		elif((( nib.ip4Dst == 0 ) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2) and ( nib.ip4Dst == 4 ))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and (not nib.s2) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ))
			or ((not nib.block) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and (not nib.s2) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or ((not nib.block) and ( nib.ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and (not nib.s2) and (not nib.block) and (not nib.s1) and (not nib.s3) and ( ip4Dst == 0 ) and ( nib.ip4Dst == 4 ))
			or (( nib.ip4Src == 2 ) and ( ip4Dst == 3 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or ((not nib.block) and ( nib.ip4Dst == 2 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2) and ( nib.ip4Dst == 4 ))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 3 ) and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( ip4Dst == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( nib.ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and (not nib.s2) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or ((not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and (not nib.s2) and ( nib.ip4Dst == 4 ))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or ((not nib.block) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2) and ( nib.ip4Dst == 4 ))
			or (( ip4Src == 3 ) and ( nib.ip4Src == 3 ) and ( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2) and ( nib.ip4Dst == 4 ))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and (not nib.s2) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2) and ( nib.ip4Dst == 4 ))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( nib.ip4Dst == 3 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))):
			nib.s2 = False 
			nib.s3 = False 
			nib.block = False 
			nib.s1 = False 
		elif((( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and nib.s2 and ( nib.ip4Dst == 4 ))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Src == 3 ) and nib.s2 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and nib.s2 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3))
			or (nib.s2 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or ((not nib.block) and ( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s3))):
			actions += [SetPort (1)]
			nib.Port = 1
			nib.block = False 
			nib.s2 = True 
			nib.s1 = False 
			nib.s3 = False 
		elif((nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 4 ) and ( ip4Src == 1 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or ((not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 4 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( nib.Port == 3 ) and ( ip4Src == 1 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and nib.block and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.block = True 
			nib.s3 = True 
			nib.s1 = False 
			nib.s2 = False 
		elif((( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (nib.s2 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (nib.s2 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and nib.s2 and ( nib.ip4Dst == 4 ))
			or (( nib.ip4Dst == 1 ) and nib.s2 and ( ip4Src == 1 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Src == 1 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Src == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))):
			actions += [SetPort (3)]
			nib.Port = 2
			nib.block = False 
			nib.s2 = True 
			nib.s1 = False 
			nib.s3 = False 
		elif((( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or ((not nib.block) and ( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 3 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and (not nib.block) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or ((not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 4 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.s1 = False 
			nib.block = True 
			nib.s2 = False 
			nib.s3 = True 
		elif((( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3)
			or (( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.s2) and nib.block and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3)):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.s3 = True 
			nib.block = False 
			nib.s1 = False 
			nib.s2 = True 
		elif((( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and (not nib.block) and (not nib.s1) and (not nib.s3) and ( ip4Dst == 0 ) and ( nib.ip4Dst == 4 ))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and nib.s2)
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s2 and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3))
			or (( ip4Src == 3 ) and nib.s2 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 3 ) and nib.s2 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or ((not nib.block) and ( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and nib.s2)
			or (( nib.ip4Dst == 0 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and (not nib.s3) and nib.s2)
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or ((not nib.block) and ( nib.ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and nib.s2)
			or (( nib.ip4Src == 2 ) and ( ip4Dst == 3 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and (not nib.s1) and (not nib.s3) and nib.s2)
			or (( ip4Src == 3 ) and nib.s2 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (nib.s2 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.Port == 0 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 3 ) and ( ip4Src == 1 or ip4Src == 3 ) and (not nib.s1) and (not nib.block) and ( nib.ip4Src == 1 ) and (not nib.s3) and ( ip4Dst == 0 ))
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.ip4Src == 1 ) and (not nib.s3))
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 3 ) and (not nib.block) and ( nib.ip4Src == 1 ) and ( ip4Dst == 2 ) and (not nib.s3))
			or ((not nib.block) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and (not nib.s1) and (not nib.s3) and nib.s2)
			or (( nib.ip4Src == 2 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and ( ip4Dst == 0 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and nib.s2 and ( nib.ip4Dst == 4 ))
			or (( ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and nib.s2 and ( nib.ip4Dst == 4 ))
			or (( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and nib.s2 and ( nib.ip4Dst == 4 ))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Dst == 0 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.Port == 0 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.ip4Src == 1 ) and (not nib.s3))
			or (( ip4Dst == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3))
			or (( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 0 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( ip4Src == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and nib.s2 and ( nib.ip4Dst == 4 ))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and nib.s2)
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( ip4Dst == 4 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Dst == 3 ) and (not nib.block) and ( nib.ip4Src == 1 ) and (not nib.s3))
			or (( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and nib.s2)
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and nib.s2)
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( ip4Src == 3 ) and ( nib.ip4Src == 3 ) and nib.s2 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 3 ) and ( nib.Port == 0 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and nib.s2 and ( nib.ip4Dst == 4 ))
			or (( nib.ip4Src == 2 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and nib.s2)
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s2 and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and (not nib.block) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and (not nib.s3))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s2 and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and nib.s2)
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Dst == 0 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Src == 1 ) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Src == 3 ) and nib.s2 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and (not nib.s3) and nib.s2)
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or ((not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s3) and nib.s2 and ( nib.ip4Dst == 4 ))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( ip4Src == 1 or ip4Src == 3 ) and nib.s2 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (nib.s2 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s2 and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s2 and (not nib.s3))
			or ((not nib.block) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s3))
			or (nib.s2 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( ip4Src == 3 ) and nib.s2 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.s2 and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 1 ) and nib.s2 and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.s2 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3))):
			nib.s3 = False 
			nib.block = False 
			nib.s2 = True 
			nib.s1 = False 
		elif((( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( ip4Dst == 3 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and nib.s3 and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.ip4Src == 2 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and nib.s3 and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s3 and (not nib.block) and (not nib.s1) and (not nib.s2))
			or ((not nib.block) and ( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.s3 and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 3 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( ip4Src == 3 ) and ( nib.ip4Src == 3 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.s3 and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and (not nib.s2) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( ip4Src == 1 or ip4Src == 3 ) and (not nib.s2) and ( nib.ip4Dst == 4 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 0 ) and nib.s3)
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 1 ) and nib.s3 and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s3 and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s3 and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 3 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.s3 and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and (not nib.s2) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Dst == 4 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 3 ) and (not nib.s2) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.s3 and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or ((not nib.block) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or ((not nib.block) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and (not nib.s2) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 3 ) and (not nib.block) and (not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and (not nib.s2) and nib.s3)
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 4 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( ip4Src == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 4 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s3 and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or ((not nib.block) and ( nib.ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 0 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and (not nib.s2) and nib.s3)
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3 and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Dst == 3 ) and ( nib.ip4Dst == 4 ) and (not nib.block) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s3 and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Dst == 4 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 4 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( ip4Dst == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and ( nib.ip4Src == 3 ) and (not nib.block) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( ip4Dst == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 3 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and (not nib.s1) and (not nib.s2) and nib.s3)
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s2))):
			nib.s2 = False 
			nib.s3 = True 
			nib.block = False 
			nib.s1 = False 
		elif((( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 1 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2) and ( nib.ip4Dst == 4 ))
			or (( nib.ip4Dst == 2 ) and ( ip4Src == 1 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and (not nib.s3) and (not nib.s2))):
			actions += [SetPort (3)]
			nib.Port = 2
			nib.block = False 
			nib.s1 = False 
			nib.s2 = False 
			nib.s3 = False 
		elif((( nib.ip4Src == 3 ) and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2) and ( nib.ip4Dst == 4 ))
			or ((not nib.block) and ( nib.ip4Dst == 2 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and (not nib.s1) and (not nib.s3) and (not nib.s2))):
			actions += [SetPort (1)]
			nib.Port = 1
			nib.block = False 
			nib.s1 = False 
			nib.s2 = False 
			nib.s3 = False 
		elif((( nib.ip4Dst == 2 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and (not nib.s2) and nib.block and ( nib.ip4Dst == 4 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3)
			or (( nib.ip4Dst == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 1 or ip4Src == 3 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and nib.block and (not nib.s2))
			or (( ip4Dst == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and ( nib.Port == 2 ) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.block and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s1 and nib.s3 and nib.block and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Dst == 3 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 2 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.Port == 0 ) and nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 1 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and (not nib.s2))
			or (( ip4Src == 3 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Dst == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 3 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( nib.Port == 3 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 1 or ip4Src == 3 ) and ( nib.Port == 3 ) and nib.block and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.block and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and ( nib.Port == 2 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and (not nib.s2) and nib.block and ( ip4Dst == 4 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 4 ) and nib.block and ( ip4Dst == 1 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 2 ) and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and (not nib.s2) and nib.block and ( ip4Dst == 4 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( ip4Dst == 4 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 2 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s1 and nib.s3 and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and nib.block and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and nib.block and ( nib.ip4Src == 3 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 3 ) and nib.s1 and nib.s3 and ( nib.ip4Dst == 3 ) and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( ip4Dst == 3 ) and nib.block and ( nib.ip4Dst == 2 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and (not nib.s2))
			or (nib.block and ( ip4Dst == 4 ) and ( nib.ip4Dst == 4 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (nib.block and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and nib.block and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (( ip4Src == 3 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.block and nib.s1 and nib.s3 and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and (not nib.s2) and ( ip4Dst == 3 ) and nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( nib.ip4Dst == 3 ) and (not nib.s2) and ( ip4Dst == 3 ) and nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3)
			or (( ip4Dst == 3 ) and nib.block and ( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 4 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( ip4Src == 3 ) and nib.block and nib.s1 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (nib.block and ( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Dst == 1 ) and (not nib.s2))
			or (( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and (not nib.s2))
			or (( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Dst == 4 ) and ( ip4Dst == 2 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (( ip4Dst == 3 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( nib.Port == 3 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (( ip4Src == 3 ) and nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and (not nib.s2))
			or (nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( ip4Src == 3 ) and nib.block and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s1 and nib.s3 and ( ip4Dst == 1 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.Port == 0 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Dst == 3 ) and nib.block and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 3 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( ip4Src == 3 ) and nib.block and ( nib.ip4Dst == 4 ) and ( ip4Dst == 2 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.Port == 0 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 0 ) and nib.block and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.s1 and nib.s3 and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.block and ( ip4Dst == 4 ) and ( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( nib.Port == 0 ) and nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( ip4Dst == 4 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (nib.block and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and (not nib.s2))
			or (( ip4Dst == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and (not nib.s2))
			or (nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and nib.block and ( nib.Port == 2 ) and (not nib.s2))
			or (nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( nib.Port == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.s2))
			or (( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Dst == 4 ) and nib.block and ( ip4Dst == 1 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( nib.Port == 3 ) and nib.block and (not nib.s2))
			or (nib.s1 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 0 ) and nib.block and (not nib.s2))
			or (( ip4Dst == 3 ) and ( nib.Port == 0 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and nib.block and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 1 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( nib.Port == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (nib.block and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( ip4Src == 3 ) and nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and ( ip4Dst == 3 ) and nib.block and ( nib.ip4Src == 3 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( nib.Port == 0 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.Port == 0 ) and ( ip4Dst == 4 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.block and (not nib.s2))
			or (( nib.ip4Src == 2 ) and nib.block and ( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( ip4Src == 3 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( nib.Port == 2 ) and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and nib.block and (not nib.s2))
			or (( ip4Src == 3 ) and nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and nib.block and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s2))
			or (nib.block and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (nib.block and nib.s1 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.block and nib.s1 and nib.s3 and ( ip4Dst == 1 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 0 ) and nib.block and ( nib.Port == 2 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 3 ) and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 4 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( ip4Src == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.block and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Dst == 1 ) and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( nib.ip4Dst == 3 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.Port == 2 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( ip4Src == 3 ) and ( nib.ip4Dst == 2 ) and nib.s1 and nib.s3 and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and nib.block and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 3 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( nib.Port == 3 ) and nib.block and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Src == 3 ) and nib.block and nib.s1 and nib.s3 and ( ip4Dst == 1 ) and ( nib.ip4Src == 3 ) and (not nib.s2))
			or (( ip4Src == 1 or ip4Src == 3 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Dst == 0 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 1 or ip4Src == 3 ) and nib.block and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( ip4Dst == 4 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and nib.block and ( nib.Port == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 2 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.block and ( ip4Src == 3 ) and ( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Dst == 1 ) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.block and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (nib.block and ( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s2))
			or (( ip4Dst == 3 ) and nib.block and ( nib.ip4Dst == 4 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( nib.ip4Dst == 1 ) and nib.block and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and (not nib.s2))):
			nib.s2 = False 
			nib.s3 = True 
			nib.block = True 
			nib.s1 = True 
		elif((( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (nib.s2 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s3))
			or (nib.s2 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 1 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))
			or (( ip4Src == 0 or ip4Src == 2 ) and nib.s2 and (not nib.block) and (not nib.s1) and (not nib.s3) and ( ip4Dst == 0 ) and ( nib.ip4Dst == 4 ))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s3))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s3))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.block = False 
			nib.s2 = True 
			nib.s1 = False 
			nib.s3 = False 
		elif((( nib.ip4Dst == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Dst == 4 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ) and nib.s2 and nib.s3)
			or (( nib.ip4Dst == 2 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and ( ip4Dst == 2 ))
			or (nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.ip4Dst == 1 ) and nib.s2 and nib.s3 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s2 and nib.s3 and ( ip4Src == 1 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))
			or (nib.s2 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 2 ))):
			actions += [SetPort (3)]
			nib.Port = 2
			nib.s3 = True 
			nib.block = False 
			nib.s2 = True 
			nib.s1 = False 
		elif(((not nib.block) and ( nib.ip4Src == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 1 ) and ( nib.ip4Dst == 2 ) and (not nib.s1))
			or (( nib.ip4Src == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and (not nib.s1) and ( ip4Dst == 0 ))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 0 ) and (not nib.s1) and ( ip4Dst == 4 ) and (not nib.block))
			or (( nib.ip4Src == 0 ) and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and (not nib.s1) and ( ip4Dst == 2 ))
			or (( ip4Src == 1 or ip4Src == 3 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and (not nib.s1) and ( nib.ip4Src == 0 ) and ( ip4Dst == 0 ))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 0 ) and (not nib.s1) and ( ip4Dst == 3 ) and (not nib.block))
			or (( ip4Src == 1 or ip4Src == 3 ) and (not nib.block) and ( nib.ip4Dst == 2 ) and (not nib.s1) and ( ip4Dst == 2 ) and ( nib.ip4Src == 0 ))
			or ((not nib.block) and ( ip4Src == 1 or ip4Src == 3 ) and ( ip4Dst == 1 ) and ( nib.ip4Dst == 2 ) and (not nib.s1) and ( nib.ip4Src == 0 ))):
			nib.s1 = True 
			nib.s2 = False 
			nib.block = True 
			nib.s3 = True 
		elif(((not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Dst == 0 ) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Dst == 0 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( nib.ip4Src == 3 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( ip4Dst == 0 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.Port == 2 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 0 ) and ( nib.Port == 0 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and ( nib.Port == 0 or nib.Port == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 0 or ip4Src == 2 ) and (not nib.s2) and ( nib.ip4Dst == 4 ) and nib.block and (not nib.s1) and ( ip4Dst == 0 ) and nib.s3)
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.Port == 1 or nib.Port == 3 ) and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and ( ip4Dst == 0 ) and (not nib.block) and (not nib.s1) and (not nib.s2))
			or (( nib.Port == 0 ) and ( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and (not nib.s1) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and (not nib.block) and ( nib.ip4Src == 3 ) and (not nib.s1) and (not nib.s2))
			or (( ip4Src == 0 or ip4Src == 2 ) and (not nib.s2) and ( nib.ip4Dst == 4 ) and (not nib.block) and (not nib.s1) and ( ip4Dst == 0 ) and nib.s3)
			or ((not nib.s1) and ( nib.ip4Src == 1 or nib.ip4Src == 3 ) and ( ip4Dst == 0 ) and nib.s3 and ( ip4Src == 0 or ip4Src == 2 ) and nib.block and ( nib.ip4Dst == 0 ) and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.s3 = True 
			nib.block = False 
			nib.s1 = False 
			nib.s2 = False 
		elif((( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 1 ) and (not nib.block) and ( nib.ip4Src == 1 ) and ( ip4Dst == 2 ) and nib.s3)
			or (( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and nib.block and ( nib.ip4Src == 1 ) and ( ip4Dst == 2 ) and (not nib.s2) and nib.s3)):
			actions += [SetPort (3)]
			nib.Port = 2
			nib.s3 = True 
			nib.block = False 
			nib.s1 = False 
			nib.s2 = True 
		elif((( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 1 ) and (not nib.block) and ( nib.ip4Src == 1 ) and ( ip4Dst == 2 ) and (not nib.s3))):
			actions += [SetPort (3)]
			nib.Port = 2
			nib.block = False 
			nib.s1 = False 
			nib.s2 = True 
			nib.s3 = False 
		elif((( nib.ip4Dst == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.s1 and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.ip4Src == 3 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.Port == 1 ) and ( nib.ip4Dst == 1 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( ip4Src == 1 ) and nib.block and ( nib.ip4Dst == 4 ) and ( ip4Dst == 2 ) and nib.s1 and (not nib.s2) and nib.s3)
			or (( nib.ip4Src == 2 ) and ( nib.ip4Dst == 2 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Src == 1 or nib.ip4Src == 3 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 1 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( nib.ip4Dst == 3 ) and ( ip4Src == 1 ) and nib.block and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.Port == 0 ) and nib.s1 and ( nib.ip4Src == 0 or nib.ip4Src == 2 ) and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.ip4Dst == 0 ) and ( ip4Dst == 2 ) and (not nib.s2))
			or (( nib.ip4Dst == 2 ) and ( nib.ip4Src == 1 ) and nib.s1 and nib.s3 and ( ip4Src == 1 ) and nib.block and ( nib.Port == 2 ) and ( ip4Dst == 2 ) and (not nib.s2))):
			actions += [SetPort (2)]
			nib.Port = 0
			nib.block = True 
			nib.s3 = True 
			nib.s1 = True 
			nib.s2 = False 
		elif((( nib.ip4Dst == 3 ) and (not nib.s1) and ( ip4Src == 1 ) and ( ip4Dst == 1 ) and (not nib.block) and ( nib.ip4Src == 1 ) and (not nib.s3))):
			actions += [SetPort (1)]
			nib.Port = 1
			nib.block = False 
			nib.s1 = False 
			nib.s2 = True 
			nib.s3 = False 
		if ((pkt.ip4Dst == "10.0.0.2")):
			nib.ip4Dst = 0
		elif ((pkt.ip4Dst == "10.0.0.1")):
			nib.ip4Dst = 1
		elif ((pkt.ip4Dst == "10.0.0.3")):
			nib.ip4Dst = 2
		elif ((pkt.ip4Dst == "10.0.0.4")):
			nib.ip4Dst = 3
		elif ((pkt.ip4Dst != "10.0.0.2" and pkt.ip4Dst != "10.0.0.1" and pkt.ip4Dst != "10.0.0.3" and pkt.ip4Dst != "10.0.0.4")):
			nib.ip4Dst = 4
		if ((pkt.ip4Src == "10.0.0.1")):
			nib.ip4Src = 0
		elif ((pkt.ip4Src == "10.0.0.2")):
			nib.ip4Src = 1
		elif ((pkt.ip4Src == "10.0.0.3")):
			nib.ip4Src = 2
		elif ((pkt.ip4Src != "10.0.0.1" and pkt.ip4Src != "10.0.0.2" and pkt.ip4Src != "10.0.0.3")):
			nib.ip4Src = 3
		print pkt
		print actions
		self.pkt_out( dpid, payload , actions) 
app = MyApp()
app.start_event_loop()
