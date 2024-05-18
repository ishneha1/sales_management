def sales():
    print('You are welcome to this platform')
    a=eval(input('Do u want to buy anything? Type Yes or No:'))

    if a!='Yes' or 'No':
        print('Invalid.')

    if a=='No':
        print('Thank you!')
        exit

    if a=='Yes':
        b=eval(input('Select what u want to buy: 1.Apple 2.Banana 3.Rice 4.Milk 5.Bread'))
        c=eval(input('Enter quantity of the product:'))

    print('Please do visit again.')
    
sales()