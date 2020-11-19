

def get_marks():

    percent_to_get = [90, 85, 80, 77, 73, 70, 67]

    original_ask = input("How many entry marks do you have")
    weight_taken= 0
    weight_lost = 0
    for i in range (0, int(original_ask)):
        weight = input("What was the weight of this entry (please enter answer like 20 if its worth 20%)")  
        weight_taken += int(weight)
        percentage = input("What percentage did you get? (0-100)")
        realpercentage = int(percentage)/100
        weight_lost += int(weight)*(1-realpercentage)
    exam_weight = int(input("What is the weight of your final exam? (please enter answer like 20 if its worth 20%)"))
    if (exam_weight + weight_taken != 100):
        print ("Your weight completed so far plus your exam weight does not add up to 100")
        print ("To complete this calculation, we will assume you score the same on all remaining grades as you have so far this semester")
    current_percentage = (weight_taken - weight_lost)/weight_taken
    print ("Your current percentage going into exam is ", current_percentage*100, "%")
    ratio_to_scale = (100 - exam_weight)/weight_taken
    real_weight_lost = ratio_to_scale*weight_lost
    print ("To finish the course with a 12 you would need",  (exam_weight - ((100 - minimum_12) - real_weight_lost))/exam_weight, "% on your final exam")
    print ("To finish the course with a 11 you would need",  (exam_weight - ((100 - minimum_11) - real_weight_lost))/exam_weight, "% on your final exam")        
     
get_marks()