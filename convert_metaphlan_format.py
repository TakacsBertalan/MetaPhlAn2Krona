from sys import argv
import subprocess
import optparse
import os


def main():
	#Parse Command Line
	parser = optparse.OptionParser(description='A small Python3 script to get Krona outputs from metaPhLan results',

	epilog="Author: Bertalan Takács, @TakacsBertalan on GitHub")
	parser.add_option( '-p', '--profile', dest='profile', default='', action='store', help='Name of the metaPhLan3 taxonomic output file. Alternatively you can specify a folder path and a search string' )
	parser.add_option( '-k', '--krona', dest='krona', default='krona.out', action='store', help='the Krona output file name [krona.out]' )
	parser.add_option( '-s', '--search-string', dest = 'search', default = "", action = "store", help="Search string for multiple samples. Generates a single Krona output")
	parser.add_option( '-f', '--folder-path', dest = 'folder', default = "./", action = "store", help="Folder path for input files [./]")
	parser.add_option( '-t', '--temporary-tag', dest = 'temporary', default = ".m2k.temp", action = "store", help="Folder path for input files [./]")
	
	( options, spillover ) = parser.parse_args()
	if options.search == "" and options.folder == "":
		print("Please specify an input file")
		parser.print_help()
		return
	if options.profile != "":
		convert_metaphlan_output(options.profile, options.profile.split(".")[0] + options.temporary)	
		call_krona(options.profile.split(".")[0] + options.temporary, options.krona, options.temporary)	
	elif options.search != "":
		files = [f for f in os.listdir(options.folder) if os.path.isfile(f) and options.search in f]
		temp_files = []
		for f in files:
			convert_metaphlan_output(f,f.split(".")[0] +options.temporary)
			temp_files.append(f.split(".")[0] + options.temporary)
		call_krona(temp_files, options.krona, options.temporary)



def convert_metaphlan_output(input_file, output_file):
	metaphlan_result = {}
	with open(input_file, "r") as inp:
		for line in inp:
			if line[0] != "#":
				line_list = line.rstrip().split("\t")
				if "s__" in line_list[0]:
					metaphlan_result[line_list[0]] = line_list[2]

	with open(output_file, "w") as outp:
		for key in metaphlan_result:
			taxonomy = key.split("|")
			taxonomy = [x[3:] for x in taxonomy]
			outp.write(metaphlan_result[key] + "\t" + "\t".join([x.replace("_", " ", 2).replace("_","-") for x in taxonomy]) + "\n")


def call_krona(input_file, output_file, temp_tag):
	command_list = ["ktImportText","-o",output_file]
	if isinstance(input_file, list):
		for s in input_file:
			command_list.append(s)
		subprocess.run(command_list)
	else:
		command_list.append(input_file)	
		subprocess.run(command_list)
	subprocess.run("rm *"+ temp_tag, shell = True)

main()