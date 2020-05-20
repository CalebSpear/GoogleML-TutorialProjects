import math
total = (-(6/12) * math.log2(6/12))-((6/12) * math.log2(6/12))
print('total entropy',total)

good = (-(3/4) * math.log2(3/4))-((1/4) * math.log2(1/4))
average = (-(1/2) * math.log2(1/2))-((1/2) * math.log2(1/2))
poor = (-(1/4) * math.log2(1/4))-((3/4) * math.log2(3/4))
credit = 1/3 * good + 1/3 * average + 1/3 * poor
print('g entropy',good)
print('a entropy',average)
print('p entropy',poor)
print('cred entropy',credit)
print('info gain cred', total - credit)

deep = (-(2/4) * math.log2(2/4))-((2/4) * math.log2(2/4))
shallow = (-(2/3) * math.log2(2/3))-((1/3) * math.log2(1/3))
plot = 4/7 * deep + 3/7 * shallow
print('Deep entropy',deep)
print('shallow entropy',shallow)
print('plot entropy',plot)

yes = (-(2/3) * math.log2(2/3))-((1/3) * math.log2(1/3))
no = (-(2/4) * math.log2(2/4))-((2/4) * math.log2(2/4))
star = 3/7 * yes + 4/7 * no
print('Deep entropy',yes)
print('shallow entropy',no)
print('plot entropy',star)