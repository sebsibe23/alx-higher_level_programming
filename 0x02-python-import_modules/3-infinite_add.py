if __name__ == "__main__":
    import sys

    strtot = 0
    for i in range(len(sys.argv) - 1):
        strtot += int(sys.argv[i + 1])
    print("{}".format(strtot))
