import MapReduce
import sys



mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    trimmed_nucleotide = (record[1])[:-10]
    mr.emit_intermediate(trimmed_nucleotide, 0)

def reducer(sequence,no_of_occourences):
    mr.emit(sequence)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)