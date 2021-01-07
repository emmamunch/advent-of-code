# content = []
# num_lines = 0
# with open('day4input.txt', 'r', newline='\n\n') as f:
#     for line in f:
#         if line == "" or line == "\n':
#             num_lines += 1
#         else:
#             cont

# print(content[0])
import re
content = open('day4input.txt').read().strip('\n').split('\n\n')
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
num_valid = 0
for pp in content:
    fields = {f.split(':')[0]: f.split(':')[1] for f in re.split(' |\n', pp)}
    # if all([v in fields for v in req_fields]):
    #     valid += 1
    valid = True
    for field in req_fields:
        if field not in fields:
            valid = False
            break
        val = fields[field]
        if field == 'byr':
            val = int(val)
            valid = val >= 1920 and val <= 2002
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
            if 'in' in val:
                hgt = int(val[:val.index('in')])
                valid = hgt >= 59 and hgt <= 76
        
        if not valid:
            break
        
        num_valid += 1

        
    # for field in re.split(' |\n', pp):
    #     if not valid:
    #         break
    #     pair = field.split(':')
    #     key = pair[0]
    #     val = pair[1]
    #     if key == 'byr':
    #         valid = val >= 1920 and val <= 2002
    #     if key == 'iyr':

    


print(valid)