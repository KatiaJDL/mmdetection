_base_ = './centernet_resnet18_dcnv2_140e_coco.py'

data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4)

work_dir = 'exp/centernet/coco/resnet18_dcnv2_1x4_140e/'
