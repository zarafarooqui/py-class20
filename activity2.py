def OnTime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print("When n is ",n," Iterations=",iteration)

OnTime(10)
OnTime(20)
OnTime(42)

print("\nWith every 'n' the time taken and iteration will increase linearly" )
#time complexity=0(n)
#Average case scenario