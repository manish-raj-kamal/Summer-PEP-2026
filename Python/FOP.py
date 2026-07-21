# print("Hello Manish")

# sen = "        this is a    s e n ta nce       "

# print(sen)
# print("|" + sen.lstrip() + "|")
# print("|" + sen.rstrip() + "|")
# print("|" + sen.strip() + "|")



unprinted_designs=['phonecase','robot pendant','dodecahedron']
completed_models=[]
def printModels(unprinted, completed):
    while unprinted:
        current_design=unprinted.pop()
        print("Printing model: "+current_design)
        completed.append(current_design)

def show_completed_models(completed):
    print("\nThe following models have been printed:")
    for model in completed:
        print(model)


printModels(unprinted_designs, completed_models)
show_completed_models(completed_models)