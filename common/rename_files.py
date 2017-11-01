import os
# a~ipad.png to a.png
[os.rename(f, f.replace('~ipad', '')) for f in os.listdir('.') if not f.startswith('.')]
