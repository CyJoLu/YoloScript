from PIL import Image
import os

def batch_convert_tif_to_jpg(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".tif") or file_name.endswith(".tiff"):
            # 构建输入和输出文件的完整路径
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name.replace(".tif", ".jpg").replace(".tiff", ".jpg"))

            try:
                # 打开TIFF图像并保存为JPEG格式
                with Image.open(input_path) as img:
                    img.convert("RGB").save(output_path, "JPEG")
                print(f"转换成功: {file_name}")
            except Exception as e:
                print(f"转换失败 ({file_name}): {e}")

# 指定TIFF文件夹路径和输出JPEG文件夹路径
tif_folder_path = r"E:\Library\JJWC\YL_dataset1\images"
jpg_output_folder = r"E:\Library\JJWC\YL_dataset1\images"

# 调用函数进行批量转换
batch_convert_tif_to_jpg(tif_folder_path, jpg_output_folder)
