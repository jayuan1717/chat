def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
		#print(chat)
		return chat

#def print_chat(filename):
#	newchat = []
#	for p in chat:

def convert_file(chat):
	new = []
	person = None
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue 
		elif line == 'Tom':
			person = 'Tom'
			continue 
		if person:
			new.append(person + ': ' + line)
	#print(new)
	return new

def write_file(filename, chat):
	with open(filename, 'w') as f:
		for line in chat:
			f.write(line + '\n')

def main(filename):
	chat = read_file(filename)
	chat = convert_file(chat)
	write_file(input("please entre the file name after conversion: ") + '.txt', chat)

main(input('Please entre the file name: '))

