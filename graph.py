from bokeh.plotting import figure,output_file,show
from videoframe import df
from bokeh.models import HoverTool,ColumnDataSource
df["start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["end_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)
p=figure(x_axis_type='datetime',plot_width=1200,plot_height=200,title="object detection",responsive=True)
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

hover = HoverTool(tooltips=[("Start","@start_string"),("End","@end_string")])
p.add_tools(hover)

p.quad(top=1,bottom=0,left="Start",right="End",color= "green",source=cds)

output_file("Graph.html")
show(p)
