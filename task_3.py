import os

file_path = os.path.join(os.getcwd(), 'sorted')
files = {}

for file_name in os.listdir(file_path):
	if file_name.endswith(".txt") and file_name != 'result.txt':
		with open(os.path.join(file_path, file_name), 'rt', encoding='utf-8') as file:
			file_content = file.readlines()
			files[file_name] = {'size': len(file_content),
								'content': file_content}

files_sorted = dict(sorted(files.items(), key=lambda item: item[1]['size']))
result_file = open(os.path.join(file_path, 'result.txt'), 'wt', encoding='utf-8')

for file, file_info in files_sorted.items():
	result_file.write(f'{file}\n')
	result_file.write(f'{file_info["size"]}\n')
	result_file.writelines(file_info["content"])
result_file.close()

