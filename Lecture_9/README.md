# Assignment for Lecture 9
Make Python >=3.5 virtual environment called "env" (can be changed):
```
virtualenv -p python3 env
```

Install OpenAI gym, follow:
```
https://github.com/openai/gym#installation3.
```

Install tensorflow+tensorboard<=1.15.04, follow:
```
https://www.tensorflow.org/install/pip
```

Install Stable-Baselines, follow:
```
https://stable-baselines.readthedocs.io/en/master/guide/install.html5.
```

Train the model:
```
Run assignment1.py
set train_model = False
```

Test the model:
```
Run assignment1.py 
set train_model = False
```

Observe the training with TensorBoard
```
tensorboard --logdir ./logs
```

## Assignment - Vivian

![](gifs/dqn_graph.png)


|Timesteps: 50000    | Timesteps: 100000    | Timesteps: 150000|
| --- | --- |
|![](gifs/50000.gif) | ![](gifs/100000.gif) | ![](gifs/150000.gif)|




