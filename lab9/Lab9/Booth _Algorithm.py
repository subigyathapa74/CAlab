# Simple Booth's Algorithm (8-bit)

def to_binary(n, bits=8):
    """Convert decimal to binary (8-bit two's complement)."""
    if n < 0:
        n = (1 << bits) + n
    return format(n, f'0{bits}b')


def arithmetic_right_shift(A, Q, Q1):
    """Perform arithmetic right shift."""
    Q1 = Q[-1]
    Q = A[-1] + Q[:-1]
    A = A[0] + A[:-1]
    return A, Q, Q1


def binary_add(a, b):
    """Add two binary strings."""
    result = int(a, 2) + int(b, 2)
    result &= 0xFF  # Keep only 8 bits
    return format(result, '08b')


def twos_complement(binary):
    """Find two's complement."""
    value = (~int(binary, 2) + 1) & 0xFF
    return format(value, '08b')


def booths_algorithm():
    M = int(input("Enter Multiplicand: "))
    Q = int(input("Enter Multiplier: "))

    M_bin = to_binary(M)
    minus_M = twos_complement(M_bin)

    A = "00000000"
    Q_bin = to_binary(Q)
    Q1 = "0"

    print("\nInitial Values")
    print("M :", M_bin)
    print("-M:", minus_M)
    print("A :", A)
    print("Q :", Q_bin)
    print()

    for step in range(8):
        last_two = Q_bin[-1] + Q1

        if last_two == "01":
            A = binary_add(A, M_bin)
            operation = "A = A + M"
        elif last_two == "10":
            A = binary_add(A, minus_M)
            operation = "A = A - M"
        else:
            operation = "No Operation"

        print(f"Step {step + 1}")
        print("Operation:", operation)

        A, Q_bin, Q1 = arithmetic_right_shift(A, Q_bin, Q1)

        print("A :", A)
        print("Q :", Q_bin)
        print("Q-1:", Q1)
        print("-" * 30)

    product = A + Q_bin

    print("Final Binary Product :", product)
    print("Decimal Product      :", M * Q)


# Run program
booths_algorithm()
