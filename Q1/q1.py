import csv

def main():
    f= open("2022_Seoul_Temp.csv", 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')

    header = next(data)

    averagetem =[0.0 ,0.0, 0.0]


    flag = 0

    for row in data:
            
        for i in range(0,3):
            if(row[i+2] == ''):
                flag -= 1
                row[2] = 0
                row[3]=0
                row[4] =0
            averagetem[i]+= float(row[i+2])
        flag += 1
    
    for i in range(0,3):
        averagetem[i] /= flag
    
    print("Average Temperature : " + str( round(averagetem[0],2)) + " Celsius" )
    print("Average Minimum Temperature : " + str( round(averagetem[1],2)) + " Celsius" )
    print("Average Maximu Temperature : " + str( round(averagetem[2],2)) + " Celsius" )
    
    
if __name__ == '__main__':
    main()
