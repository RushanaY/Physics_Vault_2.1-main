# Scanning process
apparently interval >= $175ms$ (can be impacted by other parameters) for SCAN per default 

Minimum interval for STEP mode
1. conversions per channel x conversion time 
2. Delay per channel (programmed)
3. $17ms$ break -> time to change channels 
4. auto range time (optional)

Minimum time for SCAN mode -> sum of 1-4 x number of channels scanned 

Are we using AC? => extra time DELAY needed 
-> *I don't think so, we have analogue inputs and therefore it will be DC voltage*

## fast scanning (example)
1. 3V DC range, $4 \frac{1}{2}$ resolution, FLTR off 
2. ONE SHOT trigger 
3. SCAN mode
4. SCANNER "8"
5. TRIGGER to initiate scan of eight channels 

# important commands (IEEE-488) (p.75)
- F1 - AC volts 
- R0-R3 or even R4 - range for DCV 
- Z0-Z2 - do we need zero? 
- P0-P2 - do we need filter?
- S0 -  $4 \frac{1}{2}$ digit => **2.59ms integration period**
- S1 - $5\frac{1}{2}$ resolution => **16.67ms or 20ms integration time** (depends on frequency)
	- *this is probably the one we want, because of the resolution, but if needed we can sacrifice a couple of digits*
- T1 or T3 or T5 for the ONE SHOT TRIGGER
- B0-B1 - reading mode? really needed? 
- I0-Jn - what role does DATA STORE SIZE play? 
- Q0 - default interval of **175ms** 
- Qn with $n=$interval (min **15ms**)
- C0-C2 - CALIBRATION? 
- G0-G7 - DATA FORMAT, does it matter?
- Y0-Y3 - TERMINATOR, manual operation kind of? 
- U0-U5 - STATUD -> that might be really good for testing 
- Wn - DELAY (can be set to 0ms, but needed?)
- D - DISPLAY (Da to show characters with a=character)
- N0-N28 opens a number of channels 


