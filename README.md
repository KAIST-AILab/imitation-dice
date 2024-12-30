# DemoDICE and LobsDICE
This repository is the official implementation of 
- [DemoDICE: Offline Imitation Learning with Supplementary Imperfect Demonstrations](https://openreview.net/pdf?id=BrPdX1bDZkQ) (presented at ICLR 2022).
- [LobsDICE: Offline Learning from Observation via Stationary Distribution Correction Estimation](https://arxiv.org/abs/2202.13536) (presented at NeurIPS 2022).

## Installation Guide

### MuJoCo
- Download [MuJoCo](https://mujoco.org/) version 2.1.0
- Extract the downloaded `mujoco210` directory into `~/.mujoco/mujoco210`
- Insert the following commands in `~/.bashrc`.
    ```
    export LD_LIBRARY_PATH="$HOME/.mujoco/mujoco210/bin:$LD_LIBRARY_PATH"
    ```

### Conda Environment
1. Create conda environment and activate it:
    ```
    conda env create -f environment.yml
    conda activate imitation-dice
    ```
2. (Optional) Install 'd4rl':
    ```
    pip install git+https://github.com/rail-berkeley/d4rl@master#egg=d4rl
    ```
3. (Optional) Issues with mujoco-py
    - Please see [Troubleshooting](https://github.com/openai/mujoco-py#troubleshooting) in [mujoco-py](https://github.com/openai/mujoco-py)

### How to Run
1. DemoDICE
    ```
    python lfd_mujoco.py \
      --env_id=Hopper-v2 \
      --imperfect_dataset_names=expert-v2 \
      --imperfect_dataset_names=random-v2 \ 
      --imperfect_num_trajs=100 \
      --imperfect_num_trajs=500 \
      --algorithm=demodice
    ```
2. LobsDICE
    ```
    python lfo_mujoco.py \
      --env_id=Hopper-v2 \
      --imperfect_dataset_names=expert-v2 \
      --imperfect_dataset_names=medium-v2 \
      --imperfect_dataset_names=random-v2 \ 
      --imperfect_num_trajs=100 \
      --imperfect_num_trajs=500 \
      --imperfect_num_trajs=500 \
      --algorithm=lobsdice
    ```

### Bibtex
[DemoDICE: Offline Imitation Learning with Supplementary Imperfect Demonstrations](https://openreview.net/pdf?id=BrPdX1bDZkQ)
```
@inproceedings{kim2022demodice,
  title     = {DemoDICE: Offline Imitation Learning with Supplementary Imperfect Demonstrations},
  author    = {Geon-Hyeong Kim and Seokin Seo and Jongmin Lee and Wonseok Jeon and HyeongJoo Hwang and Hongseok Yang and Kee-Eung Kim},
  booktitle = {International Conference on Learning Representations},
  year      = {2022}
}
```
[LobsDICE: Offline Learning from Observation via Stationary Distribution Correction Estimation](https://arxiv.org/abs/2202.13536)
```
@article{kim2022lobsdice,
  title   = {LobsDICE: Offline Learning from Observation via Stationary Distribution Correction Estimation},
  author  = {Geon-Hyeong Kim and Jongmin Lee and Youngsoo Jang and Hongseok Yang and Kee-Eung Kim},
  journal = {Advances in Neural Information Processing Systems},
  year    = {2022}
}
```
