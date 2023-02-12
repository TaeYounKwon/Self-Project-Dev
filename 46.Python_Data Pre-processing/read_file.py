import os
import glob
import cv2
import matplotlib.pyplot as plt

# 경로 변경 필요
root_path = "C:/Users/user/Documents/03.dataset/230206_dataset/helicopter"
new_root = "C:/Users/user/Documents/03.dataset/230206_dataset/helicopter_total"
resize_img_root = "C:/Users/user/Documents/03.dataset/230206_dataset/helicopter_resized"

# 폴더 삭제
# try: 
#     os.remove(new_root)
#     os.remove(small_img_root)
# except:
#     pass

# 폴더 생성
os.makedirs(new_root, exist_ok= True)
os.makedirs(resize_img_root, exist_ok= True)

# 모든 이미지 (경로 변경 필요)
jpg_paths = glob.glob(os.path.join(root_path, "*", '*.jpg'))
png_paths = glob.glob(os.path.join(root_path, "*", '*.png'))
jpeg_paths = glob.glob(os.path.join(root_path, "*", '*.jpeg'))
image_paths = jpg_paths + png_paths + jpeg_paths

# 최소 사이즈
WIDTH_LIMIT, HEIGHT_LIMIT = 640, 640
small_img_list, small_size_paths = [], []

# 모든 이미지 경로
for index, image_path in enumerate(image_paths):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img_name = image_path.split('\\')[-1]
    RESIZE_FLAG = False

    try:
        # (가로 > 세로) & (가로의 이미지가 640 이하인 경우)
        if (img.shape[1] > img.shape[0]) & (img.shape[1] < WIDTH_LIMIT) :
            RESIZE_FLAG = True
            small_img_list.append(img_name)
            small_size_paths.append(image_path)

            # 가로 비율 유지하면서 resize           
            aspect_ratio = float(WIDTH_LIMIT) / img.shape[1]
            dsize = (WIDTH_LIMIT, int(img.shape[0] * aspect_ratio))
            resized_img = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)

            # 이미지 저장
            cv2.imwrite( os.path.join(new_root, f'heli_{index}.png'), img)
            cv2.imwrite( os.path.join(resize_img_root, f'resize_heli_{index}.png'), resized_img)
            
        # 세로의 이미지가 640 이하인 경우
        elif (img.shape[0] > img.shape[1]) & (img.shape[0] < HEIGHT_LIMIT) :
            RESIZE_FLAG = True
            small_img_list.append(img_name)
            small_size_paths.append(image_path)

            aspect_ratio = float(HEIGHT_LIMIT) / img.shape[0]
            dsize = (int(img.shape[1] * aspect_ratio), HEIGHT_LIMIT)
            
            resized = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)

            # 이미지 저장
            cv2.imwrite( os.path.join(new_root, f'heli_{index}.png'), img)
            cv2.imwrite( os.path.join(resize_img_root, f'resize_heli_{index}.png'), resized_img)

        #  가로, 세로 둘다 640 보다 큰 경우
        else:
            cv2.imwrite(os.path.join(new_root, f'heli_{index}.png'), img)
        
        print(f'{index}/{len(image_paths)}\t' , f'{RESIZE_FLAG}\t', img_name)
    except Exception as e:
        print(e, '\t', image_path)

# print('*'*100)
# print("No. of total images: ", len(image_paths))
# print("No. of small images: ", len(small_img_list))