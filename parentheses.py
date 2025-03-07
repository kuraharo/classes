def valid(item1,item2):
    dictionary={"[":"]","{":"}","(":")","]":None,")":None,"}":None,"0":None}
    if item2==dictionary[str(item1)]:
        return True
    return False


string_input=input()
flag=1
while len(string_input)>0 and flag==1:
    flag=0
    for index in range(len(string_input)-1):
        current_simvol=string_input[index]
        next_simvol=string_input[index+1]
        if valid(current_simvol,next_simvol):
            string_input=string_input[:index]+"00"+string_input[index+2:]
            flag=1
    string_input=string_input.replace("0","")
    print(string_input)
if flag==1:
    print(True)
else:
    print(False)
