def main():
    countChar("Hello World Please", "Help")

def countChar(str, ref):
    new_dict = dict()
    for itr in ref:
        new_dict[itr.lower()] = 0

    for itr in str:
        if itr.lower() in new_dict.keys():
            freq = new_dict.get(itr.lower()) + 1
            new_dict.update({itr.lower():freq})

    for pair in new_dict.items():
        print(pair)


if __name__=="__main__":
    main()