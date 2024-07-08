import json 
file_names= ["english_wolof_0.json", 
             "english_wolof_1.json",
             "english_wolof_2.json",
             "english_wolof_3.json",
             "english_wolof_4.json",
             "english_wolof_5.json"
             ]

english_wolof= {}


for file in file_names : 
    with open(file,"r") as f:
        sub_data = json.load(f)
        english_wolof.update(sub_data)
        f.close()

with open("english_wolof_total.json", "w") as file:
    json.dump(english_wolof,file)
    file.close()

english_wolof_format = []

english_wolof = list(english_wolof.items())

for pair in english_wolof:
    english_wolof_format.append({"en": pair[0], "wo" : pair[1]})


with open("english_wolof_formated.json", "a") as file : 
    json.dump(english_wolof_format,file)




 
