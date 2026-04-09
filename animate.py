import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Plotly Animation Demo", layout="wide")

st.title("3 Basic Plotly Animations in Streamlit")

animation_choice = st.selectbox(
    "Choose an animation",
    [
        "Rotating 3D Helix",
        "Moving Sine Wave",
        "Bouncing Ball",
        "Donut",
        "Hypnotic Hypersphere",
        "Zoom Ball"
    ],
)

num_frames = 60


def rotating_3d_helix():
    t = np.linspace(0, 8 * np.pi, 200)
    x = np.cos(t)
    y = np.sin(t)
    z = np.linspace(-2, 2, 200)

    frames = []
    for i in range(num_frames):
        angle = 2 * np.pi * i / num_frames
        x_rot = x * np.cos(angle) - y * np.sin(angle)
        y_rot = x * np.sin(angle) + y * np.cos(angle)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter3d(
                        x=x_rot,
                        y=y_rot,
                        z=z,
                        mode="lines",
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=x,
                y=y,
                z=z,
                mode="lines",
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Rotating 3D Helix",
        scene=dict(
            xaxis=dict(range=[-1.5, 1.5]),
            yaxis=dict(range=[-1.5, 1.5]),
            zaxis=dict(range=[-2.5, 2.5]),
            aspectmode="cube",
        ),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 50, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def moving_sine_wave():
    x = np.linspace(0, 4 * np.pi, 300)

    frames = []
    for i in range(num_frames):
        phase = 2 * np.pi * i / num_frames
        y = np.sin(x + phase)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=x,
                        y=y,
                        mode="lines",
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=np.sin(x),
                mode="lines",
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Moving Sine Wave",
        xaxis=dict(range=[0, 4 * np.pi]),
        yaxis=dict(range=[-1.5, 1.5]),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 50, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def bouncing_ball():
    x_positions = np.linspace(0, 10, num_frames)
    y_positions = np.abs(np.sin(np.linspace(0, 3 * np.pi, num_frames))) * 5

    frames = []
    for i in range(num_frames):
        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=[x_positions[i]],
                        y=[y_positions[i]],
                        mode="markers",
                        marker=dict(size=20),
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=[x_positions[0]],
                y=[y_positions[0]],
                mode="markers",
                marker=dict(size=20),
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Bouncing Ball",
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[0, 6]),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 60, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig

def pulsing_toroid():
    # Parameters for the torus
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, 2 * np.pi, 50)
    u, v = np.meshgrid(u, v)
    
    # Base major and minor radii
    R_base = 3
    r_base = 1

    frames = []
    for i in range(num_frames):
        # The secret to the loop: Use a full 2*pi cycle over the number of frames
        # This ensures frame[0] == frame[num_frames]
        phase = 2 * np.pi * i / num_frames
        
        # Pulsing effect: radius oscillates between 0.5 and 1.5
        r_pulse = r_base * (1 + 0.5 * np.sin(phase))
        
        # Torus Parametric Equations
        x = (R_base + r_pulse * np.cos(v)) * np.cos(u)
        y = (R_base + r_pulse * np.cos(v)) * np.sin(u)
        z = r_pulse * np.sin(v)

        frames.append(
            go.Frame(
                data=[
                    go.Surface(
                        x=x, y=y, z=z,
                        colorscale="Viridis",
                        showscale=False
                    )
                ],
                name=str(i)
            )
        )

    # Initial State
    x_init = (R_base + r_base * np.cos(v)) * np.cos(u)
    y_init = (R_base + r_base * np.cos(v)) * np.sin(u)
    z_init = r_base * np.sin(v)

    fig = go.Figure(
        data=[go.Surface(x=x_init, y=y_init, z=z_init, colorscale="Viridis", showscale=False)],
        frames=frames
    )

    fig.update_layout(
        title="Pulsing Geometric Toroid",
        scene=dict(
            xaxis=dict(range=[-5, 5]),
            yaxis=dict(range=[-5, 5]),
            zaxis=dict(range=[-2, 2]),
            aspectmode="data"
        ),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [None, {"frame": {"duration": 30, "redraw": True}, "fromcurrent": True}]
                    }
                ]
            }
        ]
    )
    return fig

