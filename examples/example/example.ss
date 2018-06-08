[INPUT]
a
b

[OUTPUT]
x
y

[ENV_INIT]
& ! a ! b

[SYS_INIT]
& ! x ! y

[ENV_TRANS]
| a' ! | x y

[SYS_TRANS]
| ! x' ! y'


[SYS_LIVENESS]
& a y
