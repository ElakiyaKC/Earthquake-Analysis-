from flask import Flask,render_template,request
import time
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    return render_template('Upload.html')

@app.route('/mapreduce',methods=['POST','GET'])
def output():
    data=[]
    time=[]
    file=r'/home/ubuntu/flaskapp/static/output.csv'
    with open(file,'rb') as files:
        filelines=files.readline()
        data.append(filelines)
    print data
    time_file=r'/home/ubuntu/time.txt'
    with open(time_file,'rb') as file1:
        filelines1=file1.readline()
        time.append(filelines1)
    print time
    return render_template("Result.html",message=data,perf=time)


@app.route('/bargraph',methods=['POST','GET'])
def bargraph():
    return render_template("bargraph.html")

@app.route('/scatterplot',methods=['POST','GET'])
def scatterplot():
    return render_template("scatter_plot.html")

if __name__ == '__main__':
    app.debug='true'
    app.run()