import streamlit as st
import matplotlib.pyplot as plt
from zero_velocity import create_zvc_plot
import plotly.graph_objects as go
from simulation import run_simulation
import Initial_conditions 
from Effective_potential import create_effective_potential

steps=Initial_conditions.steps
mu=Initial_conditions.mu

# PAGE CONFIGURATION

st.set_page_config(
    page_title="Lagrange Point Simulation",
    page_icon="🌌",
    layout="wide"
)

st.title(
    "Interactive 3D Simulation of Spacecraft Motion "
    "around the Lagrange Points"
)
st.markdown("---")

status=st.empty()

if "simulation_done" not in st.session_state:
    st.session_state.simulation_done = False

if "sun_traj" not in st.session_state:
    st.session_state.sun_traj = None

if "earth_traj" not in st.session_state:
    st.session_state.earth_traj = None

if "craft_traj" not in st.session_state:
    st.session_state.craft_traj = None

if "lag_points" not in st.session_state:
    st.session_state.lag_points = None

# SIDEBAR
with st.sidebar:

    st.markdown("## ⚙️ Simulation Settings")

    st.divider()
    #mass input
    
    mass1_input = st.number_input(
        "Mass of Body 1",
        min_value=0.000001,
        value=float(Initial_conditions.m_of_object1),
        step=0.01,
        format="%.6f")
    
    mass2_input = st.number_input(
        "Mass of Body 2",
        min_value=0.000001,
        value=float(Initial_conditions.m_of_object2),
        step=0.01,
        format="%.6f")
    
    # LAGRANGE POINT
    
    st.markdown(" 📍 Lagrange Point")

    selected_point = st.selectbox(
        "Lagrange point",
        ["L1", "L2", "L3", "L4", "L5"],
        index=0,
        label_visibility="collapsed"
    )

    st.divider()

    # RUN / RESET
    run = st.button("▶ Run Simulation",use_container_width=True)
    reset = st.button("🔄 Reset",use_container_width=True)
    st.divider()
    # DISPLAY OPTIONS

    st.markdown("👁 Display Options")

    show_lagrange = st.checkbox("Show Lagrange Points",value=True)
    show_orbits = st.checkbox("Show Orbits",value=True)
    show_start = st.checkbox( "Show Start Point",value=True)
    show_end = st.checkbox("Show End Point",value=True)
    st.divider()
    # CAMERA
    st.markdown(" 📷 Camera")
    
    camera_present = st.selectbox(
        "Camera View",
        [
            "Isometric View",
            "Top View",
            "Front View",
            "Side View"
        ],
        label_visibility="collapsed"
    )
    st.divider()

# RESET

if reset:

    st.session_state.simulation_done = False

    st.session_state.sun_traj = None
    st.session_state.earth_traj = None
    st.session_state.craft_traj = None
    st.session_state.lag_points = None

    st.rerun()

# RUN SIMULATION

if run:

    with st.spinner("Running simulation..."):
        Initial_conditions.m_of_object1 = mass1_input
        Initial_conditions.m_of_object2 = mass2_input

        Initial_conditions.mu = (mass2_input)/(mass1_input+mass2_input)
        mu=Initial_conditions.mu

        sun_traj, earth_traj, craft_traj, lag_points = run_simulation(
            selected_point=selected_point,
            steps=steps
        )

    # Save simulation results
    st.session_state.sun_traj = sun_traj
    st.session_state.earth_traj = earth_traj
    st.session_state.craft_traj = craft_traj
    st.session_state.lag_points = lag_points

    st.session_state.simulation_done = True

# DISPLAY SIMULATION

