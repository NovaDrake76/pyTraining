A = int(input())
B = int(input())
C = int(input())

if((A < B and A > C) or (A < C and A > B)):
    print("A")
elif((B < A and B > C) or (B < C and B > A)):
    print("B")
elif((C < B and C > A) or (C < A and C > B)):
    print("C")
else:
    print("N")
