arr=list(map(int,input("Enter Id of sighted bird :").split()))
def migratory_bird(arr):
    max_count=-1
    max_id=-1
    for i in range(1,6):
        if arr.count(i)>max_count:
            max_count=arr.count(i)
            max_id=i
        elif arr.count==max_count and i< max_id:
            max_id=i
    return max_id

print("The most frequent sighted Bird is :",migratory_bird(arr))
