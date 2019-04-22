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


# TODO: Needed to relink on update from jetbrains toolbox. Will need to find better way than this.
# TODO: spaces are note behaving normally as they would with non shortcuts. Would usually use pathlib / subprocess.
# Need to chage shortcut 

class OpenIntellij(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		# assign to alias link location
		run_command(file_under_cursor, "C:\\Aliases\\IntelliJIDEAUltimate.lnk")

class OpenPycharm(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		run_command(file_under_cursor, "C:\\Aliases\\PyCharmProfessional.lnk")

class OpenGoland(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		run_command(file_under_cursor, "C:\\Aliases\\GoLand.lnk")

class OpenWebstorm(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		run_command(file_under_cursor, "C:\\Aliases\\WebStorm.lnk")

class OpenClion(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		run_command(file_under_cursor, "C:\\Aliases\\CLion.lnk")

