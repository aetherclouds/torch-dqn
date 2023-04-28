Based on https://github.com/pytorch/tutorials/blob/main/intermediate_source/reinforcement_q_learning.py
## Setting up
### Note (AMD@Windows)
> "After seeing those news, I can't find any benchmarks available, probably because no sane person (that understand the ML ecosystem) has a Windows PC with an AMD GPU." - [imp2](https://www.reddit.com/r/Amd/comments/qe4847/comment/hi2c4qf/?utm_source=share&utm_medium=web3x)

I have an RX480 8GB, so I had to follow [this guide](https://learn.microsoft.com/en-us/windows/ai/directml/gpu-pytorch-windows) to use it on Windows. As of right now, this approach means that you'll be using:
- PyTorch 1.13
- Python 3.9

In a nutshell (you don't have to run these -- just left it here for documentation):
```bash
pip install torch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1
pip install torch-directml
```
### Virtual environment
```bash
# for Windows AMD
py -3.9 -m venv venv
venv/Scripts/activate
pip install requirements-amd.txt

# else
python -m venv venv
venv/Scripts/activate
pip install requirements-no-torch.txt
# make sure to install pytorch through wheel or otherwise
pip install torch
```
