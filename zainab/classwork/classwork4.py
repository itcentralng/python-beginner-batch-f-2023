#import random 

#statesandcapital = {"adamawa":"yola","bayelsa":"yanagoa","kaduna":"kaduna","kebbi":"birnin kebbi","kogi":"lokoja","kwara":"illorin","lagos":"ikeja"}
#1- open a dictionary and write down the names of the states and capital of any choice.
   

def primarycolours(colours):
    primary = ["red","green","blue"]
    matching_colours = []
    for colour in colours:
        if colour in primary:
            matching_colours.append(colour)
    return matching_colours

print(primarycolours(["red","brown","orange","green","pink","blue"]))
print(primarycolours(["purple","white","silver","black"]))