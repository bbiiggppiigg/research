[INPUT]
packet_in

[OUTPUT]
port:0...1
zcount:0...1
ocount:0...1

[ENV_INIT]


[SYS_INIT]
zcount=0
ocount=0

[SYS_TRANS]
packet_in & port'=0->(zcount'=zcount+1)
packet_in & port'=1->(ocount'=ocount+1)
(zcount=ocount || zcount=(ocount+1) || ocount=zcount || ocount=(zcount+1))

[ENV_LIVENESS]
packet_in

[SYS_LIVENESS]
port=0
port=1