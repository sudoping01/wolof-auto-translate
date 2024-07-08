from deep_translator import GoogleTranslator 
from threading import Thread
import json
import numpy as np 


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
        with open(f"english_dataset_{i}.json", "a") as file :
            d = { "sentences" : list(subs[i])}
            json.dump(d, file)
            file.close()

if __name__ == '__main__': 
    upload_data_set("english_dataset_5.json")
    #devise_dataset(lot)
    english_dataset = list(english_dataset["sentences"])

    english_dataset_sub = sub_dataset(list(english_dataset), 50)

    def process_lot(lot_sentence):
        translated_lines = translate_par_sequence(lot_sentence)
        with open("english_wolof_5.txt", "a") as file:
            file.writelines(translated_lines)

    threads = []
    for lot_sentence in english_dataset_sub:
        thread = Thread(target=process_lot, args=(lot_sentence,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    with open("english_wolof_5.json", "w") as file:
        json.dump(english_wolof, file)
    