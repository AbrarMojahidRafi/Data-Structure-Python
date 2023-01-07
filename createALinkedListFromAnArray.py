class Node:
  def __init__(self, v, a):
    self.elem=v
    self.next=a

givenArray=[10, 20, 30, 40]
head=Node(givenArray[0], None)
tell=head

h=head
i=1
while (i<len(givenArray)):
  tell=Node(givenArray[i], None)
  h.next=tell
  h=h.next # / h=tell
  i+=1