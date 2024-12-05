USE_SAMPLE = False
if USE_SAMPLE:
    data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
else:
    with open('d4a.txt') as f:
        data = f.read()
data = data.splitlines()

num_found = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        # Horizontal
        try:
            if(data[y+0][x+0] == 'X' and data[y+0][x+1] == 'M' and data[y+0][x+2] == 'A' and data[y+0][x+3] == 'S' ):
                num_found += 1
        except IndexError:
            pass

        try:
            if(data[y+0][x+0] == 'S' and data[y+0][x+1] == 'A' and data[y+0][x+2] == 'M' and data[y+0][x+3] == 'X' ):
                num_found += 1
        except IndexError:
            pass

        # Vertical
        try:
            if(data[y+0][x+0] == 'X' and data[y+1][x+0] == 'M' and data[y+2][x+0] == 'A' and data[y+3][x+0] == 'S' ):
                num_found += 1
        except IndexError:
            pass

        try:
            if(data[y+0][x+0] == 'S' and data[y+1][x+0] == 'A' and data[y+2][x+0] == 'M' and data[y+3][x+0] == 'X' ):
                num_found += 1
        except IndexError:
            pass

        # Down right
        try:
            if(data[y+0][x+0] == 'X' and data[y+1][x+1] == 'M' and data[y+2][x+2] == 'A' and data[y+3][x+3] == 'S' ):
                num_found += 1
        except IndexError:
            pass
        try:
            if(data[y+0][x+0] == 'S' and data[y+1][x+1] == 'A' and data[y+2][x+2] == 'M' and data[y+3][x+3] == 'X' ):
                num_found += 1
        except IndexError:
            pass
        
        # Up right
        try:
            if(data[y+3][x+0] == 'X' and data[y+2][x+1] == 'M' and data[y+1][x+2] == 'A' and data[y+0][x+3] == 'S' ):
                num_found += 1
        except IndexError:
            pass

        try:
            if(data[y+3][x+0] == 'S' and data[y+2][x+1] == 'A' and data[y+1][x+2] == 'M' and data[y+0][x+3] == 'X' ):
                num_found += 1
        except IndexError:
            pass
print(num_found)


num_found = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        try:
            if data[y+1][x+1] != 'A':
                continue

            a0 = data[y+0][x+0]
            a2 = data[y+2][x+2]
            b0 = data[y+2][x+0]
            b2 = data[y+0][x+2]
            if( ((a0=='M' and a2=='S') or (a0=='S' and a2=='M')) and 
                ((b0=='M' and b2=='S') or (b0=='S' and b2=='M'))):
                num_found += 1
        except IndexError:
            pass
            
print(num_found)


    