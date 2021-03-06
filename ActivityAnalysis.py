# Creating dictionaries according to the type of activity being performed
# The key will be the activity and the value will be the estimation of calories burned for an individual below 65kg
# Source:https://www.health.harvard.edu/diet-and-weight-loss/calories-burned-in-30-minutes-of-leisure-and-routine-activities

gymActivities = {
    "Weight Lifting: general": 90,
    "Aerobics: water": 	120,
    "Stretching, Hatha Yoga": 120,
    "Calisthenics: moderate": 135,
    "Riders: general": 	150,
    "Aerobics: low impact": 165,
    "Stair Step Machine: general": 180,
    "Teaching aerobics": 180,
    "Weight Lifting: vigorous": 180,
    "Aerobics, Step: low impact": 210,
    "Aerobics: high impact": 210,
    "Bicycling, Stationary: moderate": 210,
    "Rowing, Stationary: moderate": 210,
    "Calisthenics: vigorous": 	240,
    "Circuit Training: general": 	240,
    "Rowing, Stationary: vigorous": 255,
    "Elliptical Trainer: general": 270,
    "Ski Machine: general": 285,
    "Aerobics, Step: high impact": 300,
    "Bicycling, Stationary: vigorous": 315
}

trainingAndSport = {
    "Billiards": 75,
    "Bowling": 90,
    "Dancing: slow, waltz, foxtrot": 90,
    "Frisbee": 90,
    "Volleyball: non-competitive, general play": 90,
    "Water Volleyball": 90,
    "Archery: non-hunting": 105,
    "Golf: using cart": 105,
    "Hang Gliding": 105,
    "Curling": 120,
    "Gymnastics: general": 120,
    "Horseback Riding: general": 120,
    "Tai Chi": 120,
    "Volleyball: competitive, gymnasium play": 120,
    "Walking: 3.5 mph (17 min/mi)": 120,
    "Badminton: general": 135,
    "Walking: 4 mph (15 min/mi)": 135,
    "Kayaking": 150,
    "Skateboarding": 150,
    "Snorkeling": 	150,
    "Softball: general play": 	150,
    "Walking: 4.5 mph (13 min/mi)": 150,
    "Whitewater: rafting, kayaking": 150,
    "Dancing: disco, ballroom, square": 165,
    "Golf: carrying clubs": 165,
    "Dancing: Fast, ballet, twist": 180,
    "Fencing": 180,
    "Hiking: cross-country": 180,
    "Skiing: downhill": 180,
    "Swimming: general": 180,
    "Walk/Jog: jog <10 min.": 180,
    "Water Skiing": 180,
    "Wrestling": 180,
    "Basketball: wheelchair": 195,
    "Race Walking": 195,
    "Ice Skating: general": 210,
    "Racquetball: casual, general": 210,
    "Rollerblade Skating": 210,
    "Scuba or skin diving": 210,
    "Sledding, luge, toboggan": 210,
    "Soccer: general": 210,
    "Tennis: general": 210,
    "Basketball: playing a game": 240,
    "Bicycling: 12-13.9 mph": 	240,
    "Football: touch, flag, general": 240,
    "Hockey: field & ice": 240,
    "Rock Climbing: rappelling": 240,
    "Running: 5 mph (12 min/mile)": 240,
    "Running: pushing wheelchair, marathon wheeling": 240,
    "Skiing: cross-country": 240,
    "Snow Shoeing": 240,
    "Swimming: backstroke": 240,
    "Volleyball: beach": 240,
    "Bicycling: BMX or mountain": 255,
    "Boxing: sparring": 270,
    "Football: competitive": 270,
    "Orienteering": 270,
    "Running: 5.2 mph (11.5 min/mile)": 270,
    "Running: cross-country": 270,
    "Bicycling: 14-15.9 mph": 	300,
    "Martial Arts: judo, karate, kickbox": 300,
    "Racquetball: competitive": 300,
    "Rope Jumping": 300,
    "Running: 6 mph (10 min/mile)": 300,
    "Swimming: breaststroke": 	300,
    "Swimming: laps, vigorous": 300,
    "Swimming: treading, vigorous": 300,
    "Water Polo": 300,
    "Rock Climbing: ascending": 330,
    "Running: 6.7 mph (9 min/mile)": 330,
    "Swimming: butterfly": 330,
    "Swimming: crawl": 330,
    "Bicycling: 16-19 mph": 360,
    "Handball: general": 360,
    "Running: 7.5 mph (8 min/mile)": 375,
    "Running: 8.6 mph (7 min/mile)": 435,
    "Bicycling: > 20 mph": 495,
    "Running: 10 mph (6 min/mile)": 495
}


