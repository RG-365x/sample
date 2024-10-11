x = input("Enter a number")
if not x.isdigit:
    print("You did not enter a number.")
set1a = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
set1b = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
set2 = ["Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
y = 0
for letter in x:
    y += 1
if y == 1:
    print(set1a[int(x)-1])
elif y == 2:
    if int(x[0]) == 1:
        d1 = ''
        d2 = set1b[int(x[1])]
    else:
        
        d1 = set1a[int(x[1])-1]
        d2 = set2[int(x[0])-1]
    if int(x[1]) == 0:
        print(d2)
    else:
        print(d2, d1)
elif y == 3:
    d3 = set1a[int(x[0])-1]
    if int(x[1:2]) == 0:
        print(d3, " hundred ")
    else:
        if int(x[1]) == 1:
            d1 = ''
            d2 = set1b[int(x[2])]
        else:
            d1 = set1a[int(x[2]) - 1]
            d2 = set2[int(x[1]) - 1]
        if int(x[2]) == 0:
            print(d3, " hundred ", d2)
        else:
            print(d3, " hundred ", d2, d1)
else:
    print("Your fellow programmer was too lazy to write code for more than three digits")









