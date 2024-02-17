import time

def product_data():
    data_list = []
    file_name = "product_data.txt"
    with open(file_name,'r') as file:
        for line in file:
            data = line.strip().split(', ')
            data_info = {'id': data[0], 'product': data[1], 'price': data[2], 'category': data[3]}
            data_list.append(data_info)
        return data_list  
print(product_data())

def add(data_list,add_item):
    data_list.append(add_item)

def delete(data_list,remove_item):
    data_list.pop(remove_item)

 #def update(data_list,)
 
def search_info(data_list, product_name):
     for i in data_list:
        if i['product'] == product_name:
            print (i)

def print_list(data_list):
    for i in data_list:
        print(data_list)

