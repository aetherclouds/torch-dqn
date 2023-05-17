
Based on https://github.com/pytorch/tutorials/blob/main/intermediate_source/reinforcement_q_learning.py
## Index
- `adam.ipynb`: Implementation of the Adam optimizer.
- `main.ipynb`: Implementation of the DQN.
- `from-github.ipynb`: The code downloaded from GitHub.
## Setting up
```bash
python -m venv venv
venv/Scripts/activate
pip install requirements-py311.txt
```
## Running
You may run the notebooks from an IDE, or from `jupyter lab .`
## Note (AMD+Windows)
> "After seeing those news, I can't find any benchmarks available, probably because no sane person (that understand the ML ecosystem) has a Windows PC with an AMD GPU." - [imp2](https://www.reddit.com/r/Amd/comments/qe4847/comment/hi2c4qf/?utm_source=share&utm_medium=web3x)

I have an RX480 8GB, so I followed [this guide](https://learn.microsoft.com/en-us/windows/ai/directml/gpu-pytorch-windows) to use it on Windows. As of right now, this approach means that we have to use:
- PyTorch 1.13
- Python 3.9

In a nutshell (you don't have to run these -- just left it here for documentation):
```bash
pip install torch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1
pip install torch-directml
```
So then, the set-up would be:
```bash
# for Windows AMD
py -3.9 -m venv venv
venv/Scripts/activate
pip install requirements-amd.txt
```
Alas, it isn't working. At least I tried.