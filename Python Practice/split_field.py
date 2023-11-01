class my_string(str):
    def splitfields(self, sep=None):
        if sep is None:
            return self.split()
        else:
            return self.split(sep)

str1 = "IIT Delhi is a good college, I have to get placemenet here"
field1 = my_string(str1).splitfields()
print(field1)

str2 = "My,name,is,chandra,prakash"
field2 = my_string(str2).splitfields(",")
print(field2)