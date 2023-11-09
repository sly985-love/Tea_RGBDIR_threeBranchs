# python train.py --cfg models/transformer/yolov5s_fusion_add_apples.yaml  --data data/multispectral/tea.yaml  --device 0 --name ts_add_RGB_D_IR

# python train.py --cfg models/transformer/yolov5s_fusion_transformer_apples.yaml  --data data/multispectral/tea.yaml --device 1  --name ts_tran_RGB_D_IR

# python train.py --cfg models/transformer/yolov5s_fusion_transformerx3_apples.yaml  --data data/multispectral/tea.yaml --device 1 --name ts_tranx3_RGB_D_IR
#
#runs/train/ts_add_RGB_D_IR/weights/best.pt

# python test.py --weight runs/train/ts_add_RGB_D_IR/weights/best.pt --data data/multispectral/tea.yaml  --device 0 --name ts_add_RGB_D_IR
#   return _VF.meshgrid(tensors, **kwargs)  # type: ignore[attr-defined]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 2/2 [00:21<00:00, 10.90s/it]
#                  all         112        1696       0.563       0.665       0.582       0.197       0.266
# Speed: 21.7/1.7/23.4 ms inference/NMS/total per 640x640 image at batch-size 64
# Results saved to runs\test\ts_add_RGB_D_IR
# 112 labels saved to runs\test\ts_add_RGB_D_IR\labels

# python test.py --weight runs/train/ts_add_RGB_D_IR/weights/best.pt --data data/multispectral/tea.yaml  --device 0 --name ts_add_RGB_D_IR
# python test.py --weight runs/train/ts_add_RGB_D_IR/weights/best.pt --data data/multispectral/tea.yaml  --device 0 --name ts_add_RGB_D_IR






# python train.py --cfg models/transformer/yolov5s_fusion_add_apples.yaml  --data data/multispectral/apple.yaml  --device 0 --name s_add_RGB_D_IR
# python train.py --cfg models/transformer/yolov5s_fusion_add_apples.yaml  --data data/multispectral/apple.yaml  --device 0 --name s_add_RGB_D_IR

# python train.py --cfg models/transformer/yolov5s_fusion_transformer_apples.yaml  --data data/multispectral/apple.yaml --device 1  --name s_tran_RGB_D_IR

# python train.py --cfg models/transformer/yolov5s_fusion_transformerx3_apples.yaml  --data data/multispectral/apple.yaml --device 0 --name s_tranx3_RGB_D_IR
#





# ------------20230315的100张图像(最新数据收集，在c2d上标注的标签)

# c2d图像和红外图像和深度图像
# python train.py --cfg models/transformer/yolov5s_fusion_add_apples.yaml  --data data/multispectral/tea2.yaml  --device 0 --name s_add_c2d_ir_depth
# python test.py --weight runs/train/s_add_c2d_ir_depth/weights/best.pt --data data/multispectral/tea2.yaml  --device 0 --name s_add_c2d_ir_depth

# python train.py --cfg models/transformer/yolov5s_fusion_transformer_apples.yaml  --data data/multispectral/tea2.yaml --device 1  --name s_tran_c2d_ir_depth
# python test.py --weight runs/train/s_tran_c2d_ir_depth/weights/best.pt --data data/multispectral/tea2.yaml  --device 1 --name s_tran_c2d_ir_depth

# python train.py --cfg models/transformer/yolov5s_fusion_transformerx3_apples.yaml  --data data/multispectral/tea2.yaml --device 1 --name s_tranx3_c2d_ir_depth
# python test.py --weight runs/train/s_tranx3_c2d_ir_depth/weights/best.pt --data data/multispectral/tea2.yaml  --device 0 --name s_tranx3_c2d_ir_depth


# color图像和红外图像和深度图像
# python train.py --cfg models/transformer/yolov5s_fusion_add_apples.yaml  --data data/multispectral/tea3.yaml  --device 0 --name s_add_color_ir_depth
# python train.py --cfg models/transformer/yolov5s_fusion_transformer_apples.yaml  --data data/multispectral/tea3.yaml --device 0  --name s_tran_color_ir_depth
# python train.py --cfg models/transformer/yolov5s_fusion_transformerx3_apples.yaml  --data data/multispectral/tea3.yaml --device 0 --name s_tranx3_color_ir_depth


# ################################20230325###################################
# python train.py --name 3_add --data data/multispectral/tea.yaml --cfg models/transformer/yolov5s_fusion_add_apples.yaml   --epochs 2500 --batch-size 4  --device 1;
# python test.py --weight D:\帅璐宇\RGBD_TEA\multispectral_3\3_add\weights\best.pt --data data/multispectral/tea.yaml  --device 0 --name 3_add

# python train.py --name 3_t --data data/multispectral/tea.yaml --cfg models/transformer/yolov5s_fusion_transformer_apples.yaml   --epochs 2500 --batch-size 4  --device 1;
# python test.py --weight D:\帅璐宇\RGBD_TEA\multispectral_3\3_t\weights\best.pt --data data/multispectral/tea.yaml  --device 0 --name 3_t

# python train.py --name 3_t3 --data data/multispectral/tea.yaml --cfg models/transformer/yolov5s_fusion_transformerx3_apples.yaml   --epochs 2500 --batch-size 4  --device 1;
# python test.py --weight D:\帅璐宇\RGBD_TEA\multispectral_3\3_t3\weights\best.pt --data data/multispectral/tea.yaml  --device 0 --name 3_t3

#

# python train.py --name 3_add --data data/multispectral/tea.yaml --cfg models/transformer/yolov5s_fusion_add_apples.yaml   --epochs 2500 --batch-size 4  --device 1; python train.py --name 3_t --data data/multispectral/tea.yaml --cfg models/transformer/yolov5s_fusion_transformer_apples.yaml   --epochs 2500 --batch-size 4  --device 1; python train.py --name 3_t3 --data data/multispectral/tea.yaml --cfg models/transformer/yolov5s_fusion_transformerx3_apples.yaml   --epochs 2500 --batch-size 4  --device 1;


# python train.py --name 3_t --data data/multispectral/tea.yaml --cfg models/transformer/yolov5s_fusion_transformer_apples.yaml   --epochs 1500 --batch-size 4  --device 1; python train.py --name 3_t3 --data data/multispectral/tea.yaml --cfg models/transformer/yolov5s_fusion_transformerx3_apples.yaml   --epochs 1500 --batch-size 4  --device 1;
