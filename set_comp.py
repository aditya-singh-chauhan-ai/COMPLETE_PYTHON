from tkinter import FIRST


s = {k**2 for k in range(1,11)}
print(s)

names = ['madhav', 'govind']
first = {name[0] for name in names}
print(first)