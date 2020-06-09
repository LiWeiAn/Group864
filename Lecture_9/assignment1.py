import gym

from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines import DQN

env = gym.make('CartPole-v1')
model = DQN(MlpPolicy, env, verbose=1, tensorboard_log='./logs')

# Set whether to train or test
train_model = True
model_filename = 'dqn_cartpole_100000'


# Train model
if train_model:
	model.learn(total_timesteps=100000)
	model.save(model_filename)
# Test model
else:
	model = DQN.load(model_filename)

	obs = env.reset()
	while True:
	    action, _states = model.predict(obs)
	    obs, rewards, dones, info = env.step(action)
	    env.render()
