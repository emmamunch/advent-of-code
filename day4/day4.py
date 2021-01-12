import re
import numpy as np
content = open('day4input.txt').read().strip('\n').split('\n\n')
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
num_valid = 0
for i, pp in enumerate(content):
    fields = {f.split(':')[0]: f.split(':')[1] for f in re.split(' |\n', pp)}
    # if not all([v in fields for v in req_fields]):
    #     continue
    valid = True
    for field in req_fields:
        if field not in fields:
            valid = False
            break
        val = fields[field]
        if field == 'byr':
            val = int(val)
            valid = (val >= 1920 and val <= 2002)
        elif field == 'iyr':
            val = int(val)
            valid = val >= 2010 and val <= 2020
        elif field == 'eyr':
            val = int(val)
            valid = val >= 2020 and val <= 2030
        elif field == 'hgt':
            if 'cm' in val:
                hgt = int(val[:val.index('cm')])
                valid = hgt >= 150 and hgt <= 193
            elif 'in' in val:
                hgt = int(val[:val.index('in')])
                valid = hgt >= 59 and hgt <= 76
            else:
                valid = False
        elif field == 'hcl':
            valid = bool(re.match(r'^#[0-9a-f]{6}$', val))
        elif field == 'ecl':
            valid = val in ecl
        elif field == 'pid':
            valid = bool(re.match('^[0-9]{9}$', val))
            
        if not valid:
            break

    if valid:
        num_valid += 1

print(num_valid)
