with open('data.csv', 'r') as data:
    data = data.read().split('\n')
    print(*data,sep='\n')