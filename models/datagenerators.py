import os
import glob
import numpy as np
import SimpleITK as sitk
import torch.utils.data as Data


class Dataset(Data.Dataset):
    def __init__(self, CT_images ,MR_images):
        # 初始化
        self.CT_images = CT_images
        self.MR_images = MR_images
    def __len__(self):
        # 返回数据集的大小
        return len(self.CT_images)

    def __getitem__(self, index):
        # 索引数据集中的某个数据，还可以对数据进行预处理
        # 下标index参数是必须有的，名字任意
        # CT_image_arr=self.CT_images[index]
        CT_image_arr = sitk.GetArrayFromImage(sitk.ReadImage(self.CT_images[index]))[np.newaxis, ...]
        MR_img_arr = sitk.GetArrayFromImage(sitk.ReadImage(self.MR_images[index]))[np.newaxis, ...]

        # 返回值自动转换为torch的tensor类型
        return CT_image_arr ,MR_img_arr