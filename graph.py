"""
Author: Martial Himanshu
Application: Motion detector graph generator for analysis
Features: 1. On mouse hover- shows start and end time for every instance of object in video
          2. Have tool like: Save,Pan,Box Zoom, Wheel Zoom,Save, Reset
          3. can be access online
"""
#import various useful library for this project
from bokeh.plotting import figure,output_file,show
from videoframe import df
from bokeh.models import HoverTool,ColumnDataSource

#Edits date format in YYYY-MM-DD HH:MM:SS in dataframe
df["start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["end_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

#create object to access column data from dataframe
cds = ColumnDataSource(df)
#create figure object for desired plot analysis using bokeh chart library
p=figure(x_axis_type='datetime',plot_width=1200,plot_height=200,title="object detection",responsive=True)

#removes tick line from y axis and grid from graph
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

#create hover object to apply hovertool on plot graph
hover = HoverTool(tooltips=[("Start","@start_string"),("End","@end_string")])
p.add_tools(hover)

#Generates quadrilateral chart html page with all the integrated value
p.quad(top=1,bottom=0,left="Start",right="End",color= "green",source=cds)

output_file("Graph.html")
show(p)
#end
