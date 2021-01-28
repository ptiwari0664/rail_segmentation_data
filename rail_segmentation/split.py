print ('hello')

import glob
from random import shuffle
import shutil

all_images = glob.glob('/home/puneet/Desktop/DATA_RAIL/ML_challenge/rail_segmentation/Images/*.jpg')
print(len(all_images))

shuffle(all_images)

mask_dir = '/home/puneet/Desktop/DATA_RAIL/ML_challenge/rail_segmentation/Masks/'

x_train_dir = '/home/puneet/Desktop/DATA_RAIL/ML_challenge/rail_segmentation/train/'
y_train_dir = '/home/puneet/Desktop/DATA_RAIL/ML_challenge/rail_segmentation/trainann/'
x_valid_dir = '/home/puneet/Desktop/DATA_RAIL/ML_challenge/rail_segmentation/val/'
y_valid_dir = '/home/puneet/Desktop/DATA_RAIL/ML_challenge/rail_segmentation/valann/'


l = int(len(all_images)*0.8)
for i in range(len(all_images)):
  src_img = all_images[i]
  name = src_img.split('/')[-1]
  # print(name)
  mask_name = name.replace('.jpg', '.png')
  src_mask = mask_dir + mask_name

  if(i<l):
    des_img = x_train_dir + name
    des_mask = y_train_dir + mask_name
  else:
    des_img = x_valid_dir + name
    des_mask = y_valid_dir + mask_name
  
  shutil.copy(src_img, des_img)
  shutil.copy(src_mask, des_mask)
  
  # if(i>210):
  #   break;
  print(i)
