import os
import glob

def rename_pdf_files(folder_path):
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print(f"文件夹 {folder_path} 不存在")
        return

    # 获取文件夹中所有的PDF文件
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    
    if not pdf_files:
        print("没有找到PDF文件")
        return

    # 对文件进行排序
    pdf_files.sort()

    # 从1开始的奇数计数器
    counter = 1

    for pdf_file in pdf_files:
        # 生成新的文件名（使用奇数）
        new_name = f"Scan{counter:03d}.pdf"
        new_path = os.path.join(folder_path, new_name)

        # 如果目标文件已存在，跳过重命名
        if os.path.exists(new_path) and pdf_file != new_path:
            print(f"文件 {new_name} 已存在，跳过重命名")
            counter += 2
            continue

        try:
            # 重命名文件
            os.rename(pdf_file, new_path)
            print(f"已将 {os.path.basename(pdf_file)} 重命名为 {new_name}")
        except Exception as e:
            print(f"重命名 {pdf_file} 时出错: {str(e)}")

        # 增加计数器（确保是奇数）
        counter += 2

if __name__ == "__main__":
    # 获取当前脚本所在的文件夹路径
    current_folder = os.path.dirname(os.path.abspath(__file__))
    rename_pdf_files(current_folder)