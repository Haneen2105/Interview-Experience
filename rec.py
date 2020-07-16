print('Round 1')
print()
print('q1: which one of these is a programming language windows or python')
q1 = input()
print()
print('q2: which one of these is an OS linux or java')
q2 = input()
print()
print('q3: which one of these is used in frontend development html or php')
q3 = input()
print()
print('q4: which one of these is a data structure arrays or android')
q4 = input()
def word_break_recursive(string, dictionary):
    n = len(string)
    if n == 0:
        return True
    for i in range(1, n + 1):
        if dictionary.__contains__(string[0: i]) and word_break_recursive(string[i: n], dictionary):
            return True

    return False


dictionary = ["arrays", "python", "linux", "html", "the", "answer", "is", "it's", " "]
total=0
if word_break_recursive(q1,dictionary):
    total+=10
if word_break_recursive(q2,dictionary):
    total+=10
if word_break_recursive(q3,dictionary):
    total+=10
if word_break_recursive(q4,dictionary):
    total+=10
gdc=total/4

print("Yes" if word_break_recursive(q1, dictionary) else "No")
print("Yes" if word_break_recursive(q2, dictionary) else "No")
print("Yes" if word_break_recursive(q3, dictionary) else "No")
print("Yes" if word_break_recursive(q4, dictionary) else "No")
print()
print('Score: ',gdc)
print()
print("Accepted welcome to OYO" if gdc>=7 else "Rejected good luck next time")

