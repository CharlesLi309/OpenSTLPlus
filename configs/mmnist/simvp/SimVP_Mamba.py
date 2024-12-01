method = 'SimVP'
# model
spatio_kernel_enc = 3
spatio_kernel_dec = 3
model_type = 'mamba'
bimamba = True
bimamba_strategy = "add"
hid_S = 64
hid_T = 512
N_T = 2
N_M = 8
N_S = 4
# training
lr = 5e-4
batch_size = 16
drop_path = 0.2
sched = 'cosine'
T_0 = 10
T_mult = 1
opt = 'adamp'
weight_decay = 1e-4
epoch = 200
use_augment=True
augment_params={
    "use_mask": True,
    "use_flip": False,
    "use_crop": False,
    "mask_prob": 0.5,
    "max_mask_ratio": 0.05,
    "max_num_masks": 3
}
clip_grad=0.2
clip_mode="value"
visualize_data=False
