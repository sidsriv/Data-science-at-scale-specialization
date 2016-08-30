import MapReduce
import sys



mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
def uniqueify(seq, idfun=None): 
  if idfun is None:
    def idfun(x): return x
  seen = {}
  result = []
  for item in seq:
    marker = idfun(item)
    if marker in seen: continue
    seen[marker] = 1
    result.append(item)
  return result

def mapper(record):
    doc_id = record[0]
    text = record[1]
    words = text.split()
    for w in uniqueify(words):
      mr.emit_intermediate(w, doc_id)

def reducer(word, list_of_doc_ids):
    doc_list = []
    for v in list_of_doc_ids:
      doc_list.append(v)
    mr.emit((word, doc_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
