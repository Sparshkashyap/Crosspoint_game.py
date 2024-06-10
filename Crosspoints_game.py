import random
print("\n============================[Welcome to the crosspoints Game with Indian Player]==========================\n")
lis=["A","B","C","D","E","F","G","H","I","J"]
print()
print(lis)
lst=[25,48,7,77,4,66,65,97,65,46]
#print(lst)
print()

random.shuffle(lst)
new_lis=[]
sum1=0
#print(lst)
for i in range(5):
    num=input("Enter the player name to this list which you have (choice any 5) :")
    new_lis.append(num)
    c=lis.index(num)
    sum1=sum1+lst[c]
    
      
      
#print(sum1)
print(new_lis)

if sum1>=200 :
    print("This team win the match")
else:
    print("This team not win the match")
        
            