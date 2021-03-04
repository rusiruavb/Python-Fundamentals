if __name__ == '__main__':
  N = int(input())

  list1 = []
  for i in range(0, N):

    S = input().split(' ')
    if S[0] == 'append':
      list1.append(int(S[1]))
    elif S[0] == 'insert':
      list1.insert(int(S[1]), int(S[2]))
    elif S[0] == 'remove':
      list1.remove(int(S[1]))
    elif S[0] == 'print':
      print(list1)
    elif S[0] == 'pop':
      list1.pop()
    elif S[0] == 'sort':
      list1.sort()
    elif S[0] == 'reverse':
      list1.sort(reverse=True)
