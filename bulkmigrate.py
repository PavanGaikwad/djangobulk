from employee.models import *
import sys
import csv
'''
function that adds data from a file to a database
'''
def file_to_db(model, data):
    
    model_object = getattr(sys.modules[__name__], model)(**data) # convert model name into model object and pass data to it
    # code to insert into database
    print model_object 
    print model_object.save()


def run(model, filepath):
    f = open(filepath, 'rb') # read file in binary format, takes care of special characters
    reader = csv.reader(f)
    line_count = 0
    headers = []
    for row in reader:
        if line_count == 0:
            headers = row # first line is a header
        else:
            data = dict(zip(headers, row))
            file_to_db(model, data)

        line_count = line_count + 1


    f.close()

