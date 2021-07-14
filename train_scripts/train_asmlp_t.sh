CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7, python -m torch.distributed.launch --nproc_per_node 8 --nnodes=1 --node_rank=0 \
 main.py --cfg configs/as_tiny_patch4_shift5_224.yaml --data-path /imagenet \
--batch-size 128 --cache-mode no --accumulation-steps 0  --output output
