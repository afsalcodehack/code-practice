def RecursiveSolution(step):

    if step == 0 or step == 1:
        return 1;

    return RecursiveSolution(step-1) + RecursiveSolution(step-2)


print(RecursiveSolution(4));