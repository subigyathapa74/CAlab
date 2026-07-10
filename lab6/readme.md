##  TOPIC : VHDL Code for Combinational
     Circuits: Code Converter




## OBJECTIVE:

• To design and simulate a BCD-to-Excess-3 code converter in VHDL.
• To design and simulate a Binary-to-Gray code converter in VHDL.



## THEORY :

## BCD to Excess-3

Excess-3 (XS-3) is a non-weighted BCD code obtained by adding 3 (0011) to each BCD digit.
It is self-complementing, making it useful in arithmetic circuits.



    



## Binary to Gray Code

Gray code is a binary numeral system where two successive values differ by only one bit. It is
widely used in rotary encoders and error minimization.
The conversion rule: Gi = Bi ⊕ Bi+1 (MSB of Gray = MSB of Binary).



## DISCUSSION :

The VHDL code for the code converter was successfully implemented and simulated. 
The output matched the expected converted codes for all valid input combinations, 
onfirming that the combinational circuit functions correctly without any delay due to clock signals.




## CONCLUSION:

The implementation and simulation of the VHDL code converter were successful. 
The experiment demonstrated the design and verification of combinational circuits using VHDL, 
and the obtained outputs were correct according to the code conversion logic.


