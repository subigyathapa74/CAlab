## TOPIC: VHDL Code for Sequential Circuits:(Flip-Flops)


## OBJECTIVE
• To design and simulate SR, D, JK, and T flip-flops in VHDL.
• To understand the role of the clock signal in sequential circuits.


## THEORY

A flip-flop is a bistable sequential element — it stores one bit of state. Unlike combinational
circuits, its output depends on both the current inputs and its previous state. Flip-flops are
triggered by a clock signal, either on the rising edge (rising edge) or falling edge.


 SR flipflop
An SR (Set-Reset) Flip-Flop is a basic sequential logic circuit used to store one bit of data. 
It has two inputs, S (Set) and R (Reset), and two outputs, Q and Q̅ (complement of Q).
The output changes only on the triggering clock edge in a clocked SR flip-flop.

D Flip-Flop
The D flip-flop captures the value of D on the clock edge: Qnext = D.


JK Flip-Flop
Eliminates the forbidden state of SR. When J = K = 1, the output toggles: Qnext = JQ+KQ.

T Flip-Flop
When T = 1, output toggles; when T = 0, output holds: Qnext = T ⊕ Q.




## DISCUSSION:

The VHDL codes for SR, D, JK, and T Flip-Flops were implemented and simulated successfully. 
The outputs changed only on the rising edge of the clock, verifying the sequential behavior of flip-flops.
Each flip-flop performed its expected operation: SR (Set, Reset, Hold), D (stores input), JK (Set, Reset, Hold, Toggle),
and T (Toggle). The simulation results matched the respective truth tables.



## CONCLUSION:
The implementation and simulation confirmed the correct operation of the SR, D, JK, and T Flip-Flops. 
This experiment demonstrated how sequential circuits store data and change states based on the clock signal, 
providing a clear understanding of flip-flop behavior in digital systems.



