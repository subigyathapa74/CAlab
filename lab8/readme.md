## TOPIC: VHDL Code for Sequential Circuits:(Counters)

## OBJECTIVE:

• To design and simulate a 4-bit synchronous up counter in VHDL.
• To design and simulate a 4-bit synchronous up/down counter in VHDL.


## THEORY:
A counter is a sequential circuit that cycles through a predefined sequence of states on each
clock edge. Counters are built from flip-flops and are fundamental to timing, sequencing, and
frequency division.
• Synchronous counter: All flip-flops are clocked simultaneously — faster and more
reliable than ripple (asynchronous) counters.
• Up counter: Increments the count by 1 on each clock edge.
• Up/Down counter: Increments or decrements based on a direction control signal.
• Reset: An active-high synchronous or asynchronous reset returns the count to zero.




## DISCUSSION:

The counter increased (or decreased) its value with every clock pulse. 
The reset signal initialized the counter to zero. The simulation verified that the 
counter worked correctly according to the VHDL design.




##CONCLUSION:
The experiment was completed successfully. We learned how sequential circuits 
use clock signals and how counters are designed and verified using VHDL simulation.
