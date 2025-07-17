#1
Thirty = 'Thirty'
Days = 'Days'
Of = 'of'
Python = 'Python'
print(Thirty + ' ' + Days + ' ' + Of + ' ' + Python)

#2
Coding = 'Coding'
_For = ' For'
All = ' All'
print(Coding + _For + All)

#3, 4, 5, 6, 7, 8, 9
company = 'Coding For All'
print(company)
print(f"length of Coding For All is {len(company)}")
print(company.upper())
print(company.lower())
print(f"""
      Preview of several methods and their effects:
      .capitalize() > {company.capitalize()}
      .title() > {company.title()}
      .swapcase() > {company.swapcase()}
      """)
company_first_word = company[0:6]
print(f"First word of {company} is ({company_first_word})")

#10
company_check = company.find('Coding') != -1
company_ans = f'"{company} contains the word {company_first_word}" is a {company_check} statement.'
company_ans_lowercase = company_ans.lower()
print(company_ans_lowercase)

#11
company_replace = company.replace('Coding', 'Python')
print(company_replace)

#12
python_all = 'Python For Everyone'
print(python_all.replace('Everyone', 'All'))

#13
company_split = company.split('*')
print(company_split)

#14
brands = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
brands_split = brands.split(', ')
print(brands_split)

#15
print(f"The character at index 0 in the string '{company}' is '{company[0:1]}'")

#16
print(f'The last index of the string "{company}" is {company.rfind('l')}')

#17
print(f"The character at index 10 in '{company}' is '{company[10:11]}'")

#18
company_acronym1 = company[0:1]
company_acronym2 = company[7:8]
company_acronym3 = company[11:12]
print(company_acronym1+company_acronym2+company_acronym3)

#19
python_all_acronym1 = python_all[0:1]
python_all_acronym2 = python_all[7:8]
python_all_acronym3 = python_all[11:12]
print(python_all_acronym1+python_all_acronym2+python_all_acronym3)

#20
print(f'The index of the first occurence of C in {company} is {company.index('C')}')

#21
print(f'The index of the first occurence of F in {company} is {company.index('F')}')

#22
people = 'Coding For All People'
print(f'The index of the last occurence of l in {people} is {people.rfind('l')}')

#23
conjuction = 'You cannot end a sentence with because because because is a conjunction'
print(f'The index of the first occurence of "because" in "{conjuction}" is {conjuction.find('because')}')

#24
print(f'The index of the last occurence of "because" in "{conjuction}" is {conjuction.rindex('because')}')

#25
#? conjuction_sliced = conjuction[31:54]
#? print(conjuction_sliced)
#! TO AMMAR: Do I need to put everything into a variable?
print(conjuction[31:54])

#26
print(f'The index of the first occurence of "because" in "{conjuction}" is {conjuction.find('because')}')

#27
print(conjuction[31:54])

#28
coding_start = company.startswith('Coding')
coding_end = company.endswith('Coding')
print(company)
print(f'"{company} starts with the word {company_first_word}" is a {str(coding_start).lower()} statement.')

#29
print(f'"{company} ends with the word {company_first_word}" is a {str(coding_end).lower()} statement.')

#30
company_space = '   Coding For All      '
company_space_stripped = company_space.strip(' ')
print(company_space_stripped)

#31
isidentifier1 = '30DaysOfPython'
isidentifier2 = 'thirty_days_of_python'
print(f'"{isidentifier1} is a {str(isidentifier1).isidentifier()} identifier.')
print(f'"{isidentifier1} is a {str(isidentifier2).isidentifier()} identifier.')

#32
list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list1))

#33
escape = 'I am enjoying this challenge. I just wonder what is next.'
#         0123456789
escape_slice1 = escape[0:29]
escape_slice2 = escape[30:]
print(escape_slice1 + '\n' + escape_slice2)

#34
print('Name\t\tAge\t\tCountry\t\tCity')
print('Asabeneh\t250\t\tFinland\t\tHelsinki')

#35
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))

#36
print('8 + 6 = {}\n8 - 6 = {}\n8 * 6 = {}\n8 / 6 = {}\n8 % 6 = {}\n8 // 6 = {}\n8 ** 6 = {}'.format(8+6, 8-6, 8*6, round(8/6, 1), 8%6, 8//6, 8**6))