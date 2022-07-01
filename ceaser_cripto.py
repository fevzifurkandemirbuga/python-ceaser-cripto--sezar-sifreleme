from prettytable import PrettyTable
def ceaser(text):
    table=PrettyTable(["encrypt","decrypt","text"])
    alphabet="abcdefghijklmnopqrstuvwxyza"
    letters=[]
    n=0
    # if the character is in the alphabet, I add the index number to the list, otherwise I add itself to the list
    for i in text:
        if not(i in alphabet):
            letters.append(str(i))
            continue
        letters.append(alphabet.index(i))
    while(n!=25):
        newtext = ""
        n+=1
        for i in letters:
            if (type(i) == str):
                newtext+=i
                continue
            newtext+=alphabet[(i+n)%26]
        table.add_row([n,n-26,newtext])
    print(table)
text=input("enter a text: ")
text=text.lower()
ceaser(text)