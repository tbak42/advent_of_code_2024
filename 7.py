DATA_FILE = 'd7b.txt'
equations = []
with open(DATA_FILE) as f:
    for line in f.read().splitlines():
        bar = line.split(': ')
        eq = {'total':int(bar[0]), 'vals':list(map(int,bar[1].split(' ')))}
        equations.append(eq)

print(equations)

def try_em(total, current_value, remaining_vals):

    if total == 7290:
        print('{}, {}'.format(current_value, remaining_vals))

    if len(remaining_vals) == 0:
        if current_value == total:
            print('hit!')
            print(total)
            return True
        return False

    if current_value > total:
        return False

    if current_value == 0:
        # Can either pop the first number or concatenate 
        c = try_em(total, remaining_vals[0], remaining_vals[1:] )
        d = False
        if len(remaining_vals) > 1:
            d = try_em(total, 0, [int(str(remaining_vals[0])+str(remaining_vals[1]))] + remaining_vals[2:])
        return c or d

    else:
        a = try_em(total, current_value+remaining_vals[0], remaining_vals[1:])
        b = try_em(total, current_value*remaining_vals[0], remaining_vals[1:])
        d = False
        if len(remaining_vals) > 0:
            #d = try_em(total, current_value, [int(str(remaining_vals[0])+str(remaining_vals[1]))] + remaining_vals[2:])
            d = try_em(total, int(str(current_value)+str(remaining_vals[0])), remaining_vals[1:])
        return a or b or d

calibration_val = 0
for eq in equations:
    if try_em(eq['total'], 0, eq['vals']):
        calibration_val += eq['total']

print(calibration_val)