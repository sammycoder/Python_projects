if __name__ =="__main__":
    
    #declaring the list
    my_list = ['Hawaiian', 'Margherita', 'Mushroom', 'Prosciutto', 'Meat Feast', 'Hawaiian', 'Bacon', 'Black Olive Special', 'Sausage', 'Sausage']

    #a variable that hold the python in built function to remove duplicate from a list
    new_list= list(dict.fromkeys(my_list))

    print(new_list)