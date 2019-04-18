from fman import DirectoryPaneCommand
from os import system
import platform
import ctypes 

def run_command(file_under_cursor, exec_path):
	if not file_under_cursor:
		ctypes.windll.user32.MessageBoxW(0, "Nothing selected", "Error", 1)
		return
	# Don't know why file is preprennded but this works
	file_under_cursor = file_under_cursor.replace("file://", "")
		
	pre_executor = ''
	if platform.system() == 'Windows':
		pre_executor = 'start'
		# If making mac and linux compatibility I think this still should be fine empty

	cmd = ' '.join([pre_executor, exec_path, file_under_cursor])
	system(cmd)


class OpenIntellij(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		# assign to alias link location
		run_command(file_under_cursor, "C:\\Aliases\\intellij")

class OpenPycharm(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		run_command(file_under_cursor, "C:\\Aliases\\pycharm")

class OpenGoland(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		run_command(file_under_cursor, "C:\\Aliases\\goland")

class OpenWebstorm(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		run_command(file_under_cursor, "C:\\Aliases\\webstorm")

class OpenClion(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		run_command(file_under_cursor, "C:\\Aliases\\clion")

