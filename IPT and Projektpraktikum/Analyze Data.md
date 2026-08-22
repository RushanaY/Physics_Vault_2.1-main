==this was a good premilinary testing, but was enough only for the two can measurements==
==the more fine analysis will come after understanding the idea of a hearing test==
- [x] absolute level at frequency -
	- specific frequ (intended one) and compare the intensity
		- resulting in a relative comparison $$\Delta x = \frac{x_2 -x_1}{x_1}$$
		- maybe we should take the band? not just the frequency as one point ?  
- [x] band power 
	-  export data from spectrum
	- convert dB in linear power proxy (?) $P_i \propto 10^{L_i/10}$
	- sum over bins (?)
	- convert back to L $L = 10 \log_{10} (P)$
	- compare by $$\Delta L = 10 \log_{10} (\frac{P_A}{P_B})$$
- [ ] Spectral slope 
	- fir a line over chosen range (maybe hearing range?
	- use brightness proxy (?)
	- good for clarity of voice ![[Analyze Data 2025-12-26 00.32.55.excalidraw]]
- [x] peaks and resonances 
	-  find local maximas 
	- measure peak frequency, prominense (peak minus surroundings)
	- positions -> resonanse (how? what to look out for?)
	- shifts in peak (also how and what to look out for? geometry of cup, tension)
- [x] noise floor and noise coloration 
	- take silent part and get the median across it 
	- compare them 
- [x] SNR = signal to noise ration in the frequency band 
	- make L_signal and L_noise
	- SNR is their difference
- [x] Bandwidth
	- over which frequency range does the phone work the best 
	- differene between the dB for the specific, indended frequency 
- [x] Harmonics and distortion 
	- check multiples !!!!!! -> overtones 
	- compare their intecities 
- [x] spectral flateness 
	- what is there more - peaks or noise? -> I guess make the sound more pleasurable? doesn't sound as important 
- [x] coherence and correlation between spectras 
	- comparison of two spectras in actual values 
	- level match a reference, compute correlation??? how....



One tone analysus to compare the absolute level and  harmonics, maybe even the noise floor 
other than that -> **chirp** for tomorrow is better, as the whole spectra will end up inside the bandwidth , or try **pink noise** 

