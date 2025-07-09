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
      capitalize() > {company.capitalize()}
      title() > {company.title()}
      swapcase() > {company.swapcase()}
      """)
company_first_word = company[0:6]
print(f"First word of {company} is ({company_first_word})")

#10
company_check = company.find(company_first_word) + 1 == 1
print(f'"{company} contains the word {company_first_word} is a {company_check} statement."')