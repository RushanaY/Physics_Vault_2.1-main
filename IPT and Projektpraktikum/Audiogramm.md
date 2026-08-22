==this is what we measure!!!==

we assume that we really want to measure 


HA HA Oldenburger satztest 



1. [[Band power]] -> how much energy gets through 
	- meaningful bands? 
		- https://blog.zagerguitar.com/acoustic-guitar-eq/#:~:text=Bass%20(Low%20Frequencies):%20This,the%20sparkle%20of%20the%20guitar.
		- low: 20 - 250
			- bass, gives the nice background
		- mid: 250 - 4000
			- main notes 
		- high: 4000 - 20 000
			- brighness, "sparkle" 
	- other than that -> **same procedure as in the first Analysis procedure**
	- compare:
		- A vs B
		- A/B vs noise -> [[SNR]]
		- A/B vs clean slate 
2. [[noise floor]] -> calc for each band one 
3. [[Brightness]] -> strong higher harmonics makes the tone sound brighter , related to [[timbre]] 
	- spectral centroid -> shows which frequency os the "centre of mass" in the spectrum , kind of brighntess 
	- $$f_c = \text{weighted mean} = \frac{\sum w_i x_i}{\sum w_i}$$
	- also possible -> difference of the higher frequ to the mid range : $L_{high} - L_{mid}$
4. [[Spectral slope (tilt)]]
	- muffled vs clear, the steeper the Steigung the more muffled 
	- try the excel comand "slope"
	- take the are aroung the peak, or the intended one
	- maybe even open it in a screenshot view and analyze this way a couple most prominent peaks 
5. Usable bandwidth abouve noise? the remaining audible parts?
	1. substract noise from signal in dB and mark the areas where the signal is still lounder ....
	2. conditional formatting?
6. Check for hamronics and the bandpower around it 

for pink noise : -> same as for the seperate frequencies, just apparently cleaner results
1. same band power -> cleaner way to compare setups 
2. Band gains 
	1. same three band segments and compare also their band powers 

for speech:
- RMS -> apparently loudness won't matter 
- SNR -> same.... band power
- clarity -> same....
- vowels
- make slope of the whole thing 
- compressionn :$peak (dB)-RMS (dB)$ 