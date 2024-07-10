from deep_translator import GoogleTranslator 
from threading import Thread
import json
import numpy as np 
import sys 


english_dataset = None
english_wolof = {}

def upload_data_set(path):
    global english_dataset

    with open(path, "r") as file: 
        english_dataset = json.load(file)

def sub_dataset(dataset, divison): 
    return np.array_split(dataset, divison)

def translate(sentence):
    global english_wolof
    global english_dataset
    translation = GoogleTranslator(source='en', target='wo').translate(sentence)
    english_wolof[sentence] = translation
    print(f"{sentence} : {translation}")
    print(f"{round((len(english_wolof) / len(english_dataset)) * 100, 2)} %")
    return f"{sentence} : {translation}\n"

def translate_par_sequence(sequence):
    lines = []
    for sentence in sequence:
        lines.append(translate(sentence))
    return lines

def devise_dataset(lot):
    subs = sub_dataset(english_dataset,lot)
    for i in range (lot) : 
        with open(f"english_3_{i}.json", "a") as file :
            d = { "sentences" : list(subs[i])}
            json.dump(d, file)
            file.close()
    exit()

def process_lot(lot_sentence):
    translated_lines = translate_par_sequence(lot_sentence)
    with open(f"wolof_{sys.argv[2][:-4]}.txt", "a") as file:
        file.writelines(translated_lines)


def run_translation_process():
    global english_dataset
    english_dataset = english_dataset["sentences"]
    english_dataset_sub = sub_dataset((english_dataset), 50)
    threads = []
    for lot_sentence in english_dataset_sub:
        thread = Thread(target=process_lot, args=(lot_sentence,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    with open(f"wolof_{sys.argv[1]}", "w") as file:
        json.dump(english_wolof, file)


if __name__ == '__main__': 
    if len(sys.argv) >3:
        print('arguments missing\n path: path to dataset \n option: d: device the dataset \n t translate the dataset')
        exit()
    else : 
        upload_data_set(sys.argv[1])
        if(sys.argv[2].lower()=="d"):
            devise_dataset(int(sys.argv[3]))
        
        elif(sys.argv[2].lower()=="t"):
            run_translation_process()



            
            

    
    
    





    