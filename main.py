

def get_marks():

    original_ask = input("How many entry marks do you have")
    weight_earned = 0
    weight_lost = 0
    for i in range (0, int(original_ask)):
        weight = input("What was the weight of this entry (please enter answer like 20 if its worth 20%)")  
        percentage = input("What percentage did you get? (0-100)")
        realpercentage = int(percentage)/100
        weight_lost += int(weight)*(1-realpercentage)
    weight = input("What is the weight of your final exam? (please enter answer like 20 if its worth 20%)")  

    def get_final_marks_needed():
        
print (weight_lost)