# AS-MLP architecture for Image Classification

## Model Zoo

### Image Classification on ImageNet-1K

| Network | Resolution | Top-1 (%) | Params | FLOPs | Throughput (image/s) | model |
|:---:|:---:|:---:|:---:| :---:| :---:|:---:|
| AS-MLP-T | 224x224 | 81.3 | 28M | 4.4G | 1047 | [download](https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_tiny_patch4_window7_224.pth) |
| AS-MLP-S | 224x224 | 83.1 | 50M | 8.5G | 619 | [download](https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_small_patch4_window7_224.pth) |
| AS-MLP-B | 224x224 | 83.3 | 88M | 15.2G | 455 | [download](https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_base_patch4_window7_224.pth) |


## Usage

### Install

- Clone this repo:

```bash
git clone https://github.com/microsoft/Swin-Transformer.git
cd Swin-Transformer
```

- Create a conda virtual environment and activate it:

```bash
conda create -n swin python=3.7 -y
conda activate swin
```

- Install `CUDA==10.1` with `cudnn7` following
  the [official installation instructions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
- Install `PyTorch==1.7.1` and `torchvision==0.8.2` with `CUDA==10.1`:

```bash
conda install pytorch==1.7.1 torchvision==0.8.2 cudatoolkit=10.1 -c pytorch
```

- Install `timm==0.3.2`:

```bash
pip install timm==0.3.2
```

- Install `Apex`:

```bash
git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
```

- Install other requirements:

```bash
pip install opencv-python==4.4.0.46 termcolor==1.1.0 yacs==0.1.8
```

### Data preparation

We use standard ImageNet dataset, you can download it from http://image-net.org/. We provide the following two ways to
load data:

- For standard folder dataset, move validation images to labeled sub-folders. The file structure should look like:
  ```bash
  $ tree data
  imagenet
  ├── train
  │   ├── class1
  │   │   ├── img1.jpeg
  │   │   ├── img2.jpeg
  │   │   └── ...
  │   ├── class2
  │   │   ├── img3.jpeg
  │   │   └── ...
  │   └── ...
  └── val
      ├── class1
      │   ├── img4.jpeg
      │   ├── img5.jpeg
      │   └── ...
      ├── class2
      │   ├── img6.jpeg
      │   └── ...
      └── ...
 
  ```


### Evaluation

To evaluate a pre-trained `AS-MLP` on ImageNet val, run:

```bash
bash train_scripts/test.sh
```


### Training from scratch

To train a `AS-MLP` on ImageNet from scratch, run:

```bash
bash train_scripts/train.sh
```


### Throughput

To measure the throughput, run:

```bash
bash train_scripts/get_throughput.sh
```


<!-- ### Citation
If this project is helpful for you, you can cite our paper:
```
@article{Lian_2021_ASMLP,
author = {Lian, Dongze and Yu, Zehao and Sun, Xing and Gao, Shenghua},
title = {AS-MLP: An Axial Shifted MLP Architecture for Vision},
journal={arXiv preprint arXiv:xxx},
year = {2021}
}
``` -->


### Acknowledgement
The code is built upon [Swin-Transformer](https://github.com/microsoft/Swin-Transformer)
