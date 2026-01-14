# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#range(start?, stop, step?);
seq = range(5);
print(seq[0]);
print(seq[1]);
print(seq[3]);
print(seq[4]);

print("Using loops\n")
for i in seq:
    print(i);


for i in range(10):
    print(i);

for i in range(1, 5):
    print(i);

print("Using three conditions");
for i in range(2, 20, 2):
    print(i);

for i  in range(100, 0, -2):
    print(i);

#Pass Statement: pass is a null statement that does nothing. It is used as a placeholder for future code.

for i in range(6):
    pass
print("We are working on pass statement");
print("Find factorial");
n = 5;
fact = 1;
for i in range(1, n+1):
    fact = fact * i;
print("factorial: ",fact);

