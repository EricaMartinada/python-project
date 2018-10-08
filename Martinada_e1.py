# filename  : Martinada_e1.py
#author     : Erica Martinada
# description :  this is a python program
#                that prints the contents 
#                of a dictionary in a specific 
#                format 

message = "I am {}.\n" + \
        "My spirit animal is {},\n" + \
        "because {}.\n" + \
        "When not in school, I love {}.\n" + \
        "I dream of being an {} in the future"

data = {        "name":"Erica Martinada",\
                "Spirit Animal":"Dragon", \
                "Reason": "Idunno" ,\
                "Hobby":"Watching", \
                "Profession":"Engineer"
                }

print (message.format ( \
    data ["name"], \
    data ["Spirit Animal"], \
    data ["Reason"], \
    data ["Hobby"], \
    data ["Profession"], \
    ))