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
src_ip_in = src_ip_out'
infect -> infected'
packet_in && infected && src_ip_in=1 -> dst_ip_out'=3 && packet_out'
packet_in && infected && src_ip_in=2 -> dst_ip_out'=3 && packet_out' 
packet_in && infected && !(src_ip_in=1 || src_ip_in=2) -> !(packet_out' )


[ENV_LIVENESS]

packet_in
infect
!infect

[SYS_LIVENESS]
packet_out
