import os
from PIL import Image

def convert_to_jpg(input_path, output_path):
    """
    将图片转换为 JPG 格式
    :param input_path: 输入图片路径
    :param output_path: 输出图片路径
    """
    try:
        # 打开图片
        with Image.open(input_path) as img:
            # 如果图片是 RGBA 模式（包含透明通道），将其转换为 RGB 模式
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, img.split()[-1])
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            # 保存为 JPG 格式
            img.save(output_path, 'JPEG')
            print(f"成功将 {input_path} 转换为 JPG 格式，保存为 {output_path}")
    except Exception as e:
        print(f"转换 {input_path} 时出错: {e}")

def batch_convert_to_jpg(input_folder, output_folder):
    """
    批量将文件夹中的图片转换为 JPG 格式
    :param input_folder: 输入文件夹路径
    :param output_folder: 输出文件夹路径
    """
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        if os.path.isfile(input_path):
            # 获取文件名和扩展名
            name, ext = os.path.splitext(filename)
            # 跳过已经转换过的 JPG 文件
            if ext.lower() == '.jpg':
                continue
            # 生成输出路径
            output_path = os.path.join(output_folder, f"{name}.jpg")
            # 转换图片
            convert_to_jpg(input_path, output_path)

if __name__ == "__main__":
    # 在这里指定输入和输出文件夹
    input_folder = r"E:\美的\434\417" # 输入文件夹路径
    output_folder = r"E:\美的\434\417jpg"  # 输出文件夹路径

    # 执行批量转换
    batch_convert_to_jpg(input_folder, output_folder)