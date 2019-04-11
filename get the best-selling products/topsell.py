# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:21:19 2019
Returning top 3 top selling products

@author: Hassan
"""

from heapq import nlargest

class Product:
    def __init__ (self, name, sales):
        self.name= name
        self.sales= sales
    def getname(self):
        return self.name
    
    def getsales(self):
        return self.sales

def gettopselling(productlist):
    return nlargest(3, productlist, key=lambda product : product.getsales())
    
productlist=(Product('orange', 13),
             Product('apple', 23),
             Product('anana', 7),
             Product('bread',32),
             Product('milk', 20),
             Product('banana', 17),
             Product('coffee',3),)

top= gettopselling(productlist)
print('This is the most frequent sold product:')
for i in top:
    print(i.getname(), ':', i.getsales())
