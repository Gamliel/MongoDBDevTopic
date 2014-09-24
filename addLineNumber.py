if __name__ == "__main__":
	with open("MongoDevTopic.history", "r") as f:
		counter = 0;
		for line in f:
			if (not (line.startswith('//')) and not(line.startswith('\n'))):
				lineWithoutEndLine = line[0:(len(line) -1)];
				print lineWithoutEndLine + '// #', counter;
				counter += 1;
