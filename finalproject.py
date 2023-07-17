#! usr/bin/env python3

#The goal of my project is to create a tool intended to be used by Little League coaches to track pitches thrown by their players to promote player safety.



#pitch_stats = [{'pitcher': {'name': 'jackson', 'num_pitches': 45}}]

#pitcher name

#number of pitches


#pitches = {'name': 'jackson', 'num_pitches': 45}

#name = input('pitcher.')
#throws = input('Enter number of pitches. ')
#pitches['name'] = name
#pitches['num_pitches'] = throws
#print(pitches)

#Initial prompt

answer = input("Hey Coach Aaron, Welcome Back!!!  Are you here to log pitches for your Minor or Major league team today? ")
if answer.lower().strip() == "minor":
    answer = input("Great! I hope the Cardinals had a good game and everyone had fun, tried their hardest, and played well. Who was your starting pitcher today? ")

    if answer.lower().strip() == "jackson" or "harrison" or "levi" or "sam":
         answer = input("Nice!  Hopefully he brought his A game today.  How many pitches did he throw? ")

#how can i take the answer from who pitched and input the pitchers name into the following statements instead of using "he"
    if answer <= "60":
        answer = input("Perfect, he will be available to pitch in your next game. Did another player make a pitching apperance ? ")

    elif answer > "60":
        input("He threw over 60 pitches and may be unavailable to pitch later this week. How many days until your next game? ")

        if answer >= "3":
            answer = input("Great, with enough rest and stretching as long as he feels fine, he will be available to pitch in your next game.  Did another pitcher make a pitching appearnce? ")

        elif answer < "3":
            answer = input("He will be unavaiable to pitch until having adequate rest.  Did another player make a pitching apperance ? ")

            if answer == "yes":
                answer = input ("Ok, who came in to relieve to the starting pitcher? ")

                if answer.lower().strip() == "jackson" or "harrison" or "levi" or "sam":
                    answer = input("Nice!  Hopefully he brought his A game today.  How many pitches did he throw? ")
 
                    if answer <= "60":
                        answer = input("Perfect, he will be available to pitch in your next game. ")              

                    elif answer > "60":
                        input("He threw over 60 pitches and may be unavailable to pitch later this week. How many days until your next game? ")

                        if answer >= "3":
                            answer = input("Great, with enough rest and stretching, he will be available to pitch in your next game.  Did another pitcher make a pitching appearnce? ")

                        elif answer < "3":
                            answer = input("He will be unavaiable to pitch until having adequate rest.  Did another player make a pitching apperance ? ")

                            if answer == "yes":
                                answer = input ("Ok, who came in to close out the game? ")

                                if answer.lower().strip() == "jackson" or "harrison" or "levi" or "sam":
                                    answer = input("Nice!  Hopefully he brought his A game today.  How many pitches did he throw? ")

                                    if answer <= "60":
                                        answer = input("Perfect, he will be available to pitch in your next game. ")
                                                
                                    elif answer > "60":
                                        input("He threw over 60 pitches and may be unavailable to pitch later this week. How many days until your next game? ")

                                        if answer >= "3":
                                            answer = input("Great, with enough rest and stretching, he will be available to pitch in your next game.  Did another player make a pitching appearnce? ")

                                        elif answer < "3":
                                            answer = input("He will be unavaiable to pitch until having adequate rest.  Did another player make a pitching apperance ? ")

                                            if answer == "yes":
                                                answer = input ("Ok, who came in to close out the game? ")

                                                if answer.lower().strip() == "jackson" or "harrison" or "levi" or "sam":
                                                    answer = input("Nice!  Hopefully he brought his A game today.  How many pitches did he throw? ")

                                                    if answer <= "60":
                                                        answer = input("Perfect, he will be available to pitch in your next game. ")
                                                                
                                                    elif answer > "60":
                                                        input("He threw over 60 pitches and may be unavailable to pitch later this week. How many days until your next game? ")

                                                        if answer >= "3":
                                                            answer = input("Great, with enough rest and stretching, he will be available to pitch in your next game.  Did another player make a pitching appearnce? ")

                                                        elif answer < "3":
                                                            answer = input("He will be unavaiable to pitch until having adequate rest.  Did another player make a pitching apperance ? ")

