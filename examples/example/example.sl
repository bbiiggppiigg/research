[INPUT]
a
b


[OUTPUT]
x
y


[ENV_TRANS]
| a' ! | x y


[ENV_INIT]
& ! a ! b


[SYS_TRANS]
| ! x' ! y'



[SYS_INIT]
& ! x ! y


[SYS_LIVENESS]
& a y

