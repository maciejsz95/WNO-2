import keyboard #Using module keyboard
import gym

env = gym.make('Pendulum-v0')
env.reset()

while True:#making a loop
    try: #used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('a'):
            env.render()
            action = [-1.6]
            observation, reward, done, info = env.step(action)
        if keyboard.is_pressed('d'):
            env.render()
            action = [1.6]
            observation, reward, done, info = env.step(action)
        if keyboard.is_pressed('esc'):
            break
        else:
            env.render()
            action = [0]
            observation, reward, done, info = env.step(action)
    except:
        pass