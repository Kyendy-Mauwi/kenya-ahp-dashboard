import plotly.express as px
import plotly.graph_objects as go

def plot_funnel(color):
    fig = px.funnel(x=[1102012, 85000, 42150, 4462], y=["Applicants", "Ongoing", "Completed", "Allocated"], color_discrete_sequence=[color])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white", height=400)
    return fig

def plot_impact_bar(df, color):
    fig = px.bar(df, x='Component', y='Value', title="MSME Contract Value (Billions KES)", color_discrete_sequence=[color])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
    return fig
