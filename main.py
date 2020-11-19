

def get_marks():

    minimum_12 = 90
    minimum_11 = 85
    minimum_10 = 80
    minimum_9 = 77
    minimum_8 = 73
    minimum_7 = 70   
    minimum_6 = 67
    original_ask = input("How many entry marks do you have")
    weight_taken= 0
    weight_lost = 0
    for i in range (0, int(original_ask)):
        weight = input("What was the weight of this entry (please enter answer like 20 if its worth 20%)")  
        weight_taken += int(weight)
        percentage = input("What percentage did you get? (0-100)")
        realpercentage = int(percentage)/100
        weight_lost += int(weight)*(1-realpercentage)
    exam_weight = input("What is the weight of your final exam? (please enter answer like 20 if its worth 20%)")  
    if (exam_weight + weight_taken != 100):
        print ("Your weight completed so far plus your exam weight does not add up to 100")
        print ("To complete this calculation, we will assume you score the same on all remaining grades as you have so far this semester")
    print ("Your current percentage going into exam is " + (weight_taken - weight_lost)/weight_taken)

    print ("To finish the course with a 12 you would need" +   + "% on your final exam")
        
     
print (weight_lost)