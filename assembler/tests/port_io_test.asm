@256			// 0100					//0100 # Select 256
D = -A			// 1000 0100 1000 1000	//8488 # Write 1111 1111 0000 0000 in D_Reg
@0				// 0000					//0000 # Select DDR
M = D			// 1000 0000 1101 0000	//80d0 # Write 1111 1111 0000 0000 in DDR_Reg
@2   			// 0002					//0	   # Select Pin_Reg
D = M			// 1000 0010 1000 1000	//8288 # Write Pin_Reg in D_Reg
@256			// 0100					//	   # Select 256
D = D * A 		// 1000 1000 0100 1000	//8848 # Write Pin_Reg * 256 in D_Reg
@1   			// 0001					//0001 # Select Port_Reg
M = D			// 1000 0000 1101 0000	//80d0 # Write Pin_Reg in Port_Reg
@4				// 0004					//	   # Select 4
0 ; JMP 		// 1000 0000 0000 0111  //8007 # Jump to start
