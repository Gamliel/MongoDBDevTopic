if __name__ == "__main__":
	with open("MongoDevTopic.history", "r") as f:
		counter = 0;
		for line in f:
			lineWithoutEndLine = line[0:(len(line) -1)];
			if (not (line.startswith('//')) and not(line.startswith('\n'))):
				print lineWithoutEndLine + '; // #'  + str(counter) + '/';
				counter += 1;
			else:
				print lineWithoutEndLine;
