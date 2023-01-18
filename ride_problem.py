"""
ID: alyshar1
LANG: PYTHON3
PROG: ride
"""
import sys
sys.stderr.write('message')
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
x = list(map(str, fin.readline().split()))
y = list(map(str, fin.readline().split()))

alpha = list(map(chr, range(97, 123)))
ALPHA = list(map(lambda letter: letter.upper(), alpha))

def ride(x, y):
    x = list(map(lambda letter: letter.upper(), x))
    y = list(map(lambda letter: letter.upper(), y))
    x = x[0]
    y = y[0]
    totalX = 1
    totalY = 1
    for i in range(len(x)):
        letterIdx = ALPHA.index(x[i]) + 1 
        totalX *= letterIdx
    for i in range(len(y)):
        letterIdx = ALPHA.index(y[i]) + 1 
        totalY *= letterIdx
    if totalX % 47 == totalY % 47:
        fout.write ("GO\n")
        fout.close()
    else: 
        fout.write ("STAY\n")
        fout.close()

ride(x, y)