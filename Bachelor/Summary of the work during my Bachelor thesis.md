```table-of-contents
```


# 4. Work completed during the thesis 
The goal of this Bachelor thesis was to work on the calorimetric wire detector. We continued to work on a set up, that was constructed by Surhabi Deshpande during her Master thesis, taking into account her suggestions to improve the detection of atomic hydrogen. In this section there will be the collection of observations and results that were made during the bachelor thesis. 


## 4.1 Minor changes to the setup (PCB, conversion factor for gauges, GPIB communication)

The minor change that were done on the set up are the professionally made PCB instead of the handmade one. For the measurement devices, the conversion factor of on both Pfeiffer Gauges was set to 2.4, as it is the one for hydrogen. Before both gauges were set for nitogen. This change only impacts the values for pressure that we see, but doesn't change the gas itself. In addition all the measurement devices, Keithley multimeter and HP3478A multimeter, were connected to the computer via GPIB connection, which allowed to have measurements taken almost every second. Also theses devices were all positioned under the table of the set up in order to shield the multimeters from the RF power, whose microwaves caused faulty data points. Before a jump in resistance of about 200mOhm was observed just from turning on the RF power, where as now this effect is reduced to only a couple mOhm jumps. 

In addition a small ruler was installed. It allows to track the distance, that the wire is moved along the beam flux. 


## 4.2 Big changes in the set up 

### 4.2.1 The Nozzle 

#### 4.2.1 Nozzle cooling with pelltier element
On of the suggested changes from the master thesis, was the cooling of the nozzle using a pelltier element. The hypothesis was, that a cold nozzle would cool down the exiting beam, which would lead to less heating of the wire and also the nozzle itself will be a smaller source of radiative cooling. As a result the should lead to better contrast between the signals of atomic and molecular hydrogen.

In order to test this theory a good cooling system had to be installed. The first step is to use the pelltier, which was already available. A pelltier element needs a way to lead the heat away, as it work by "pushing" thermal energy from one side to another. Suggested from Surhabi it was attempted to install a water cooling system. Tubes with flowing water would go into the vacuum chamber and inside the right side of the copper block, where it is then flowing out through the second tube and out of the chamber. Sadly both the plastic and metallic connections ended up leaking water vapor into the chamber, which was not compatible with the goal pressure of e-6 mbar. Instead it was decided to use the conductivity of the copper and make it the guide for the thermal energy. Now both the right block of the nozzle and the foot are made out of full copper. This is mounted to the aluminium bread board, which is firmly connected to the vacuum chamber on the inside. This is the current setup and also the one that was used to take measurements. 
#### 4.2.2 update on water cooling 
The water cooling system, that was started by the previous thesis, made the vacuum worse, because the water was evaporating through the tubes. Even changing the plastic tubes with festo connection to a metall tube with welded connections didn't create enough of an enclosure for the water. Therefore a different approach was chosen. A new foot for the nozzle was made out of copper and is now acting as a heat guide, that leads the heat from the pelltier element through the copper foot to the almunimum breadboard, that is connected to the vacuum chamber on the inside, and then outside. 
#### 4.2.3 effect of cooled nozzle on the wire
Unfortunalty the cooled or even heated nozzle imapcts the resistance much much more than any recombination. Just form observation from the 15mu signal, the temperature change impacts the resistance change probably by a couple magnitudes, so that atomic hydrogen impact is not visible. With the 5 mu wire the result is same, but the temperature effect form the nozzle is even less visible. There is a difference in the two wires, one of them (front) cools and heats up faster, but that might be due to a slight difference in distanses between nozzle and wire. 

### 4.2.2 Platform for both PCBs
The two PCB where installed on the same motorized stage, so that they move silmutatinously along the z axis. This allows to take the difference of the reistance between front and back wire. The front wire has the hydrogen beam, while the back wire is facing the homogenous nozzle back, which doesn't have a hole. This allows to see the impact of the hydrogen beam and recombination visible. 
#### 4.2.2.1 Results from having a back wire as comparison 
This actually allowed us to see, that the "blind" back wire is also receiving a signal from the activated plasma. When only looking at the front wire, that is impacted by the recombination, we can just see that there is a signal, but not where the signal is from. Therefore it was very benefitial to have a wire, that doesn't have the beam hitting it. 
The fact that we observe identical signal on both wires, even though the back wire should have ideally no signal, does make us doubt, that the initial resistance jump is just form the recombination. A couple theories that could be applicable here, is that the signal could be from the RF power. Even though we assumed that the shielding by the vacuum chamber with thick walls, should be enough. Maybe the electric signal goes through the cables directly into the multimeter. 

