def driver(data):
    months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06', 'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'} 
    name = data[2][:5].upper().ljust(5,'9')

    dec = data[3][-2]

    month = months[data[3][3:6]]
    if data[4] == "F":
        month = str(int(month[0])+5) + month[1]

    date = data[3][:2]

    year = data[3][-1]

    firstname = data[0][0].upper()

    if data[1] == "":
        secondname  ='9'
    else:
        secondname = data[1][0].upper()
    return name  + dec + month + date + year + firstname + secondname + "9AA"