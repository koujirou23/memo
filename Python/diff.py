### Differクラスでファイルを比較
import os
import difflib


file1_name = 'file1.txt'
file2_name = 'file2.txt'

file1_path = os.path.join(file1_name)
file2_path = os.path.join(file2_name)

file1 = open(file1_path)
file2 = open(file2_path)
diff = difflib.Differ()

output_diff = diff.compare(file1.readlines(), file2.readlines())
print('\n'.join(output_diff))

file1.close()
file2.close()