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


change = -1
while(change<0):
    try:
        change = float(input("Change owed: "))
        if(change<0):
            continue
        minimum_number_of_coins(change)
    except Exception as e:
        change = -1