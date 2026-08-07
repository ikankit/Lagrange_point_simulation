import streamlit as st
from simulation import run_simulation
import plotly.graph_objects as go


st.set_page_config(
    page_title="simulation",
    page_icon="",
    layout= "wide"
    )

st.title("Interactive 3D simulation of spacecraft motion around the Sun-Earth Lagrange Points.")
st.markdown("----")

with st.sidebar:
    st.markdown("⚙️ Simulation Settings")
    st.divider()
    st.markdown(" 📍 Lagrange Point")

    selected_point=st.selectbox(
        "",
        ["L1","L2","L3","L4","L5"],
        index=0
    )
    st.divider()
    st.markdown(" 🔄 Simulation")
    steps=st.slider(
        "Total simulation steps",
        min_value=100,
        max_value=100000
        )
    
    
    animation_speed = st.slider(
        "Animation speed",
        min_value=1,
        max_value=100
)
    
run=st.button("▶ Run Simulation",use_container_width=True)
reset=st.button("🔄 Reset",use_container_width=True)

left, right = st.columns([4, 1])


with right:
    
    st.subheader("Information")
    
if run:
    
    with st.spinner("Running simulation"):
        
        sun_traj, earth_traj, craft_traj, lag_points=run_simulation(
            selected_point=selected_point,
            steps=steps
        )
        
    with left:
        
        st.subheader("3D simulation ")
        
        skip=10
        s=sun_traj[::skip]
        e=earth_traj[::skip]
        c=craft_traj[::skip]
        fig=go.Figure()
        
        colors={
            "L1":"red",
            "L2":"green",
            "L3":"yellow",
            "L4":"purple",
            "L5":"orange"}
        
        #sun orbit
        fig.add_trace(
            go.Scatter3d(
                x=[],y=[],z=[],
                mode="lines",
                line=dict(color="yellow",width=3),
                name="Object1 Orbit"
            )
        )
        
        #earth orbit
        fig.add_trace(
            go.Scatter3d(
                x=[],y=[],z=[],
                mode="lines",
                line=dict(color="blue",width=3),
                name="Object2 Orbit"
            )
        )
        
        #craft orbit
        fig.add_trace(
            go.Scatter3d(
                x=[],y=[],z=[],
                mode="lines",
                line=dict(color="red",width=3),
                name="Craft orbit"
            )
        )
        
        #sun maker
        fig.add_trace(
            go.Scatter3d(x=[s[0,0]],y=[s[0,1]],z=[s[0,2]],
                mode="markers",
                marker=dict(
                    size=14,color="yellow"
                    ),
                name="Object1"
            )
        )
        
        #earth maker
        fig.add_trace(
            go.Scatter3d(x=[e[0,0]],y=[e[0,1]],z=[e[0,2]],
                mode="markers",
                marker=dict(
                    size=9,color="blue"
                    ),
                name="Object2"
            )
        )
        
        #craft maker
        fig.add_trace(
            go.Scatter3d(x=[c[0,0]],y=[c[0,1]],z=[c[0,2]],
                mode="markers",
                marker=dict(
                    size=5,color="red"
                    ),
                name="craft"
            )
        )
        
        #craft start
        fig.add_trace(
            go.Scatter3d(
                x=[c[0,0]],y=[c[0,1]],z=[c[0,2]],
                mode="markers+text",
                text=["Start"],
                textposition="top center",
                marker=dict(
                    size=2,color="lime"),
                name="Start"
            )
        )
        
        #craft end
        #fig.add_trace(
           # go.Scatter3d(
            #    x=[c[-1,0]],y=[c[-1,1]],z=[c[-1,2]],
             #   mode="markers+text",
              #  text=["End"],
               # textposition="top center",
              #  marker=dict(
                  #  size=6,color="white"),
             #   name="End"
         #   )
      #  )
        #Lag points
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
                    size=5,
                    color=colors[selected_point],
                    symbol="x"
                ),
            name=selected_point
            )
        )
        #frame
        frames=[]
        for i in range(len(s)):
            frame=go.Frame(
                data=[
                #sun orbit
                go.Scatter3d(x=s[:i+1,0],y=s[:i+1,1],z=s[:i+1,2]),
                
                #earth orbit
                go.Scatter3d(x=e[:i+1,0],y=e[:i+1,1],z=e[:i+1,2]),
                
                #craft orbit
                go.Scatter3d(x=c[:i+1,0],y=c[:i+1,1],z=c[:i+1,2]),
                
                #sun maker
                go.Scatter3d(x=[s[i,0]],y=[s[i,1]],z=[s[i,2]]),
                
                #earth maker
                go.Scatter3d(x=[e[i,0]],y=[e[i,1]],z=[e[i,2]]),
                
                #craft maker
                go.Scatter3d(x=[c[i,0]],y=[c[i,1]],z=[c[i,2]])],
                traces=[0,1,2,3,4,5]
                
            )
            frames.append(frame)
            
            
        fig.frames=frames
        
        fig.update_layout(
            scene=dict(
                bgcolor="black",
                xaxis=dict(
                    title="X",
                    range=[-25,25]
                ),
                yaxis=dict(
                    title="Y",
                    range=[-25,25]
                ),
                zaxis=dict(
                    title="Z",
                    range=[-25,25]
                ),
                aspectmode="cube"
            ),
            showlegend=True,
            margin=dict(
                l=0,
                r=0,
                t=30,
                b=0
            ),
            updatemenus=[
                dict(type="buttons",showactive=False,
                     buttons=[dict(label="▶ Play",
                                   method="animate",
                                   args=[None,
                                        dict(
                                            frame=dict(
                                                duration=100,
                                                redraw=True
                                                ),
                                                transition=dict(duration=0),
                                                fromcurrent=True
                                                )
                                        ]
                                   ),
                              dict(label="⏸ Pause",
                                   method="animate",
                                   args=[[None],
                                        dict(
                                            frame=dict(duration=0),
                                            mode="immediate",
                                            transition=dict(duration=0)
                                        )
                                    ]
                                   )
                              ]
                     )
                ]
            )
                              
        st.plotly_chart(fig, use_container_width=True)
    st.success("Simulation Complete")
        
