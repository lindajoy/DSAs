"""
 Compute the cost to make the recipe based on ingredients cost
# Example: 
# computeCost(["bread","meat","bread"], [("bread",1),("meat",2)]) => 4

"""
 
costs = [["bread",1], ["tomatoes",2], ["cheese",4], ["meat",5] ] 
  
burger = [ "bread","meat","cheese","tomatoes","bread"]

def totalCostOfIngredients(cost, recipe):
    dict_costs = dict(cost) # Convert the costs list to a dictionary

    total_cost = 0 # Initialize the total cost to zero.
    
    for i in recipe:
        if i in dict_costs:
            total_cost += dict_costs[i]
    return total_cost
        


print(totalCostOfIngredients(costs,burger))