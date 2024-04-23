# GLM-learning

## Utilities 

You can execute 
`python cp_wudao.py <num>`
to copy <num> files to `/dataset/fd5061f6/chinese_data/WuDao_processed` in docker container.

This script can help you make a toy dataset to debug and learn the whole pipeline of [GLM](https://github.com/THUDM/GLM).

If your WuDao dataset is downloaded from [BAAI data platform](https://data.baai.ac.cn/data), you need run 
`python process_wudao.py` to transform the original format into the format satisfied for `pretrain_glm.py`.

## Notes & Diary

### Hardware

I explored this project by myself with my own homelab:

1. Machine1:
    1. annoymous motherboard with name X99M-G2
    2. RTX 2080Ti 22G * 2
    3. Xeon E5 2650v4 
    4. 88G Memory
    5. Ubuntu 18.04 LTS
2. Machine2: 
    1. Asus B450M pro-gaming
    2. AMD Ryzen 5 3600 
    3. RTX 3080 20G * 1
    4. 32G Memory
    5. Ubuntu 20.04 LTS
3. Machine3:
    1. MSI B460M Mortar Wifi
    2. Intel Core I3 10100t
    3. RTX 2080Ti 22G * 1
    4. 48G Memory 
    5. Ubuntu 20.04 LTS
4. Machine4 (is not enabled):
    1. ASUS Z9ped8-ws 
    2. Xeon E5 2670v2 * 2
    3. 16G Memory (will be extended)
    4. Tesla V100 16G SXM2 * 4
    5. the OS is not installed
    
I have been set up a swarm to exploit my machines. Actually, two machines' operating system were Win10 with WSL in the early stages. 
It's really hard to build a distributed system for deepspeed and NCCL, so that I installed Ubuntu 20.04 for them finally. 
The exploring details for system building can be found in [my article on zhihu](https://zhuanlan.zhihu.com/p/692657719).


### Diary 

Other records during my exploring also can be found in [my record on zhihu](https://zhuanlan.zhihu.com/p/693793952). It will be updated for long. 
    
### Notes 

`GLM代码分析.png` is note of analyzing the pretraining of GLM, especially the relevant code of lazy loader and scatter loader. 
It will help you understand the difference between running `pretrain_glm.py` on one machine and more machines.

![GLM code analyzing](GLM代码分析.png)
