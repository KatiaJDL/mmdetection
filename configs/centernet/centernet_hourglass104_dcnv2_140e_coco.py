_base_ = './centernet_resnet18_dcnv2_140e_coco.py'

work_dir = 'exp/centernet/coco/hourglass_dcnv2_140e/'

model = dict(
    backbone=dict(
        _delete_=True,
        type='HourglassNet',
        num_stacks=2, #2 for CenterNet, 1 for CenterPoly
        norm_cfg=dict(type='BN', requires_grad=True),
        pretrained=None,
        init_cfg=None),
    neck=None,
    bbox_head=dict(in_channel=256))

data = dict(
    samples_per_gpu = 4,
    workers_per_gpu = 4
)