outdoorActivities = {
    "Planting seedlings, shrubs": 120,
    "Raking Lawn": 	120,
    "Sacking grass or leaves": 	120,
    "Gardening: general": 135,
    "Mowing Lawn: push, power": 135,
    "Operate Snow Blower: walking": 135,
    "Plant trees": 135,
    "Gardening: weeding": 139,
    "Carrying & stacking wood": 150,
    "Digging, spading dirt": 150,
    "Laying sod / crushed rock": 150,
    "Mowing Lawn: push, hand": 165,
    "Chopping & splitting wood": 180,
    "Shoveling Snow: by hand": 180
}

homeAndDailyActivities = {
    "Sleeping": 19,
    "Watching TV": 	23,
    "Reading: sitting": 34,
    "Standing in line": 38,
    "Cooking": 	75,
    "Child-care: bathing, feeding, etc.": 	105,
    "Food Shopping: with cart": 105,
    "Moving: unpacking": 105,
    "Playing w/kids: moderate effort": 120,
    "Heavy Cleaning: wash car, windows": 135,
    "Child games: hop-scotch, jacks, etc.": 150,
    "Playing w/kids: vigorous effort": 150,
    "Moving: household furniture": 	180,
    "Moving: carrying boxes": 	210

}


homeRepairActivities = {
    "Auto Repair": 	90,
    "Wiring and Plumbing": 90,
    "Carpentry: refinish furniture": 135,
    "Lay or remove carpet/tile": 135,
    "Paint, paper, remodel: inside": 135,
    "Cleaning rain gutters": 50,
    "Hanging storm windows": 150,
    "Paint house: outside": 150,
    "Carpentry: outside": 180,
    "Roofing": 180
}


occupationalActivities = {
    "Computer Work": 41,
    "Light Office Work": 45,
    "Sitting in Meetings": 49,
    "Desk Work": 53,
    "Sitting in Class": 53,
    "Truck Driving: sitting": 60,
    "Bartending/Server": 75,
    "Heavy Equip. Operator": 75,
    "Police Officer": 75,
    "Theater Work": 90,
    "Welding": 	90,
    "Carpentry Work": 105,
    "Coaching Sports": 	120,
    "Masseur, standing": 120,
    "Construction, general": 165,
    "Coal Mining": 	180,
    "Horse Grooming": 180,
    "Masonry": 	210,
    "Forestry, general": 240,
    "Heavy Tools, not power": 240,
    "Steel Mill: general": 	240,
    "Firefighting": 360
}

# Function which prints out the activity details(based on the indexing) that user has logged in
def printWorkout(chosenActivities, activityCalories):
    if len(chosenActivities) == 0:
        print("No activities chosen")
    for activity in chosenActivities:
        if activity < 100:
            print("\nGym Activities:")
            time = chosenActivities[activity]
            act = list(gymActivities)[activity]
            print(act, ", time engaged:", time, " minutes"
                  ", calories burned:", int(gymActivities[act] * (time/30) ))
            activityCalories += (gymActivities[act] * (time/30))

        elif activity < 200:
            print("\nTraining And Sport:")
            time = chosenActivities[activity]
            act = list(trainingAndSport)[activity-100]
            print(act, ", time engaged:", time, " minutes"
                  ", calories burned:", int(trainingAndSport[act] * (time / 30)))
            activityCalories += (trainingAndSport[act] * (time / 30))

        elif activity < 300:
            print("\nOutdoor Activities:")
            time = chosenActivities[activity]
            act = list(outdoorActivities)[activity-200]
            print(act, ", time engaged:", time, " minutes"
                  ", calories burned:", int(outdoorActivities[act] * (time / 30)))
            activityCalories += (outdoorActivities[act] * (time / 30))

        elif activity < 400:
            print("\nHome And Daily Activities:")
            time = chosenActivities[activity]
            act = list(homeAndDailyActivities)[activity-300]
            print(act, ", time engaged:", time, " minutes"
                  ", calories burned:", int(homeAndDailyActivities[act] * (time / 30)))
            activityCalories += (homeAndDailyActivities[act] * (time / 30))

        elif activity < 500:
            print("\nHome Repair Activities:")
            time = chosenActivities[activity]
            act = list(homeRepairActivities)[activity-400]
            print(act, ", time engaged:", time, " minutes"
                  ", calories burned:", int(homeRepairActivities[act] * (time / 30)))
            activityCalories += (homeRepairActivities[act] * (time / 30))

        elif activity < 600:
            print("\nOccupational Activities:")
            time = chosenActivities[activity]
            act = list(occupationalActivities)[activity-500]

            print(act, ", time engaged:", time, " minutes"
                  ", calories burned:", int(occupationalActivities[act] * (time / 30)))
            activityCalories += (occupationalActivities[act] * (time / 30))

    return activityCalories

