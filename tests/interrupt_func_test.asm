@3
D = A
@MASK
M = D
@PRESCALER
M = 1

(LOOP)
@R0
M = M + 1
M = M + 1
M = M + 1
M = M + 1
M = M + 1
M = M + 1
@LOOP
0 ; JEQ

(INTERRUPT_FUNCTION)
SD = 1
SD = D + 1
SD = D + 1
S = D + 1
S
S
S
S

D = S
@OLD_A
M = S
@OLD_PC
M = S
@OLD_A
S = M
@OLD_PC
A = M
A = S ; JMP
