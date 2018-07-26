[INPUT]
act
deact

[OUTPUT]
policy
active
callback

[ENV_INIT]
!act 
!deact

[SYS_INIT]
!active

[ENV_TRANS]
!(act & deact)

[SYS_TRANS]
act -> X(active)
(active & !deact) -> X(active)
deact -> X(!active)
deact -> X(callback)

[ENV_LIVENESS]

[SYS_LIVENESS]
