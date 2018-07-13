from urllib.request import urlopen

#with urlopen('https://abaft-surgeon.glitch.me/') as req: # open the url page
with urlopen('file:///C:/Sarah/avinci_club/AskMPS/sandbox/simplempsweb/simplemps.html') as req: # open the url page
    print(req.read())
