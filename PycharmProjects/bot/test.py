import tree
import random
f = open("countries.txt", "r")
def fill_the_tree():
  f = open("countries.txt", "r")
  root=None
  countries=[]
  for x in f:
    x=x.replace('\n','')
    x=x.lower()
    root = tree.insert(root, x)
  f.close()
  return root
def check_user_first_letter(last_letters, user_word):
  if last_letters:
    if user_word[0]==last_letters[-1]:
      return 'ok'
    else:
      return 'no'
  else:
    return 'ok'
def check_first_letter(letter, word):
  if letter== word[0]:
    return 'ok'
  else:
    return 'no'
def check_input(word, root):
  a = []
  tree.find(root, word, a)
  if a:
    root = tree.deleteNode(root, a[0])
    return ('ok', root)
  else:
    return(0,1)

def find_word(root, letter, delete_node):
  arr = []
  tree.find_g(root, letter, arr)
  for capital in reversed(arr):
    if check_first_letter(letter, capital)!='ok':
      arr.remove(capital)
  if not arr:
    return ('NONE',0)
  else:
    word= random.choice(arr)
    if delete_node==1:
      root=tree.deleteNode(root,word)
    #else:
      #root = tree.insert(root, word)
    return (word, root)
root=fill_the_tree()
root1=fill_the_tree()
'''

print ("Inorder traversal of the given tree")
tree.inorder(root)
a=[]
tree.find_g(root, 'Y',a)

print(a[0])
root=tree.deleteNode(root, 'zagreb' )
print ("Inorder traversal of the given tree")
#print('found')
a=[]
tree.find(root, 'sofiaa',a)
print(a)
'''
