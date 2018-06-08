[INPUT]
src_ip_in:0...3
dst_ip_in:0...3
packet_in
auth

[OUTPUT]
src_ip_out:0...3
dst_ip_out:0...3
packet_out
authedip0

[ENV_INIT]
!auth

[SYS_INIT]
!authedip0

[SYS_TRANS]
src_ip_in = src_ip_out
dst_ip_in = dst_ip_out
(auth && src_ip_in=0) -> authedip0'
authedip0 -> authedip0'
(packet_in && authedip0 && src_ip_in=0) ->  packet_out
!authedip0 -> !packet_out


[ENV_LIVENESS]
packet_in

[SYS_LIVENESS]

