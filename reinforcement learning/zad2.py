import gym
env = gym.make('Pendulum-v0')
reward, info, done = None, None, None
for i_episode in range(20):
    print("ppp")
    observation = env.reset()
    done = False
    while done != True:
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("cccc")
