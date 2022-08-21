# a = input(" ")
# a = a.split()
# a = "-".join(a)
# print(a)


# def print_full_name(first, last):
#
#     print('Hello {0} {1}! You just delved into python.'.format(first,last))
#
#
# # Write your code here
#
# if __name__ == '__main__':
#     first_name = input(" ")
#     last_name = input(" ")
#     print_full_name(first_name, last_name)


# def mutate_string(string, position, character):
#     res = string[:position]+character+string[position+1:]
#
#     return res
#
# if __name__ == '__main__':
#     s = input(" ")
#     i, c = input(" ").split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


def count_substring(string, sub_string):
    count = 0
    i = 0
    k=0
    res=0
    while(i<len(string)):
        while(k<len(sub_string)):
            if string[i]==sub_string[k]:
                count+=1
                if count==len(sub_string):
                    res+=1
                    count=0
                    k=0
                    break

                i+=1
                k+=1
            else:
                if count>0:
                    i-=1
                k=0
                break

        i+=1

    return res


if __name__ == '__main__':
    string = input(" ").strip()
    sub_string = input(" ").strip()

    count = count_substring(string, sub_string)
    print(count)