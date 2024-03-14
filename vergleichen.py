import os
import csv

folder1_path = r'C:\Users'
folder2_path = r'C:\Users'

files_in_folder1 = set(os.listdir(folder1_path))
files_in_folder2 = set(os.listdir(folder2_path))

unique_to_folder1 = files_in_folder1 - files_in_folder2
unique_to_folder2 = files_in_folder2 - files_in_folder1

rows = []
for file in unique_to_folder1:
    rows.append([file, 'Unique to Folder 1'])
for file in unique_to_folder2:
    rows.append([file, 'Unique to Folder 2'])
    
csv_file_name = r'D:\Differenzen.csv'

with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Dateiname', 'Ordner'])
    csvwriter.writerows(rows)

print(f'Differenzen wurden in {csv_file_name} gespeichert') 