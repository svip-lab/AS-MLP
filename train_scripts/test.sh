CUDA_VISIBLE_DEVICES=3 python -m torch.distributed.launch --nproc_per_node 1  main.py --eval \
--cfg configs/asmlp_tiny_patch4_shift5_224.yaml --resume checkpoints/asmlp_tiny_patch4_shift5_224.pth --data-path /imagenet
