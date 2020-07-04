@DDR
M = -1

@x
M = 0
@y
M = 0

@3
D = A
@r
M = D
@g
M = D
@b
M = D

(PAINT_SCREEN_WHITE)
@out
M = 0

@x
D = M
@2048
D = D * A
@out
M = M + D

@y
D = M
@64
D = D * A
@out
M = M + D

@r
D = M
@16
D = D * A
@out
M = M + D

@g
D = M
@4
D = D * A
@out
M = M + D


@b
D = M
@out
MD = M + D

@PORT
M = D

@x
M = M + 1
@y
M = M + 1
@PAINT_SCREEN_WHITE
0 ; JMP
