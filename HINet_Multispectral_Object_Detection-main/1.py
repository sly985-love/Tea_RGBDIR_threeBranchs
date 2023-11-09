# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/apple.yaml --epochs 400 --device 1 --name sa_RGB_IR
#
import torch

torch.cuda.is_available()
print(torch.cuda.is_available())
# python train.py --weights yolov5m.pt --cfg models/MHT/yolov5m_fusion_apple_dct.yaml --data data/multispectral/apple.yaml --epochs 400 --device 1 --name ma_RGB_IR
#
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/apple.yaml --epochs 400 --device 1 --name sa_RGB_IR
#
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/apple.yaml --epochs 400 --device 1 --name sa_RGB_IR
#
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/apple.yaml --epochs 400 --device 1 --name sa_RGB_IR
#
# python test.py --weights runs/train/ma_RGB_IR/weights/best.pt  --data data/multispectral/apple.yaml  --device 1 --name ma_RGB_IR


# ------------20230315的100张图像(最新数据收集，在c2d上标注的标签)

# c2d图像和红外图像
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea.yaml --epochs 500 --device 0 --name st2_c2d_IR
# python test.py --weights runs/train/st2_c2d_IR2/weights/best.pt  --data data/multispectral/tea.yaml  --device 1 --name st2_c2d_IR

# python train.py --weights yolov5m.pt --cfg models/MHT/yolov5m_fusion_apple_dct.yaml --data data/multispectral/tea.yaml --epochs 500 --device 1 --name mt2_c2d_IR
# python test.py --weights runs/train/mt2_c2d_IR/weights/best.pt  --data data/multispectral/tea.yaml  --device 1 --name mt2_c2d_IR

# python train.py --weights yolov5m.pt --cfg models/MHT/yolov5m_fusion_apple_dct.yaml --data data/multispectral/tea.yaml --epochs 1000 --device 1 --name mt2_c2d_IR
# python test.py --weights runs/train/mt2_c2d_IR2/weights/best.pt  --data data/multispectral/tea.yaml  --device 1 --name mt2_c2d_IR


# c2d图像和深度图像
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_depth.yaml --epochs 500 --device 0 --name st2_c2d_depth
# python test.py --weights runs/train/st2_c2d_depth/weights/best.pt  --data data/multispectral/tea_c2d_depth.yaml  --device 1 --name st2_c2d_IR

# python train.py --weights yolov5m.pt --cfg models/MHT/yolov5m_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_depth.yaml --epochs 500 --device 1 --name mt2_c2d_depth
# python test.py --weights runs/train/mt2_c2d_depth/weights/best.pt  --data data/multispectral/tea_c2d_depth.yaml --device 1 --name mt2_c2d_IR



# c2d图像和color图像
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_color.yaml --epochs 500 --device 0 --name st2_c2d_color
# python test.py --weights runs/train/st2_c2d_color/weights/best.pt  --data data/multispectral/tea_c2d_color.yaml  --device 1 --name st2_c2d_IR

# python train.py --weights yolov5m.pt --cfg models/MHT/yolov5m_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_color.yaml --epochs 500 --device 1 --name mt2_c2d_color
# python test.py --weights runs/train/mt2_c2d_color/weights/best.pt  --data data/multispectral/tea_c2d_color.yaml  --device 1 --name mt2_c2d_IR



# color图像和depth图像
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_color_depth.yaml --epochs 500 --device 0 --name st2_color_depth
# python test.py --weights runs/train/st2_color_depth/weights/best.pt  --data data/multispectral/tea_color_depth.yaml  --device 1 --name st2_color_depth

# python train.py --weights yolov5m.pt --cfg models/MHT/yolov5m_fusion_apple_dct.yaml --data data/multispectral/tea_color_depth.yaml --epochs 500 --device 1 --name mt2_color_depth
# python test.py --weights runs/train/mt2_color_depth/weights/best.pt  --data data/multispectral/tea_color_depth.yaml  --device 1 --name mt2_color_depth



# color图像和ir图像
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_color_ir.yaml --epochs 500 --device 0 --name st2_color_ir
# python test.py --weights runs/train/st2_color_ir/weights/best.pt  --data data/multispectral/tea_color_ir.yaml --device 1 --name st2_color_ir

# python train.py --weights yolov5m.pt --cfg models/MHT/yolov5m_fusion_apple_dct.yaml --data data/multispectral/tea_color_ir.yaml --epochs 500 --device 1 --name mt2_color_ir
# python test.py --weights runs/train/mt2_color_ir/weights/best.pt  --data data/multispectral/tea_color_ir.yaml  --device 1 --name mt2_color_ir

