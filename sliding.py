def maxsubArray(a,k):
  sum=0
  max=sum
  for i in range(k):
    sum+=a[i]
  print(sum)
  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]
    if sum>max:
      max=sum
  print(max)

def minsubArray(a,k):
  sum=0
  min=sum
  for i in range(k):
    sum+=a[i] 
  print(sum)
  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]
    if sum<min:
      min=sum
  print(min)
  

a=[10,20,30,40,50,60]
k=3
maxsubArray(a,k)
minsubArray(a,k)