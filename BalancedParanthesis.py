def main():
    print(isBalanced("[()({})]"))

def isBalanced(s):
    # Write your code here
   
    # if not s or len(s) == 0:
    #     return "NO"
    stack = []
    i = 0
    for i in s:
        if i in ["[", "{", "("]:
            stack.append(i)
        else:
            current = stack.pop()
            if(current == "{"):
                if i != "}":
                    return False
            if(current == "["):
                if i != "]":
                    return False
            if(current == "("):
                 if i != ")":
                    return False   
   
    if len(stack) == 0:
        return True
    else:
        return False
    


if __name__=="__main__":
    main()