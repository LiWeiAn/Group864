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
## Graph

![](gifs/dqn_graph.png)


### GIF for timesteps: 50000
![](gifs/50000.gif)

### GIF for timesteps: 100000
![](gifs/100000.gif)

### GIF for timesteps: 150000
![](gifs/150000.gif)





