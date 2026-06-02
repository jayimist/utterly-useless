#!/home/jay/Python/bin/python3
import random
import pyperclip

combining_marks = (
    "̀", "́", "̂", "̃", "̄", "̅", "̆", "̇", "̈", "̉", "̊", "̋", "̌", "̍", "̎", "̏", "̐", "̑", "̒", "̓",
    "̔", "̕", "̖", "̗", "̘", "̙", "̚", "̛", "̜", "̝", "̞", "̟", "̠", "̡", "̢", "̣", "̤", "̥", "̦", "̧",
    "̨", "̩", "̪", "̫", "̬", "̭", "̮", "̯", "̰", "̱", "̲", "̳", "̴", "̵", "̶", "̷", "̸", "̹", "̺", "̻",
    "̼", "̽", "̾", "̿", "̀", "́", "͂", "̓", "̈́", "ͅ", "͆", "͇", "͈", "͉", "͊", "͋", "͌", "͍", "͎", "͏",
    "͐", "͑", "͒", "͓", "͔", "͕", "͖", "͗", "͘", "͙", "͚", "͛", "͜", "͝", "͞", "͟", "͠", "͡", "͢", "ͣ",
    "ͤ", "ͥ", "ͦ", "ͧ", "ͨ", "ͩ", "ͪ", "ͫ", "ͬ", "ͭ", "ͮ", "ͯ"
)



def zalgoify(text: str, strength: int = 20) -> str:
	new_text = []

	for char in text:
		marks = ''.join(
			random.choice(combining_marks)
			for _ in range(strength)
		)

		new_text.append(char + marks)

	return ''.join(new_text)

# text = zalgoify("Zalgo")
# print(f"Zalgoify: {text}")
# pyperclip.copy(text)
# print(f"Copied: {text}")