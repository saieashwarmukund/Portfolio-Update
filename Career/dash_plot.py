# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import datetime


# Set the current date in the format you want
present_dt = datetime.datetime.now()
present = str(present_dt.strftime("%Y-%m"))


df = pd.DataFrame([
        dict(Type="Education", Start='2016-09', Finish='2020-12', Title="B.S. in Data Science", Location="University of California San Diego", Notes=""),
        dict(Type="Experience", Start='2018-10', Finish='2019-06', Title="Research Assistant/Intern", Location="Computational Neural Data and Dynamics Lab", Notes=""),
        dict(Type="Experience", Start='2019-06', Finish='2019-08', Title="Business Intelligence Internship", Location="Alliant Insurance", Notes=""),
        dict(Type="Experience", Start='2021-04', Finish='2022-09', Title="Business Intelligence Analyst", Location="Liftoff", Notes=""),
        dict(Type="Experience", Start='2023-03', Finish=present, Title="Technical Analyst", Location="Coforge", Notes=""),
        dict(Type="Projects", Start='2018-06', Finish='2018-09', Title="BhajanBook Web Application", Location="Sai Center of Tustin", Notes=""),
        dict(Type="Projects", Start='2020-04', Finish='2020-06', Title="Red Means Go", Location="University of California San Diego", Notes="")
    ])

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([

    dash_table.DataTable(data=df.to_dict('records')),
    dcc.Graph(figure={}, id='career-timeline'),
    dcc.Dropdown(
        id="Type",
        options=["Education", "Experience", "Projects"],
        value="Experience",
        clearable=False,
    ),
])


@app.callback(
    Output("career-timeline", "figure"), 
    Input("Type", "value"))

def time_plot(df):
    fig = px.timeline(
        df,
        x_start="Start",
        x_end="Finish",
        y="Type",
        color="Title",
        custom_data=['Title', 'Location', 'Start', 'Finish']
    )

    # Reverse the y-axis so tasks are listed from top to bottom
    fig.update_yaxes(autorange="reversed")

    # Update the hover template to display in the desired format
    fig.update_traces(
        hovertemplate="<b>%{customdata[0]}</b><br>" +  # Title
                        "%{customdata[1]}<br>" +         # Location
                        "%{base|%b %Y} - %{x|%b %Y}<extra></extra>"  # Start Date - End Date
    )


    # Update layout for styling
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Arial"
        ),
        title=None,
        showlegend=False,
        xaxis_title=None,
        yaxis_title=None
    )

    return fig


app.run_server(debug=True)
