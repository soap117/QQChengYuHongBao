import pickle
fpy_dict = pickle.load(open('fpy.pkl', 'rb'))
strinput = 'None'
while strinput != 'exit':
    strinput = input("Enter your input: ")
    if strinput in fpy_dict.keys():
        cys = fpy_dict[strinput]
        for k in range(5):
            print(cys[k])

