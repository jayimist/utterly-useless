#!/home/jay/Python/bin/python3
# MiniJoyse Langauge
import sys, time
from pathlib import Path
from rich.text import Text
from rich import print as rich_print

MINIJOYSE_VERSION = "1.0.0"



def warn(*args):
	msg = Text(*args, style="yellow")
	rich_print(msg)

class MiniJoyse:
	DEBUG = False

	# Evironmetal functions
	def _env_print(self, *args) -> None:
		print("[MiniJoyse]:", *args)
	def _env_raw_print(self, *args) -> None:
		print(*args)
	def _env_warn(self, *args) -> None:
		msg = Text("[MiniJoyse - WARNING]: ", style="yellow")
		msg.append(" ".join(args))
		rich_print(msg)
	def _env_quit(self) -> None:
		self._env_print("Bye!")
		sys.exit()

	# Methods
	def set_env(self, new_env: dict) -> dict:
		self.env = new_env

	def get_env(self) -> dict:
		return self.env

	# Environment
	def __init__(self):
		self.env = {
			"_funcs": {
				"print": self._env_print,
				"raw_print": self._env_raw_print,
				"warn": self._env_warn,
				"quit": self._env_quit,
				"exit": self._env_quit,
				"set_env": self.set_env,
				"get_env": self.get_env,
				# "var": self._env_var,
				# "const": self._env_const
			},

			"true": True,
			"false": False
		}

	# Methods
	def run(self, program: str) -> None:
		if self.DEBUG:print(f"[MiniJoyse]: Program started!\nProgram: {program}")

		program = program.replace(";", "\n")
		lines = program.strip().splitlines()

		for line in lines:
			if self.DEBUG:print(f"Current line: {line}")

			line.strip()

			if not line or line.startswith("#"):
				continue

			if "#" in line:
				line = line.split("#", 1)[0].strip()

			tokens = line.split()
			if not tokens:
				continue
			func = tokens[0]
			args = tokens[1:]
			if self.DEBUG:print(f"Func: {func}\nArgs: {args}")

			if func in self.env["_funcs"]:
				self.env["_funcs"][func](*args)
			else:
				self._env_warn(f"The function '{func}' is not recognizable.")

		if self.DEBUG:print("[MiniJoyse]: End of program.")



#print("Waiting, hold on bucko...")
MiniJoyse = MiniJoyse()

time.sleep(0.01)

cmd = sys.argv[0]
args = sys.argv[1:]

if not args:
	print(f"𝓜𝓲𝓷𝓲𝓙𝓸𝔂𝓼𝓮 - v{MINIJOYSE_VERSION}\nMiniJoyse is a small programming language by Jay\nCommands:\n    version - Shows the MiniJoyse version.\n\nType 'quit' or 'exit' to quit the loop.")

	while True:
		line = input(">>> ")
		MiniJoyse.run(line)
elif args[0] == "version":
	print(f"𝓜𝓲𝓷𝓲𝓙𝓸𝔂𝓼𝓮 - v{MINIJOYSE_VERSION} (MiniJoyse)")
elif args[0]:
	file = Path(args[0])
	
	if not file.exists():
		warn(f"File not found: {args[0]}")
		sys.exit(1)
	
	program = file.read_text()
	MiniJoyse.run(program)
