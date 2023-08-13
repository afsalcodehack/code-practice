
def generate_paranthesis(n , open, close , str):

    if open == n and close == n:
        print(str)
        return

    if n > open:
        #open paranthesis
        generate_paranthesis(n,open+1 , close , str+"(")
    if open > close:
        generate_paranthesis(n,open , close+1 , str+")")


generate_paranthesis(3, 1 , 0 , "(")

#generate_paranthesis(0, 1 , 0 , "(")