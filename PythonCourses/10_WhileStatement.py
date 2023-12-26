num = 10

while num > 5:
    print(f"the number is still bigger than 5: {num}")
    num -=1;
else:
    print("number is less than 5")

#---------------------- PASS KEYWORD -----------------------------
#I want to do nothing for now(will be back later on) thus i put PASS  keyword
x = [1,2,3]

for item in x:
     pass

#------------------CONTINOUE KEYWORD ----------------------------------

str1= "Abdullah"

for item in str1:
    if item == "a" or item == "A": #a olursa hiçbirşey yapma, sıradaki loop'a devam et
    # if item.lower() == "a";
        continue
    print(item)


print("---------------------------------------")
#------------------BREAK  KEYWORD ----------------------------------

for item in str1:
    if item == "a": #a olursa hiçbirşey yapma, sıradaki loop'a devam et
    # if item.lower() == "a";
        break
    print(item)

