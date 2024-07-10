import json 
import sys 

english_wolof= {}
file_names = sys.argv[1:] 

for file in file_names : 
    with open(file,"r") as f:
        try :
            sub_data = json.load(f)
            english_wolof.update(sub_data)
            f.close()
        except Exception as e : 
            print(f"{file} : {e}")
            exit()

with open("pair_english_wolof.json", "w") as file:
    json.dump(english_wolof,file)
    file.close()

english_wolof_format = []

english_wolof = list(english_wolof.items())

for pair in english_wolof:
    english_wolof_format.append({"en": pair[0], "wo" : pair[1]})


with open("english_wolof_huggingface_dataset_format.json", "a") as file : 
    json.dump(english_wolof_format,file)




 
