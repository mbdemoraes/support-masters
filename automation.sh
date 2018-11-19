#!/bin/bash

counter=1
window=10
reduction=10
algorithm=3
algorithm_name=OFS
dataset=hyperplane_incremental.arff

END=0

while [ "$END" != 9 ]
do
  for i in 1 2 3 4 5 6 7 8 9 10
  do
    counter=$((i))
    folder=$algorithm_name/win$window"/"
    results_file=$folder${dataset%.arff}"_$reduction""_$counter.txt"
	java -cp MOA_FeatureSelection.jar:moa.jar:weka.jar -javaagent:sizeofag-1.0.4.jar moa.DoTask \
	  "EvaluateInterleavedTestThenTrain -l (moa.featureselection.classifiers.NaiveBayes -f $reduction -m $algorithm -w $window) \
	  -s (ArffFileStream -f /home/athos/Documentos/datasets/$dataset) \
	  -f 100" > $results_file
  done
  END=$((END+1))
  if [ $reduction -eq 10 ]
  then
    reduction=$((100))
  elif [ $reduction -eq 100 ]
  then
    reduction=$((1000))
  elif [ $reduction -eq 1000 ]
  then
    reduction=$((10))
    if [ $window -eq 10 ] 
    then     
      window=$((100))
    else
      window=$((1000))
    fi
  fi
 
  
done


