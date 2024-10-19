import zipfile
import os

def compress_files(file_list, output_filename):
    with zipfile.ZipFile(output_filename, 'w') as zipf:
        for file in file_list:
            zipf.write(file, os.path.basename(file))
    
    print("Compression successful!")
    

def descompress_files(zip_file, output_folder):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(output_folder)
        
    print("Descompression successful!")
    
#create a list of files to compress
files_to_compress = ['file1.txt', 'file2.txt', 'file3.txt']

#specify the name of the zip file
output_zip_file = 'compressed_files.zip'

#compress files
compress_files(files_to_compress, output_zip_file)


#specify the path to the zip file
#zip_file_path = 'compressed_files.zip'

#specify where the files will be extracted
#output_folder = 'extracted_files'

#Decompress files
#descompress_files(zip_file_path, output_folder)