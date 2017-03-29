dicter = {}
with open('gc.txt', 'r') as f:
    for line in f:
        if line.startswith('>'):
            name = line[1:].rstrip('\n')
            dicter[name] = ''
        else:
            dicter[name] += line.rstrip('\n')
            dicter[name] = str(100*(dicter[name].count('G') + dicter[name].count('C'))/len(dicter[name]))


print(dicter)

for d in dicter:
    print("The sequence %s is %s %% GC pairs" % (d, dicter[d])  )
