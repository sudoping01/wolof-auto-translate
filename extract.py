import json
data = []

def load_and_process(path):
    source= []
    global data 
    with open(path, "r") as file: 
        for line in file: 
            source.append(line)
        file.close()

    source.pop(0)

    print(f"{path}: {len(source)}")

    for line in source : 
        for sentence in line.split("\t")[:-1] : 
            data.append(sentence)  


if __name__=='__main__':
    paths = [f"{i}.tsv" for i in range(1,18)]
    for path in paths:
        load_and_process(path)

with open("data.json", "w") as file:
    json.dump(data, file)
    file.close()
    




    

        



