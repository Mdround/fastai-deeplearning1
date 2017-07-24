# Code adapted from 'Deep Learning for Coders' (fast.ai courses)
... and a few extra experiments with additional datasets.

This repo is based on [Practical Deep Learning for Coders](http://course.fast.ai/). 
It contains some adapted versions of their code, and some experiments of my own.

Major adaptations include:
- converting the code from Python 2.7 to Python 3.6
- adding plenty of my own comments - what worked, what didn't, why, etc.

There are some odd little things I've built along the way. I found some simple bash commands for manually adjusting the GPU fans on NVIDIA cards, so these are now wrapped up in a simple set_gpu_fan_speed() function (currently to be found here: https://github.com/Mdround/fastai-deeplearning1/blob/master/deeplearning1/_MDR/2_distracted_driver/utils_MDR.py). 