#20230318需要跑的实验
#———————————————————————————————————————————————————————————————————————————————————————————
# c2d图像和红外图像
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea.yaml --epochs 1000 --device 0 --name st2_c2d_IR
# python test.py --weights runs/train/tea/weights/best.pt  --data data/multispectral/tea.yaml --device 1 --name tea
# c2d图像和深度图像
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_depth.yaml --epochs 1000 --device 0 --name st2_c2d_depth
# python test.py --weights runs/train/tea_c2d_depth/weights/best.pt  --data data/multispectral/tea_c2d_depth.yaml --device 1
# c2d图像和add图像
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_add.yaml--epochs 1000 --device 0 --name st2_c2d_color
# python test.py --weights runs/train/st2_c2d_depth/weights/best.pt  --data data/multispectral/tea_c2d_depth.yaml --device 1
# c2d图像和addW图像
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_addW.yaml --epochs 1000 --device 0 --name st2_c2d_color
# python test.py --weights runs/train/tea_c2d_addW/weights/best.pt  --data data/multispectral/tea_c2d_addW.yaml --device 1
# c2d图像和addab图像
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_addab.yaml --epochs 1000 --device 0 --name st2_c2d_color
# python test.py --weights runs/train/tea_c2d_addab/weights/best.pt  --data data/multispectral/tea_c2d_addab.yaml --device 1
# c2d图像和3p图像
# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_add3p.yaml--epochs 500 --device 0 --name st2_c2d_color
# python test.py --weights runs/train/st2_c2d_depth/weights/best.pt  --data data/multispectral/tea_c2d_add3p.yaml --device 1 --name st2_c2d_depth



# python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea.yaml --epochs 1000 --device 1 --name tea; python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_depth.yaml --epochs 1000 --device 1 --name tea_c2d_depth; python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_add.yaml--epochs 1000 --device 1 --name tea_c2d_add; python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_addW.yaml --epochs 1000 --device 1 --name tea_c2d_addW; python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_addab.yaml --epochs 1000 --device 1 --name tea_c2d_addab; python train.py --weights best.pt --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_add3p.yaml--epochs 100 --device 1 --name tea_c2d_add3p


# python train.py  --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --data data/multispectral/tea_c2d_buds_ir.yaml --epochs 500 --device 1 --name st2_buds_ir_nopre
# python test.py --weights runs/train/st2_buds_ir_nopre/weights/best.pt  --data data/multispectral/tea_c2d_buds_ir.yaml --device 1 --name st2_buds_ir_nopre



# ###########################20230325########################################

# python train.py --name tea_ir_depth --data data/mutil_feature/tea_ir_depth.yaml  --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
# python train.py --name tea_c2d_depth  --data data/mutil_feature/tea_c2d_depth.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
# python test.py --weights D:\帅璐宇\RGBD_TEA\HINet\tea_c2d_depth\weights\best.pt  --data data/mutil_feature/tea_c2d_depth.yaml --device 0 --name tea_c2d_depth

# python train.py --name tea_c2d_ir  --data data/mutil_feature/tea_c2d_ir.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
# python test.py --weights D:\帅璐宇\RGBD_TEA\HINet\tea_c2d_ir\weights\best.pt  --data data/mutil_feature/tea_c2d_ir.yaml --device 0 --name tea_c2d_ir

# python train.py --name c2dx_ir_depth_aw --data data/multi_pixle_feature/c2dx_ir_depth_aw.yaml  --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_add --data data/multi_pixle_feature/c2d2_ir_add.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
# python test.py --weights D:\帅璐宇\RGBD_TEA\HINet\c2d2_ir_add\weights\best.pt  --data data/multi_pixle_feature/c2d2_ir_add.yaml --device 0 --name c2d2_ir_add

# python train.py --name c2d2_ir_subtract --data data/multi_pixle_feature/c2d2_ir_subtract.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
# python test.py --weights D:\帅璐宇\RGBD_TEA\HINet\c2d2_ir_subtract\weights\best.pt  --data data/multi_pixle_feature/c2d2_ir_subtract.yaml --device 0 --name c2d2_ir_subtract

# python train.py --name c2d2_ir_aw --data data/multi_pixle_feature/c2d2_ir_aw.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
# python test.py --weights D:\帅璐宇\RGBD_TEA\HINet\c2d2_ir_aw\weights\best.pt  --data data/multi_pixle_feature/c2d2_ir_aw.yaml --device 0 --name c2d2_ir_aw

# python train.py --name c2d2_ir_depth_aw --data data/multi_pixle_feature/c2d2_ir_depth_aw.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
# python test.py --weights D:\帅璐宇\RGBD_TEA\HINet\c2d2_ir_depth_aw\weights\best.pt  --data data/multi_pixle_feature/c2d2_ir_depth_aw.yaml --device 0 --name c2d2_ir_depth_aw

# python train.py --name c2d_buds_depth --data data/multi_pixle_feature/c2d_buds_depth.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
# python train.py --name c2d_buds_ir --data data/multi_pixle_feature/c2d_buds_ir.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;

#

# python train.py --name tea_c2d_depth  --data data/mutil_feature/tea_c2d_depth.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
# python train.py --name tea_c2d_ir  --data data/mutil_feature/tea_c2d_ir.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_depth_aw --data data/multi_pixle_feature/c2d2_ir_depth_aw.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0; python train.py --name c2d2_ir_aw --data data/multi_pixle_feature/c2d2_ir_aw.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0; python train.py --name c2d2_ir_add --data data/multi_pixle_feature/c2d2_ir_add.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0; python train.py --name c2d2_ir_subtract --data data/multi_pixle_feature/c2d2_ir_subtract.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;


# python train.py --name c2d_buds_depth --data data/multi_pixle_feature/c2d_buds_depth.yaml--cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0; python train.py --name c2d_buds_ir --data data/multi_pixle_feature/c2d_buds_ir.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 0;
