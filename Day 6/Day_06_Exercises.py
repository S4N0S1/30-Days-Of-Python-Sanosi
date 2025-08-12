# LEVEL 1

emp = tuple() #1
cpu_archeticture = ('comet_lake','tiger_lake','raptor_lake') #2
gpu_archeticture = ('Maxwell','Blackwell','Turing') #2
computer = cpu_archeticture + gpu_archeticture #3
print(len(computer)) #4

extras = ('RAM','Stoarge')
full_computer = computer + extras #5
print(full_computer)

# LEVEL 2
*stuff, volatile, non_volatile = full_computer #1
print(stuff)
print(volatile)

meyveler = ('elma','hurma','muz')
sebzeler = ('domates','patates','kabak')
yemek_tp = meyveler + sebzeler #2
yemek_lt = list(yemek_tp) #3

yarim_yemek = yemek_tp[2:3] #4

s1 = yemek_lt[0:3]
s2 = yemek_lt[-3:] #5

del yemek_tp #6

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"Estonia is a nordic country is a {('Estonia' in nordic_countries).lower()} statement.")
print(f"Iceland is a nordic country is a {'Iceland' in nordic_countries} statement.")