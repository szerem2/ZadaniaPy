# https://pl.python.org/forum/index.php?action=printpage;topic=2731.0
# '''
# Zliczanie ile razy dana litera wystepuje w wyrazie.
# '''

tresc = 'aaAA asyyds '
def stat(words):
    a = {}
    for x in words:
        if not x in a:
            a[x] = 1
        else:
            a[x] += 1
    return a

print stat(tresc)