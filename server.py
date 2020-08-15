from flask import *
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html')


# The app creates an URL route for any possible page and links that to static html files
@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)


def write_to_txt(db):  # writes submission form data to textfile
    with open('./data.txt', 'a') as dat:
        email = db['email']
        message = db['message']
        subject = db['subject']
        dat.write(
            f'Email: {email} --- Subject: {subject} --- Message: {message}\n')

# a csv file is a file containing text seperated by commas or other special characters


def write_to_csv(db):  # writes submission form data to a csv file
    with open('./data.csv', 'a', newline='\n') as dat:
        email = db['email']
        message = db['message']
        subject = db['subject']
        csv_writer = csv.writer(
            dat, delimiter=',', quotechar='>', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # returns values on form as a dictionary. Check terminal for format
            data = request.form.to_dict()
            # print(data)
            # write_to_txt(data)
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return redirect('db_persist_fail.html')
    else:
        return redirect('/submit_fail.html')
