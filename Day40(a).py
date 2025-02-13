def staircase(n):
    # Write your code here
     i = 1
     j = n-1
     while i<=n:
        if i !=n:
            print(j*"."+"#"*i)

        else:
            print("#"*n)
        i+=1
        j-=1
n = int(input())
staircase(n)