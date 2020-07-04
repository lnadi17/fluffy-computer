@256			// 0100					//0100 # Select 256
D = -A			// 1000 0100 1000 1000	//8488 # Write 1111 1111 0000 0000 in D_Reg
@0				// 0000					//0	   # Select DDR_Reg
M = D			// 1000 0000 1101 0000	//80d0 # Write D_Reg in DDR_Reg
@1				// 0001					//0001 # Select Port_Reg
M = -1			// 1000 0101 0101 0000	//8550 # Write 1111 1111 1111 1111 in Port_Reg
				//							   # Turn on first 8 LEDs
