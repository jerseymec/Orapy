if __name__ == '__main__':
    N = int(input())
commands = []
sample = []
for i in range(N):
    commands += [input()]


def list_insert(i, a):
    sample.insert(1, a);
    return


def list_append(a):
    sample.append(a)
    return


def list_print():
    print(sample)
    return


def list_remove(e):
    sample.remove(e)
    return


def list_sort():
    sorted(sample)
    return


def list_pop():
    elemtent = sample.pop()
    return


def list_reverse():
    sample.sort(reverse=True)
    return


Commands = {
    "insert": (lambda sample: sample.insert(i, e)),
"append": (lambda sample: sample.append(e)),
"print": (lambda sample: print(sample)),
"remove": (lambda sample: sample.remove(e)),
"sort": (lambda sample: sample.sort()),
"pop": (lambda sample: sample.pop()),
"reverse": (lambda sample: sample.sort(reverse=True))
}


for string in commands:
      arg = []
      e = 0
      i = 0
# print(string.split())
      s = string.split()
      comm = s[0]
      args = s[1:]
      if (len(arg) > 1):
         (i, e) = arg
      else:
         e = arg
# print(f"i = {i}")
# print("e = {}".format(e))
# print(comm)
# print(arg)

# params, i, e = string.split()
# print(params)
      Commands[comm]
      print(sample)
