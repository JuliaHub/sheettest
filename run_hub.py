import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import os
import json

def step1():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    #file_name = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    #credentials =  ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)

    credentials_dict = os.environ['CREDENTIALS_DICT']
    cred_dict = json.loads(credentials_dict, strict=False)
    credentials =  ServiceAccountCredentials.from_json_keyfile_dict(cred_dict, scope)

    gc = gspread.authorize(credentials)
    wks = gc.open('test2').sheet1
    wks.clear()

    data = str(datetime.datetime.now())
    wks.append_row(['data'])
    wks.append_row([data])