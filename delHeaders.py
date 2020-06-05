import cvs, os
# make a directory named Headers Removed
os.makedirs('Headers Removed', exist_ok = True)

for csv_file in os.listdir('.'):
	if not csv_file.endswith('.csv') : continue
	#if the file does not end with .csv then skip over it

	out_csv_fhand = open (os.path.join('Headers Removed', csv_file),'w', newline = '')
	csv_writer = csv.writer (out_csv_fhand)

	csv_fhand = open (csv_file)
	csv_reader = csv.reader(csv_fhand)

	for row in csv_reader:
		if row.line_num == 1 : continue
		#skip over the first line 

		#overwrite the files to the headers removed folder
		print ('Writing files without the header to the new folder... ')
		csv_writer.writerow(row)

		csv_fhand.close()

	out_csv_fhand.close()


