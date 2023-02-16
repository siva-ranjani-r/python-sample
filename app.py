ip="aaabbccccaabbbbbddddd"
t = []
t1 = ""
count = 0
for i in ip:
    if t1 != i:
        count = 1
        t1 = i
    else: 
        count += 1
        t.append((t1, count))
print(t)
temp=0
string=""
for i in range(len(t)):
    if t[i][i]==t[i+1][i]:





# dic={}
# for i in st:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# temp=""
# for i in dic:
#     temp+=i+str(dic[i])
# print(temp)


# def compress(input_str):
#     output_str = ""
#     count = 1
#     for i in range(len(input_str)):
#         if i + 1 < len(input_str) and input_str[i] == input_str[i + 1]:
#             count += 1
#         else:
#             output_str += input_str[i] + str(count)
#             count = 1
#     return output_str

# input_str = "aaabbccccaabbbbbddddd"
#print(compress(input_str))

