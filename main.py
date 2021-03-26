
import csv
import itertools
import pandas as pd


class userMarks:

    def __init__(self):
        self.totalList = []

        
    def clearText(self):  
        title = ['Serial', "Price"]       
        with open('markstoget.csv.csv', 'w') as csvFile:

            df = pd.DataFrame(columns = title)
            df.to_csv(csvFile, sep=',')

    def get_marks(self):
        percent_to_get = [90, 85, 80, 77, 73, 70, 67, 63, 60, 57, 53, 50]
        classCode = input("what class is this for")
        marktoGet = []
        examNeeded = []
        marktoGet.append("Final Grade")
        examNeeded.append("Exam Mark Needed")
        marktoGet.append(classCode)
        examNeeded.append(" ")

        original_ask = input("How many entry marks do you have")
        weight_taken= 0
        weight_lost = 0
        for i in range (0, int(original_ask)):
            weight = input("What was the weight of this entry (please enter answer like 20 if its worth 20%)")  
            weight_taken += float(weight)
            percentage = input("What percentage did you get? (0-100)")
            realpercentage = float(percentage)/100
            weight_lost += float(weight)*(1-realpercentage)
        exam_weight = float(input("What is the weight of your final exam? (please enter answer like 20 if its worth 20%)"))
        if (exam_weight + weight_taken != 100):
            print ("Your weight completed so far plus your exam weight does not add up to 100")
            print ("To complete this calculation, we will assume you score the same on all remaining grades as you have so far this semester")
        current_percentage = (weight_taken - weight_lost)/weight_taken
        marks_earned = weight_taken - weight_lost
        print ("Your current percentage going into exam is " + str(current_percentage*100) + "%")
        print ("marks you have earned so far " + str(marks_earned))
        if (marks_earned > 50):
            print("CONGRATS BROTHA YOU HAVE ALREADY PASSED THE COURSE")
        else:
            print("Sorry buad you need some more marks on exam to pass. guess you gotta show up")
        ratio_to_scale = (100 - exam_weight)/weight_taken

        real_weight_lost = ratio_to_scale*weight_lost

        for i in range (0, len(percent_to_get)):
            examMark = str(((exam_weight - ((100 - percent_to_get[i]) - real_weight_lost))/exam_weight)*100)
            marktoGet.append(str(12-i))
            examNeeded.append(examMark)

        self.totalList.append(marktoGet)
        self.totalList.append(examNeeded) 

    def getAllMarks(self, nummarks):
        for i in range (0, nummarks):
            self.get_marks()

    def printoption(self):
    

        with open('markstoget.csv', 'w') as csvFile:           
            wr = csv.writer(csvFile)
            #for element in self.totallist:
             #   for row in self.totallist[element]
             #       for column in row

            #for i in range (0, self.totallist.length):
           #     wr.writerow()
            export_data = itertools.zip_longest(*self.totalList)
            #wr.writerow(("List1", "List2"))
            wr.writerows(export_data)



user = userMarks()
#numofclasses = 2
numofclasses = int(input("How many entry marks do you have"))

user.getAllMarks(numofclasses)

user.printoption()