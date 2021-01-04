import pickle


def store(dictionary, loc=None):
    file_name = "schools" if loc is None else loc
    with open(f"obj/{file_name}.pkl", "wb") as f:
        pickle.dump(dictionary, f, pickle.HIGHEST_PROTOCOL)


def read(loc=None):
    file_name = "schools" if loc is None else loc
    with open(f"obj/{file_name}.pkl", "rb") as f:
        return pickle.load(f)
