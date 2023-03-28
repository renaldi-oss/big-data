mylist = ["my", "pair", "rdd"]
myRDD = sc.parallelize(mylist)
myPairRDD = myRDD.map(lambda s: (s, len(s)))
myPairRDD.collect()

myPairRDD.keys().collect()

myPairRDD.values().collect()
#['my', 'pair', 'rdd']
#[('my', 2), ('pair', 4), ('rdd', 3)]
#[2, 4, 3]
