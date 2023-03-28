'''
Start Pyspark Command line using standalone master
[root@myhost ~]# pyspark --master spark://sparkmasterhostname:7077 --total-executor-cores 4

or

[root@myhost ~]# pyspark --master local[4]

'''


sc.defaultParallelism



myList = ["big", "data", "analytics", "hadoop" , "spark"]
myRDD = sc.parallelize(myList)
myRDD.getNumPartitions()


myRDDWithMorePartitions = sc.parallelize(myList,6)
myRDDWithMorePartitions.getNumPartitions()
 

myRDD.count()



myRDD.mapPartitionsWithIndex(lambda index,iterator: ((index, list(iterator)),)).collect()


mySixPartitionsRDD = myRDD.repartition(6)
mySixPartitionsRDD.mapPartitionsWithIndex(lambda index,iterator: ((index, list(iterator)),)).collect()


myTwoPartitionsRDD = mySixPartitionsRDD.coalesce(2)
myTwoPartitionsRDD.mapPartitionsWithIndex(lambda index,iterator: ((index, list(iterator)),)).collect()


print myTwoPartitionsRDD.toDebugString()

