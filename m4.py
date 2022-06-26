# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.animation as animation
from matplotlib import pyplot as plt


def create_grid_pos(x_size=5, y_size=5):

    x_pos = np.zeros((y_size, x_size))
    y_pos = np.zeros((y_size, x_size))

    for x in range(x_size):
        y_pos[:, x] = np.arange(y_size)

    for y in range(y_size):
        x_pos[y, :] = np.arange(x_size)

    return x_pos, y_pos


def transverse_wave(x_positions, y_positions, frames_per_cycle=20, wave_len=10, amplitude=1, phase=0, num_frames=100):
    # frames_per_cycle = number of frames per cycle
    # num_frames = frames to be generated
    k = 2 * np.pi / wave_len
    omega = 2 * np.pi / frames_per_cycle
    x_frames = np.zeros(
        (num_frames, x_positions.shape[0], x_positions.shape[1]))
    y_frames = np.zeros(
        (num_frames, y_positions.shape[0], y_positions.shape[1]))

    for t in range(num_frames):
        x_frames[t, :, :] = x_positions
        for x in range(x_positions.shape[1]):
            y_frames[t, :, x] = y_positions[:, x] + amplitude * \
                np.sin(k * x_positions[:, x] - omega * t + phase)

    return x_frames, y_frames


def longitudinal_wave(x_positions, y_positions, frames_per_cycle=20, wave_len=10,  amplitude=1, phase=0, num_frames=100):

    k = 2 * np.pi / wave_len
    omega = 2 * np.pi / frames_per_cycle
    x_frames = np.zeros(
        (num_frames, x_positions.shape[0], x_positions.shape[1]))
    y_frames = np.zeros(
        (num_frames, y_positions.shape[0], y_positions.shape[1]))

    for t in range(num_frames):
        y_frames[t, :, :] = y_positions
        for x in range(x_positions.shape[1]):
            x_frames[t, :, x] = x_positions[:, x] + amplitude * \
                np.sin(k * x_positions[:, x] - omega * t + phase)

    return x_frames, y_frames


def combined_wave(x_positions, y_positions, frames_per_cycle=20, wave_len=[10, 10], amplitude=[1, 1], phase=[0, 0], num_frames=100):
    x_trans, y_trans = transverse_wave(x_positions, y_positions, frames_per_cycle=frames_per_cycle,
                                       wave_len=wave_len[0], amplitude=amplitude[0], phase=phase[0], num_frames=num_frames)
    x_long, y_long = longitudinal_wave(x_positions, y_positions, frames_per_cycle=frames_per_cycle,
                                       wave_len=wave_len[1], amplitude=amplitude[1], phase=phase[1], num_frames=num_frames)
    x_comb = x_long
    y_comb = y_trans
    return x_comb, y_comb


x_size = 20
y_size = 5
x_pos, y_pos = create_grid_pos(x_size=x_size, y_size=y_size)

frames_per_cycle = 100
num_frames = 400
x_trans, y_trans = transverse_wave(x_pos, y_pos, frames_per_cycle=frames_per_cycle,
                                   wave_len=10, amplitude=1, num_frames=num_frames)
x_long, y_long = longitudinal_wave(x_pos, y_pos, frames_per_cycle=frames_per_cycle,
                                   wave_len=10, amplitude=1, num_frames=num_frames)
x_comb, y_comb = combined_wave(x_pos, y_pos, frames_per_cycle=frames_per_cycle,
                               wave_len=[10, 10], amplitude=[1, 0.9], phase=[0, np.pi/2+0.5], num_frames=num_frames)


def update(frame_num, scat, x, y):
    idx = frame_num % x.shape[0]
    scat.set_offsets(np.column_stack(
        (x[idx, :, :].flatten(), y[idx, :, :].flatten())))

    return scat


fig_trans, ax_trans = plt.subplots()
fig_trans.set_size_inches(6, 2.5)
plt.axis("off")
ax_trans.set_xlim([-1.5, x_size + 0.5])
ax_trans.set_ylim([-1.5, y_size + 0.5])
scat_trans = ax_trans.scatter(x_trans[0, :, :], y_trans[0, :, :])

frames_per_seconds = 20
interval = 1000 / frames_per_seconds
ani_trans = animation.FuncAnimation(fig_trans, update, frames=num_frames,
                                    fargs=(scat_trans, x_trans, y_trans), interval=interval)
#writervideo = animation.FFMpegWriter(fps=60)
#ani_trans.save(r"reports/graph_1.gif", writer=writervideo)
plt.show()

"""
fig_long, ax_long = plt.subplots()
fig_long.set_size_inches(6, 2.5)
plt.axis('off')
ax_long.set_xlim([-1.5, x_size + 0.5])
ax_long.set_ylim([-1.5, y_size + 0.5])
scat_long = ax_long.scatter(x_long[0, :, :], y_long[0, :, :])

ani_long = animation.FuncAnimation(fig_long, update, frames=num_frames,
                                   fargs=(scat_long, x_long, y_long), interval=interval)
plt.show()
"""

fig_comb, ax_comb = plt.subplots()
fig_comb.set_size_inches(6, 2.5)
plt.axis('off')
ax_comb.set_xlim([-1.5, x_size + 0.5])
ax_comb.set_ylim([-1.5, y_size + 0.5])
scat_comb = ax_comb.scatter(x_comb[0, :, :], y_comb[0, :, :])

ani_comb = animation.FuncAnimation(fig_comb, update, frames=num_frames,
                                   fargs=(scat_comb, x_comb, y_comb), interval=interval)
#writervideo = animation.FFMpegWriter(fps=60)
#ani_comb.save(r"reports/graph_2.gif", writer=writervideo)
plt.show()
