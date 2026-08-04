## TOPIC: Program to Implement the Booth  Algorithm

## OBJECTIVE:

• To understand the Booth multiplication algorithm for signed binary numbers.
• To implement the Booth algorithm and verify it with test cases.


## THEORY:

The Booth Algorithm (1951) is an efficient method for multiplying two signed integers in
two’s complement representation. It reduces the number of addition/subtraction operations
by exploiting runs of consecutive 1s and 0s in the multiplier.




##  ALGORITHM:
Given multiplicand M and multiplier Q, both n bits:
1. Initialize: Accumulator A = 0, Q−1 = 0, step count = n.
2. Examine the last bit of Q (Q0) and Q−1:
Q0 Q−1 Operation
0 0 No operation (shift only)
0 1 A = A + M
1 0 A = A − M
1 1 No operation (shift only)
3. Arithmetic right shift the combined register [A, Q, Q−1] by 1 bit.
4. Repeat step 2–3 for n cycles.
5. The result is in [A, Q].


## DISCUSSION:

The Booth's Algorithm program was implemented successfully. It correctly performs signed binary 
multiplication using addition, subtraction, and arithmetic shifts, producing the expected result.


## CONCLUSION:

This lab helped in understanding Booth's Algorithm for signed binary multiplication.
The algorithm is efficient, accurate, and commonly used in computer architecture.
