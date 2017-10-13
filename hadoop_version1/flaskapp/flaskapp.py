from flask import Flask,render_template,request
import os



app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/station',methods=['POST'])
def upload():
    try:
        output = []
        user="sudo su"
        os.system(user)
        del_inputfolder = "hadoop dfs -rmdir -rm -r /input_hadoop"
        del_outputfolder = "hadoop dfs -rmdir -rm -r /output_hadoop"
        os.system(del_inputfolder)
        os.system(del_outputfolder)
        os.system("hadoop dfs -mkdir /input_hadoop")
        os.system("hadoop fs -put /home/ubuntu/input/UNPrecip.csv /input_hadoop/UNPrecip.csv")
        run_hadoop="/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -input /input_hadoop/UNprecip.csv -output /output_hadoop -mapper /home/ubuntu/mapper.py  -file /home/ubuntu/mapper.py  -reducer /home/ubuntu/reducer.py  -file /home/ubuntu/reducer.py"
        os.system(run_hadoop)
        hadoop_result="hadoop dfs -cat /output_hadoop/part-00000"
        reducer_output=os.system(hadoop_result)
        print reducer_output
        # Read the file
        os.system("hadoop dfs -cat /output_hadoop/part-00000 > /home/ubuntu/flaskapp/output_ec2.csv")
        file=open("output_ec2.txt",'r')
        #contents=file2.read()
        for line in file.readlines():
            output.append(line)
    except:
        print "Error"
    return render_template("Result.html",message=output)

@app.route('/survive',methods=['POST'])
def survive():
    try:
        output = []
        user="sudo su"
        os.system(user)
        del_inputfolder = "hadoop dfs -rmdir -rm -r /input_hadoop"
        del_outputfolder = "hadoop dfs -rmdir -rm -r /output_hadoop"
        os.system(del_inputfolder)
        os.system(del_outputfolder)
        os.system("hadoop dfs -mkdir /input_hadoop")
        os.system("hadoop fs -put /home/ubuntu/input/titanic.csv /input_hadoop/titanic.csv")
        run_hadoop="/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -input /input_hadoop/titanic.csv -output /output_hadoop -mapper /home/ubuntu/mapper_age.py  -file /home/ubuntu/mapper_age.py  -reducer /home/ubuntu/reducer.py  -file /home/ubuntu/reducer.py"
        os.system(run_hadoop)
        hadoop_result="hadoop dfs -cat /output_hadoop/part-00000"
        reducer_output=os.system(hadoop_result)
        print reducer_output
        # Read the file
        os.system("hadoop dfs -cat /output_hadoop/part-00000 > /home/ubuntu/flaskapp/output1_ec2.csv")
        file=open("output_ec2.csv",'r')
        #contents=file2.read()
        for line in file.readlines():
            output.append(line)
    except:
		  print "Error"
    return render_template("Result.html",message=output)


if __name__ == '__main__':
    app.run()