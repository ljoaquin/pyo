#!/usr/bin/python
import os
import sys

#===================================
def cleanup(full_path, is_rup):
	cmd_list = []
	cmd_list.append("svn status %s | grep ^? | awk -F'  ' '{print $NF}' | sed 's/^ //g' | awk '{print \"\\\"\"$0\"\\\"\"}' | xargs rm -rf")
	cmd_list.append("svn revert -R %s")
	cmd_list.append("svn update %s")
	if is_rup:
		cmd_list = cmd_list[1:]
	for cmd in cmd_list:
		full_cmd = cmd % (full_path) + " > /dev/null"
		print full_cmd, "..."
		os.system(full_cmd)
#===================================
def main():

	if len(sys.argv) > 1:
		clean_path = sys.argv[1]
		if os.path.exists(clean_path):
			print "clean up " + clean_path
			is_rup = False
			if len(sys.argv) == 3:
				is_rup = True
			cleanup(clean_path, is_rup)
		else:
			print clean_path + " not exist"
		return

#===================================
if __name__ == '__main__':
	main()
