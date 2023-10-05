#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    t = dir(hidden_4)
    t = [q for q in t if not q.startswith('__')]
    t.sort()
    for q in t:
        print(q)
