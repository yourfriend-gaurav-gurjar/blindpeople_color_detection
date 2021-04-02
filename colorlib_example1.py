# Original NOAA color map and levels
def demo(
     noaax = 
	    ["#ffffff",
	     "#7fff00", 
	     "#00cd00", 
             "#008b00", 
             "#104e8b",
             "#1e90ff", 
             "#00b2ee", 
             "#00eeee", 
             "#8968cd",
             "#912cee",
             "#8b008b",
             "#8b0000",
             "#cd0000",
             "#ee4000",
             "#ff7f00",
             "#cd8500",
             "#ffd700",
             "#ffff00",
             "#ffaeb9"],
     lev = 
	  [0, 0.01, 0.1, 0.25, 0.75, 1, 1.25, 1.50, 1.75, 2,2.5, 3, 4, 5, 7, 10, 15, 20, 60])

from colorspace import deutan
demo(lev, noaahex, titles= ["Original NOAA Colors"])
