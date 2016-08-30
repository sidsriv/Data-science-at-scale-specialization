import json
import sys

instance = {}
count = 0
def create_histogram():
	tweet_file = open(sys.argv[1])
	global count
	for line in tweet_file:
		res = json.loads(line)
		string = res.get('text','').encode("ascii","ignore")
		words = string.split()
		for word in words:
			instance[word]  = int(instance.get(word,0)) + 1
			count += 1
	

def frequency():
	print instance
	for key in instance.keys():
		print "%s %0.4f" % (key, instance[key]/count)


def main():
	create_histogram()
	frequency()


if __name__ == '__main__':
	main()