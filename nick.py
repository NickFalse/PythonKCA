def potato (var1, var2, var3, var8675309):
    stuff = (var1 + var3)
    othercrap = (var2 + var8675309)
    return (stuff, othercrap)

thing = raw_input("thinggy here 4char")
varr1 = thing[0]
varr2 = thing[1]
varr3 = thing[2]
varr4 = thing[3]
varr1 = int(varr1)
varr2 = int(varr2)
varr3 = int(varr3)
varr4 = int(varr4)
print (potato(varr1, varr2, varr3, varr4))
