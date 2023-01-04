import os

file_path = os.path.join(os.getcwd(), 'sorted')
result_file = open(os.path.join(file_path, 'result.txt'), 'wt', encoding='utf-8')

for file_name in os.listdir(file_path):
    if file_name.endswith(".txt") and file_name != 'result.txt':
        with open(os.path.join(file_path, file_name), 'rt', encoding='utf-8') as file:
            file_content = file.readlines()
            result_file.write(f'{file_name}\n')
            result_file.write(f'{str(len(file_content))}\n')
            result_file.writelines(file_content)
result_file.close()
