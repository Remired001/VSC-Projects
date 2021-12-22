import json

def readJsonFile(insulin):
    data=""
    try:
        with open('python Labs/insulin.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print("could not read file")
    return data