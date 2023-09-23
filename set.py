s1={1,2,3,4}
s2={1,4,789,65}


print("s1: {}".format(s1))
print("s2: {}".format(s2))

s3=s1.union(s2)
print("union of s1 and s2: {}".format(s3))

s4=s1.intersection(s2)
print("Intersection of s1 and s2: {}".format(s4))

s5=s1.difference(s2)
print("Difference of s1 and s2: {}".format(s5))

s6=s2.difference(s1)
print("Difference of s2 and s1: {}".format(s6))

s7=s1.symmetric_difference(s2)
print("Symmentric Difference of s1and s2: {}".format(s7))

s1.update(5)
print(s1)
