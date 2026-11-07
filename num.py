# integer number from 1 to 50 conversion


dict = {1:"One", 2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Fourty",50:"Fifty"}



try:
    x = int(input("Enter value: "))

    power = 1
    numlist = []
    if x not in dict:
        while(x!=0):
            last = x%10
            x = x//10

            num = last*power
            power = power *10

            numlist.append(num)
    else:
        print(dict[x])


    while numlist:
        last = numlist.pop()
        print(dict[last],end=" ")

except Exception:
    print("Expected only 1 to 49")
