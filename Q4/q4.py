import csv

def main ():
    f= open("202303_Seoul_Subway.csv", 'r', encoding='utf-8')
    data = csv.reader(f, delimiter=',')

    header = next(data)
    print(header)

    Line1  = [0, "", 9999990 , ""]
    Line2  = [0, "", 9999990 , ""]
    Line3  = [0, "", 9999990 , ""]
    Line4  = [0, "", 9999990 , ""]

    for row in data: 
        if (int(row[1][0]) == 1):
            if(int(row[4])+int(row[5]) > Line1[0]):
                Line1[0] =  int(row[4])+int(row[5])
                Line1[1] = row[3]
            elif(int(row[4])+int(row[5]) < Line1[2]):
                Line1[2] =  int(row[4])+int(row[5])
                Line1[3] = row[3]
        if (int(row[1][0]) == 2):
            if(int(row[4])+int(row[5]) > Line2[0]):
                Line2[0] =  int(row[4])+int(row[5])
                Line2[1] = row[3]
            elif(int(row[4])+int(row[5]) < Line2[2]):
                Line2[2] =  int(row[4])+int(row[5])
                Line2[3] = row[3]
        if (int(row[1][0]) == 3):
            if(int(row[4])+int(row[5]) > Line3[0]):
                Line3[0] =  int(row[4])+int(row[5])
                Line3[1] = row[3]
            elif(int(row[4])+int(row[5]) < Line3[2]):
                Line3[2] =  int(row[4])+int(row[5])
                Line3[3] = row[3]
        if (int(row[1][0]) == 4):
            if(int(row[4])+int(row[5]) > Line4[0]):
                Line4[0] =  int(row[4])+int(row[5])
                Line4[1] = row[3]
            elif(int(row[4])+int(row[5]) < Line4[2]):
                Line4[2] =  int(row[4])+int(row[5])
                Line4[3] = row[3]    


    print("Line 1:")
    print("Busiest Station :" + str(Line1[1]) + " (" + str(Line1[0]) +")")
    print("Least used Station :" + str(Line1[3]) + " (" + str(Line1[2])+")")
    print("Line 2:")
    print("Busiest Station :" + str(Line2[1]) + " (" + str(Line2[0])+")")
    print("Least used Station :" + str(Line2[3]) + " " + str(Line2[2])+")")
    print("Line 3:")
    print("Busiest Station :" + str(Line3[1]) + " (" + str(Line3[0])+")")
    print("Least used Station :" + str(Line3[3]) + " (" + str(Line3[2])+")")
    print("Line 4:")
    print("Busiest Station :" + str(Line4[1]) + " (" + str(Line4[0])+")")
    print("Least used Station :" + str(Line4[3]) + " (" + str(Line4[2])+")")
    

if __name__ == '__main__':
    main()
