class Day:
    def __init__(self, dayOfWeek, activities, score):
        self.dayOfWeek = dayOfWeek
        self.activities = activities
        self.score = score

class Activity:
    def __init__(self,startTime, endTime, type): #Minutes
        self.startTime = startTime
        self.endTime = endTime
        self.totalTime = endTime-startTime
        self.type = type #0 = general, 1 = relax, 2 = work

days = [Day("Monday",[], 0),Day("Tuesday",[], 0),Day("Wednesday",[], 0)]

#Setting up already existing activities

#Monday
days[0].activities.append(Activity(0,60,0))
days[0].activities.append(Activity(90,135,0))
days[0].activities.append(Activity(180,240,0))

#Tuesday
days[1].activities.append(Activity(0,90,0))

#Wednesday
days[2].activities.append(Activity(0,90,0))
days[2].activities.append(Activity(135,180,0))

#We are considering that 2h of general is equally painful as 1h of work for this test, and relaxation affects nothing
difficultyDict = {
    0 : 1,
    1 : 0,
    2 : 2
}

def CalculateScore(day):
    #Score is a measure of how "difficult" a day is - higher is more difficult
    total = 0
    for activity in day.activities:
        total += activity.totalTime * difficultyDict[activity.type]
    
    return total

#For testing sake we are saying this i a 4h work day
homeworksToSort = [60, 20, 35] #60m hwk, 20m hwk and a 35m hwk

homeworksToSort.sort(reverse=True) #It is better to fit in the big homeworks first, and sort out the smaller homeworks after

for homeworkToSort in homeworksToSort:
    
    #Finding the day we should use
    easiestDay = None
    for day in days:
        day.score = CalculateScore(day)
        if(easiestDay == None) or (day.score < easiestDay.score):
            easiestDay = day
    
    #Finding a time we can do this activity
    foundTime = False


    validTimes = []
    for i in range(0,245, 5):
        validTimes.append(i)

    for activity in easiestDay.activities:
        for i in range(activity.startTime, activity.endTime, 5):
            validTimes.remove(i)

    for validTime in validTimes:
        if(foundTime):
            break
        
        validAttempt = True
        for i in range(validTime, validTime + homeworkToSort + 5, 5):
            if validAttempt and ((i in validTimes) == False):
                validAttempt = False
                break
        
        if(validAttempt):
            #We have found a time
            easiestDay.activities.append(Activity(validTime, validTime + homeworkToSort, 2))
            foundTime = True



#Displaying days
displayDict = {
    0 : "general work",
    1 : "relaxation",
    2 : "homework"
}
print("Timetable below")
for day in days:
    print(f"\n{day.dayOfWeek}:")  # Printing the day of the week
    if day.activities:  # Check if there are activities for the day
        for activity in day.activities:
            print(f"    I have {displayDict[activity.type]} from {activity.startTime} until {activity.endTime}")
    else:
        print("    No activities scheduled.")
