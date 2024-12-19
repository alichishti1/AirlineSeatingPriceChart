import random
ROW_NUMBER = 6
COLUMN_NUMBER = 4


def display_title():

    print()
    print('Seating-Price Chart Program in Python')
    print()
    print('Created by: Muhammad Chishti')
    print('Created at: 11-01-2021')
    print('Description: The program is designed to')
    print('1 - Create an airplane seating-price chart')
    print('2 - Display the seating-price chart')
    print('3 - Find and display the highest seat-price')
    print('4 - Find and display the lowest seat-price')
    print('5 - Calculate the average price')
    print('6 - Find ALL seats (row and column) that have the lowest Price')
    print('7 - Find ALL seats (row and column) that have the highest Price')
    print('8 - Find a seat (row and column) based on the price entered by users - \
          (Extra Point: 5 points')
    print()


def create_seating_price_chart(row_number, col_number):

    # initialize a list to hold the seat-price chart
    chart_2d = []
    for row in range(row_number):
        row_list = []
        for col in range(col_number):
            seat_price = random.randint(500, 1000)
            row_list.append(seat_price)
        chart_2d.append(row_list)
    return chart_2d


def display_seating_price_chart(chart_2d):

    print()
    print('---------Display Seating Price Chart---------')
    print(f'There are {len(chart_2d)} rows and {len(chart_2d[0])} \
          columns in the plane')
    print()
    for i in range(len(chart_2d)):
        print(chart_2d[i])
    print('---------------------------------------------')


def find_max_value(chart_2d):

    row_number = len(chart_2d)
    column_number = len(chart_2d[0])
    the_max = chart_2d[0][0]
    maxs = []
    for i in range(row_number):
        for j in range(column_number):
            if chart_2d[i][j] == the_max:
                maxs.append([i+1, j+1])
            if chart_2d[i][j] > the_max:
                maxs = [i+1, j+1]
                the_max = chart_2d[i][j]
    return the_max, maxs


def find_min_value(chart_2d):

    row_number = len(chart_2d)
    column_number = len(chart_2d[0])
    the_min = chart_2d[0][0]
    mins = []
    for i in range(row_number):
        for j in range(column_number):
            if chart_2d[i][j] == the_min:
                mins.append([i+1, j+1])
            if chart_2d[i][j] < the_min:
                mins = [i+1, j+1]
                the_min = chart_2d[i][j]

    return the_min, mins


def calculate_average_price(chart_2d):

    total = 0
    row_number = len(chart_2d)
    column_number = len(chart_2d[0])
    for i in range(row_number):
        for j in range(column_number):
            total += chart_2d[i][j]
    average = total / (row_number * column_number)
    return average


def find_seats_with_price(chart_2d, price):

    row_number = len(chart_2d)
    column_number = len(chart_2d[0])
    founds = []
    for i in range(row_number):
        for j in range(column_number):
            if chart_2d[i][j] == price:
                founds.append([i+1, j+1])
    return founds


if __name__ == '__main__':
    # display the title
    display_title()

    # create and display the seating-price chart
    chart_2D = create_seating_price_chart(ROW_NUMBER, COLUMN_NUMBER)
    display_seating_price_chart(chart_2D)

    # find the highest price
    highest_price, maxs = find_max_value(chart_2D)
    print(f'The highest price is ${highest_price}')

    # find the lowest price
    lowest_price, mins = find_min_value(chart_2D)
    print(f'The lowest price is ${lowest_price}')

    # find the average price
    average_price = calculate_average_price(chart_2D)
    print(f'The average price is ${average_price}')

    print()
    print('-----------Display the seat list(s) with lowest price---------')
    print(mins)

    print()
    print('-----------Display the seat list(s) with highest price---------')
    print(maxs)

    print()
    price = int(input('Please enter a price between 500 and 1000: '))
    while price < 500 or price > 1000:
        print('Please enter a valic number (between 500 and 1000)')
        price = int(input('Please enter a price between 500 and 1000: '))

    founds = find_seats_with_price(chart_2D, price)
    if founds == []:
        print(f'Cannot find a seat with the price {price}')
    else:
        print('------Display seat list with entered price-------')
        print(founds)

    print()
    print('Process finished with exit code 0')
