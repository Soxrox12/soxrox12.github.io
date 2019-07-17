print("I'm running")
a = ["bee", "wasp", "moth", "ant"]
a.sort()
print(a)

b = [3,6,5,2,4,1]
b.sort()
print(b)

L = ["cccc", "b", "dd", "aaa"]

print("Normal sort :", sorted(L))
print(L)
print("Sort with len :", sorted(L, key = len))
