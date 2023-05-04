import csv

def main():
    f= open("2022_Seoul_Temp.csv", 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')

    header = next(data)

    Difftem =[0.0 ,90.0]

    maxday = ''
    minday = ''


    for row in data:
        for i in range(0,3):
            if(row[i+2] == ''):
                row[0] = ''
                row[1] = ''
                row[2] = 0
                row[3]=0
                row[4] =0
    
        if(float(row[4])- float(row[3]) >= Difftem[0]):
            maxday = row[0]
            Difftem[0] = float(row[4])- float(row[3])
        elif (float(row[4])- float(row[3]) <= Difftem[1] and float(row[4])- float(row[3]) != 0 ):
            minday = row[0]
            Difftem[1] = float(row[4])- float(row[3])


    print("Day with the Largest Temperature Variation : " + maxday)
    print("Maximum Temperature Difference : " + str(Difftem[0])  + "Celsius")

    print("Day with the Smallest Temperature Variation : " + minday)
    print("Minimum Temperature Difference : " + str(round(Difftem[1], 1))  + "Celsius")
    
    
if __name__ == '__main__':
    main()
