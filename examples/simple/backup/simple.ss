[INPUT]
packet_in

[OUTPUT]
port:0...3
zcount:0...3
ocount:0...3

[ENV_INIT]


[SYS_INIT]
zcount=0
ocount=0

[SYS_TRANS]
port=0->(zcount'=zcount+1)
port=1->(ocount'=ocount+1)
(zcount=ocount || zcount=(ocount+1) || ocount=zcount || ocount=(zcount+1))

[ENV_LIVENESS]
packet_in

[SYS_LIVENESS]
port=0
port=1
port=2
port=3
