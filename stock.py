
def stock():
    in_stock={
    "grocerries" : ["apple","banana","rice","milk","bread"],
    "toiletries" : ['tissue','toothbrush','toothpaste'],
    "stationery" : ['pen','copy'],
    "clothes"    : ['tshirt','pant','jacket']
}

stock()

def add_stock():
    yes_no=input('do you want to add other products?')

    if yes_no=="yes":
        print('Proceeding to add products!')
add_stock()
