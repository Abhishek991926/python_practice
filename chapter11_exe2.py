# # python program to define a function that take a list 
# # and print the first letter of the string is capital


def func(l1):
    a=[]
    for i in range(len(l1)):
        a.append(l1[i].title())
    return a

#     return a
l2=["abhishek","satyam"] 
# print(func(l2))       

print(func(l2))

a=["abhishek","satyam"]
# b=a.split()
# print(b)

# solution 1
print('solution 1 - ',list(map(lambda s: s.title(), a)))

# solution 2
print('solution 2 - ')

# solution 3
print('solution 3 - ',[s[0].upper()+s[1:] for s in a])

# jo tum socha rhe the uspar dhyan do
print('ye jo tum soch rhe the',[s[0].title() for s in a])



# solution of Chapter11 exe 2

def func1(l1,**kwargs):
        print([i[::-1].title() if kwargs.get('reverse_str')==True else i.title() for i in l1 ])    
func1(l2)    