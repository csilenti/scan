import os
import glob
from PyPDF2 import PdfMerger
import re

def merge_pdf_files(folder_path):
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print(f"文件夹 {folder_path} 不存在")
        return

    # 获取文件夹中所有的PDF文件
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    
    if not pdf_files:
        print("没有找到PDF文件")
        return

    # 创建一个字典来存储文件名和对应的序号
    file_numbers = {}
    pattern = re.compile(r'Scan(\d+)\.pdf')
    
    for pdf_file in pdf_files:
        filename = os.path.basename(pdf_file)
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            file_numbers[pdf_file] = number

    # 如果没有找到符合命名规则的文件
    if not file_numbers:
        print("没有找到符合命名规则(Scan001.pdf等)的文件")
        return

    # 按序号排序文件
    sorted_files = sorted(file_numbers.keys(), key=lambda x: file_numbers[x])

    try:
        # 创建PDF合并器
        merger = PdfMerger()

        # 按顺序添加PDF文件
        for pdf_file in sorted_files:
            print(f"正在添加: {os.path.basename(pdf_file)}")
            merger.append(pdf_file)

        # 生成输出文件名
        output_file = os.path.join(folder_path, "merged_output.pdf")
        
        # 如果输出文件已存在，在文件名后添加数字
        counter = 1
        while os.path.exists(output_file):
            base, ext = os.path.splitext("merged_output.pdf")
            output_file = os.path.join(folder_path, f"{base}_{counter}{ext}")
            counter += 1

        # 保存合并后的文件
        merger.write(output_file)
        merger.close()
        print(f"\n合并完成！输出文件: {os.path.basename(output_file)}")

    except Exception as e:
        print(f"合并PDF文件时出错: {str(e)}")

if __name__ == "__main__":
    # 获取当前脚本所在的文件夹路径
    current_folder = os.path.dirname(os.path.abspath(__file__))
    merge_pdf_files(current_folder)