def hypnotic_hypersphere():
    theta = np.linspace(0, 2 * np.pi, 60)
    phi = np.linspace(0, 2 * np.pi, 60)
    theta, phi = np.meshgrid(theta, phi)
    R, r_base = 4, 1.5
    frames = []
    for i in range(num_frames):
        t = 2 * np.pi * i / num_frames
        r = r_base * (1 + 0.3 * np.sin(t))
        # Base coordinates
        x = (R + r * np.cos(phi)) * np.cos(theta)
        y = (R + r * np.cos(phi)) * np.sin(theta)
        z = r * np.sin(phi)
        # Dual-axis rotation math
        y_rot = y * np.cos(2*t) - z * np.sin(2*t)
        z_final = y * np.sin(2*t) + z * np.cos(2*t)
        x_final = x * np.cos(t) - y_rot * np.sin(t)
        y_final = x * np.sin(t) + y_rot * np.cos(t)
        
        frames.append(go.Frame(data=[go.Surface(x=x_final, y=y_final, z=z_final, colorscale="Magma", showscale=False)], name=str(i)))

    fig = go.Figure(data=frames[0].data, frames=frames)
    fig.update_layout(
        title="Hypnotic Hypersphere Loop",
        scene=dict(xaxis=dict(range=[-7, 7]), yaxis=dict(range=[-7, 7]), zaxis=dict(range=[-4, 4]), bgcolor='black'),
        paper_bgcolor='black', font=dict(color='white'),
        updatemenus=[{"type": "buttons", "buttons": [{"label": "Play Loop", "method": "animate", "args": [None, {"frame": {"duration": 30, "redraw": True}, "loop": True}]}]}]
    )
    return fig

def infinite_zoom_sphere():
    """Simulates a sphere flying toward the viewer and looping infinitely."""
    # Higher resolution grid for a smoother looking sphere
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 60), np.linspace(0, np.pi, 60))
    r = 5
    frames = []
    
    for i in range(num_frames):
        # We want the ball to move from Z = -100 to Z = +100
        # Frame 0: Z = -100 (Small/Far)
        # Frame 59: Z = +100 (Filling the screen/Passing the camera)
        z_offset = -100 + (i / num_frames) * 210 # Increased to 210 to ensure it clears the frame
        
        x = r * np.sin(v) * np.cos(u)
        y = r * np.sin(v) * np.sin(u)
        z = r * np.cos(v) + z_offset

        frames.append(
            go.Frame(
                data=[go.Surface(
                    x=x, y=y, z=z, 
                    colorscale="Plasma", 
                    showscale=False,
                    # We add a slight transparency shift so it 'fades' in from the dark
                    opacity=min(1.0, (i + 10) / 20) 
                )],
                name=str(i)
            )
        )

    fig = go.Figure(data=frames[0].data, frames=frames)
    
    fig.update_layout(
        title="Infinite Flyby Loop",
        scene=dict(
            # X and Y are tight to make the ball look like it's filling the screen
            xaxis=dict(range=[-15, 15], visible=False),
            yaxis=dict(range=[-15, 15], visible=False),
            # Z range is set so the camera 'lives' at the front edge
            zaxis=dict(range=[-100, 100], visible=False),
            bgcolor='black',
            # Positioning the camera directly at the end of the Z-axis
            camera=dict(
                eye=dict(x=0, y=0, z=0.1), # Very close to the center
                up=dict(x=0, y=1, z=0)
            ),
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=4) # Stretches the 'tunnel' for better depth
        ),
        paper_bgcolor='black',
        font=dict(color='white'),
        updatemenus=[
            {
                "type": "buttons",
                "direction": "left",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [None, {
                            "frame": {"duration": 80, "redraw": True}, 
                            "fromcurrent": False, # Always restart for the loop
                            "transition": {"duration": 20},
                            "loop": True
                        }]
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}]
                    }
                ],
                "x": 0.1, "y": 0, "xanchor": "left", "yanchor": "bottom"
            }
        ]
    )
    return fig

if animation_choice == "Rotating 3D Helix":
    fig = rotating_3d_helix()
elif animation_choice == "Moving Sine Wave":
    fig = moving_sine_wave()
elif animation_choice == "Bouncing Ball":
    fig = bouncing_ball()
elif animation_choice == "Donut":
    fig = pulsing_toroid()
elif animation_choice == "Hypnotic Hypersphere":
    fig = hypnotic_hypersphere()
elif animation_choice == "Zoom Ball":
    fig = infinite_zoom_sphere()

st.plotly_chart(fig, use_container_width=True)