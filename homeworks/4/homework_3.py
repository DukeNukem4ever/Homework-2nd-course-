from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)
filename = 'results.csv'

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/thanks', methods = ['POST'])
def save_to_csv():
    if request.method == 'POST':
        ask = request.form['ASK']
        what = request.form['WHAT']
        how = request.form['HOW']
        name = request.form['NAME']
        surname = request.form['SURNAME']
        fin_form = 'Спасибо за ответ!'
        fieldnames = ['ASK', 'WHAT', 'HOW', 'NAME', 'SURNAME']
        with open(filename, 'a+', encoding = 'utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({'ASK': ask, 'WHAT': what, 'HOW': how, 'NAME': name,
                             'SURNAME': surname})
        #with open('C:\Users\ARTEM\Desktop\Homework\PYTHON-2\HOMEWORK3\table.csv', 'w', encoding = 'utf-8') as csvoutput:
        #    writer = csv.DictWriter(csvoutput, fieldnames = fieldnames)
        #    writer.writerow({'ASK': ask, 'WHAT': what, 'HOW': how, 'NAME': name,
        #                     'SURNAME': surname})   
        return render_template('thanks.html', fin_form = fin_form)

@app.route('/stats')
def show_stats():
    #stats_list = [ask, what, how, name, surname]
    with open(filename, 'r', encoding = 'utf-8') as content:
        lit = []
        with open (filename, 'r+', encoding = 'utf-8') as csvfile:
            content = csv.reader(content)
            content = list(content)
            for i in content:
                for m in i:
                    lit.append(m)
    return render_template("stats.html", lit = lit)

#return render_template("stats2.html", json = str(dict_csv).replace("{","").replace("}", "").replace("'",''))
#dict_csv = {}
    #list2 = []
    #fieldnames = ['ASK', 'WHAT', 'HOW', 'NAME', 'SURNAME']
        #spisok = content[0]
        #with open('results.csv','w',encoding='utf-8') as file2:
        #    file2.write(content)
#reader = list(csv.DictReader(csvfile, fieldnames = fieldnames))
        #for row in reader:
        #    name = row['NAME'] + ' ' + row['SURNAME']
        #    dict_csv[name] = json.loads(json.dumps(row))

@app.route('/json')
def json_maker():
    dict_csv = {}
    fieldnames = ['ASK', 'WHAT', 'HOW', 'NAME', 'SURNAME']
    with open (filename, 'r+', encoding = 'utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile, fieldnames = fieldnames))
        for row in reader:
            name = row['NAME'] + ' ' + row['SURNAME']
            dict_csv[name] = json.loads(json.dumps(row))
    return render_template('json.html', json = dict_csv)

@app.route('/search')
def do_search():
    return render_template('search.html')

@app.route('/result', methods = ['POST'])
def show_result():
    dict_csv = {}
    if request.method == 'POST':
        ask = request.form['ask_search']
        what = request.form['what_search']
        fieldnames = ['ASK', 'WHAT', 'HOW', 'NAME', 'SURNAME']
        with open(filename, 'r', encoding = 'utf-8') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            for row in reader:
                if row['ASK'] == ask:
                    if (row['WHAT'] == what or row['HOW'] == what or
                        row['NAME'] == what or row['SURNAME'] == what):
                        name = row['NAME'] + ' ' + row['SURNAME']
                        dict_csv[name] = json.loads(json.dumps(row))
        return render_template('result.html', result = str(dict_csv).replace("{","").replace("}", "").replace("'",''))

if __name__ == '__main__':
    app.run(debug = True)
