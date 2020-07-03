// Set mask to 0000 0000 0000 0011
@3 // 0003
M = A // 1000 0000 1001 0000 # 8090
// Set prescaler to 1
@4 // 0004
M = 1 // 1000 0001 0101 0000 # 8150
// Increase value of Memory[7] (Will happen more than once if interrupt works)
@7 // 0007
M = M + 1 // 1000 0011 1001 0000 # 8390
// Start infinite loop
@6 // 0006
0 ; JMP // 1000 0000 0000 0111 # 8007
