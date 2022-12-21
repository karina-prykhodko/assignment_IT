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


def check_valid_country_year(country, year):
  valid_country = False
  valid_year = False
  file = args.infile
  with open(file) as file:
        next_line = file.readline()
        for line in file:
            row = line.split('\t')
            team = row[6].strip()
            noc = row[7].strip()
            annum = row[9].strip()
            if country in (team, noc):
                valid_country = True
            if year in annum:
                valid_year = True
            if valid_country and valid_year:
                return valid_country, valid_year
  return valid_country, valid_year


def first_ten(medalists):
  ten = []
  for i in range(10):
    ten.append(f'{medalists[i][1]} - {medalists[i][12]} - {medalists[i][14]}'.strip())
  return ten




if args.medals is not None:
  country, year = args.medals
  
if args.total is not None:
  country, year = args.total

valid_country, valid_year = check_valid_country_year(country, year)
 
  

if valid_country == False :
  print("This country doesn't exsist")
  exit()

if valid_year == False:
  print("In this year country didn't take part ")
  exit()

medalists = medalist(country, int(year))

if len(medalists) < 10:
  print(f"In {country} in {year} less than 10 medalists")
  exit()

gold, silver, bronze = total_medals(medalists)
ten = first_ten(medalists)

def store(ten, gold, silver, bronze):
    store = f"{ten}\n" \
            f" Gold medals - {gold}\n " \
            f"Silver medals - {silver}\n " \
            f"Bronze medals - {bronze}"
    return store


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
              if team in totalInfo and medal in totalInfo[team]:
                totalInfo[team][medal] += 1
              else:
                totalInfo[team][medal] = 1
                sorted_totalInfo[team] += 1
            else:
              totalInfo[team]=dict()
              totalInfo[team][medal] = 1
              sorted_totalInfo[team] = 1
                        
                           
                        
            line = file.readline()

        for countryName, results in totalInfo.items():
          print(f'{countryName}')
        for medal, count in results.items():
          print(f'\t{medal} - {count}')


A = total(year)
print(A)

