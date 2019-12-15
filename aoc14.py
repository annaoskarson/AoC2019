import math
def initiera():
    fil = open('14-input.txt', 'r')
    lines = fil.read().split('\n')[:-1]

    skafferi = {}
    recept= {}
    for x in lines:
        ingredienser = []
        [left, right] = x.split('=>')
        [no_right, right] = right.split()
        lefts = left.split(',')
        for i in lefts:
            (mängd, ingrediens) = i.split()
            ingredienser = ingredienser + [(ingrediens, int(mängd))]
            skafferi[ingrediens] = 0
        # lägg in recept för all mat
        recept[right] = int(no_right), ingredienser
        # lägg in ingredienserna i skafferiet
        skafferi[right] = 0
    return(skafferi, recept)

def laga_mat(mat, port):
    if mat == 'ORE':
        #Dessa lånar vi av grannen och behöver inte betala för
        skafferi[mat] = skafferi[mat] - port
    else:
        a_recept = 1
        #kolla recept
        (ny_port, ingredienser) = recept[mat]
        if port > skafferi[mat]: #om det inte finns i skafferiet
            #det blev ny_port stycken av ett recept
            #kolla hur många gånger vi behöver göra receptet
            multipel_recept = math.ceil((port - skafferi[mat]) / ny_port)
            #lägg till alla nya portioner vi gör nu
            skafferi[mat] = skafferi[mat] + ny_port*multipel_recept
            #laga_mat varje ingrediens, multiplicera här med hur många vi behövde av maten
            for i_mat, i_port in ingredienser:
                laga_mat(i_mat, i_port*multipel_recept)
        skafferi[mat] = skafferi[mat] - port

skafferi, recept = initiera()

def part1():
    laga_mat('FUEL',1)
    print(abs(skafferi['ORE']))

#part1()

guess = 1
numbers = 1
laga_mat('FUEL', guess)
ores = abs(skafferi['ORE'])
print(numbers, ":", guess, "FUEL av antal ORES:", ores)
while ores < 1000000000000:
    numbers = numbers + 1
    guess = math.ceil(guess + ((1000000000000 - ores) * (guess/ores))-(ores/1000000000000)+1)
    skafferi, recept = initiera()
    laga_mat('FUEL', guess)
    ores = abs(skafferi['ORE'])
    print(numbers, ":", guess, "FUEL av antal ORES:", ores)
print("svar:", guess-1)


