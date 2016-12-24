Python Program | by Cory Sollberger 5/4/2016

A program that simulates a turing machine by reading a turing machine into the program by parsing a
text file. 

The machine has several implementations:

- A turing machine that uses only 3 symbols, (0,1, B "blank"), and determines if the number of 0s
  and 1s in a block are the same. If the number of 0s and 1s are the same then the machine halts
  on a blank space, if the block contains a differing number of 0s and 1s then the machine halts
  on a non-blank space.

- A turing machine that recognizes strings in the form of (0^n)(1^n)(2^n), if the turing machine
  halts on a blank space n for each variable is the same (ex. 001122). If the machine halts on a
  non-blank space n differs for at least one of the variables (ex. 0001112222).

The program evaluates strings that are given to the program by showing the current state of the tape
through each iteration of the machine, which modifies the tape based on the value of the input to the
machine.