import tensorflow as tf
import numpy as np
import tfplot

def symmetrize(M):
    with tf.compat.v1.variable_scope("symmetrize"):
        M_lower = tf.linalg.band_part(M, -1, 0)
        return M_lower + tf.linalg.transpose(M_lower) - tf.linalg.tensor_diag_part(M)

def waveform_plot(waveform, delta_t):
    fig, ax = tfplot.subplots(figsize=(3, 3))
    times = np.arange(len(waveform)) * delta_t
    ax.plot(times, waveform)
    ax.set_ylabel('signal')
    ax.set_xlabel('time')

    return fig
