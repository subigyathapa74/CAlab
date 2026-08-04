# Add two binary numbers
def add(A, M):
    carry = 0
    Sum = ""

    for i in range(len(A) - 1, -1, -1):
        temp = int(A[i]) + int(M[i]) + carry
        Sum += str(temp % 2)
        carry = 1 if temp > 1 else 0

    return Sum[::-1]


# Find 2's complement
def complement(m):
    # Flip bits
    M = ''.join('1' if b == '0' else '0' for b in m)

    # Add 1
    one = '0' * (len(m) - 1) + '1'
    return add(M, one)


# Non-Restoring Division
def nonRestoringDivision(dividend_dec, divisor_dec):

    # Determine number of bits (+1 for sign)
    bit_len = max(dividend_dec.bit_length(), divisor_dec.bit_length()) + 1

    Q = format(dividend_dec, f'0{bit_len}b')
    M = format(divisor_dec, f'0{bit_len}b')
    A = '0' * bit_len

    comp_M = complement(M)
    flag = "successful"

    print(f"\nInitial Values:")
    print(f"A : {A}")
    print(f"Q : {Q}")
    print(f"M : {M}")

    for i in range(bit_len):

        print(f"\nStep {i + 1}")

        # Left Shift
        combined = A + Q
        combined = combined[1:]

        A = combined[:bit_len]
        Q_temp = combined[bit_len:]

        # Add/Subtract
        if flag == "successful":
            A = add(A, comp_M)
            print("Operation : Shift Left & Subtract")
        else:
            A = add(A, M)
            print("Operation : Shift Left & Add")

        # Update Q
        if A[0] == '1':
            Q = Q_temp + '0'
            flag = "unsuccessful"
        else:
            Q = Q_temp + '1'
            flag = "successful"

        print(f"A = {A}")
        print(f"Q = {Q}")

    # Final correction
    if A[0] == '1':
        print("\nFinal Correction: A = A + M")
        A = add(A, M)

    print("\n" + "-" * 30)
    print(f"Binary Quotient  : {Q}")
    print(f"Decimal Quotient : {int(Q, 2)}")
    print(f"Binary Remainder : {A}")
    print(f"Decimal Remainder: {int(A, 2)}")


# Main Program
if __name__ == "__main__":

    try:
        dividend = int(input("Enter Dividend (Decimal): "))
        divisor = int(input("Enter Divisor (Decimal): "))

        if divisor == 0:
            print("Division by zero is not allowed.")
        else:
            nonRestoringDivision(dividend, divisor)

    except ValueError:
        print("Please enter valid integers.")
