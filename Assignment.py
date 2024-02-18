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

def add(data_list,id,product,price,category):
    data_list.append({'id': id, 'product': product, 'price': price, 'category': category})

def delete(data_list,remove_item):
    data_list.pop(remove_item)

def update_data(data_list,id,product,price,category):
     for i in data_list:
         if i['id']==id:
             i['product'] = product
             i['price'] = price
             i['category']=category
             return(product,price,category)
     return None
 
def search_info(data_list, product_name):
     for i in data_list:
        if i['product'] == product_name:
            return (i)
     return None

def print_list(data_list):
    for i in data_list:
        print(data_list)

def bubble_sort(data_list):
    for i in range (len(data_list)-1,0,-1):
        for j in range(i):
            if data_list[j]['price'] > data_list[j+1]['price']:
               data_list[j],data_list[j+1] = data_list[j+1], data_list[j]
    return(data_list)

if __name__== '__main__':
    data_list = product_data()
    print_list(data_list)
    
    update_data(data_list, '3', 'Product A' , '15.00', 'Category 3')
    print_list(data_list)
    
    add(data_list, '2','Product A', '15.00','Category 2')
    print_list(data_list)
    
    delete(data_list,4)
    print_list(data_list)
    
    sorted=bubble_sort(data_list)
    print_list(sorted)

    search=search_info(data_list, 'Product A')
    print(search)
    
    