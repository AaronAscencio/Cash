def minimum_number_of_coins(change):
    change = int(change*100)
    coins = [25,10,5,1]
    number_coins = 0
    for i in coins:
        if(change==0):
            break
        number_coins+=(change//i)
        change = change%i    
    print(number_coins,end='')
    return number_coins

if(__name__ == '__main__'):
    minimum_number_of_coins(0.41)