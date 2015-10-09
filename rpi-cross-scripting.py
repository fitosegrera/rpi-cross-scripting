import sublime, sublime_plugin
from subprocess import PIPE,Popen
import json
import os

print("plugin loaded")

class Rpi(sublime_plugin.TextCommand):
	def run(self, edit):

		# script_dir = os.path.dirname(__file__)
		# rel_path = "rpi-config.json"
		# abs_file_path = os.path.join(script_dir, rel_path)
		# with open(abs_file_path, 'r') as f:
		# 	jsonData = json.load(f)

		# commandToExecute = "scp " + jsonData["origin"] + " " + jsonData["username"] + "@" + jsonData["ip"] + jsonData["target"]
		# subprocess.call(commandToExecute, shell=True)
		#subprocess.call('sshpass -pFito_1015! ssh -o StrictHostKeyChecking=no root@192.168.1.106 ls /shares', shell=True)
		proc = Popen(['sshpass', '-p', 'Fito_1015!', 'ssh', '-o', 'StrictHostKeyChecking=no', 'root@192.168.1.106', 'ls', '/shares'], stdout=PIPE)
		print(proc.communicate())