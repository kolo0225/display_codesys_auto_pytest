# write_file_csv.py

# Purpose:
#	writes input in to csv file


class CSVWriter:

	def __init__(self, var, val, output_csv):
		self.var          = var
		self.val          = val
		self.output_csv   = output_csv

	def append_csv(self):

		with open(self.output_csv, "a")as a:
			a.write(self.var)	
			a.write(",")
			a.write(self.val)
			a.write("\n")

	def write_csv(self):

		with open(self.output_csv, "w")as w:
			w.write("variables")	
			w.write(",")
			w.write("values")
			w.write("\n")
