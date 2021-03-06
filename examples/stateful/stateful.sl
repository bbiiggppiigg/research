[INPUT]
src_ip_in@0.0.3
src_ip_in@1
dst_ip_in@0.0.3
dst_ip_in@1
packet_in
infect


[OUTPUT]
src_ip_out@0.0.3
src_ip_out@1
dst_ip_out@0.0.3
dst_ip_out@1
packet_out
infected


[ENV_INIT]
! infect



[SYS_TRANS]
$ 1 & ! ^ src_ip_in@1 src_ip_out@1 & ! ^ src_ip_in@0.0.3 src_ip_out@0.0.3 1
$ 1 & ! ^ dst_ip_in@1 dst_ip_out@1 & ! ^ dst_ip_in@0.0.3 dst_ip_out@0.0.3 1
| ! & packet_in infected packet_out
| ! & packet_in ! infected ! packet_out



[SYS_INIT]
! infected


[ENV_LIVENESS]
packet_in


