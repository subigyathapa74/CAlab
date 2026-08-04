## TOPIC: Program to Implement the  Non-Restoring Division Algorithm

## OBJECTIVE:

• To understand the non-restoring division algorithm for unsigned binary numbers.
• To implement the algorithm in Python and verify with test cases.



## THEORY:

The Non-Restoring Division Algorithm is a binary division method that avoids the costly
restoration step found in the restoring algorithm. It works with a partial remainder A and
divisor M over n steps.
In restoring division, if a subtraction yields a negative partial remainder, the dividend is
restored by adding back the divisor. Non-restoring division skips this: instead, it remembers
the sign of A and uses it to decide the next operation.



## ALGORITH:


Given dividend Q (n bits) and divisor M (n bits), both unsigned:
1. Initialize: A = 0, load Q into the quotient register.
2. For each of n steps:
(a) Left-shift [A, Q] by 1 bit.
(b) If A ≥ 0: subtract M from A (i.e., A = A − M).
If A < 0: add M to A (i.e., A = A + M).
(c) If A ≥ 0: set Q0 = 1 (quotient bit = 1).
If A < 0: set Q0 = 0 (quotient bit = 0).
3. After n steps, if A < 0, restore by adding M (final correction).
4. Q holds the quotient; A holds the remainder.
