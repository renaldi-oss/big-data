access_log = sc.textFile("file:///home/cloudera/Documents/test.txt")

error_log = access_log.filter(lambda x: "map" in x)

cached_log = error_log.cache()

print "Total number of error records are %s" % (cached_log.count())

print "Number of product pages visited that have Errors is %s" % (cached_log.filter(lambda x: "product" in x).count()) 
# Get the lines from the textfile, create 4 partitions
# Now find the number of lines with 
# Now perform an action -  count
# Cache error log in memory
#Filter Lines with map only
