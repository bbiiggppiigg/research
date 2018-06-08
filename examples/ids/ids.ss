[INPUT]
src_ip_in:0...3
dst_ip_in:0...3
packet_in
infect

[OUTPUT]
src_ip_out:0...3
dst_ip_out:0...3
packet_out
infected

[ENV_INIT]
!infect


[SYS_INIT]
!infected

[SYS_TRANS]
src_ip_in = src_ip_out
dst_ip_in = dst_ip_out
packet_in && infected ->  !packet_out
packet_in && !infected ->  packet_out


[ENV_LIVENESS]
packet_in

[SYS_LIVENESS]
