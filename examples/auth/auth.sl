[INPUT]
src_ip_in@0.0.3
src_ip_in@1
dst_ip_in@0.0.3
dst_ip_in@1
packet_in
auth


[OUTPUT]
src_ip_out@0.0.3
src_ip_out@1
dst_ip_out@0.0.3
dst_ip_out@1
packet_out
authedip0


[ENV_INIT]
! auth


[SYS_TRANS]
$ 1 & ! ^ src_ip_in@1 src_ip_out@1 & ! ^ src_ip_in@0.0.3 src_ip_out@0.0.3 1
$ 1 & ! ^ dst_ip_in@1 dst_ip_out@1 & ! ^ dst_ip_in@0.0.3 dst_ip_out@0.0.3 1
| ! & auth $ 1 & ! src_ip_in@1 & ! src_ip_in@0.0.3 1 authedip0'
| ! authedip0 authedip0'
| ! & & packet_in authedip0 $ 1 & ! src_ip_in@1 & ! src_ip_in@0.0.3 1 packet_out
| ! ! authedip0 ! packet_out



[SYS_INIT]
! authedip0


[ENV_LIVENESS]
packet_in


[SYS_LIVENESS]


