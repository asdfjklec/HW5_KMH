import csv

def main():
    f= open("202303_Seoul_Subway.csv", 'r', encoding='utf-8')
    data = csv.reader(f, delimiter=',')

    header = next(data)
    print(header)

    users = [0,0,0,0,0,0,0,0,0]

    for row in data:
        for x in range(1,10):
            if (int(row[1][0]) == x):
                users[x-1] += int(row[4]) + int(row[5])


    userslarge = [0,0,0,0,0,0,0,0,0]  

    for x in range(0,9):
        userslarge[x] = users[x]


    userslarge.sort()
    print(users)
    print(userslarge)

    for x in range(0,9):
        if( userslarge[8] == users[x]):
            print("1st Busiest Line : Line" + str(x+1) + " ("+str(userslarge[8])+ ")")


    for x in range(0,9):
        if( userslarge[7] == users[x]):
            print("2st Busiest Line : Line" + str(x+1) + " ("+str(userslarge[7])+ ")")

    for x in range(0,9):
        if( userslarge[0] == users[x]):
            print("1st Least used Line : Line" + str(x+1)+ " ("+str(userslarge[0])+ ")")


    for x in range(0,9):
        if( userslarge[1] == users[x]):
            print("2st Least used Line : Line" + str(x+1)+ " ("+str(userslarge[1])+ ")")


if __name__ == '__main__':
    main()
