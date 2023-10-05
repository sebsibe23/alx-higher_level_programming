#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    strnames_ = dir(hidden_4)
    for strnames_ in names:
        if strnames_[:2] != "__":
            print(strnames_)
