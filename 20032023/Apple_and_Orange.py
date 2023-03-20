
def countApplesAndOranges(s,t,a,b,apples,oranges):
    apple_count=0
    orange_count=0
    for ele in apples:
        dist=a+(ele)
        if dist>=s and dist<=t:
            apple_count+=1
    for ele in oranges:
        dist=b +(ele)
        if dist <= t and dist >=s:
            orange_count+=1
    print("Number of oranges on the sam house is" ,orange_count)
    print("Number of apples on the sam house is" ,apple_count)




if __name__=="__main__":
    first_line=input("Enter Starting Point and Ending point of Sam house :").split()
    #s: integer, starting point of Sam's house location.
    s=int(first_line[0])
    #t: integer, ending location of Sam's house location.
    t=int(first_line[1])
    second_line=input("Enter point of apples tree and orange tree: ").split()
    #a: integer, location of the Apple tree.
    a=int(second_line[0])
    #b: integer, location of the Orange tree.
    b=int(second_line[1])
    #apples: integer array, distances at which each apple falls from the tree.
    apples=list(map(int,input("Enter position of fall apples:").split()))
    #oranges: integer array, distances at which each orange falls from the tree.
    oranges=list(map(int,input("Enter Position of fall oranges:").split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)


