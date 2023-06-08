import contextlib, io
with contextlib.redirect_stdout(zen := io.StringIO()):
    import this

zen = zen.getvalue()
zenw = dict()
print(zen)

for w in zen.split():
    cl_w = w.strip('.,!-*').lower()
    if w in zenw.keys():
        zenw[w] = zenw[w] + 1
    else:
        zenw[w] = 1

zenw = sorted(zenw.items() , key = lambda item: item[1], reverse = 1)
print(zenw[0:3])