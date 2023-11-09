



# python train.py --name tea3_c2d_depth  --data data/mutil3_feature/tea_c2d_depth.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 1;
# python train.py --name tea3_c2d_ir   --data data/mutil3_feature/tea_c2d_ir.yaml   --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 1;
# python train.py --name tea3_ir_depth   --data data/mutil3_feature/tea_ir_depth.yaml   --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 1;
# python train.py --name tea3_c2d2_ir_depth_aw  --data data/multi3_pixle_feature/c2d2_ir_depth_aw.yaml   --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 1;


# python train.py --name tea3_c2d_depth  --data data/mutil3_feature/tea_c2d_depth.yaml --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 1; python train.py --name tea3_c2d_ir   --data data/mutil3_feature/tea_c2d_ir.yaml   --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 1; python train.py --name tea3_ir_depth   --data data/mutil3_feature/tea_ir_depth.yaml   --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 1; python train.py --name tea3_c2d2_ir_depth_aw  --data data/multi3_pixle_feature/c2d2_ir_depth_aw.yaml   --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 1;




# python train.py --name dct  --data data/mutil_feature/tea_ir_depth.yaml   --cfg models/MHT/yolov5s_fusion_apple_dct.yaml --epochs 2000 --batch-size 4  --device 1;

# python train.py --name sly_dct  --data data/mutil_feature/tea_ir_depth.yaml   --cfg models/MHT/yolov5s_fusion_apple_sly_dct.yaml  --epochs 2000 --batch-size 4  --device 1;

#AttributeError: module 'distutils' has no attribute 'version'