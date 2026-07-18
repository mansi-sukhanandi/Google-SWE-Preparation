def base_ball_game(ops):
    stack = []
    for op in ops:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            num = int(op)
            stack.append(num)

    total = sum(stack)
    return total

testing = ["5", "2", "C", "D", "+"]
print("Result :", base_ball_game(testing))  
