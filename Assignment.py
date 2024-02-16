def product_data(product_data.txt):
    data = []
    with open(product_data.txt,'r') as file:
        for line in file:
            data_strip = line.strip().split(',')
            data ={}