f = file('scores.txt')
lines = f.readlines()
#print lines
f.close()

results = []

for line in lines:
   #print line
   data = line.split()
   #print data
  
   sum = 0
   i = 0
   for score in data[1:]:
       sum += int(score)
       i +=1
   result = '%s \t: %d\taverage: %d\n' % (data[0], sum, sum/i)
   #print result

   results.append(result)

#print results
output = file('result.txt', 'w')
output.writelines(results)
output.close()
