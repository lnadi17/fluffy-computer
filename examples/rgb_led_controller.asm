// Write 0000 0000 0000 0111 in DDR
@7
D = A
@DDR
M = D

(LOOP)
@portval
M = 0
// RED
@32
D = A
@PIN
D = M & D

@WRITE_RED_HIGH
D ; JGT
(RED_END)

// GREEN
@16
D = A
@PIN
D = M & D

@WRITE_GREEN_HIGH
D ; JGT
(GREEN_END)

// BLUE
@8
D = A
@PIN
D = M & D

@WRITE_BLUE_HIGH
D ; JGT
(BLUE_END)

@portval
D = M
@PORT
M = D

@LOOP
0 ; JMP

(WRITE_RED_HIGH)
@4
D = A
@portval
M = M + D
@RED_END
0 ; JMP

(WRITE_GREEN_HIGH)
@2
D = A
@portval
M = M + D
@GREEN_END
0 ; JMP

(WRITE_BLUE_HIGH)
@1
D = A
@portval
M = M + D
@BLUE_END
0 ; JMP
