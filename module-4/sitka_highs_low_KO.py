import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = r"C:\Users\Kimy\csd\csd-325\module-4\sitka_weather_2018_simple.csv" #I was having trouble here, it wouldn't recognize the filename. :(

dates, highs, lows = [], [], [] #Added lows, []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            date = datetime.strptime(row[2], '%m/%d/%Y') #I kept getting an error here and I found out the order of this needed to be switched.
            high = int(row[5])
            low = int(row[6]) #added low
        except Exception as e: #Right here it made it so if there was any line error, because I got them a lot, I just added this continue. It like skips the error and keeps going. It became too tedious U_U So I am leaving it here. 
            continue
        dates.append(date)
        highs.append(high)
        lows.append(low)
#This is the Menu loop, Where I added the L and Q, for the Low Temp and the Quit option.
while True:
    print("H - Show High Temps")
    print("L - Show Low Temps")
    print("Q - Exit")
    choice = input("Pick H, L, or Q: ").upper()
#This part I changed completely, since we added choice there needed to be an if thingy here. 
    if choice == 'H':
        plt.plot(dates, highs, color='red')
        plt.title("High Temps - 2018")
        plt.show()
    elif choice == 'L':
        plt.plot(dates, lows, color='blue')
        plt.title("Low Temps - 2018")
        plt.show()
    elif choice == 'Q':
        print("Thanks a bunches, Bye Bye!")
        break #I didnt include sys because when I did, it wouldn't work anymore U_U 
    else:
        print("Not a valid input. Please, try again.")