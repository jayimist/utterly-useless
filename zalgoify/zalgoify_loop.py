from zalgoify import zalgoify
import pyperclip
import time

time.sleep(0.1)

ZALGO = zalgoify("Zalgo", 5)

while True:
	text = input(f"Convert to {ZALGO}: ")

	if text.lower() == "q" or text.lower == "quit":
		break

	stength = input("Strength? (Leave nothing = 20): ")

	try:
		text = zalgoify(text, int(stength))
	except ValueError:
		print("Going for 20 strength!")
		text = zalgoify(text, 20)
	
	print(f"Zalgoified: {text}")
	pyperclip.copy(text)
	print(f"Copied '{text}'!")

print("Bye!")