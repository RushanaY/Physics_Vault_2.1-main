# 3. Wire Detector 
The main idea of a wire detector is to use the recombination energy of the molecular hydrogen. This energy heats up a very thin wire, in our case made out of tungsten. even though there are cases of it being done out of platinum and also have different coatings. This heat changes the resistance of the wire according to the equation for R(T) and from that one can derive how high the recombination energy is. 

## 3.1. set up 
The thin wire is part of the "Four wire method", which is build on a PCB. This method has the benifit of cancelling out any resistance form the system itself and just keeping the actual resistance change on the wire. Both the probing current and the measurement of the resistance are done with the HP multimeter, just like in the Surhabis thesis. In general terms the set up look like this. Molecular hydrogen goes form a small hydrogen bottle into a glass tube. Around this tube is a microwave cavity, in our case the Evansen MW cavity, which is powerd by an RF power, producing plasma inside the glass tube. This ionized gas, now having a determinable ratio of disaccosiated hydrogen atoms, is then flowing through a teflon tube inside into the vacuum chamber. The teflon tube ends inside the "cup"  which has a hole on one side. This cup is inside the copper nozzle and also is inline with the same hole in the nozzle. Here the molecular and atomic hydrogen flux enters the insides of the chamber and hits the wire in 5mm distance. 

### 3.1.1 PCB 
The PCB with the wire are mounted on a moving platform, that moves in the z axis, up and down. It has to be noted, that that platform does not have a reliable way to track the moved distance, as it uses the "slip and stick" method, making any "step" count unreliable. The wire can be therefore both moved through the hydrogen beam and also be positioned stationary in front of the nozzle. In the previous setup of Surhabi there already were already two PCBs, on both sides of the nozzle. One, the 'front' wire has the beam hitting it, while the other one - 'back' wire is positioned behind the nozzle and sees only the copper nozzles back. There is no hole, neither in the copper itself, or the teflon cup in side the nozzle. This is done in order to have a reference signal, that is not supposed to experience any recombination energy or the hydrogen beam at all. As part of this thesis both PCBs were mounted onto a platform, which is moved by one motor. In the previous iterations each PCB had its own motor. 

### 3.1.2. Nozzle 
Another important aspect is the nozzle itself. In Surhabis version the nozzle had a plastic foot, while the nozzle is made out of copper. It has a place for a pelltier element, in order to cool the nozzle down. This pelltier in this setup can cool the copper down to 0 degrees celcius or 277K or heat it up to 377K if needed. In Surhabis hypothesis a cold nozzle can incerase the contrast between the atomic and molecular signal. But more about that later. 




## 3.2 Physical description of acting forces and energies 
All energies that influence the resistance should sum up to zero, as we look only at the steady state of thermal equillibrium. 

### 3.2.1. Recombination energy
Each pair of hydrogen atoms releases 4.46eV of energy, when reaching the more energetically ideal position of being together in a molecule. How much the wire gets heated up from this recombination energy does depend on more factors than just the number of molecules that hit the metall. The first obstacle is the number of particles that will hit the surface and actually interact, transferring energy to the metall, instead of bouncing away in and elastic jump. This is the so called sticking coefficient. The next question is how the heat gets transferred around the wire and how much it gets dissapated in the metall or into the air around. With that we get to the next big aspect of all the other parameters, that cool or heat up the wire at the same time and are impossible to isolate. 

## 3.2.2 other energies impacting the resistance
In the master thesis of Surhabi D., she identified five important sources of heat transfer, which I will list of on this section. 
The conduction, derived from Joules law, describes the way the heat conducts along the wire. 
Probe current heating, from the Ohm's law.
Cooling from the beam gas of molecular hydrogen and the background gas in the vacuum chamber.
Radiative cooling from nozzle, vacuum chamber walls and the wire itself. 
Recombination energy is part of , but was already described above. 