if st.session_state.simulation_done:

    # GET SAVED TRAJECTORIES

    sun_traj = st.session_state.sun_traj
    earth_traj = st.session_state.earth_traj
    craft_traj = st.session_state.craft_traj

    lag_points = st.session_state.lag_points

    # Safety check
    if (
        sun_traj is None
        or earth_traj is None
        or craft_traj is None
        or lag_points is None
    ):

        st.error(
            "Simulation data is missing. "
            "Please run the simulation again."
        )

        st.stop()


    # REDUCE TRAJECTORY DATA
    skip = 10
    s = sun_traj[::skip]
    e = earth_traj[::skip]
    c = craft_traj[::skip]


    # LAGRANGE POINT COLORS

    colors = {
        "L1": "red",
        "L2": "green",
        "L3": "yellow",
        "L4": "purple",
        "L5": "orange"
    }

    # CREATE 3D FIGURE

    fig = go.Figure()

    # SUN ORBIT
    fig.add_trace(
        go.Scatter3d(x=[],y=[],z=[],
            mode="lines",
            line=dict(color="yellow",width=3),
            name="Body1 Orbit"
        )
    )
    # EARTH ORBIT
    fig.add_trace(
        go.Scatter3d(x=[],y=[],z=[],
            mode="lines",
            line=dict(color="blue",width=3),
            name="Body2 Orbit"
        )
    )
    # CRAFT ORBIT

    fig.add_trace(
        go.Scatter3d(x=[],y=[],z=[],
            mode="lines",
            line=dict(color="red",width=3),
            name="Craft Orbit"
        )
    )
    # SUN MARKER
    fig.add_trace(
        go.Scatter3d(x=[s[0, 0]],y=[s[0, 1]],z=[s[0, 2]],
            mode="markers",
            marker=dict(size=10,color="yellow"),
            name="Body1"
        )
    )
    # EARTH MARKER

    fig.add_trace(
        go.Scatter3d( x=[e[0, 0]],y=[e[0, 1]],z=[e[0, 2]],
            mode="markers",
            marker=dict(size=9,color="blue"),
            name="Body2"
        )
    )
    # SPACECRAFT MARKER
    fig.add_trace(
        go.Scatter3d(x=[c[0, 0]],y=[c[0, 1]],z=[c[0, 2]],
            mode="markers",
            marker=dict(size=5,color="red"),
            name="craft"
        )
    )
    # START POINT
    fig.add_trace(
        go.Scatter3d(x=[c[0, 0]],y=[c[0, 1]],z=[c[0, 2]],
            mode="markers+text",
            text=["Start"],
            textposition="top center",
            marker=dict(size=4,color="lime"),
            name="Start"
        )
    )
    # END POINT

    fig.add_trace(
        go.Scatter3d(x=[c[-1, 0]],y=[c[-1, 1]],z=[c[-1, 2]],
            mode="markers+text",
            text=["End"],
            textposition="top center",
            marker=dict(size=6,color="white"),
            name="End"
        )
    )
    # SELECTED LAGRANGE POINT

    px, py, pz = lag_points[selected_point]

    fig.add_trace(
        go.Scatter3d(x=[px],y=[py],z=[pz],
            mode="markers+text",
            text=[selected_point],
            textposition="top center",
            marker=dict(size=6,color=colors[selected_point],symbol="x"),
            name=selected_point
        )
    )
    # VISIBILITY
    
    # Orbits
    fig.data[0].visible = show_orbits
    fig.data[1].visible = show_orbits
    fig.data[2].visible = show_orbits

    # Start
    fig.data[6].visible = show_start

    # End
    fig.data[7].visible = show_end

    # Lagrange
    fig.data[8].visible = show_lagrange

    # ANIMATION FRAMES

    frames = []
    max_frames = 200
    frame_step = max(1,len(s) // max_frames)
    for i in range(0,len(s),frame_step):
        frame = go.Frame(
            data=[
                # SUN ORBIT
                go.Scatter3d(x=s[:i + 1, 0],y=s[:i + 1, 1],z=s[:i + 1, 2]),
                
                # EARTH ORBIT
                go.Scatter3d(x=e[:i + 1, 0],y=e[:i + 1, 1],z=e[:i + 1, 2]),
                
                # CRAFT ORBIT

                go.Scatter3d(x=c[:i + 1, 0],y=c[:i + 1, 1],z=c[:i + 1, 2]),

                # SUN MARKER
                
                go.Scatter3d(x=[s[i, 0]],y=[s[i, 1]],z=[s[i, 2]]),

                # EARTH MARKER

                go.Scatter3d(x=[e[i, 0]],y=[e[i, 1]],z=[e[i, 2]]),

                # CRAFT MARKER

                go.Scatter3d(x=[c[i, 0]],y=[c[i, 1]],z=[c[i, 2]])
            ],

            traces=[0,1,2,3,4,5]
        )

        frames.append(frame)
    fig.frames = frames
    
    # CAMERA

    camera_views = {

        "Isometric View": dict(
            eye=dict(x=1.5,y=1.5,z=1.2)
        ),

        "Top View": dict(
            eye=dict( x=0,y=0, z=2.5)
        ),

        "Front View": dict(
            eye=dict( x=0,y=2.5,z=0)
        ),

        "Side View": dict(
            eye=dict(x=2.5,y=0,z=0)
        )
    }
    # FIGURE LAYOUT

    fig.update_layout(
        height=700,
        scene=dict(
            bgcolor="black",
            xaxis=dict(title="X",range=[-25, 25]),
            yaxis=dict(title="Y",range=[-25, 25]),
            zaxis=dict(title="Z",range=[-25, 25]),
            aspectmode="auto",
            camera=camera_views[camera_present]
        ),
        showlegend=True,
        margin=dict(l=0,r=0, t=20,b=0),
        # PLAY / PAUSE
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                direction="left",
                x=0.02,
                y=0.98,
                xanchor="left",
                yanchor="top",
                buttons=[
                    # PLAY
                    dict(
                        label="▶ Play",
                        method="animate",
                        args=[
                            None,
                            dict(
                                frame=dict(duration=70,redraw=True),
                                transition=dict(duration=0),
                                fromcurrent=True,
                                mode="immediate"
                            )
                        ]
                    ),
                    # PAUSE
                    dict(
                        label="Ⅱ Pause",
                        method="animate",
                        args=[
                            [None],
                            dict(
                                frame=dict( duration=0,redraw=False),
                                transition=dict(duration=0),
                                mode="immediate"
                            )
                        ]
                    )
                ]
            )
        ]
    )
    # MAIN COLUMNS

    left, right = st.columns([6.2, 2])
    # LEFT SIDE

    with left:
        st.markdown(" 🌌 3D Simulation" )
        st.plotly_chart( fig,use_container_width=True,config={"scrollZoom": True,"displayModeBar": True})

        # EFFECTIVE POTENTIAL
        st.markdown("---")
        st.markdown(" 🌌 Effective Potential Plot")
        potential_fig = create_effective_potential(mu)

        st.pyplot(potential_fig,use_container_width=True)

        plt.close(potential_fig)
        
       
        # ZERO VELOCITY CURVES
        st.markdown("---")
        st.markdown( "🚫 Zero-Velocity Curves" )
        
        zvc_fig = create_zvc_plot(mu)

        st.pyplot(zvc_fig, use_container_width=True)
        plt.close(zvc_fig)
        
    # RIGHT INFORMATION PANEL

    with right:
        st.markdown("ℹ️ Information")
        st.divider()
        
        # SELECTED LAGRANGE POINT
        st.markdown(" 📍 Selected Point")
        st.write(f"**Point:** {selected_point}")
        st.write(f"**X:** {px:.5f}")
        st.write( f"**Y:** {py:.5f}")
        st.write(f"**Z:** {pz:.5f}")
        st.divider()
        
        # SPACECRAFT

        st.markdown( "🚀 craft" )

        st.write(f"**Initial X:** "f"{c[0, 0]:.5f}")
        st.write(f"**Initial Y:** " f"{c[0, 1]:.5f}" )
        st.write(f"**Initial Z:** " f"{c[0, 2]:.5f}")
        st.write("")
        st.write(f"**Final X:** "f"{c[-1, 0]:.5f}")
        st.write(f"**Final Y:** "f"{c[-1, 1]:.5f}")
        st.write(f"**Final Z:** "f"{c[-1, 2]:.5f}")
        st.divider()
        
        # SIMULATION INFORMATION

        st.markdown("🔄 Simulation" )
        st.write( f"**Steps:** {steps}")
        st.write(f"**Displayed Frames:** "f"{len(frames)}")
        st.write(f"**Selected Lagrange Point:** "f"{selected_point}")
        st.divider()
        status.success(
            "Simulation Complete ✓"
        )
# BEFORE SIMULATION


else:
    st.markdown("""
    <h2>Welcome</h2> 
    <p>Please follow the following steps:</p>
    <p>Step1:Open the sidebar at the top left corner</p>
    <p>Step2:Select a Lagrange point </p>
    <p>Step3:In Display option select the checkbox u want to see </p>
    <p>Step4:click ▶ Run Simulation to start.</p>


    
""",unsafe_allow_html=True)
