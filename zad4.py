#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import base64

"""def nicely_print(thing):
    if isinstance(thing, basestring):
        if isinstance(thing, str):
            print(base64.b64encode(thing))
        else:
            print(thing)
    else:
        print(repr.repr(thing))"""


def nicely_print(thing):
    if isinstance(thing, bytes):
        print(base64.b64encode(thing))
    elif isinstance(thing, str):
        print(thing)
    else:
        print(repr(thing))


"""def main():
    print u"Podaj proszę liczbę (max 50): "
    no_text = raw_input()
    try:
        no_int = int(no_text)
    except ValueError:
        print u"O nie, to nie jest poprawna liczba (całkowita)!"
        exit(1)
    if no_int <= 0:
        print u"Wartość musi być większa niż 0"
        exit(1)
    elif no_int > 50:
        print u"Wartość musi być mniejsza lub równa 50"
        exit(1)
    string_build = ''
    unicode_build = u''

    for _ in range(no_int):
        string_build += chr(random.randint(0,255))
        unicode_build += unichr(32 + random.randint(0,94))
    nicely_print(string_build)
    nicely_print(unicode_build)
    nicely_print(no_int)

    dict_example = {
        u'ziemaniaki': 2,
        u'pomidory': 6,
        u'marchewki': u'brak'
    }

    nicely_print(dict_example)
    for name, quantity in dict_example.iteritems():
        print "%s : %s" % (name, quantity)"""


def main():
    print("Podaj proszę liczbę (max 50): ")
    no_text = input()
    no_int = 0
    try:
        no_int = int(no_text)
    except ValueError:
        print("O nie, to nie jest poprawna liczba (całkowita)!")
        exit(1)
    if no_int <= 0:
        print("Wartość musi być większa niż 0")
        exit(1)
    elif no_int > 50:
        print("Wartość musi być mniejsza lub równa 50")
        exit(1)
    string_build = bytes([random.randint(0, 255) for _ in range(no_int)])
    unicode_build = "".join([chr(32 + random.randint(0, 94)) for _ in range(no_int)])

    print(string_build)
    print(unicode_build)

    nicely_print(string_build)
    nicely_print(unicode_build)
    nicely_print(no_int)

    dict_example = {
        'ziemaniaki': 2,
        'pomidory': 6,
        'marchewki': 'brak'
    }

    nicely_print(dict_example)
    for name, quantity in dict_example.items():
        print("%s : %s" % (name, quantity))

m
if __name__ == "__main__":
    main()
