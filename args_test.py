import argparse

parser = argparse.ArgumentParser()
parser.add_argument('infile', type=argparse.FileType('r'))
parser.add_argument('-medals', dest='medals', nargs=2, required=True)
parser.add_argument('-output', '--output', type=argparse.FileType('w', encoding='UTF-8'))
parser.add_argument('-year', dest='year' , nargs=1, type= int )
parser.add_argument('-country', dest='country', nargs=1, type= str)

args = parser.parse_args()
print(args.medals)


with args.infile as file:
  next_line = file.readline()
  store = [next_line]
  while next_line:
      # do stuff with line
      next_line = file.readline()
      store.append(next_line)

if args.output is not None:
  args.output.writelines(f'{store[0]}\n')

def medalist(file_name, country, year):
  medalists = []

  with open(file_name) as file:
    next_line = file.readline()

    for line in file:

      part = line.split('/t')

      medal = part[14].strip()
      annum = int(part[9].strip())
      team = part[6].strip()
      noc = part[7].stip()

      if medal != 'NA' and annum == year in (team, noc):
        medalists.append(part)

  return medalists


def total_medals(medalists):
  golg = 0
  silver = 0
  bronze = 0

  for each in medalists:

    medal = each[14].stip()

    if medal == 'Gold':
      golg += 1
    elif medal == 'Silwer':
      silver += 1
    elif medal == 'Bronze':
      bronze += 1

  return golg, silver, bronze


def check_valid_country_year(file_name, country, year):
  country = False
  year = False

  with open(file_name) as file:
    next_line = file.readline()

    for line in file:
      part = line.split('/t')
      team = part[6].strip()
      noc = part[7].stip()
      annum = int(part[9].strip())

      if country in (team, noc):
        country = True
      if year in annum:
        year = True

  return country, year


def first_ten(medalists):
  ten = []
  for i in range(10):
    ten.append(f'{medalists[i][1]}-{medalists[i][12]}-{medalists[i][14]}'.strip())
    
  return ten
