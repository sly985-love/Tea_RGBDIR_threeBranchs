import os
from pathlib import Path

# with open("val.txt", "w") as f:
#     path = r"C:\Users\shuailuyu\AllTea\apple\DataSet\depth\val"
#     for foldName, subfolders, filenames in os.walk(path):
#         for filename in filenames:
#             line = str(os.path.join(foldName, filename))
#             line = line + '\n'
#             f.write(line)
# C:\Users\shuailuyu\AllTea\apple\DataSet\depth


def main():
    root_path = Path(r'D:\data\apple\DataSet')

    for tmp_path in root_path.iterdir():
        for tv_path in tmp_path.iterdir():
            if tv_path.is_dir():
                txt_name = tmp_path / (tv_path.stem + '.txt')
                with open(txt_name, 'w') as f:
                    for line in tv_path.iterdir():
                        if line.suffix == '.png' or line.suffix == '.jpg':
                            line = str(line) + '\n'
                            f.write(line)
            f.close()

if __name__ == '__main__':
    main()