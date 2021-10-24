import numpy as np
import torch
import paddle
from reprod_log import ReprodLogger, ReprodDiffHelper

lrt = torch.load('loss_dic_torch.bin')
lrp = paddle.load('loss_dic_paddle.bin')

paddle_list = []
torch_list = []
for k, v in lrt.items():
    torch_list.append(v)
for k, v in lrp.items():
    paddle_list.append(v)

# 加载ReprodLogger
rl_torch = ReprodLogger()
rl_paddle = ReprodLogger()
rl_torch.add('backward_loss', np.array(torch_list))
rl_paddle.add('backward_loss', np.array(paddle_list))
rl_torch.save('../log_reprod/b_loss_torch.npy')
rl_paddle.save('../log_reprod/b_loss_paddle.npy')



diff = ReprodDiffHelper()
info_torch = diff.load_info('../log_reprod/b_loss_torch.npy')
info_paddle = diff.load_info('../log_reprod/b_loss_paddle.npy')
diff.compare_info(info1=info_torch, info2=info_paddle)
diff.report(diff_method='mean', diff_threshold=1e-5, path='../log_diff/loss_diff.txt')











