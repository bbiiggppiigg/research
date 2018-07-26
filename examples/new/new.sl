[INPUT]
act
deact


[OUTPUT]
policy
active
callback


[ENV_TRANS]
! & act deact


[ENV_INIT]
! act
! deact


[SYS_TRANS]
| ! act active'
| ! & active ! deact active'
| ! deact ! active'
| ! deact callback'


[SYS_INIT]
! active


[ENV_LIVENESS]


