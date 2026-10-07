def traversal(ar):
  print('[',end="")
  for i in range(len(ar)-1):
    print(ar[i],end=', ')
  print(ar[-1],end=']')


def insert(ar,el,ind):
  ar2=[0 for i in range(len(ar)+1)]
  for i in range(ind):
    ar2[i]=ar[i]
  for i in range(ind,len(ar)):
    ar2[i+1]=ar[i]
  ar2[ind]=el
  return ar2
  
def delete(ar,ind):
  if ind<=0 or ind>=len(ar):
    print('Invalid size')
    return ar
  else:
    ar2=[0 for i in range(len(ar)-1)]
    for i in range(ind):
      ar2[i]=ar[i]
    for i in range(ind+1,len(ar)):
      ar2[i-1]=ar[i]
    return ar2
    
def search(ar,el):
  for i in range(len(ar)):
    if a[i]==el:
      print(f'Element {el} is found at index {i}')
      return
  print(f'Element {el} is not found')


a=[1,2,3,4,5]
b=15
print(b)
print(a)
traversal(a)
print()
a=insert(a,15,4)
print(a)
c=delete(a,5)
print(c)
search(a,15)