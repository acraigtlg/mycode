

#empty dictionary to enter name and num_pitches

pitcher_stats = {}

 

#prompt for number of pitcher stats

num_pitchers = int(input("How many pitchers stats do you need to enter? "))

 

#loop throw number of pitcher stats, enter name and pitches, and save

for i in range(num_pitchers):

    name = input("Enter pitcher's name: ")

    num_pitches = input("Enter number of pitches thrown: ")

    pitcher_stats[name] = num_pitches

 

#print filled dictionary

print(pitcher_stats)
