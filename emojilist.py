import emoji_list
numbers = set(map(str, range(10)))
emojis=list(filter(lambda x: x not in numbers, emoji_list.all_emoji))

if __name__ == "__main__":
	print(emojis)