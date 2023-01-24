_base_ = './centernet_resnet18_dcnv2_140e_cityscapes.py'

work_dir = 'exp/centerpoly/cityscapes/hourglass_dcnv2_140e/'

model = dict(
    backbone=dict(
        _delete_=True,
        type='HourglassNet',
        num_stacks=2, #2 for CenterNet, 1 for CenterPoly
        norm_cfg=dict(type='BN', requires_grad=True),
        pretrained=None,
        init_cfg=None))
