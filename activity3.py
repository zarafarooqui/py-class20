def test(n):
    iteration = 0
    for i in range(0,n):
        for j in range (0,n):
            print("*",end="")
            iteration+=1
            print("")
            print("\nwhen n is ",n,"iteration=",iteration)
test(5)
test(4)
test(3)
print("\n with every 'n' the taken = n^2")
print("(n^2)")
#worst scenario
#time comnplexity = 0(n^2)