# -*- coding:utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from app import app

if __name__ == "__main__":
    #app.run(debug=True, ssl_context=("ca/server-cert.pem","ca/server-key.pem"))
    app.run(debug=True)
