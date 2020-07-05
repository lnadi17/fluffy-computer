@DDR
M = 1
@3
D = A
@MASK
M = D
@PRESCALER
M = D - 1

(LOOP)
@LOOP
0 ; JMP

(INTERRUPT_FUNCTION)
// Trigger LED
@PORT
M = !M

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
