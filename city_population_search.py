

def output_formatted(year, rank, population):
    """ takes in field values for the year, rank and population
        of a given city and prints them with the appropriate
        formatting
    """
    pop = int(float(population) * 1000)
    print(year + '    ' + format(rank, '2s') + format(pop, '14,d'))

def find_results(filename, city, state):
    ''' returns the year, rank and population fields of the file cities.txt'''
    file = open(filename)
    count = 0
    
    
    for line in file:
        line = line[:-1]
        fields = line.split(',')
        if fields[2] == city and fields[3] == state:
            output_formatted(fields[0], fields[1], fields[4])
            count += 1
    if count == 0:
        print('no results found for', city, state)
        
    file.close()
    
    
    
    

def main():
    ''' interactive program that outputs the year, rank and population fields'''
    filename = input('Enter the name of data file: ')
    
    while True:
        city = input('city: ')
        if city == 'quit':
            break
        state = input('state abbreviation: ')
        find_results(filename, city, state)
        print()
        

        