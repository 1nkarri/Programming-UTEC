num_input = 0
while num_input<= 0 or number_input > 500:
    num_input = int(input("Número [1 - 500]: "))

i = 0
while i < num_input:
    i += 1
    if i % 4 == 0 and i % 6 == 0:
        print(i, "TicTac")
    elif i % 6 == 0:
        print(i, "Tac")
    elif i % 4 == 0:
        print(i, "Tic")
    else:
        print(i)