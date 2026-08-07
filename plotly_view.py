import numpy as np
import plotly.graph_objects as go


def create_plotly_animation(
    object1_hist,
    object2_hist,
    probe_hist,
    lag_points,
    selected_point="L1"
):

    skip = 10

    s = object1_hist[::skip]
    e = object2_hist[::skip]
    p = probe_hist[::skip]

    colors = {
        "L1":"red",
        "L2":"green",
        "L3":"magenta",
        "L4":"orange",
        "L5":"purple"
    }

    fig = go.Figure()

    # Sun Orbit
    fig.add_trace(
        go.Scatter3d(
            x=[],
            y=[],
            z=[],
            mode="lines",
            line=dict(color="yellow", width=4),
            name="Object1 Orbit"
        )
    )

    # Earth Orbit
    fig.add_trace(
        go.Scatter3d(
            x=[],
            y=[],
            z=[],
            mode="lines",
            line=dict(color="cyan", width=4),
            name="Object2 Orbit"
        )
    )

    # Probe Orbit
    fig.add_trace(
        go.Scatter3d(
            x=[],
            y=[],
            z=[],
            mode="lines",
            line=dict(color="white", width=3),
            name="Probe Path"
        )
    )

    # Sun
    fig.add_trace(
        go.Scatter3d(
            x=[s[0,0]],
            y=[s[0,1]],
            z=[s[0,2]],
            mode="markers",
            marker=dict(
                size=18,
                color="yellow"
            ),
            name="Object1"
        )
    )

    # Earth
    fig.add_trace(
        go.Scatter3d(
            x=[e[0,0]],
            y=[e[0,1]],
            z=[e[0,2]],
            mode="markers",
            marker=dict(
                size=10,
                color="deepskyblue"
            ),
            name="Object2"
        )
    )

    # Probe
    fig.add_trace(
        go.Scatter3d(
            x=[p[0,0]],
            y=[p[0,1]],
            z=[p[0,2]],
            mode="markers",
            marker=dict(
                size=6,
                color="white"
            ),
            name="Probe"
        )
    )

    # Lagrange Point

    px, py, pz = lag_points[selected_point]

    fig.add_trace(
        go.Scatter3d(
            x=[px],
            y=[py],
            z=[pz],
            mode="markers+text",
            text=[selected_point],
            textposition="top center",
            marker=dict(
                size=8,
                color=colors[selected_point],
                symbol="x"
            ),
            name=selected_point
        )
    )

    frames = []

    for i in range(len(s)):

        frames.append(

            go.Frame(

                data=[

                    go.Scatter3d(
                        x=s[:i+1,0],
                        y=s[:i+1,1],
                        z=s[:i+1,2]
                    ),

                    go.Scatter3d(
                        x=e[:i+1,0],
                        y=e[:i+1,1],
                        z=e[:i+1,2]
                    ),

                    go.Scatter3d(
                        x=p[:i+1,0],
                        y=p[:i+1,1],
                        z=p[:i+1,2]
                    ),

                    go.Scatter3d(
                        x=[s[i,0]],
                        y=[s[i,1]],
                        z=[s[i,2]]
                    ),

                    go.Scatter3d(
                        x=[e[i,0]],
                        y=[e[i,1]],
                        z=[e[i,2]]
                    ),

                    go.Scatter3d(
                        x=[p[i,0]],
                        y=[p[i,1]],
                        z=[p[i,2]]
                    )

                ],

                traces=[0,1,2,3,4,5]

            )

        )

    fig.frames = frames

    all_points = np.vstack((s, e, p))

    margin = 5

    xmin = all_points[:,0].min() - margin
    xmax = all_points[:,0].max() + margin

    ymin = all_points[:,1].min() - margin
    ymax = all_points[:,1].max() + margin

    zmin = all_points[:,2].min() - margin
    zmax = all_points[:,2].max() + margin

    fig.update_layout(

        title=f"Sun–Earth {selected_point} Simulation",

        scene=dict(

            bgcolor="black",

            xaxis=dict(range=[xmin,xmax]),

            yaxis=dict(range=[ymin,ymax]),

            zaxis=dict(range=[zmin,zmax]),

            aspectmode="data",

            camera=dict(
                eye=dict(
                    x=1.8,
                    y=1.8,
                    z=0.8
                )
            )

        ),

        margin=dict(l=0,r=0,t=40,b=0),

        updatemenus=[

            dict(

                type="buttons",

                showactive=False,

                buttons=[

                    dict(

                        label="▶ Play",

                        method="animate",

                        args=[
                            None,
                            dict(
                                frame=dict(
                                    duration=25,
                                    redraw=True
                                ),
                                fromcurrent=True
                            )
                        ]

                    ),

                    dict(

                        label="❚❚ Pause",

                        method="animate",

                        args=[
                            [None],
                            dict(
                                frame=dict(
                                    duration=0,
                                    redraw=False
                                ),
                                mode="immediate"
                            )
                        ]

                    )

                ]

            )

        ]

    )

    return fig
