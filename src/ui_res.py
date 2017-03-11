#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import base64
from wx.lib.embeddedimage import PyEmbeddedImage
smile = PyEmbeddedImage(
    "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"
)
def image2base64(path):
    icon = open(path, 'rb')
    iconData = icon.read()
    iconData = base64.b64encode(iconData)
    LIMIT = 72
    liIcon = []
    fn = os.path.basename(path).split(".")[0]
    liIcon.append("{} = PyEmbeddedImage(".format(fn))
    while True:
        sLimit = iconData[:LIMIT]
        iconData = iconData[LIMIT:]
        liIcon.append('    \"%s\"' % sLimit)
        if len(sLimit) < LIMIT:
            break
    liIcon.append(")")
    return '\n'.join(liIcon)

def insert2file(str, res_path, line):
    fp = file(res_path)
    s = fp.read()
    fp.close()
    a = s.split('\n')
    s = '\n'.join(a[:line]) + '\n'+str+'\n' + '\n'.join(a[line:])
    fp = file(res_path, 'w')
    fp.write(s)
    fp.close()

if __name__ == '__main__':
    import sys
    str = image2base64(sys.argv[1])
    res_path = sys.argv[0]
    insert2file(str, res_path, 5)






