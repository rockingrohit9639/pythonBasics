import requests
import pickle

# Downloading Data and creating a txt file
# r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# text = r.text
# file = "data.txt"
# fp = open(file, "a")
# fp.write(text)
# fp.close()

# Converting the txt file to pickle file
# with open("data.txt","r") as fp:
#     data_set = fp.readlines()
#     pickle_file = "dataset.pkl"
#     with open(pickle_file, "wb") as pf:
#         pickle.dump(data_set, pf)

# Reading pickle file
with open("dataset.pkl", "rb") as pf:
    print(pickle.load(pf))
