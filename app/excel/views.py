#coding:utf-8
from flask import Flask,request,jsonify
from flask_excel import make_response_from_array
from . import excel


@excel.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        return jsonify({"result": request.get_array(field_name='file')})
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''
@excel.route("/download", methods=['GET'])
def download_file():
    return excel.make_response_from_array([[1,2], [3, 4]], "csv")

@excel.route("/export", methods=['GET'])
def export_records():
    return excel.make_response_from_array([[1,2], [3, 4]], "csv", file_name="export_data")

# insert database related code here
@excel.route('/')
def index():
    return '<h1>hello,excel</h1>'
