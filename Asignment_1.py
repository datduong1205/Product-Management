# Name: Le Minh Dat Duong
# ID: 100886108
# Assignment 1 - Data Structure and Algorithms

import time 
import sys

class ProductManager:
    
    def __init__(self):
        global  product_list 

    def load_product(self):
        for count, value in enumerate(product_list):
            print(f'Product {count}: {value[0]}, {value[1]}, {value[2]}, {value[3]}')

    def insert_product(self):
        new_product = list(input('Please enter new product (ID, Name, Price, Category): ').split(', '))
        index = int(input('Where do you want to insert it?[0-{}]: '.format(len(product_list))))

        if index <= len(product_list):
            product_list.insert(index, new_product)
            print('Inserted Successful!')
        
        else:
            print('Out of range! Please try again [0-{}]: '.format(len(product_list)))

        
    def update_product(self):

        count = 0 
        key = input('Please enter product ID: ')

        for i in product_list:

            if key in i:
                update_option = int(input('Update Options:\n1: ID\n2: Name\n3: Price\n4: Category\n5: Exit\nChoose: '))
                if update_option == 1:
                    update_value = input('Please enter new ID: ')
                    product_list[count][0] = update_value
                    print('Update Successful!')
                    break

                if update_option == 2:
                    update_value = input('Please enter new Name: ')
                    product_list[count][1] = update_value
                    print('Update Successful!')
                    break

                if update_option == 3:
                    update_value = input('Please enter new Price: ')
                    product_list[count][2] = update_value
                    print('Update Successful!')
                    break

                if update_option == 4:
                    update_value = input('Please enter new Category: ')
                    product_list[count][3] = update_value
                    print('Update Successful!')
                    break

                if update_option == 5:
                    print('Exit Program!')
                    break
            count += 1
        else:
            print('Product not found! Please try again')

    def delete_product(self):
        
        count = 0
        key = input('Please enter product ID: ')

        for i in product_list:

            if key in i:
                product_list.pop(count)
                print('Deleted Successful!')
                break
                
            count += 1
        
        else:
            print('Product does not exist! Please try again')

    def search_product(self):

        count = 0 
        key = input('Please enter product ID: ')
        
        for i in product_list:
            
            if key in i:
                print(f'Product {count}: {i[0]}, {i[1]}, {i[2]}, {i[3]}')
                print('Product Found!')
                break

            count += 1

        else:
            print('Product does not exist! Please try again')

def bubble_sort(array):
    length = len(array)

    if length == 1:
        return array

    elif length > 1:
        for i in range(len(array)):
            swapped = False
            for j in range(len(array) - i - 1):
                if float(array[j][2]) > float(array[j+1][2]):
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                    swapped = True
            if not swapped:
                break

    else: 
        print('Empty list!')
        
def analyzeSortPerformance(data, description, time_complexity):
    print(f'\n{description} - Starting array: {data}')
    start = time.time()
    bubble_sort(data)
    end = time.time()
    space_complexity = sys.getsizeof(data) + sys.getsizeof(start) + sys.getsizeof(end) + 64
    print(f'{description} - Time taken: {end - start:.8f} seconds, Space used: {space_complexity} bytes')
    print(f'Time Complexity: {time_complexity}\n')


if __name__ == '__main__':
    
    product_list = []
    with open('product_data.txt', 'r') as f1:
        for line in f1:
            product_data = line.strip().split(', ')
            product_list.append(product_data)

    product = ProductManager()

    while True:
        try:

            choice = int(input('Options:\n1: Load Product\n2: Insert Product\n3: Update Product\n4: Delete Product\n5: Search Product\n6. Bubble Sort \n7. Complexity Analysis Report\n8: Exit\nChoose: '))

            print('---------------------------------------------------------------------------------------------')

            if choice == 1:
                product.load_product()

            elif choice == 2:
                product.insert_product()

            elif choice == 3:
                product.update_product()

            elif choice == 4:
                product.delete_product()

            elif choice == 5:
                product.search_product()

            elif choice == 6:
                bubble_sort(product_list)
                product.load_product()

            elif choice == 7:

                product_list_sorted = []
                with open('product_data_sorted.txt', 'r') as f2:
                    for line in f2:
                        product_data_sorted = line.strip().split(', ')
                        product_list_sorted.append(product_data_sorted)


                product_list_reversed = []
                with open('product_data_reversed.txt', 'r') as f:
                    for line in f:
                        product_data_reversed = line.strip().split(', ')
                        product_list_reversed.append(product_data_reversed)
                        
                analyzeSortPerformance(product_list, 'Original Data', "O(n^2)")
                analyzeSortPerformance(product_list_sorted, 'Best Case (Sorted)', 'O(n)')
                analyzeSortPerformance(product_list_reversed, 'Worst Case (Reverse Sorted)', 'O(n^2)')
                        
            elif choice == 8:
                print('Exit Program!')
                break
            
            else:
                print('Option does not exist! Please choose again.')
            
            print('---------------------------------------------------------------------------------------------')
        except TypeError:
            print('Invalid Input!')
