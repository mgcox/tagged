from hashids import Hashids
import re
import itertools

def reduceBrand(brand):
    newstr = brand.title()

    newstr = newstr.replace(" ", "")
    print newstr
    vowels = ('a', 'e', 'i', 'o', 'u')
    for index, x in enumerate(newstr.lower()):
        if index != 0 or index != len(newstr):
                if x in vowels:
                        newstr = newstr.replace(x, "")

    #remove duplicates
    newstr = ''.join(ch for ch, _ in itertools.groupby(newstr))

    return newstr


def hashTag(brand, sku):
    brand = reduceBrand(brand)

    hashids = Hashids()

    hashid = hashids.encode(int(sku))

    print sku
    print hashid

    print '#' + 'tag' + brand + hashid

hashTag(raw_input(), raw_input())

