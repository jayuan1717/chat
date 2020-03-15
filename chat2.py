def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
		return chat

def convert_file(chat):
	person = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image = 0
	for line in chat:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen says', allen_word_count, 'sent', allen_sticker_count, 'stickers, and', allen_image, 'images')
	print('Viki says', viki_word_count, 'sent', viki_sticker_count, 'stickers, and', viki_image, 'images')

def write_file(filename, chat):
	with open(filename, 'w') as f:
		for line in chat:
			f.write(line + '\n')

def main(filename):
	chat = read_file(filename)
	chat = convert_file(chat)
	# write_file(input("please entre the file name after conversion: ") + '.txt', chat)

main(input('Please entre the file name: ') + '.txt')
