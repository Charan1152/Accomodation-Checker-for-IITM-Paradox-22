from flask import request,Flask,render_template,redirect
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)
source = requests.get("https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vSm6N9R14cCqQRezzQjFxB5zMkaMppujXQka2VSb2k2hNtPd0_EX27XcREGnOpA2gZNaK6MH75hx6Eo/pubhtml").text
soup = BeautifulSoup(source,"lxml")
a = soup.find_all("td",class_="s4",dir="ltr")
l = []
for i in a:
  l.append((i.text))
final = []
for i in range(0,int(len(l)),2):
  final.append((l[i],l[i+1]))
source1 = requests.get("https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vTYt1fhB8BKABXrz7YRMt-D9dt4JDtsJXEAw7WVrun3kHboCediMBgTzUqfbdYtAupqZG27qn2GWuZ3/pubhtml").text
soup = BeautifulSoup(source1,"lxml")
a = soup.find_all("td",class_="s4",dir="ltr")
l1= []
for i in a:
  l1.append((i.text))
final1 = []
for i in range(0,int(len(l1)),2):
  final1.append((l1[i],l1[i+1]))
global f
f = final+final1
@app.route('/')
def index():
  return render_template("index.html",members=f,flag=None)
@app.route('/mailsub',methods=['GET','POST'])
def mailsub():
  mailid = request.form['mailid']
  if mailid=="":
    return redirect('/')
  for k in f:
    if k[0]==str(mailid+"@student.onlinedegree.iitm.ac.in"):
      return render_template('success.html',mail=mailid)
  return render_template('fail.html',mail=mailid)
