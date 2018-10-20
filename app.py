#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import pandas as pd
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, DATA
from pandas.io.parsers import read_csv
#import numpy as np
from numpy.core.numeric import nan
import logging
import sys
import re
from time import strftime
from decimal import *
import datetime

app = Flask(__name__)

files = UploadSet('files', extensions=('csv'))

app.config['UPLOADED_FILES_DEST'] = 'static/csv'
configure_uploads(app, files)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST' and 'file' in request.files:
		filename = files.save(request.files['file'])
		x = 'static/csv/' + filename
		try:
			df = read_csv(x, sep=';', encoding='windows-1250')
		except:
			df = read_csv(x, sep=';')
		data = df.replace(nan, '', regex=True)
		print(data)
		return str(data)
	return render_template('upload.html')


if __name__ == '__main__':
	app.run(debug=True)