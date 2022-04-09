import argparse
ENV_ID = [
    'Hopper-v2',
    'Walker2d-v2',
    'HalfCheetah-v2',
    'Ant-v2',
]

def boolean(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm', default='demodice', type=str)
    parser.add_argument('--env_id', default='Hopper-v2', type=str, choices=ENV_ID)
    # parser.add_argument('--dataset_dir', default='dataset', type=str)
    parser.add_argument('--dataset_dir', default='/ext2/d4rl_noised', type=str)
    parser.add_argument('--expert_dataset_info', default=("expert-v2", 1))
    parser.add_argument('--imperfect_dataset_info', default=(["expert-v2", "random-v2"], [400, 1600]))
    parser.add_argument('--total_iterations', default=int(3e6), type=int)
    parser.add_argument('--save_interval', default=int(1e4), type=int)
    parser.add_argument('--log_interval', default=int(1e4), type=int)
    parser.add_argument('--critic_lr', default=3e-4, type=float)
    parser.add_argument('--actor_lr', default=3e-4, type=float)
    parser.add_argument('--gamma', default=0.99, type=float)
    parser.add_argument('--alpha', default=0.1, type=float)
    parser.add_argument('--hidden_size', default=256, type=int)
    parser.add_argument('--batch_size', default=512, type=int)
    parser.add_argument('--using_absorbing', default=True, type=bool)
    parser.add_argument('--grad_reg_coeffs', default=(0.1, 1e-4))
    parser.add_argument('--resume', default=True, type=bool)
    parser.add_argument('--use_last_layer_bias_cost', default=False, type=bool)
    parser.add_argument('--use_last_layer_bias_critic', default=False, type=bool)
    parser.add_argument('--kernel_initializer', default='he_normal', type=str)
    parser.add_argument('--seed', default=0, type=int)
    return parser