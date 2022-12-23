import argparse
from statistics import mean

parser = argparse.ArgumentParser()
parser.add_argument('infile')
parser.add_argument('-medals', dest='medals', nargs=2)
parser.add_argument('-output', '--output', type=argparse.FileType('w', encoding='UTF-8'))
parser.add_argument('-total' , dest='total' )
parser.add_argument('-overall',dest='overall', nargs='+')
parser.add_argument('-interactive',dest='interactive')
args = parser.parse_args()

#task 1
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
  with open(args.infile) as file:
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


def check_valid_year(year):
    with open(args.infile) as file:
        next_line = file.readline()
        for line in file:
            part = line.split('\t')
            annum = part[9].strip()
            if year == annum:
                return True
    return False


def first_ten(medalists):
  ten = []
  for i in range(10):
    ten.append(f'{medalists[i][1]} - {medalists[i][12]} - {medalists[i][14]}'.strip())
  return ten


def store(ten, gold, silver, bronze):
    store = f"{ten}\n" \
            f" Gold medals - {gold}\n " \
            f"Silver medals - {silver}\n " \
            f"Bronze medals - {bronze}"
    return store


if args.medals is not None:
 country, year = args.medals
 valid_country = check_valid_country(country)
 valid_year = check_valid_year(year)

 if valid_country == False:
  print("This country doesn't exsist")
  exit()

if valid_year == False:
  print("In this year country didn't take part ")
  exit()

medalists = medalist(country, int(year))
 gold, silver, bronze = total_medals(medalists)
 ten = first_ten(medalists)
 store = store(ten, gold, silver, bronze)
 print(store)
if len(medalists) < 10:
  print(f"In {country} in {year} less than 10 medalists")
  exit()


if args.output is not None:
    args.output.writelines(f'{store}\n')



# task 2
def total(year):
    totalInfo = dict()
    with open(args.infile,'r') as file:
        next_line = file.readline()
        for line in file:
            part = line.split('\t')
            team = part[6].strip()
            annum = part[9].strip()
            medal = part[14].strip()
            if annum == year and medal != 'NA':

                if not team in totalInfo:
                    totalInfo[team] = {'Gold' : 0 , 'Silver' : 0, 'Bronze' : 0}
                totalInfo[team][medal] +=  1

    return totalInfo


if args.total is not None:
    year = args.total
    country_in_this_year = total(year)
    for a in country_in_this_year:
        print(a)
        for y in country_in_this_year[a]:
            print(y, ':', country_in_this_year[a][y])

#task 3
def overall(countries_list):
    for country in countries_list:
        results = {}
        with open(args.infile, "r") as file:
            for line in file:
                part = line.split('\t')
                team = part[6].strip()
                annum = part[9].strip()
                medal = part[14].strip()
                if country == team and medal != "NA":
                    if annum not in results:
                        results[annum] = 1
                    else:
                        results[annum] += 1

            print(country, max(results, key=results.get), max(results.values()))


if args.overall:
    countries_list = args.overall
    countries_list_result = overall(countries_list)


def interective(country):
        results = {}
        with open(args.infile, "r") as file:
            for line in file:
                part = line.split('\t')
                team = part[6].strip()
                annum = part[9].strip()
                medal = part[14].strip()
                if country == team and medal != "NA":
                    if annum not in results:
                        results[annum] = 1
                    else:
                        results[annum] += 1
            best_game = max(results.values())
            best_year = max(results, key=results.get)
            lose_game = min(results.values())
            worst_year = min(results, key=results.get)
            min_year = min(results.keys())
            return best_game, best_year, lose_game, worst_year, min_year


def average(country):
    data = {}
    with open(args.infile,'r') as file:
        next_line = file.readline()
        for line in file:
            part = line.split('\t')
            team = part[6].strip()
            annum = part[9].strip()
            medal = part[14].strip()
            noc = part[7].strip()
            if country in (team, noc) and medal != 'NA':
                if not team in data:
                    data[team] = {'Gold' : 0 , 'Silver' : 0, 'Bronze' : 0}
                data[team][medal] +=  1
    return data


def count(country):
    count = 0
    years = []
    with open(args.infile,'r') as file:
        next_line = file.readline()
        for line in file:
            part = line.split('\t')
            team = part[6].strip()
            annum = part[9].strip()
            medal = part[14].strip()
            noc = part[7].strip()
            if country in (team, noc) and medal != 'NA':
                if not annum in years:
                    years.append(annum)
    return years


if args.interactive is not None:
    country = args.interactive
    best_game, best_year, lose_game, worst_year, min_year = interective(country)
    statictic = average(country)
    involved_years = len(count(country))
    count_gold_medals = int(statictic[country]['Gold'])
    count_silver_medals = int(statictic[country]['Silver'])
    count_bronze_medals = int(statictic[country]['Bronze'])
    average_gold = count_gold_medals / involved_years
    average_silver = count_silver_medals /involved_years
    average_bronze = count_bronze_medals / involved_years
    print(f'The firt game in {min_year}')
    print(f'The best game in {best_year}, medals - {best_game}')
    print(f'The worst game in {worst_year}, medals - {lose_game}')
    print(f'The average of Gold medals for all years - {average_gold}')
    print(f'The average of Silver medals for all years - {average_silver}')
    print(f'The average of Bronze medals for all years - {average_bronze}')



