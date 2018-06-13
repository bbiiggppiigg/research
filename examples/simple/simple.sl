[INPUT]
packet_in


[OUTPUT]
port@0.0.3
port@1
zcount@0.0.3
zcount@1
ocount@0.0.3
ocount@1


[ENV_INIT]



[SYS_TRANS]
| ! & packet_in $ 1 & ! port@1' & ! port@0.0.3' 1 $ 5 ^ 1 zcount@0.0.3 & 1 zcount@0.0.3 ^ zcount@1 ? 1 & zcount@1 ? 1 & ! ? 3 & ! ^ zcount@1' ? 2 & ! ^ zcount@0.0.3' ? 0 1
| ! & packet_in $ 1 & ! port@1' & ! ^ port@0.0.3' 1 1 $ 5 ^ 1 ocount@0.0.3 & 1 ocount@0.0.3 ^ ocount@1 ? 1 & ocount@1 ? 1 & ! ? 3 & ! ^ ocount@1' ? 2 & ! ^ ocount@0.0.3' ? 0 1
| | | $ 1 & ! ^ zcount@1 ocount@1 & ! ^ zcount@0.0.3 ocount@0.0.3 1 $ 5 ^ 1 ocount@0.0.3 & 1 ocount@0.0.3 ^ ocount@1 ? 1 & ocount@1 ? 1 & ! ? 3 & ! ^ zcount@1 ? 2 & ! ^ zcount@0.0.3 ? 0 1 $ 1 & ! ^ ocount@1 zcount@1 & ! ^ ocount@0.0.3 zcount@0.0.3 1 $ 5 ^ 1 zcount@0.0.3 & 1 zcount@0.0.3 ^ zcount@1 ? 1 & zcount@1 ? 1 & ! ? 3 & ! ^ ocount@1 ? 2 & ! ^ ocount@0.0.3 ? 0 1


[SYS_INIT]
$ 1 & ! zcount@1 & ! zcount@0.0.3 1
$ 1 & ! ocount@1 & ! ocount@0.0.3 1


[ENV_LIVENESS]
packet_in


[SYS_LIVENESS]
$ 1 & ! port@1 & ! port@0.0.3 1
$ 1 & ! port@1 & ! ^ port@0.0.3 1 1
$ 1 & ! ^ port@1 1 & ! ^ port@0.0.3 0 1
$ 1 & ! ^ port@1 1 & ! ^ port@0.0.3 1 1

