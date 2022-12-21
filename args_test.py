import argparse

parser = argparse.ArgumentParser()
parser.add_argument('infile')
parser.add_argument('-medals', dest='medals', nargs=2)
parser.add_argument('-output', '--output', type=argparse.FileType('w', encoding='UTF-8'))
parser.add_argument('-total' , dest='total', nargs=1 )
args = parser.parse_args()

def medalist(country, year):
  medalists = []
  file = args.infile
  with open(file , 'r') as file:
    next_line = file.readline()
    for line in file:
      part = line.split('\t')
      medal = part[14].strip()
      annum = int(part[9].strip())
      team = part[6].strip()
      noc = part[7].strip()
      if medal != 'NA' and annum == year and country in (team, noc):
        medalists.append(part)
  return medalists


def total_medals(medalists):
  gold = 0
  silver = 0
  bronze = 0
  for each in medalists:
    medal = each[14].strip()
    if medal == 'Gold':
      gold += 1
    elif medal == 'Silwer':
      silver += 1
    elif medal == 'Bronze':
      bronze += 1
  return gold, silver, bronze


def check_valid_country(country):
  valid_country = False
  valid_year = False
  file = args.infile
  with open(file) as file:
        next_line = file.readline()
        for line in file:
            part = line.split('\t')
            team = part[6].strip()
            noc = part[7].strip()
            if country in (team, noc):
                valid_country = True
            if valid_country:
                return valid_country
  return valid_country


def check_valid_year (year):
    valid_year = False
    file = args.infile
    with open(file) as file:
        next_line = file.readline()
        for line in file:
            part = line.split('\t')
            annum = part[9].strip()
            if year in annum:
                valid_year = True
            if valid_year:
                return valid_year
    return valid_year


def first_ten(medalists):
  ten = []
  for i in range(10):
    ten.append(f'{medalists[i][1]} - {medalists[i][12]} - {medalists[i][14]}'.strip())
  return ten


if args.medals is not None:
 country, year = args.medals
 valid_country = check_valid_country(country)
 valid_year = check_valid_year(year)

 if valid_country == False:
  print("This country doesn't exsist")
  exit()


 if args.total is not None:
   year = args.total
   valid_year = check_valid_year(year)
 
 
  

if valid_year == False:
  print("In this year country didn't take part ")
  exit()

if args.medals is not None:
 medalists = medalist(country, int(year))

if len(medalists) < 10:
  print(f"In {country} in {year} less than 10 medalists")
  exit()

if args.medals is not None:
  gold, silver, bronze = total_medals(medalists)
ten = first_ten(medalists)

def store(ten, gold, silver, bronze):
    store = f"{ten}\n" \
            f" Gold medals - {gold}\n " \
            f"Silver medals - {silver}\n " \
            f"Bronze medals - {bronze}"
    return store

if args.medals is not None:
 store = store(ten, gold, silver, bronze)
#print(store)

if args.output is not None:
  args.output.writelines(f'{store}\n')



def total(year):
  totalInfo = dict()
  sorted_totalInfo = dict()
  with open(args.infile,'r') as file:
        next_line = file.readline()
        for line in file:
            part = line.split('\t')
            team = part[6].strip()
            annum = part[9].strip()
            medal = part[14].strip()
            if annum == year and  medal != 'NA':
                if not team in totalInfo:
                    totalInfo[team] = {'Gold' : 0 , 'Silver' : 0, 'Bronze' : 0}
                totalInfo[team][medal] +=  1
  return totalInfo


if args.total is not None:
    country_in_this_year = total(year)
    for a in country_in_this_year:
        print(a)
        for y in country_in_this_year[a]:
            print(y, ':', country_in_this_year[a][y])