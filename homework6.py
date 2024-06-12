my_dict={'Monday':12, 'Tuesday':14, 'Wednesday':15, 'Thursday':16}
print(my_dict)
print(my_dict['Monday'])
print(my_dict.get('Friday'))
my_dict.update({'Saturday':18,'Sunday':20})
del my_dict['Tuesday']
print(my_dict.get('Tuesday'))
print(my_dict)

my_set={1,2,4,9,True,"fghj",2,4,9,True,4,9,True}
print(my_set)
my_set.add(8)
my_set.add(7)
my_set.discard(2)
print(my_set)