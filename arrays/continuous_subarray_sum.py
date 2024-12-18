a=[3,12,2,2,7,5]
start=0
end=1
target =12
sol=a[start]

while(start < len(a) and end < len(a)):
    if(start==end):
        print(start+1, end+1)
        break 
        
    if(sol+a[end]==target):
        print(start+1, end+1)
        break 
    elif(sol+a[end]>target):
        sol-=a[start]
        start+=1 
    else:
        sol+=a[end]
        end+=1

  
