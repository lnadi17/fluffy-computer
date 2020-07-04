// Set up DDR
@255
D = A
@DDR
M = D
// Keyboard loop
(KBD_LOOP)
@KEYBOARD
D = M
@KEY_PRESSED
D ; JNE
@256
D = A
@PIN
D = M & D
@KBD_LOOP_END
D ; JEQ
@128
D = A
@PORT
M = D
M = 0
(KBD_LOOP_END)
@KBD_LOOP
0 ; JMP

// Key pressed event
(KEY_PRESSED)
@PORT
M = D
M = 0
// Wait for zero in keyboard value (Key up event)
(KEY_UP_WAIT)
@KEYBOARD
D = M
@KEY_UP_WAIT
D ; JNE
@KBD_LOOP
0 ; JMP
