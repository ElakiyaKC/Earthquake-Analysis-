#!/bin/bash
#Restart the hadoop to avoid memory issue
#echo "Stop the hadoop"
#/home/ubuntu/hadoop-2.8.0/sbin/stop-all.sh
#echo "Start the hadoop"
#/home/ubuntu/hadoop-2.8.0/sbin/start-all.sh
read -p "Enter the no.of mapper: " mc
read -p "Enter the no.of reducer:" rc
echo "Mapper $mc"
echo "Reducer $rc"
echo "Removing the input directory"
/home/ubuntu/hadoop-2.8.0/bin/hdfs dfs -rm -r /input
echo "Removing the output directory"
/home/ubuntu/hadoop-2.8.0/bin/hdfs dfs -rm -r /output
echo "Creating the input directory"
/home/ubuntu/hadoop-2.8.0/bin/hdfs dfs -mkdir /input
echo "Copying the input file to hdfs input directory"
/home/ubuntu/hadoop-2.8.0/bin/hdfs dfs -put /home/ubuntu/titanic.csv /input/titanic.csv
echo "Executing the hadoop mapreduce"
start_time="`date +%s`";
/home/ubuntu/hadoop-2.8.0/bin/hadoop jar /home/ubuntu/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapreduce.job.maps=$mc -D mapreduce.job.reduces=$rc -mapper /home/ubuntu/mapper_sum.py -reducer /home/ubuntu/reducer.py -input /input/titanic.csv -output /output
echo "Displaying the result of the reducer output"
/home/ubuntu/hadoop-2.8.0/bin/hdfs dfs -cat /output/part-00000
echo "Copying the reducer output to the ubuntu"
/home/ubuntu/hadoop-2.8.0/bin/hdfs dfs -cat /output/part-00000 > /home/ubuntu/flaskapp/static/output.csv
end_time="`date +%s`";
total_time=$((end_time-start_time))
echo $start_time
echo $end_time
echo "Time taken to run Map Reduce:$total_time"
location="/home/ubuntu/time.txt"
echo "Time taken to run Map Reduce:$total_time">"$location"
