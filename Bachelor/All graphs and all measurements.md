*I have gave chatGPT a couple promts to write me a code in order to analyze the data. 
"plot_csv_columns_onw_image.py -> plots all columns and puts them all in one png image
"plot_csv)columns(GPT) -> every columns gets its own plot and will get exported as a png
wire_temperature(1).py -> calculates only the temperature
wire_temeprature_res(gpt).py -> calculates both temperature and resistance jump

I will go through the codes to check if they are correct, at least to my own knowledge and ability*

I start the analysis of data with the measurements, that were taken with Malte's code, as it has shown to have the most data points and also to be more reliable. 
First I will try and put all the data as it is (if flow is 0 , then assume normal conditions of 0.37mlm/min, as it was the suggested value and we did our best to hold it there. At least we tried to hold the pressure at a constant value, that was correlated before with the flow of 0.37mlm/min)
Next I will try and get to the actual value and see what I needed to change for that. First change the flow and then try to remove one of the cooling/warming parts
# August 6 last measurements with the 15mu wire 
Experimental:
with recomb 12.975 Ohm
no recomb 13.060 Ohm
-> 0.0075 Ohm 

Modell:
with recomb 10.644.. Ohm
no recomb 10.63.. Ohm 
-> 0.0076 Ohm 

The difference seems to be correct, but the theoretically predicted resistance in absolute value is not. Probably that is really due to the soldering mistakes 

# August 6: pumping hydrogen down with 15mu wire , no plasma
starting with highest pressure value of 1.6mbar background pressure 
experimental: a bit under 12.8 Ohm 
theoretical:  11.4 Ohm

with the lowest value of 4e-6
experimental:
	front: 12.9 Ohm
	back: 13.0 Ohm 

theoretical: 
with/without recomb: 11.30 Ohm 

Difference: low - high 
experimental: $12.9-12.8 = 0.1 Ohm$  
theoretical: $11.294398704 - 11.406816308 \approx - 0.112 Ohm$ 

=> similar enough 
# August 11: temperature sweep, 15mu wire, no plasma 
At max temperature of 377 K:
	experiment
		front: 13.319 Ohm
		back: 13.366 Ohm 
	theory
		front: 11.313911404 (11.313879270 with no k(T))
		

at minimum temperature of 277K 
	experiment
		front 13.248
		back: 13.351 
	theory: 
		front  11.290883673  Ohm (11.290833844 with no k(T))
	
=> similar enough


what if it was with 5mu:
difference between hot and cold; 121.924710606- 121.552783262 = 0.37
 121.843452006-121.474027311 = 0.36 (no k(T), it looks like difference isn't that big, or the code is wrong)



# with suggestions form Dylan
-> distance from wire to nozzle : 1mm
-> higher probing current (I put it as a test to 10mA)
-> shorter wire : 2cm 
-> generally better plasma 


WHOLE-WIRE RESISTANCE
Reference R0 at 293.15 K: 57.041131604 ohm
Without recombination: 81.076455244 ohm
With recombination: 96.696710966 ohm

**delta R from mean delta T (same model): 15.620255721 ohm**
15 Ohm jump! 

and they probably had also better plasma (the values above are at 0.5 dissacosiation rate)




























