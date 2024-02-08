method = 'TAU'
project='openstl'
# model
spatio_kernel_enc = 3
spatio_kernel_dec = 3
model_type = 'tau'
hid_S = 128
hid_T = 512
N_T = 12
N_S = 2
alpha = 0.1
# training
lr = 1e-3
batch_size = 2  # bs = 4 x 4GPUs
drop_path = 0.1
sched = 'onecycle'
save_best_hook = dict()
wandb_hook = dict()