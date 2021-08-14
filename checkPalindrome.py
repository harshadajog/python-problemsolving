def main():
    print(solution("rabar"))

def solution(s):
    if len(s) <= 2:
        return True
    length = int(len(s))    
    for i in range(0, int(length/2)):
        if s[i] != s[length-i-1]:
            return False
    return True

if __name__=="__main__":
    main()    
