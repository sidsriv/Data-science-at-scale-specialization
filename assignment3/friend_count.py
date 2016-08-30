import MapReduce
import sys



mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    mr.emit_intermediate(person, 1)

def reducer(person, no_of_friends):
    total = 0
    for v in no_of_friends:
      total += v
    mr.emit((person, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
