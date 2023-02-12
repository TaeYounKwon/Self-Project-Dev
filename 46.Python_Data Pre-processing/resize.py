import os
import glob
import cv2

# 경로 변경 필요
root_path = "C:/Users/user/Documents/03.dataset/230206_dataset/helicopter"
new_root = "C:/Users/user/Documents/03.dataset/230206_dataset/helicopter_total"
small_img_root = "C:/Users/user/Documents/03.dataset/230206_dataset/helicopter_small"

# 폴더 삭제
# try: 
#     os.remove(new_root)
#     os.remove(small_img_root)
# except:
#     pass

# 폴더 생성
os.makedirs(new_root, exist_ok= True)
os.makedirs(small_img_root, exist_ok= True)

# 모든 이미지 (경로 변경 필요)
jpg_paths = glob.glob(os.path.join(root_path, "", '.jpg'))
png_paths = glob.glob(os.path.join(root_path, "", '.png'))
image_paths = jpg_paths + png_paths

# 최소 사이즈
IMG_SIZE = 640/4
COUNT = 0
small_img_list, small_size_list, small_size_paths = [], [], []
for index, image_path in enumerate(image_paths):
    img = cv2.imread(image_path)
    # cv2.imwrite( os.path.join(newroot, f'heli{index}.png'), img)
    try:
        if (img.shape[0] < IMG_SIZE) | (img.shape[1] < IMG_SIZE) :
            img_name = image_path.split('\')[-1]
            small_img_list.append(img_name)
            small_size_list.append((img.shape[0], img.shape[1]))
            small_size_paths.append(image_path)
            # cv2.imwrite( os.path.join(small_imgroot, f'heli{COUNT}.png'), img)
            COUNT += 1
        else:
            pass
    except Exception as e:
        print(e, '\t', image_path)

for small_size_path in small_size_paths:
    image = cv2.imread(small_size_path)

    # if 
    # img_640 = image.resize())
    # img_480 = 

# for i in range(len(small_img_list)):
#     print(small_img_list[i], small_size_list[i])
# print(''100)
# print("No. of total images: ", len(image_paths))
# print("No. of small images: ", len(small_img_list))