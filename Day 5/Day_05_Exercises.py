
# DAY_05_Exercises

# LEVEL 1
empty_list = [] #1
six_items = ["item1", "item2", "item3", "item4", "item5", "item6"] #2
print(f"The length of six_items is {len(six_items)}") #3
print(six_items[0], six_items[1], six_items[-1]) #4
mixed_data_types = list(["Ahmad", 21, 192.5,"KHHV","Islamic University"]) #5
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"] #6
print(it_companies) #7
print(f"The length of it_companies is {len(it_companies)}") #8

#! Attempted to make a print that'll always print the middle company REGARDLESS of the number of companies :P
middle_company = round(len(it_companies)/2)
print(it_companies[0], it_companies[middle_company-1], it_companies[-1]) #9
it_companies[0] = "Telegram"
print(it_companies) #10
it_companies.append("X") #11
print(it_companies)
middle_company = round(len(it_companies)/2)
it_companies.insert(middle_company, "LinkedIn") #12
print(it_companies)
it_companies[3] = it_companies[3].upper() #13
print(it_companies)

joined_companies1 = '#; '.join(it_companies) #14
print(joined_companies1)

lookup = input("Type a company name and I'll see if it exists in it_companies: ") #15
#  if it_companies.index(lookup) != -1 :
#  print(f"Yes, {lookup} exists in it_companies.\nIt is the item number {it_companies.index(lookup)+1} from right.")
#  else:
#  print(f"Sorry, {lookup} doesn't exist in that list")

#! This is probably a better method (because it can deal with the errors):
#? How to make an if to make it point from left or right depending on the closest path.
try: print(f"Yes, {lookup} exists in it_companies.\nIt is the item number {it_companies.index(lookup)+1} from right.")
except ValueError: print(f"Sorry, {lookup} doesn't exist in that list")

sorted_it_companies = sorted(it_companies) #16 (better?)
print(f"This is the list in alphabetical order:\n {sorted_it_companies}")
it_companies.sort() #16
print(it_companies)

it_companies.reverse() #17
print(it_companies)

print(it_companies[0:3]) #18

print(it_companies[-3:]) #19
#! Why is print(it_companies[-3:-1]) wrong?

middle_company = round(len(it_companies)/2)
print(it_companies[middle_company-2], it_companies[middle_company-1], it_companies[middle_company]) #20 (REGARDLESS OF NUMBER OF ITEMS)
print(it_companies[2:5]) #20 (Won't work if the list gets modified)

it_companies.pop(0) #21
print(it_companies)

del it_companies[middle_company-1] #22
print(it_companies)

it_companies.pop() #23
print(it_companies)

del it_companies[0:] #24 #? Other methods?
print(it_companies)

del it_companies #25

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end) #26

full_stack = front_end.copy() #27
full_stack.insert(4, 'Python')
full_stack.insert(5, 'SQL')
print(full_stack)

# LEVEL 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(f"The min age is {ages[0]} and the max age is {ages[-1]}.")
ages.append(ages[0])
ages.append(ages[-2])
print(ages)

median_age = (ages[5] + ages[6])/2
print(f"The median age is {round(median_age)}")

average_age = (ages[0]+ages[1]+ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9]+ages[10]+ages[11])/len(ages)
print(f"The average age is around {round(average_age, 1)}")

ages.sort()
print(f"The range of the ages is {round(ages[-1] - ages[0])}")

abs(ages[-1] - average_age)
abs(ages[0] - average_age)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
# print(len(countries))
middle_country = (round(len(countries)/2))
print(middle_country)
print(f"The middle country is {countries[middle_country-1]}")

first_countries = countries[0:(middle_country)]
last_countries = countries[middle_country+1:-1]
print(first_countries)

Sean, Rousia, Amrika, *Scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(Amrika)
print(Scandic)