#### 4.2.2.2 Problems with the cavity and how they were solved 
When trying to ignite the plasma, we encounterd a number of problems, that connected to the fact that either plasma was not ignited or it was difficult to maintain a good quality of plasma. The quality plasma was determined in worst case visually, as a very white or orange light indicated that absolute abscense of the Balmber lines,meaning no atomic hydorgen. In use also came the hand held spectographer and in the end the program and spectrometer of Malte Powohl. 
Starting with the major problem, of the plasma not igniting. In the test setup is a different cavity than the one in the main set up. Main difference is that the test set up cavity has a sliding coupler, while the one from the main setup has a screw for that. The sliding mechanism opend a bigger room for uncertainties and movement. Also coupling became harder, as precise tuning is harder. It was much harder to get and stay in the resonant area, where the plasma would ignite. Therefore more methods for ignition were tried out:
Using Surhabis big tesla coil was the most powerful and certain way to ignite. But the dangers to the person holding the coil and also the multimeters was significant enough, to try and stay away from this method if possible. Any time a power RF source was turned on, even for a short while and especially when the cavity reached resonance, gave a spike in the mulitmeter measurements for resistance. Therefore one could not be sure if the resistance jump was only partially or fully due to the aftereffects of the RF source. For the same logic we refrained from using also the small tesla coil. This one was a modified small tesla coil form Amazon, where the wires were exposed and a spark was produced. Even though the impact on the measurement devices was smaller, it still was impactful and at the same time less reliable for ignitioin. 
As a completely new method of producing a starting point for plasma was done by using the apparatus for the neon signs. The wires were tightly wrapped around the glass tube, left and right to the cavity. This way we did not observe any impact on the multimeters, even though the other health risk were not fully explored. In any case we advice against touching the wires when the power is on. 

Ending with a smaller problem, of having difficulties to ignit the plasma. We experienced a process we called "arking". When the two tuning rods came in close proxomity of eachother, a spark between them would span. This spark appeard usually near resonance, which meant we experienced it a lot when trying to get plasma. Because of the high temperature, the spark broke many tuning rods. First the ceramic ones, that came form the producer with the cavity. They did not handle the sudden temperature incerase and would crack and break of. Also any movement from side to side, instead of in line with the rod, would also easily break the rod. This was challenging as exacly this cavity required a lot of tuning with this exact rod. As a next iteration we tried using different kinds of plastic. Fespel, a hard temperature resistant, brown plastic, would burn and produce a carbon ash. So over time the rod would burn up and disappear. Another plastic we tried, actually melted inside the cavity. 
Our solution was to combine the strong sides of all the materials we tired. The new rod had an inner kernel made out of the not melting, hard fespel. On the outside it is coverd with by a tube out of pure ceramics. The ceramics on its own would break too easily, while the fespel would burn or melt. Together, the fespel provides a strong inner core and ceramics protect against the open heat of the spark. 
The reason for this problem was also described in the manual sheet of the cavities. Apparently for the same position of the tuning rod, there are two positions of the other rod, where the resonance is reached. And one of these points, the one closer to the bottom, is the one where the two rods come in too close of a contact and create a spark. The producer suggest as a solution to find the other point, that leaves enough distance between the rods. Sadly we were not able to find it, even though we tried multiple frequencies and RF powers. Out solution was to increase the distance between the rods, by making our ceramic fespel combination thinner by almost a millimeter, that the original rods. A test trial showed, that this allowed for both reliable and easy tuning. 




# 1.2 the model
The modell should be working fine, atl least the experimental and theoretical results match up. 
We can look at extreme conditions as boundaries, like extreme temeprature, pressure, flow. Both for the 5 and 15mu wire. 

  
# 1.3 Outlook based on Dylans approach
suggestions for improvement (dylans ideas and show why his resistance jump was so impressive -> use the modell)
- here some attempts to make the plasma better, by moving the cavity further away from the nozzle, even though DYlan said the opposite. about the quality of plasma it's better to ask Malte and his optical meaurements 