from PIL import Image
import os


def crop_images(input_folder, output_folder, horizontal_split, vertical_split):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 打开图片文件
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # 获取图片的宽度和高度
            width, height = img.size

            # 计算每个部分的尺寸
            horizontal_size = width // horizontal_split
            vertical_size = height // vertical_split

            # 裁剪并保存图片
            for i in range(horizontal_split):
                for j in range(vertical_split):
                    # 计算裁剪区域的坐标
                    left = i * horizontal_size
                    upper = j * vertical_size
                    right = left + horizontal_size
                    lower = upper + vertical_size

                    # 裁剪图片
                    if i == horizontal_split - 1 and right < width:
                        right = width
                    if j == vertical_split - 1 and lower < height:
                        lower = height

                    cropped_img = img.crop((left, upper, right, lower))

                    # 保存裁剪后的图片
                    base, extension = os.path.splitext(filename)
                    new_filename = f"{base}_{i}_{j}{extension}"
                    new_path = os.path.join(output_folder, new_filename)
                    cropped_img.save(new_path)
                    print(f"Saved: {new_path}")


# 设置参数
input_folder = r"E:\MD数据\断裂\测试 (2)\新建文件夹"  # 输入文件夹路径
output_folder = r"E:\MD数据\划痕\分割\2.1"  # 输出文件夹路径
horizontal_split = 2   # 横向分割数
vertical_split = 1  # 纵向分割数

# 执行裁剪图片函数
crop_images(input_folder, output_folder, horizontal_split, vertical_split)