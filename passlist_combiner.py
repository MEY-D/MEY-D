print("\nhey mother fucker im MEY-D\n\nthis easy project can combine 2 text files\n\n")
first_txt_name = input("write your(( First )) txt_file   but without .txt  :  ")
key = open("{}.txt".format(first_txt_name))
second_txt_name = input("write your(( Second )) txt_file   but without .txt  :  ")
suffix = open("{}.txt".format(second_txt_name))
s1 = ["".join([x.strip()]) for x in key.readlines()]
s2 = ["".join([x.strip()]) for x in suffix.readlines()]
code = []
for x in s1:
    for z in s2:
        c = [x+z]
        code.append(c)
with open("result.txt", 'w') as file:
        for row in code:
            s = "".join(map(str, row))
            file.write(s+'\n')