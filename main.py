import gymnasium as gym

import math
import random
from collections import namedtuple, deque
from itertools import count

import matplotlib
import matplotlib.pyplot as plt

import torch
import torch_directml


env = gym.make("CartPole-v1")

# In interactive mode (enabled with plt.ion()):
# - newly created figures will be shown immediately;
# - figures will automatically redraw on change;
# - `pyplot.show` will not block by default.
plt.ion()

# check if using DirectML or not
import imp
try:
    imp.find_module('torch_directml')
    # https://learn.microsoft.com/en-us/windows/ai/directml/gpu-pytorch-windows
    device = torch_directml.device()
except ImportError:
    torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Experience memory: https://deeplizard.com/learn/video/Bcuj2fTH4_4
# At time t, the agent's experience e_t is defined as this tuple:
# e_t = (s_t, a_t, r_{t+1}, s_{t+1})
# which gives us information about its current state, the action taken from state s_t, the reward at
# t+1, and the next state in the environment (at t+1). The last one, we won't know of course unless
# this experience is in at least 1 timestep in the past. (you can't see the future!)
Transition = namedtuple('Transition', ('state', 'action', 'next_state', 'reward'))

class ReplayMemory(object):
    # TODO