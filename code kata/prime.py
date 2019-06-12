g=int(input())
if g>1:
  for i in range(4,g):
    if(g%i==0):
      print("no")
      break    
  else:
    print("yes")
else:
  print("no")
