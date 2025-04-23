import os
import shutil
import glob
from odd_number_naming.rename_pdf import rename_pdf_files as rename_odd
from even_number_naming.rename_pdf_even import rename_pdf_files as rename_even
from merge.merge_pdf import merge_pdf_files

def move_pdf_files(source_folder, dest_folder):
    # 确保目标文件夹存在
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 获取源文件夹中所有的PDF文件
    pdf_files = glob.glob(os.path.join(source_folder, "*.pdf"))
    
    for pdf_file in pdf_files:
        # 构建目标文件路径
        dest_path = os.path.join(dest_folder, os.path.basename(pdf_file))
        try:
            # 移动文件
            shutil.move(pdf_file, dest_path)
            print(f"已移动文件: {os.path.basename(pdf_file)}")
        except Exception as e:
            print(f"移动文件 {pdf_file} 时出错: {str(e)}")

def main():
    # 获取当前脚本所在的文件夹路径
    base_folder = os.path.dirname(os.path.abspath(__file__))
    odd_folder = os.path.join(base_folder, "odd_number_naming")
    even_folder = os.path.join(base_folder, "even_number_naming")
    merge_folder = os.path.join(base_folder, "merge")

    # 1. 对奇数命名文件夹进行处理
    print("\n开始处理奇数命名文件夹...")
    rename_odd(odd_folder)

    # 获取奇数命名文件夹中的文件数量
    pdf_count = len(glob.glob(os.path.join(odd_folder, "*.pdf")))
    
    # 2. 对偶数命名文件夹进行处理
    print("\n开始处理偶数命名文件夹...")
    rename_even(even_folder, pdf_count)

    # 3. 移动文件到合并文件夹
    print("\n开始移动文件到合并文件夹...")
    move_pdf_files(odd_folder, merge_folder)
    move_pdf_files(even_folder, merge_folder)

    # 4. 合并PDF文件
    print("\n开始合并PDF文件...")
    merge_pdf_files(merge_folder)

if __name__ == "__main__":
    main()