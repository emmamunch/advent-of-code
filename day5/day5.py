import pandas as pd

def read_row(seat):
    seat = seat[:-3]
    seat = seat.replace('F', '0')
    seat = seat.replace('B', '1')
    row = 0
    for i in range(7):
        row += int(seat[i]) * (2 ** (7-i-1))
    return row

def read_col(seat):
    seat = seat[-3:]
    seat = seat.replace('L', '0')
    seat = seat.replace('R', '1')
    col = 0
    for i in range(3):
        col += int(seat[i]) * (2 ** (3-i-1))
    return col

def part1():
    with open('day5input.txt', 'r') as f:
        content = f.read()

    max_seat_id = 0
    for line in content.split('\n'):
        row = read_row(line.strip())
        col = read_col(line.strip())
        if 8*row +col > max_seat_id:
            max_seat_id = 8*row +col

    print('part 1:', max_seat_id)
part1()

def part2():
    seats = pd.read_csv('day5input.txt', names=['Seat String'])
    seats['Seat ID'] = seats.apply(lambda x: read_row(x['Seat String']) * 8 + read_col(x['Seat String']), axis=1)
    min_seat = seats['Seat ID'].min()
    max_seat = seats['Seat ID'].max()
    seat = [seat for seat in range(min_seat, max_seat) if seat not in list(seats['Seat ID'])]
    print('part 2:', seat)

part2()