elif answer.lower().strip() == "major":
    answer = input("Great!  I hope the Rockies had a good game and everyone played well.  Who was your starting pitcher today? ")

    if answer.lower().strip() == "zack" or "adam" or "miles" or "caleb":
           answer = input("Nice!  Hopefully he brought his A game today.  How many pitches did he throw? ")

#how can i take the answer from who pitched and input the pitchers name into the following statements instead of using "he"
    if answer <= "75":
        answer = input("Perfect, he will be available to pitch in your next game. Did another player make a pitching apperance ? ")

    elif answer > "75":
        input("He threw over 75 pitches and may be unavailable to pitch later this week. How many days until your next game? ")

        if answer >= "3":
            answer = input("Great, with enough rest and stretching as long as he feels fine, he will be available to pitch in your next game.  Did another pitcher make a pitching appearnce? ")

        elif answer < "3":
            answer = input("He will be unavaiable to pitch until having adequate rest.  Did another player make a pitching apperance ? ")

            if answer == "yes":
                answer = input ("Ok, who came in to relieve to the starting pitcher? ")

                if answer.lower().strip() == "zack" or "adam" or "miles" or "caleb":
                    answer = input("Nice!  Hopefully he brought his A game today.  How many pitches did he throw? ")
 
                    if answer <= "75":
                        answer = input("Perfect, he will be available to pitch in your next game. ")              

                    elif answer > "75":
                        input("He threw over 75 pitches and may be unavailable to pitch later this week. How many days until your next game? ")

                        if answer >= "3":
                            answer = input("Great, with enough rest and stretching, he will be available to pitch in your next game.  Did another pitcher make a pitching appearnce? ")

                        elif answer < "3":
                            answer = input("He will be unavaiable to pitch until having adequate rest.  Did another player make a pitching apperance ? ")

                            if answer == "yes":
                                answer = input ("Ok, who came in to close out the game? ")

                                if answer.lower().strip() == "zack" or "adam" or "miles" or "caleb":
                                    answer = input("Nice!  Hopefully he brought his A game today.  How many pitches did he throw? ")

                                    if answer <= "75":
                                        answer = input("Perfect, he will be available to pitch in your next game. ")
                                                
                                    elif answer > "75":
                                        input("He threw over 75 pitches and may be unavailable to pitch later this week. How many days until your next game? ")

                                        if answer >= "3":
                                            answer = input("Great, with enough rest and stretching, he will be available to pitch in your next game.  Did another player make a pitching appearnce? ")

                                        elif answer < "3":
                                            answer = input("He will be unavaiable to pitch until having adequate rest.  Did another player make a pitching apperance ? ")

                                            if answer == "yes":
                                                answer = input ("Ok, who came in to close out the game? ")

                                                if answer.lower().strip() == "zack" or "adam" or "miles" or "caleb":
                                                    answer = input("Nice!  Hopefully he brought his A game today.  How many pitches did he throw? ")

                                                    if answer <= "75":
                                                        answer = input("Perfect, he will be available to pitch in your next game. ")
                                                                
                                                    elif answer > "75":
                                                        input("He threw over 75 pitches and may be unavailable to pitch later this week. How many days until your next game? ")

                                                        if answer >= "3":
                                                            answer = input("Great, with enough rest and stretching, he will be available to pitch in your next game.  Did another player make a pitching appearnce? ")

                                                        elif answer < "3":
                                                            answer = input("He will be unavaiable to pitch until having adequate rest.  Did another player make a pitching apperance ? ")




#else answer.lower().strip() != minor or major:
#maj        print("No valid input!")

#log number of pitches for starting pitcher
#who relieved starting pitcher.  how many pitches
#who closed out the game.  how many pitches
#ask how many days until next game.  if number of days <3 and a player threw >45 pitches, they are inelgible to pitch next game


#Major League Team- Rockies
#possible pitchers for Rockies- Zack, Adam, Miles, Caleb
#starting pitcher
#relieving pitcher
#closing pitcher
#ask how many days until next game.  if number of days <3 and a player threw >60 pitches, they are ineligible to pitch next game.  






    #print("That's too bad.  We can only assist with pitch counts."