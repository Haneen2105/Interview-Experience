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
def word_break(string, dictionary):
    n = len(string)
    if n == 0:
        return False
    dp = [False for _ in range(n + 1)]

    matched_index = [-1]

    for i in range(n):
        msize = len(matched_index)
        is_matched = False

        for j in range(msize - 1, -1, -1):
            sub_string = string[matched_index[j] + 1: i + 1]
            if( dictionary.__contains__(sub_string)):
                is_matched = True
                break
        print(dp)
        if is_matched:
            dp[i] = True
            matched_index.append(i)
    print(dp)
    return dp[n - 1]


dictionary = ["arrays", "python", "linux", "html", "the", "answer", "is", "it's", " "]

total=0


if(word_break(q1, dictionary)):
    total+=10
if(word_break(q2, dictionary)):
    total+=10
if(word_break(q3, dictionary)):
    total+=10
if(word_break(q4, dictionary)):
    total+=10

gdc=total/4

print("Yes" if word_break(q1, dictionary) else "No")
print("Yes" if word_break(q2, dictionary) else "No")
print("Yes" if word_break(q3, dictionary) else "No")
print("Yes" if word_break(q4, dictionary) else "No")
print()
print('Score: ',gdc)
print()
print("Accepted welcome to OYO" if gdc>=7 else "Rejected good luck next time")

