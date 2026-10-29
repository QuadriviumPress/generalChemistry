(src-averill-1-0-ch18)=

# Chapter 18 Chemical Thermodynamics

Chemical reactions obey two fundamental laws. The first of these, the **law of conservation of mass**, states that matter can be neither created nor destroyed. (For more information on matter, see [Chapter 1 \"Introduction to Chemistry\"](/chapters/ch-01-introduction-to-chemistry.md#src-averill-1-0-ch01).) The law of conservation of mass is the basis for all the stoichiometry and equilibrium calculations you have learned thus far in chemistry. The second, the **law of conservation of energy**, states that energy can be neither created nor destroyed. (For more information on energy, see [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05).) Instead, energy takes various forms that can be converted from one form to another. For example, the energy stored in chemical bonds can be released as heat during a chemical reaction.

In [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05), you also learned about *thermochemistry*, the study of energy changes that occur during chemical reactions. Our goal in this chapter is to extend the concepts of thermochemistry to an exploration of thermodynamics[^chem-1] (from the Greek *thermo* and *dynamic*, meaning "heat" and "power," respectively), the study of the interrelationships among heat, work, and the energy content of a system at equilibrium. Thermodynamics tells chemists whether a particular reaction is energetically possible in the direction in which it is written, and it gives the composition of the reaction system at equilibrium. It does not, however, say anything about whether an energetically feasible reaction will *actually* occur as written, and it tells us nothing about the reaction rate or the pathway by which it will occur. The rate of a reaction and its pathway are described by chemical kinetics. (For more information on reaction rates and kinetics, see [Chapter 14 \"Chemical Kinetics\"](/chapters/ch-14-chemical-kinetics.md#src-averill-1-0-ch14).)

![The melting of ice is a thermodynamic process. When a cube of ice melts, there is a spontaneous and irreversible transfer of heat from a warm substance, the surrounding air, to a cold substance, the ice cube. The direction of heat flow in this process and the resulting increase in entropy illustrate the second law of thermodynamics.](/images/section_22/08c2ae94913b0c0ff5f2f51570f42a52.jpg)

**The melting of ice is a thermodynamic process.** When a cube of ice melts, there is a spontaneous and irreversible transfer of heat from a warm substance, the surrounding air, to a cold substance, the ice cube. The direction of heat flow in this process and the resulting increase in entropy illustrate the second law of thermodynamics.

Chemical thermodynamics provides a bridge between the macroscopic properties of a substance and the individual properties of its constituent molecules and atoms. As you will see, thermodynamics explains why graphite can be converted to diamond; how chemical energy stored in molecules can be used to perform work; and why certain processes, such as iron rusting and organisms aging and dying, proceed spontaneously in only one direction, requiring no net input of energy to occur.

## 18.1 Thermodynamics and Work

````````````{note} Learning Objectives

1.  To understand the relationships between work, heat, and energy.
2.  To become familiar with the concept of *PV* work.

````````````

We begin our discussion of thermodynamics by reviewing some important terms introduced in [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05). First, we need to distinguish between a system and its surroundings. A **system** is that part of the universe in which we are interested, such as a mixture of gases in a glass bulb or a solution of substances in a flask. The **surroundings** are everything else---the rest of the *universe*. We can therefore state the following:

(src-averill-1-0-ch18-s01-eq01)=

Equation 18.1

system + surroundings = universe

A **closed system**, such as the contents of a sealed jar, cannot exchange matter with its surroundings, whereas an **open system** can; in this case, we can convert a closed system (the jar) to an open system by removing the jar's lid.

In [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05), we also introduced the concept of a state function[^chem-2], a property of a system that depends on only the present state of the system, not its history. Thus a change in a state function depends on only the difference between the initial and final states, not the pathway used to go from one to the other. To help understand the concept of a state function, imagine a person hiking up a mountain ([Figure 18.1 \"Altitude Is a State Function\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-f01)). If the person is well trained and fit, he or she may be able to climb almost vertically to the top (path A), whereas another less athletic person may choose a path that winds gradually to the top (path B). If both hikers start from the same point at the base of the mountain and end up at the same point at the top, their *net change in altitude* will be the same regardless of the path chosen. Hence altitude is a state function. On the other hand, a person may or may not carry a heavy pack and may climb in hot weather or cold. These conditions would influence changes in the hiker's fatigue level, which depends on the path taken and the conditions experienced. Fatigue, therefore, is not a state function. Thermodynamics is generally concerned with state functions and does not deal with how the change between the initial state and final state occurs.

(src-averill-1-0-ch18-s01-f01)=

Figure 18.1 Altitude Is a State Function

![Figure 18.1 Altitude Is a State Function](/images/section_22/1a0becf7580ac7c3ad14b8767bb2c7ee.jpg)

When hiking up a mountain, a person may decide to take path A, which is almost vertical, or path B, which gradually winds up to the top. Regardless of the path taken, the net change in altitude going from the initial state (bottom of the climb) to the final state (top of the climb) is the same. Thus altitude is a state function.

### The Connections among Work, Heat, and Energy

The internal energy (*E*)[^chem-3] of a system is the sum of the potential energy and the kinetic energy of all the components; internal energy is a state function. Although a closed system cannot exchange matter with its surroundings, it can exchange energy with its surroundings in two ways: by doing work or by releasing or absorbing heat---the flow of thermal energy. Work and heat are therefore two distinct ways of changing the internal energy of a system. We defined *work* (*w*) in [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05) as a force *F* acting through a distance *d*:

(src-averill-1-0-ch18-s01-s01-eq01)=

Equation 18.2

*w* = *Fd*

Because work occurs only when an object, such as a person, or a substance, such as water, moves against an opposing force, work requires that a system and its surroundings be connected. In contrast, the flow of *heat*, the transfer of energy due to differences in temperature between two objects, represents a thermal connection between a system and its surroundings. Thus doing work causes a physical displacement, whereas the flow of heat causes a temperature change. The units of work and heat must be the same because both processes result in the transfer of energy. In the SI system, those units are joules (J), the same unit used for energy. There is no difference between an energy change brought about by doing work on a system and an equal energy change brought about by heating it.

The connections among work, heat, and energy were first described by Benjamin Thompson (1753--1814), an American-born scientist who was also known as Count Rumford. While supervising the manufacture of cannons, Rumford recognized the relationship between the amount of work required to drill out a cannon and the temperature of the water used to cool it during the drilling process ([Figure 18.2 \"The Relationship between Heat and Work\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-s01-f01)). At that time, it was generally thought that heat and work were separate and unrelated phenomena. Hence Rumford's ideas were not widely accepted until many years later, after his findings had been corroborated in other laboratories.

(src-averill-1-0-ch18-s01-s01-f01)=

Figure 18.2 The Relationship between Heat and Work

![Figure 18.2 The Relationship between Heat and Work](/images/section_22/9c1c1d1179148f5b75e8aa47443d635d.jpg)

In the 1780s, an American scientist named Benjamin Thompson, also known as Count Rumford, was hired by the Elector of Bavaria to supervise the manufacture of cannons. During the manufacturing process, teams of horses harnessed to a large-toothed wheel supplied the power needed to drill a hole several inches in diameter straight down the center of a solid brass or bronze cylinder, which was cooled by water. Based on his observations, Rumford became convinced that heat and work are equivalent ways of transferring energy.

### *PV* Work

As we saw in [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05), there are many kinds of work, including mechanical work, electrical work, and work against a gravitational or a magnetic field. Here we will consider only mechanical work, focusing on the work done during changes in the pressure or the volume of a gas. To describe this *pressure--volume work* (*PV* work), we will use such imaginary oddities as frictionless pistons, which involve no component of resistance, and ideal gases, which have no attractive or repulsive interactions.

Imagine, for example, an ideal gas, confined by a frictionless piston, with internal pressure *P*<sub>int</sub> and initial volume *V*<sub>i</sub> ([Figure 18.3](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-s02-f01)). If *P*<sub>ext</sub> = *P*<sub>int</sub>, the system is at equilibrium; the piston does not move, and no work is done. If the external pressure on the piston (*P*<sub>ext</sub>) is less than *P*<sub>int</sub>, however, then the ideal gas inside the piston will expand, forcing the piston to perform work on its surroundings; that is, the final volume (*V*<sub>f</sub>) will be greater than *V*<sub>i</sub>. If *P*<sub>ext</sub> \> *P*<sub>int</sub>, then the gas will be compressed, and the surroundings will perform work on the system.

If the piston has cross-sectional area *A*, the external pressure exerted by the piston is, by definition, the force per unit area: *P*<sub>ext</sub> = *F*/*A*. The volume of any three-dimensional object with parallel sides (such as a cylinder) is the cross-sectional area times the height (*V* = *Ah*). Rearranging to give *F* = *P*<sub>ext</sub>*A* and defining the distance the piston moves (*d*) as Δ*h*, we can calculate the magnitude of the work performed by the piston by substituting into [Equation 18.2](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-s01-eq01):

Equation 18.3

*w* = *Fd* = *P*<sub>ext</sub>*A*Δ*h*

(src-averill-1-0-ch18-s01-s02-f01)=

Figure 18.3 *PV* Work

![Figure 18.3 PV Work](/images/section_22/b36c28640dbe9e375030203bd76e1e00.jpg)

Using a frictionless piston, if the external pressure is less than *P*<sub>int</sub> (a), the ideal gas inside the piston will expand, forcing the piston to perform work on its surroundings. The final volume (*V*<sub>f</sub>) will be greater than *V*<sub>i</sub>. Alternatively, if the external pressure is greater than *P*<sub>int</sub> (b), the gas will be compressed, and the surroundings will perform work on the system.

The change in the volume of the cylinder (Δ*V*) as the piston moves a distance *d* is Δ*V* = *A*Δ*h*, as shown in [Figure 18.4 \"Work Performed with a Change in Volume\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-s02-f02). The work performed is thus

(src-averill-1-0-ch18-s01-s02-eq02)=

Equation 18.4

*w* = *P*<sub>ext</sub>Δ*V*

The units of work obtained using this definition are correct for energy: pressure is force per unit area (newton/m<sup>2</sup>) and volume has units of cubic meters, so

$$w = \left( \frac{F}{A} \right)_{\text{ext}}(\Delta V) = \frac{\text{newton}}{\text{m}^{2}} \times \text{m}^{3} = \text{newton} \cdot \text{m} = \text{joule}$$

(src-averill-1-0-ch18-s01-s02-f02)=

Figure 18.4 Work Performed with a Change in Volume

![Figure 18.4 Work Performed with a Change in Volume](/images/section_22/b47b25398b05c27b31c9824243dfa2e0.jpg)

The change in the volume (Δ*V*) of the cylinder housing a piston is Δ*V* = *A*Δ*h* as the piston moves. The work performed by the surroundings on the system as the piston moves inward is given by *w* = *P*<sub>ext</sub>Δ*V*.

If we use atmospheres for *P* and liters for *V*, we obtain units of L·atm for work. These units correspond to units of energy, as shown in the different values of the ideal gas constant *R*:

$$R = \frac{0.08206\text{~L} \cdot \text{atm}}{\text{mol} \cdot \text{K}} = \frac{8.314\text{~J}}{\text{mol} \cdot \text{K}}$$

Thus 0.08206 L·atm = 8.314 J and 1 L·atm = 101.3 J. (For more information on the ideal gas law, see [Chapter 10 \"Gases\"](/chapters/ch-10-gases.md#src-averill-1-0-ch10).)

Whether work is defined as having a positive sign or a negative sign is a matter of convention. In [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05), we defined heat flow *from* a system *to* its surroundings as negative. Using that same sign convention, we define work done *by* a system *on* its surroundings as having a negative sign because it results in a transfer of energy from a system to its surroundings.[^chem-4] Because Δ*V* \> 0 for an expansion, [Equation 18.4](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-s02-eq02) must be written with a negative sign to describe *PV* work done *by* the system as negative:

(src-averill-1-0-ch18-s01-s02-eq03)=

Equation 18.5

*w* = −*P*<sub>ext</sub>Δ*V*

The work done by a gas expanding against an external pressure is therefore negative, corresponding to work done *by* a system *on* its surroundings. Conversely, when a gas is compressed by an external pressure, Δ*V* \< 0 and the work is positive because work is being done *on* a system *by* its surroundings.

Suppose, for example, that the system under study is a mass of steam heated by the combustion of several hundred pounds of coal and enclosed within a cylinder housing a piston attached to the crankshaft of a large steam engine. The gas is not ideal, and the cylinder is not frictionless. Nonetheless, as steam enters the engine chamber and the expanding gas pushes against the piston, the piston moves, so useful work is performed. In fact, *PV* work launched the Industrial Revolution of the 19th century and powers the internal combustion engine on which most of us still rely for transportation.

In contrast to internal energy, work is not a state function. We can see this by examining [Figure 18.5 \"Work Is Not a State Function\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-s02-f03), in which two different, two-step pathways take a gaseous system from an initial state to a final state with corresponding changes in temperature. In pathway A, the volume of a gas is initially increased while its pressure stays constant (step 1); then its pressure is decreased while the volume remains constant (step 2). In pathway B, the order of the steps is reversed. The temperatures, pressures, and volumes of the initial and final states are identical in both cases, but the amount of work done, indicated by the shaded areas in the figure, is substantially different. As we can see, the amount of work done depends on the pathway taken from (*V*<sub>1</sub>, *P*<sub>1</sub>) to (*V*<sub>2</sub>, *P*<sub>2</sub>), which means that work is not a state function.

````````````{important} Note the Pattern

Internal energy is a state function, whereas work is not.

````````````

(src-averill-1-0-ch18-s01-s02-f03)=

Figure 18.5 Work Is Not a State Function

![Figure 18.5 Work Is Not a State Function](/images/section_22/0ab7f22b5655be982f1d70d39a3e3e12.jpg)

In pathway A, the volume of a gas is initially increased while its pressure stays constant (step 1). Its pressure is then decreased while the volume remains constant (step 2). Pathway B reverses these steps. Although (*V*<sub>1</sub>, *P*<sub>1</sub>) and (*V*<sub>2</sub>, *P*<sub>2</sub>) are identical in both cases, the amount of work done (shaded area) depends on the pathway taken.

### Example 1

A small high-performance internal combustion engine has six cylinders with a total nominal displacement (volume) of 2.40 L and a 10:1 compression ratio (meaning that the volume of each cylinder decreases by a factor of 10 when the piston compresses the air--gas mixture inside the cylinder prior to ignition). How much work in joules is done when a gas in one cylinder of the engine expands at constant temperature against an opposing pressure of 40.0 atm during the engine cycle? Assume that the gas is ideal, the piston is frictionless, and no energy is lost as heat.

**Given:** final volume, compression ratio, and external pressure

**Asked for:** work done

**Strategy:**

**A** Calculate the final volume of gas in a single cylinder. Then compute the initial volume of gas in a single cylinder from the compression ratio.

**B** Use [Equation 18.5](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-s02-eq03) to calculate the work done in liter-atmospheres. Convert from liter-atmospheres to joules.

**Solution:**

**A** To calculate the work done, we need to know the initial and final volumes. The final volume is the volume of one of the six cylinders with the piston all the way down: *V*<sub>f</sub> = 2.40 L/6 = 0.400 L. With a 10:1 compression ratio, the volume of the same cylinder with the piston all the way up is *V*<sub>i</sub> = 0.400 L/10 = 0.0400 L. Work is done by the system on its surroundings, so work is negative.

*w* = −*P*<sub>ext</sub>Δ*V* = −(40.0 atm)(0.400 L − 0.0400 L) = −14.4 L·atm

Converting from liter-atmospheres to joules,

$$w = - (14.4\cancel{\text{L} \cdot \text{atm}})\lbrack 101.3\text{~J/}(\cancel{\text{L} \cdot \text{atm}})\rbrack = - 1.46 \times 10^{3}\text{~J}$$

In the following exercise, you will see that the concept of work is not confined to engines and pistons. It is found in other applications as well.

Exercise

Breathing requires work, even if you are unaware of it. The lung volume of a 70 kg man at rest changed from 2200 mL to 2700 mL when he inhaled, while his lungs maintained a pressure of approximately 1.0 atm. How much work in liter-atmospheres and joules was required to take a single breath? During exercise, his lung volume changed from 2200 mL to 5200 mL on each in-breath. How much additional work in joules did he require to take a breath while exercising?

**Answer:** −0.500 L·atm, or −50.7 J; −304 J; if he takes a breath every three seconds, this corresponds to 1.4 Calories per minute (1.4 kcal).

````````````{important} Summary

**Thermodynamics** is the study of the interrelationships among heat, work, and the energy content of a system at equilibrium. The sum of the potential energy and the kinetic energy of all the components of a system is the **internal energy (***E***)** of the system, which is a **state function**. When the pressure or the volume of a gas is changed, any mechanical work done is called *PV work*. Work done by a system on its surroundings is given a negative value, whereas work done on a system by its surroundings has a positive value.

````````````

````````````{important} Key Takeaway

- Internal energy is a state function that is the sum of the potential and kinetic energy of the system, whereas work is not a state function.

````````````

````````````{important} Key Equation

**Definition of** *PV* **work**

[Equation 18.5](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-s02-eq03): *w* = −*P*<sub>ext</sub>Δ*V*

````````````

### Conceptual Problems

1.  Thermodynamics focuses on the energetics of the reactants and products and provides information about the composition of the reaction system at equilibrium. What information on reaction systems is not provided by thermodynamics?

2.  Given a system in which a substance can produce either of two possible products, A → B or A → C, which of the following can be predicted using chemical thermodynamics?

    1.  At equilibrium, the concentration of product C is greater than the concentration of product B.
    2.  Product C forms more quickly than product B.
    3.  The reaction A → C is exothermic.
    4.  Low-energy intermediates are formed in the reaction A → B.
    5.  The reaction A → C is spontaneous.

3.  In what two ways can a closed system exchange energy with its surroundings? Are these two processes path dependent or path independent?

4.  A microwave oven operates by providing enough energy to rotate water molecules, which produces heat. Can the change in the internal energy of a cup of water heated in a microwave oven be described as a state function? Can the heat produced be described as a state function?

### Answers

1.  Thermodynamics tells us nothing about the rate at which reactants are converted to products.

2.  

3.  heat and work; path dependent

4.  

### Numerical Problems

1.  Calculate the work done in joules in each process.

    1.  compressing 12.8 L of hydrogen gas at an external pressure of 1.00 atm to 8.4 L at a constant temperature
    2.  expanding 21.9 L of oxygen gas at an external pressure of 0.71 atm to 23.7 L at a constant temperature

2.  How much work in joules is done when oxygen is compressed from a volume of 22.8 L and an external pressure of 1.20 atm to 12.0 L at a constant temperature? Was work done by the system or the surroundings?

3.  Champagne is bottled at a CO<sub>2</sub> pressure of about 5 atm. What is the force on the cork if its cross-sectional area is 2.0 cm<sup>2</sup>? How much work is done if a 2.0 g cork flies a distance of 8.2 ft straight into the air when the cork is popped? Was work done by the system or the surroundings?

4.  One mole of water is converted to steam at 1.00 atm pressure and 100°C. Assuming ideal behavior, what is the change in volume when the water is converted from a liquid to a gas? If this transformation took place in a cylinder with a piston, how much work could be done by vaporizing the water at 1.00 atm? Is work done by the system or the surroundings?

5.  Acceleration due to gravity on the earth's surface is 9.8 m/s<sup>2</sup>. How much work is done by a 175 lb person going over Niagara Falls (approximately 520 ft high) in a barrel that weighs 145 lb?

6.  Recall that force can be expressed as mass times acceleration (*F* = *ma*). Acceleration due to gravity on the earth's surface is 9.8 m/s<sup>2</sup>.

    1.  What is the gravitational force on a person who weighs 52 kg?
    2.  How much work is done if the person leaps from a burning building out of a window that is 20 m above the ground?
    3.  If the person lands on a large rescue cushion fitted with a pressure-release valve that maintains an internal pressure of 1.5 atm, how much air is forced out of the cushion?

7.  A gas is allowed to expand from a volume of 2.3 L to a volume of 5.8 L. During the process, 460 J of heat is transferred from the surroundings to the gas.

    1.  How much work has been done if the gas expands against a vacuum?
    2.  How much work has been done if the gas expands against a pressure of 1.3 atm?
    3.  What is the change in the internal energy of the system?

8.  One mole of an ideal gas is allowed to expand from an initial volume of 0.62 L to a final volume of 1.00 L at constant temperature against a constant external pressure of 1.0 atm. How much work has been done?

### Answers

1.  

2.  

3.  

4.  

5.  −230 kJ

6.  

7.  1.  0 J
    2.  −460 J
    3.  0 J

8.  

(src-averill-1-0-ch18-s02)=

## 18.2 The First Law of Thermodynamics

````````````{note} Learning Objective

1.  To calculate changes in internal energy.

````````````

The relationship between the energy change of a system and that of its surroundings is given by the first law of thermodynamics[^chem-5], which states that the *energy of the universe is constant*. Using [Equation 18.1](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-eq01), we can express this law mathematically as follows:

Equation 18.6

$$\begin{aligned}
{\Delta E_{\text{univ}}} & {= \Delta E_{\text{sys}} + \Delta E_{\text{surr}} = 0} \\
{\Delta E_{\text{sys}}} & {= - \Delta E_{\text{surr}}}
\end{aligned}$$

where the subscripts *univ*, *sys*, and *surr* refer to the universe, the system, and the surroundings, respectively. Thus the change in energy of a system is identical in magnitude but opposite in sign to the change in energy of its surroundings.

An important factor that determines the outcome of a chemical reaction is the tendency of all systems, chemical or otherwise, to move toward the lowest possible overall energy state. As a brick dropped from a rooftop falls, its potential energy is converted to kinetic energy; when it reaches ground level, it has achieved a state of lower potential energy. Anyone nearby will notice that energy is transferred to the surroundings as the noise of the impact reverberates and the dust rises when the brick hits the ground. Similarly, if a spark ignites a mixture of isooctane and oxygen in an internal combustion engine, carbon dioxide and water form spontaneously, while potential energy (in the form of the relative positions of atoms in the molecules) is released to the surroundings as heat and work. The internal energy content of the CO<sub>2</sub>/H<sub>2</sub>O product mixture is less than that of the isooctane/O<sub>2</sub> reactant mixture. The two cases differ, however, in the form in which the energy is released to the surroundings. In the case of the falling brick, the energy is transferred as work done on whatever happens to be in the path of the brick; in the case of burning isooctane, the energy can be released as solely heat (if the reaction is carried out in an open container) or as a mixture of heat and work (if the reaction is carried out in the cylinder of an internal combustion engine). Because heat and work are the only two ways in which energy can be transferred between a system and its surroundings, any change in the internal energy of the system is the sum of the heat transferred (*q*) and the work done (*w*):

(src-averill-1-0-ch18-s02-eq02)=

Equation 18.7

Δ*E*<sub>sys</sub> = *q* + *w*

Although *q* and *w* are not state functions on their own, their sum (Δ*E*<sub>sys</sub>) is independent of the path taken and is therefore a state function. A major task for the designers of any machine that converts energy to work is to maximize the amount of work obtained and minimize the amount of energy released to the environment as heat. An example is the combustion of coal to produce electricity. Although the maximum amount of energy available from the process is fixed by the energy content of the reactants and the products, the fraction of that energy that can be used to perform useful work is not fixed, as discussed in [Section 18.5 \"Free Energy\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05). Because we focus almost exclusively on the changes in the energy of a system, we will not use "sys" as a subscript unless we need to distinguish explicitly between a system and its surroundings.

````````````{important} Note the Pattern

The tendency of all systems, chemical or otherwise, is to move toward the state with the lowest possible energy.

````````````

````````````{important} Note the Pattern

Although *q* and *w* are not state functions, their sum (Δ*E*<sub>sys</sub>) is independent of the path taken and therefore is a state function.

````````````

### Example 2

A sample of an ideal gas in the cylinder of an engine is compressed from 400 mL to 50.0 mL during the compression stroke against a constant pressure of 8.00 atm. At the same time, 140 J of energy is transferred from the gas to the surroundings as heat. What is the total change in the internal energy (Δ*E*) of the gas in joules?

**Given:** initial volume, final volume, external pressure, and quantity of energy transferred as heat

**Asked for:** total change in internal energy

**Strategy:**

**A** Determine the sign of *q* to use in [Equation 18.7](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-eq02).

**B** From [Equation 18.5](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-s02-eq03), calculate *w* from the values given. Substitute this value into [Equation 18.7](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-eq02) to calculate Δ*E*.

**Solution:**

**A** From [Equation 18.7](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-eq02), we know that Δ*E* = *q* + *w*. We are given the magnitude of *q* (140 J) and need only determine its sign. Because energy is transferred from the system (the gas) to the surroundings, *q* is negative by convention.

**B** Because the gas is being compressed, we know that work is being done *on* the system, so *w* must be positive. From [Equation 18.5](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-s02-eq03),

$$w = - P_{\text{ext}}\Delta V = - 8.00\cancel{\text{atm}}(0.0500\ \cancel{\text{L}} - 0.400\ \cancel{\text{L}})\left( \frac{101.3\text{~J}}{\cancel{\text{L}} \cdot \cancel{\text{atm}}} \right) = 284\text{~J}$$

Thus

Δ*E* = *q* + *w* = −140 J + 284 J = 144 J

In this case, although work is done *on* the gas, increasing its internal energy, heat flows *from* the system *to* the surroundings, decreasing its internal energy by 144 J. The work done and the heat transferred can have opposite signs.

Exercise

A sample of an ideal gas is allowed to expand from an initial volume of 0.200 L to a final volume of 3.50 L against a constant external pressure of 0.995 atm. At the same time, 117 J of heat is transferred from the surroundings to the gas. What is the total change in the internal energy (Δ*E*) of the gas in joules?

**Answer:** −216 J

````````````{important} Note the Pattern

By convention, both heat flow and work have a negative sign when energy is transferred from a system to its surroundings and vice versa.

````````````

### Enthalpy

To further understand the relationship between heat flow (*q*) and the resulting change in internal energy (Δ*E*), we can look at two sets of limiting conditions: reactions that occur at constant volume and reactions that occur at constant pressure. We will assume that *PV* work is the only kind of work possible for the system, so we can substitute its definition from [Equation 18.5](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s01-s02-eq03) into [Equation 18.7](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-eq02) to obtain the following:

(src-averill-1-0-ch18-s02-s01-eq01)=

Equation 18.8

Δ*E* = *q* − *P*Δ*V*

where the subscripts have been deleted.

If the reaction occurs in a closed vessel, the volume of the system is fixed, and Δ*V* is zero. Under these conditions, the heat flow (often given the symbol *q*<sub>v</sub> to indicate constant volume) must equal Δ*E*:

Equation 18.9

$$\underset{\text{constant~volume}}{q_{\text{v}} = \Delta E}$$

No *PV* work can be done, and the change in the internal energy of the system is equal to the amount of heat transferred from the system to the surroundings or vice versa.

Many chemical reactions are not, however, carried out in sealed containers at constant volume but in open containers at a more or less constant pressure of about 1 atm. The heat flow under these conditions is given the symbol *q*<sub>p</sub> to indicate constant pressure. Replacing *q* in [Equation 18.8](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s01-eq01) by *q*<sub>p</sub> and rearranging to solve for *q*<sub>p</sub>,

Equation 18.10

$$\underset{\text{constant~pressure}}{q_{\text{p}} = \Delta E + P\Delta V}$$

Thus, at constant pressure, the heat flow for any process is equal to the change in the internal energy of the system plus the *PV* work done, as we stated in [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05).

Because conditions of constant pressure are so important in chemistry, a new state function called enthalpy (*H*)[^chem-6] is defined as *H* = *E* + *PV*. At constant pressure, the change in the enthalpy of a system is as follows:

(src-averill-1-0-ch18-s02-s01-eq04)=

Equation 18.11

Δ*H* = Δ*E* + Δ(*PV*) = Δ*E* + *P*Δ*V*

Comparing the previous two equations shows that at constant pressure, the change in the enthalpy of a system is equal to the heat flow: Δ*H* = *q*<sub>p</sub>. This expression is consistent with our definition of enthalpy in [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05), where we stated that enthalpy is the heat absorbed or produced during any process that occurs at constant pressure.

````````````{important} Note the Pattern

At constant pressure, the change in the enthalpy of a system is equal to the heat flow: Δ*H* = *q*<sub>p</sub>.

````````````

### Example 3

The molar enthalpy of fusion for ice at 0.0°C and a pressure of 1.00 atm is 6.01 kJ, and the molar volumes of ice and water at 0°C are 0.0197 L and 0.0180 L, respectively. Calculate Δ*H* and Δ*E* for the melting of ice at 0.0°C. (For more information on enthalpy, see [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05), [Section 5.2 \"Enthalpy\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05-s02).)

**Given:** enthalpy of fusion for ice, pressure, and molar volumes of ice and water

**Asked for:** Δ*H* and Δ*E* for ice melting at 0.0°C

**Strategy:**

**A** Determine the sign of *q* and set this value equal to Δ*H*.

**B** Calculate Δ(*PV*) from the information given.

**C** Determine Δ*E* by substituting the calculated values into [Equation 18.11](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s01-eq04).

**Solution:**

**A** Because 6.01 kJ of heat is absorbed from the surroundings when 1 mol of ice melts, *q* = +6.01 kJ. When the process is carried out at constant pressure, *q* = *q*<sub>p</sub> = Δ*H* = 6.01 kJ.

**B** To find Δ*E* using [Equation 18.11](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s01-eq04), we need to calculate Δ(*PV*). The process is carried out at a constant pressure of 1.00 atm, so

$$\begin{aligned}
{\Delta(PV)} & {= P\Delta V = P(V_{\text{f}} - V) = (1.00\text{~atm})(0.0180\text{~L} - 0.0197\text{~L})} \\
 & {= ( - 1.7 \times 10^{- 3}\ \cancel{\text{L} \cdot \text{atm}})(101.3\text{~J/}\cancel{\text{L} \cdot \text{atm}}) = - 0.0017\text{~J}}
\end{aligned}$$

**C** Substituting the calculated values of Δ*H* and *P*Δ*V* into [Equation 18.11](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s01-eq04),

Δ*E* = Δ*H* − *P*Δ*V* = 6010 J − (−0.0017 J) = 6010 J = 6.01 kJ

Exercise

At 298 K and 1 atm, the conversion of graphite to diamond requires the input of 1.850 kJ of heat per mole of carbon. The molar volumes of graphite and diamond are 0.00534 L and 0.00342 L, respectively. Calculate Δ*H* and Δ*E* for the conversion of C (graphite) to C (diamond) under these conditions.

**Answer:** Δ*H* = 1.85 kJ/mol; Δ*E* = 1.85 kJ/mol

### The Relationship between Δ*H* and Δ*E*

If Δ*H* for a reaction is known, we can use the change in the enthalpy of the system ([Equation 18.11](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s01-eq04)) to calculate its change in internal energy. When a reaction involves only solids, liquids, liquid solutions, or any combination of these, the volume does not change appreciably (Δ*V* = 0). Under these conditions, we can simplify [Equation 18.11](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s01-eq04) to Δ*H* = Δ*E*. If gases are involved, however, Δ*H* and Δ*E* can differ significantly. We can calculate Δ*E* from the measured value of Δ*H* by using the right side of [Equation 18.11](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s01-eq04) together with the ideal gas law, *PV* = *nRT*. Recognizing that Δ(*PV*) = Δ(*nRT*), we can rewrite [Equation 18.11](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s01-eq04) as follows:

Equation 18.12

Δ*H* = Δ*E* + Δ(*PV*) = Δ*E* + Δ(*nRT*)

At constant temperature, Δ(*nRT*) = *RT*Δ*n*, where Δ*n* is the difference between the final and initial numbers of moles of gas. Thus

(src-averill-1-0-ch18-s02-s02-eq02)=

Equation 18.13

Δ*E* = Δ*H* − *RT*Δ*n*

For reactions that result in a net production of gas, Δ*n* \> 0, so Δ*E* \< Δ*H*. Conversely, endothermic reactions (Δ*H* \> 0) that result in a net consumption of gas have Δ*n* \< 0 and Δ*E* \> Δ*H*. The relationship between Δ*H* and Δ*E* for systems involving gases is illustrated in Example 4.

````````````{important} Note the Pattern

For reactions that result in a net production of gas, Δ*E* \< Δ*H*. For endothermic reactions that result in a net consumption of gas, Δ*E* \> Δ*H*.

````````````

### Example 4

The combustion of graphite to produce carbon dioxide is described by the equation C (graphite, s) + O<sub>2</sub>(g) → CO<sub>2</sub>(g). At 298 K and 1.0 atm, Δ*H* = −393.5 kJ/mol of graphite for this reaction, and the molar volume of graphite is 0.0053 L. What is Δ*E* for the reaction?

**Given:** balanced chemical equation, temperature, pressure, Δ*H*, and molar volume of reactant

**Asked for:** Δ*E*

**Strategy:**

**A** Use the balanced chemical equation to calculate the change in the number of moles of gas during the reaction.

**B** Substitute this value and the data given into [Equation 18.13](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s02-eq02) to obtain Δ*E*.

**Solution:**

**A** In this reaction, 1 mol of gas (CO<sub>2</sub>) is produced, and 1 mol of gas (O<sub>2</sub>) is consumed. Thus Δ*n* = 1 − 1 = 0.

**B** Substituting this calculated value and the given values into [Equation 18.13](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s02-eq02),

$$\begin{aligned}
{\Delta E = \Delta H - RT\Delta n} & {= ( - 393.5\text{~kJ/mol}) - \lbrack 8.314\text{~J/}(\text{mol} \cdot \text{K})\rbrack(298\text{~K})(0)} \\
 & {= ( - 393.5\text{~kJ/mol}) - (0\text{~J/mol}) = - 393.5\text{~kJ/mol}}
\end{aligned}$$

To understand why only the change in the volume of the gases needs to be considered, notice that the molar volume of graphite is only 0.0053 L. A change in the number of moles of gas corresponds to a volume change of 22.4 L/mol of gas at standard temperature and pressure (STP), so the volume of gas consumed or produced in this case is (1)(22.4 L) = 22.4 L, which is much, much greater than the volume of 1 mol of a solid such as graphite.

Exercise

Calculate Δ*E* for the conversion of oxygen gas to ozone at 298 K: 3O<sub>2</sub>(g) → 2O<sub>3</sub>(g). The value of Δ*H* for the reaction is 285.4 kJ.

**Answer:** 288 kJ

As the exercise in Example 4 illustrates, the magnitudes of Δ*H* and Δ*E* for reactions that involve gases are generally rather similar, even when there is a net production or consumption of gases.

````````````{important} Summary

The **first law of thermodynamics** states that the energy of the universe is constant. The change in the internal energy of a system is the sum of the heat transferred and the work done. At constant pressure, heat flow (*q*) and internal energy (*E*) are related to the system's **enthalpy (***H***)**. The heat flow is equal to the change in the internal energy of the system plus the *PV* work done. When the volume of a system is constant, changes in its internal energy can be calculated by substituting the ideal gas law into the equation for Δ*E*.

````````````

````````````{important} Key Takeaway

- Enthalpy is a state function, and the change in enthalpy of a system is equal to the sum of the change in the internal energy of the system and the *PV* work done.

````````````

````````````{important} Key Equations

**Internal energy change**

[Equation 18.7](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-eq02): Δ*E*<sub>sys</sub> = *q* + *w*

**Enthalpy change**

[Equation 18.11](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s01-eq04): Δ*H* = Δ*E* + Δ(*PV*)

**Relationship between Δ** *H* **and Δ** *E* **for an ideal gas**

[Equation 18.13](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s02-eq02): Δ*E* = Δ*H* − *RT*Δ*n*

````````````

### Conceptual Problems

1.  Describe how a swinging pendulum that slows with time illustrates the first law of thermodynamics.

2.  When air is pumped into a bicycle tire, the air is compressed. Assuming that the volume is constant, express the change in internal energy in terms of *q* and *w*.

3.  What is the relationship between enthalpy and internal energy for a reaction that occurs at constant pressure?

4.  An intrepid scientist placed an unknown salt in a small amount of water. All the salt dissolved in the water, and the temperature of the solution dropped several degrees.

    1.  What is the sign of the enthalpy change for this reaction?
    2.  Assuming the heat capacity of the solution is the same as that of pure water, how would the scientist calculate the molar enthalpy change?
    3.  Propose an explanation for the decrease in temperature.

5.  For years, chemists and physicists focused on enthalpy changes as a way to measure the spontaneity of a reaction. What arguments would you use to convince them not to use this method?

6.  What is the relationship between enthalpy and internal energy for a reaction that occurs at constant volume?

7.  The *enthalpy of combustion* (Δ*H*<sub>comb</sub>) is defined thermodynamically as the enthalpy change for complete oxidation. The complete oxidation of hydrocarbons is represented by the following general equation: hydrocarbon + O<sub>2</sub>(g) → CO<sub>2</sub>(g) + H<sub>2</sub>O(g). Enthalpies of combustion from reactions like this one can be measured experimentally with a high degree of precision. It has been found that the less stable the reactant, the more heat is evolved, so the more negative the value of Δ*H*<sub>comb</sub>. In each pair of hydrocarbons, which member do you expect to have the greater (more negative) heat of combustion? Justify your answers.

    1.  cyclopropane or cyclopentane
    2.  butane or 2-methylpropane
    3.  hexane or cyclohexane

8.  Using a structural argument, explain why the *trans* isomer of 2-butene is more stable than the *cis* isomer. The enthalpies of formation of *cis*- and *trans*-2-butene are −7.1 kJ/mol and −11.4 kJ/mol, respectively.

9.  Using structural arguments, explain why cyclopropane has a positive $\Delta H_{\text{f}}^{\text{°}}$ (12.7 kJ/mol), whereas cyclopentane has a negative $\Delta H_{\text{f}}^{\text{°}}$ (−18.4 kJ/mol). (Hint: consider bond angles.)

### Answers

1.  

2.  

3.  At constant pressure, Δ*H* = Δ*E* + *P*Δ*V*.

4.  

5.  

6.  

7.  

8.  

9.  With bond angles of 60°, cyclopropane is highly strained, causing it to be less stable than cyclopentane, which has nearly ideal tetrahedral geometry at each carbon atom.

### Numerical Problems

1.  A block of CO<sub>2</sub> weighing 15 g evaporates in a 5.0 L container at 25°C. How much work has been done if the gas is allowed to expand against an external pressure of 0.98 atm under isothermal conditions? The enthalpy of sublimation of CO<sub>2</sub> is 25.1 kJ/mol. What is the change in internal energy (kJ/mol) for the sublimation of CO<sub>2</sub> under these conditions?

2.  Zinc and HCl react according to the following equation:

    Zn(s) + 2HCl(aq) → Zn<sup>2+</sup>(aq) + 2Cl<sup>−</sup>(aq) + H<sub>2</sub>(g)

    When 3.00 g of zinc metal is added to a dilute HCl solution at 1.00 atm and 25°C, and this reaction is allowed to go to completion at constant pressure, 6.99 kJ of heat must be removed to return the final solution to its original temperature. What are the values of *q* and *w*, and what is the change in internal energy?

3.  Acetylene torches, used industrially to cut and weld metals, reach flame temperatures as high as 3000°C. The combustion reaction is as follows:

    $$\left. \text{2C}_{\text{2}}\text{H}_{\text{2}}\left( \text{g} \right) + \text{5O}_{\text{2}}\left( \text{g} \right)\rightarrow\text{4CO}_{\text{2}}\left( \text{g} \right) + \text{2H}_{\text{2}}\text{O}\left( \text{l} \right)\quad\Delta H = - \text{2599~kJ} \right.$$

    Calculate the amount of work done against a pressure of 1.0 atm when 4.0 mol of acetylene are allowed to react with 10 mol of O<sub>2</sub> at 1.0 atm at 20°C. What is the change in internal energy for the reaction?

4.  When iron dissolves in 1.00 M aqueous HCl, the products are FeCl<sub>2</sub>(aq) and hydrogen gas. Calculate the work done if 30 g of Fe react with excess hydrochloric acid in a closed vessel at 20°C. How much work is done if the reaction takes place in an open vessel with an external pressure of 1.0 atm?

### Answer

1.  −350 J; 8.2 kJ

2.  

3.  

4.  

## 18.3 The Second Law of Thermodynamics

````````````{note} Learning Objective

1.  To understand the relationship between internal energy and entropy.

````````````

The first law of thermodynamics governs changes in the state function we have called internal energy (*E*). According to [Section 18.2 \"The First Law of Thermodynamics\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02), changes in the internal energy (Δ*E*) are closely related to changes in the enthalpy (Δ*H*), which is a measure of the heat flow between a system and its surroundings at constant pressure. You also learned in [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05) that the enthalpy change for a chemical reaction can be calculated using tabulated values of enthalpies of formation. This information, however, does not tell us whether a particular process or reaction will occur spontaneously.

Let's consider a familiar example of spontaneous change. If a hot frying pan that has just been removed from the stove is allowed to come into contact with a cooler object, such as cold water in a sink, heat will flow from the hotter object to the cooler one, in this case usually releasing steam. Eventually both objects will reach the same temperature, at a value between the initial temperatures of the two objects. This transfer of heat from a hot object to a cooler one obeys the first law of thermodynamics: energy is conserved.

Now consider the same process in reverse. Suppose that a hot frying pan in a sink of cold water were to become hotter while the water became cooler. As long as the same amount of thermal energy was gained by the frying pan and lost by the water, the first law of thermodynamics would be satisfied. Yet we all know that such a process cannot occur: heat always flows from a hot object to a cold one, never in the reverse direction. That is, *by itself* the magnitude of the heat flow associated with a process does not predict whether the process will occur spontaneously.

For many years, chemists and physicists tried to identify a single measurable quantity that would enable them to predict whether a particular process or reaction would occur spontaneously. Initially, many of them focused on enthalpy changes and hypothesized that an exothermic process would always be spontaneous. But although it is true that many, if not most, spontaneous processes are exothermic, there are also many spontaneous processes that are *not* exothermic. For example, at a pressure of 1 atm, ice melts spontaneously at temperatures greater than 0°C, yet this is an endothermic process because heat is absorbed. Similarly, many salts (such as NH<sub>4</sub>NO<sub>3</sub>, NaCl, and KBr) dissolve spontaneously in water even though they absorb heat from the surroundings as they dissolve (i.e., Δ*H*<sub>soln</sub> \> 0). Reactions can also be both spontaneous and highly endothermic, like the reaction of barium hydroxide with ammonium thiocyanate shown in [Figure 18.6 \"An Endothermic Reaction\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-f01).

(src-averill-1-0-ch18-s03-f01)=

Figure 18.6 An Endothermic Reaction

![Figure 18.6 An Endothermic Reaction](/images/section_22/e114d8b906636e9d35e46b12b2d9118b.jpg)

The reaction of barium hydroxide with ammonium thiocyanate is spontaneous but highly endothermic, so water, one product of the reaction, quickly freezes into slush. When water is placed on a block of wood under the flask, the highly endothermic reaction that takes place in the flask freezes water that has been placed under the beaker, so the flask becomes frozen to the wood.

Thus enthalpy is not the only factor that determines whether a process is spontaneous. For example, after a cube of sugar has dissolved in a glass of water so that the sucrose molecules are uniformly dispersed in a dilute solution, they never spontaneously come back together in solution to form a sugar cube. Moreover, the molecules of a gas remain evenly distributed throughout the entire volume of a glass bulb and never spontaneously assemble in only one portion of the available volume. To help explain why these phenomena proceed spontaneously in only one direction requires an additional state function called entropy (*S*)[^chem-7], a thermodynamic property of all substances that is proportional to their degree of disorder. In [Chapter 13 \"Solutions\"](/chapters/ch-13-solutions.md#src-averill-1-0-ch13), we introduced the concept of entropy in relation to solution formation. Here we further explore the nature of this state function and define it mathematically.

### Entropy

Chemical and physical changes in a system may be accompanied by either an increase or a decrease in the disorder of the system, corresponding to an increase in entropy (Δ*S* \> 0) or a decrease in entropy (Δ*S* \< 0), respectively. As with any other state function, the change in entropy is defined as the difference between the entropies of the final and initial states: Δ*S* = *S*<sub>f</sub> − *S*<sub>i</sub>.

When a gas expands into a vacuum, its entropy increases because the increased volume allows for greater atomic or molecular disorder. The greater the number of atoms or molecules in the gas, the greater the disorder. The magnitude of the entropy of a system depends on the number of microscopic states, or *microstates*, associated with it (in this case, the number of atoms or molecules); that is, the greater the number of microstates, the greater the entropy.

We can illustrate the concepts of microstates and entropy using a deck of playing cards, as shown in [Figure 18.7 \"Illustrating Low- and High-Entropy States with a Deck of Playing Cards\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s01-f01). In any new deck, the 52 cards are arranged by four suits, with each suit arranged in descending order. If the cards are shuffled, however, there are approximately 10<sup>68</sup> different ways they might be arranged, which corresponds to 10<sup>68</sup> different microscopic states. The entropy of an ordered new deck of cards is therefore low, whereas the entropy of a randomly shuffled deck is high. Card games assign a higher value to a hand that has a low degree of disorder. In games such as five-card poker, only 4 of the 2,598,960 different possible hands, or microstates, contain the highly ordered and valued arrangement of cards called a royal flush, almost 1.1 million hands contain one pair, and more than 1.3 million hands are completely disordered and therefore have no value. Because the last two arrangements are far more probable than the first, the value of a poker hand is inversely proportional to its entropy.

(src-averill-1-0-ch18-s03-s01-f01)=

Figure 18.7 Illustrating Low- and High-Entropy States with a Deck of Playing Cards

![Figure 18.7 Illustrating Low- and High-Entropy States with a Deck of Playing Cards](/images/section_22/ca50eebb29059147760ce6b89af6fe50.jpg)

An new, unshuffled deck (top) has only a single arrangement, so there is only one microstate. In contrast, a randomly shuffled deck (bottom) can have any one of approximately 10<sup>68</sup> different arrangements, which correspond to 10<sup>68</sup> different microstates.

We can see how to calculate these kinds of probabilities for a chemical system by considering the possible arrangements of a sample of four gas molecules in a two-bulb container ([Figure 18.8 \"The Possible Microstates for a Sample of Four Gas Molecules in Two Bulbs of Equal Volume\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s01-f02)). There are five possible arrangements: all four molecules in the left bulb (I); three molecules in the left bulb and one in the right bulb (II); two molecules in each bulb (III); one molecule in the left bulb and three molecules in the right bulb (IV); and four molecules in the right bulb (V). If we assign a different color to each molecule to keep track of it for this discussion (remember, however, that in reality the molecules are indistinguishable from one another), we can see that there are 16 different ways the four molecules can be distributed in the bulbs, each corresponding to a particular microstate. As shown in [Figure 18.8 \"The Possible Microstates for a Sample of Four Gas Molecules in Two Bulbs of Equal Volume\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s01-f02), arrangement I is associated with a single microstate, as is arrangement V, so each arrangement has a probability of 1/16. Arrangements II and IV each have a probability of 4/16 because each can exist in four microstates. Similarly, six different microstates can occur as arrangement III, making the probability of this arrangement 6/16. Thus the arrangement that we would expect to encounter, with half the gas molecules in each bulb, is the *most probable* arrangement. The others are not impossible but simply less likely.

(src-averill-1-0-ch18-s03-s01-f02)=

Figure 18.8 The Possible Microstates for a Sample of Four Gas Molecules in Two Bulbs of Equal Volume

![Figure 18.8 The Possible Microstates for a Sample of Four Gas Molecules in Two Bulbs of Equal Volume](/images/section_22/16332a96c8e876b99cc7e54f47db2867.jpg)

There are 16 different ways to distribute four gas molecules between the bulbs, with each distribution corresponding to a particular microstate. Arrangements I and V each produce a single microstate with a probability of 1/16. This particular arrangement is so improbable that it is likely not observed. Arrangements II and IV each produce four microstates, with a probability of 4/16. Arrangement III, with half the gas molecules in each bulb, has a probability of 6/16. It is the one encompassing the most microstates, so it is the most probable.

Instead of four molecules of gas, let's now consider 1 L of an ideal gas at standard temperature and pressure (STP), which contains 2.69 × 10<sup>22</sup> molecules (6.022 × 10<sup>23</sup> molecules/22.4 L). If we allow the sample of gas to expand into a second 1 L container, the probability of finding all 2.69 × 10<sup>22</sup> molecules in one container and none in the other at any given time is extremely small, approximately $\frac{2}{2.69 \times 10^{22}}\text{.}$ The probability of such an occurrence is effectively zero. Although nothing prevents the molecules in the gas sample from occupying only one of the two bulbs, that particular arrangement is so improbable that it is never actually observed. The probability of arrangements with essentially equal numbers of molecules in each bulb is quite high, however, because there are *many* equivalent microstates in which the molecules are distributed equally. Hence a macroscopic sample of a gas occupies all of the space available to it, simply because this is the most probable arrangement.

A disordered system has a greater number of possible microstates than does an ordered system, so it has a higher entropy. This is most clearly seen in the entropy changes that accompany phase transitions, such as solid to liquid or liquid to gas. As you know from [Chapter 11 \"Liquids\"](/chapters/ch-11-liquids.md#src-averill-1-0-ch11), [Chapter 12 \"Solids\"](/chapters/ch-12-solids.md#src-averill-1-0-ch12), and [Chapter 13 \"Solutions\"](/chapters/ch-13-solutions.md#src-averill-1-0-ch13), a crystalline solid is composed of an ordered array of molecules, ions, or atoms that occupy fixed positions in a lattice, whereas the molecules in a liquid are free to move and tumble within the volume of the liquid; molecules in a gas have even more freedom to move than those in a liquid. Each degree of motion increases the number of available microstates, resulting in a higher entropy. Thus the entropy of a system must increase during melting (Δ*S*<sub>fus</sub> \> 0). Similarly, when a liquid is converted to a vapor, the greater freedom of motion of the molecules in the gas phase means that Δ*S*<sub>vap</sub> \> 0. Conversely, the reverse processes (condensing a vapor to form a liquid or freezing a liquid to form a solid) must be accompanied by a decrease in the entropy of the system: Δ*S* \< 0.

````````````{important} Note the Pattern

Entropy (*S*) is a thermodynamic property of all substances that is proportional to their degree of disorder. The greater the number of possible microstates for a system, the greater the disorder and the higher the entropy.

````````````

Experiments show that the magnitude of Δ*S*<sub>vap</sub> is 80--90 J/(mol·K) for a wide variety of liquids with different boiling points. However, liquids that have highly ordered structures due to hydrogen bonding or other intermolecular interactions tend to have significantly higher values of Δ*S*<sub>vap</sub>. For instance, Δ*S*<sub>vap</sub> for water is 102 J/(mol·K). Another process that is accompanied by entropy changes is the formation of a solution. As illustrated in [Figure 18.9 \"The Effect of Solution Formation on Entropy\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s01-f03), the formation of a liquid solution from a crystalline solid (the solute) and a liquid solvent is expected to result in an increase in the number of available microstates of the system and hence its entropy. Indeed, dissolving a substance such as NaCl in water disrupts both the ordered crystal lattice of NaCl and the ordered hydrogen-bonded structure of water, leading to an increase in the entropy of the system. At the same time, however, each dissolved Na<sup>+</sup> ion becomes hydrated by an ordered arrangement of at least six water molecules, and the Cl<sup>−</sup> ions also cause the water to adopt a particular local structure. Both of these effects *increase* the order of the system, leading to a *decrease* in entropy. The overall entropy change for the formation of a solution therefore depends on the relative magnitudes of these opposing factors. In the case of an NaCl solution, disruption of the crystalline NaCl structure and the hydrogen-bonded interactions in water is quantitatively more important, so Δ*S*<sub>soln</sub> \> 0.

(src-averill-1-0-ch18-s03-s01-f03)=

Figure 18.9 The Effect of Solution Formation on Entropy

![Figure 18.9 The Effect of Solution Formation on Entropy](/images/section_22/b8c52b3c38b3bc645d4a6e8649a04f21.jpg)

Dissolving NaCl in water results in an increase in the entropy of the system. Each hydrated ion, however, forms an ordered arrangement with water molecules, which decreases the entropy of the system. The magnitude of the increase is greater than the magnitude of the decrease, so the overall entropy change for the formation of an NaCl solution is positive.

### Example 5

Predict which substance in each pair has the higher entropy and justify your answer.

1.  1 mol of NH<sub>3</sub>(g) or 1 mol of He(g), both at 25°C
2.  1 mol of Pb(s) at 25°C or 1 mol of Pb(l) at 800°C

**Given:** amounts of substances and temperature

**Asked for:** higher entropy

**Strategy:**

From the number of atoms present and the phase of each substance, predict which has the greater number of available microstates and hence the higher entropy.

**Solution:**

1.  Both substances are gases at 25°C, but one consists of He atoms and the other consists of NH<sub>3</sub> molecules. With four atoms instead of one, the NH<sub>3</sub> molecules have more motions available, leading to a greater number of microstates. Hence we predict that the NH<sub>3</sub> sample will have the higher entropy.
2.  The nature of the atomic species is the same in both cases, but the phase is different: one sample is a solid, and one is a liquid. Based on the greater freedom of motion available to atoms in a liquid, we predict that the liquid sample will have the higher entropy.

Exercise

Predict which substance in each pair has the higher entropy and justify your answer.

1.  1 mol of He(g) at 10 K and 1 atm pressure or 1 mol of He(g) at 250°C and 0.2 atm
2.  a mixture of 3 mol of H<sub>2</sub>(g) and 1 mol of N<sub>2</sub>(g) at 25°C and 1 atm or a sample of 2 mol of NH<sub>3</sub>(g) at 25°C and 1 atm

**Answer:**

1.  1 mol of He(g) at 250°C and 0.2 atm (higher temperature and lower pressure indicate greater volume and more microstates)
2.  a mixture of 3 mol of H<sub>2</sub>(g) and 1 mol of N<sub>2</sub>(g) at 25°C and 1 atm (more molecules of gas are present)

### Reversible and Irreversible Changes

Changes in entropy (Δ*S*), together with changes in enthalpy (Δ*H*), enable us to predict in which direction a chemical or physical change will occur spontaneously. Before discussing how to do so, however, we must understand the difference between a reversible process and an irreversible one. In a reversible process[^chem-8], every intermediate state between the extremes is an equilibrium state, regardless of the direction of the change. In contrast, an irreversible process[^chem-9] is one in which the intermediate states are not equilibrium states, so change occurs spontaneously in only one direction. As a result, *a reversible process can change direction at any time, whereas an irreversible process cannot*. When a gas expands reversibly against an external pressure such as a piston, for example, the expansion can be reversed at any time by reversing the motion of the piston; once the gas is compressed, it can be allowed to expand again, and the process can continue indefinitely. In contrast, the expansion of a gas into a vacuum (*P*<sub>ext</sub> = 0) is irreversible because the external pressure is measurably less than the internal pressure of the gas. No equilibrium states exist, and the gas expands irreversibly. When gas escapes from a microscopic hole in a balloon into a vacuum, for example, the process is irreversible; the direction of airflow cannot change.

Because work done during the expansion of a gas depends on the opposing external pressure (*w* = *P*<sub>ext</sub>Δ*V*), *work done in a reversible process is always equal to or greater than work done in a corresponding irreversible process*: *w*<sub>rev</sub> ≥ *w*<sub>irrev</sub>. Whether a process is reversible or irreversible, Δ*E* = *q* + *w*. Because *E* is a state function, the magnitude of Δ*E* does *not* depend on reversibility and is independent of the path taken. So

(src-averill-1-0-ch18-s03-s02-eq01)=

Equation 18.14

Δ*E* = *q*<sub>rev</sub> + *w*<sub>rev</sub> = *q*<sub>irrev</sub> + *w*<sub>irrev</sub>

````````````{important} Note the Pattern

Work done in a reversible process is always equal to or greater than work done in a corresponding irreversible process: *w*<sub>rev</sub> ≥ *w*<sub>irrev</sub>.

````````````

In other words, Δ*E* for a process is the same whether that process is carried out in a reversible manner or an irreversible one. We now return to our earlier definition of entropy, using the magnitude of the heat flow for a reversible process (*q*<sub>rev</sub>) to define entropy quantitatively.

### The Relationship between Internal Energy and Entropy

Because the quantity of heat transferred (*q*<sub>rev</sub>) is directly proportional to the absolute temperature of an object (*T*) (*q*<sub>rev</sub> ∝ *T*), the hotter the object, the greater the amount of heat transferred. Moreover, adding heat to a system increases the kinetic energy of the component atoms and molecules and hence their disorder (Δ*S* ∝ *q*<sub>rev</sub>). Combining these relationships for any reversible process,

(src-averill-1-0-ch18-s03-s03-eq01)=

Equation 18.15

$$\begin{array}{rcc}
{q_{\text{rev}} = T\Delta S} & \text{and} & {\Delta S = \frac{q_{\text{rev}}}{T}}
\end{array}$$

Because the numerator (*q*<sub>rev</sub>) is expressed in units of energy (joules), the units of Δ*S* are joules/kelvin (J/K). Recognizing that the work done in a reversible process at constant pressure is *w*<sub>rev</sub> = −*P*Δ*V*, we can express [Equation 18.14](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s02-eq01) as follows:

(src-averill-1-0-ch18-s03-s03-eq02)=

Equation 18.16

Δ*E* = *q*<sub>rev</sub> + *w*<sub>rev</sub> = *T*Δ*S* − *P*Δ*V*

Thus the change in the internal energy of the system is related to the change in entropy, the absolute temperature, and the *PV* work done.

To illustrate the use of [Equation 18.15](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-eq01) and [Equation 18.16](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-eq02), we consider two reversible processes before turning to an irreversible process. When a sample of an ideal gas is allowed to expand reversibly at constant temperature, heat must be added to the gas during expansion to keep its *T* constant ([Figure 18.10 \"Expansion of Gas at Constant Temperature\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-f01)). The internal energy of the gas does not change because the temperature of the gas does not change; that is, Δ*E* = 0 and *q*<sub>rev</sub> = −*w*<sub>rev</sub>. During expansion, Δ*V* \> 0, so the gas performs work on its surroundings: *w*<sub>rev</sub> = −*P*Δ*V* \< 0. According to [Equation 18.16](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-eq02), this means that *q*<sub>rev</sub> must increase during expansion; that is, the gas must absorb heat from the surroundings during expansion, and the surroundings must give up that same amount of heat. The entropy change of the system is therefore Δ*S*<sub>sys</sub> = +*q*<sub>rev</sub>/*T*, and the entropy change of the surroundings is Δ*S*<sub>surr</sub> = −*q*<sub>rev</sub>/*T*. The corresponding change in entropy of the universe is then as follows:

Equation 18.17

$$\Delta S_{\text{univ}} = \Delta S_{\text{sys}} + \Delta S_{\text{surr}} = \frac{q_{\text{rev}}}{T} + \left( {- \frac{q_{\text{rev}}}{T}} \right) = 0$$

Thus no change in Δ*S*<sub>univ</sub> has occurred.

(src-averill-1-0-ch18-s03-s03-f01)=

Figure 18.10 Expansion of Gas at Constant Temperature

![Figure 18.10 Expansion of Gas at Constant Temperature](/images/section_22/1e65b4a8cafffa18456c357e1ca95974.jpg)

In the initial state (top), the temperatures of a gas and the surroundings are the same. During the reversible expansion of the gas, heat must be added to the gas to maintain a constant temperature. Thus the internal energy of the gas does not change, but work is performed on the surroundings. In the final state (bottom), the temperature of the surroundings is lower because the gas has absorbed heat from the surroundings during expansion.

Now consider the reversible melting of a sample of ice at 0°C and 1 atm. The enthalpy of fusion of ice is 6.01 kJ/mol, which means that 6.01 kJ of heat are absorbed reversibly from the surroundings when 1 mol of ice melts at 0°C, as illustrated in [Figure 18.11 \"Thermograms Showing That Heat Is Absorbed from the Surroundings When Ice Melts at 0°C\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-f02). The surroundings constitute a sample of low-density carbon foam that is thermally conductive, and the system is the ice cube that has been placed on it. The direction of heat flow along the resulting temperature gradient is indicated with an arrow. From [Equation 18.15](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-eq01), we see that the entropy of fusion of ice can be written as follows:

(src-averill-1-0-ch18-s03-s03-eq04)=

Equation 18.18

$$\Delta S_{\text{fus}} = \frac{q_{\text{rev}}}{T} = \frac{\Delta H_{\text{fus}}}{T}$$

(src-averill-1-0-ch18-s03-s03-f02)=

Figure 18.11 Thermograms Showing That Heat Is Absorbed from the Surroundings When Ice Melts at 0°C

![Figure 18.11 Thermograms Showing That Heat Is Absorbed from the Surroundings When Ice Melts at 0°C](/images/section_22/f23b4ca3c9202a6a98137966a0e9c520.jpg)

By convention, a thermogram shows cold regions in blue, warm regions in red, and thermally intermediate regions in green. When an ice cube (the system, dark blue) is placed on the corner of a square sample of low-density carbon foam with very high thermal conductivity, the temperature of the foam is lowered (going from red to green). As the ice melts, a temperature gradient appears, ranging from warm to very cold. An arrow indicates the direction of heat flow from the surroundings (red and green) to the ice cube. The amount of heat lost by the surroundings is the same as the amount gained by the ice, so the entropy of the universe does not change.

In this case, Δ*S*<sub>fus</sub> = (6.01 kJ/mol)/(273 K) = 22.0 J/(mol·K) = Δ*S*<sub>sys</sub>. The amount of heat lost by the surroundings is the same as the amount gained by the ice, so Δ*S*<sub>surr</sub> = *q*<sub>rev</sub>/*T* = −(6.01 kJ/mol)/(273 K) = −22.0 J/(mol·K). Once again, we see that the entropy of the universe does not change:

Δ*S*<sub>univ</sub> = Δ*S*<sub>sys</sub> + Δ*S*<sub>surr</sub> = 22.0 J/(mol·K) − 22.0 J/(mol·K) = 0

In these two examples of reversible processes, the entropy of the universe is unchanged. This is true of all reversible processes and constitutes part of the second law of thermodynamics[^chem-10]: *the entropy of the universe remains constant in a reversible process, whereas the entropy of the universe increases in an irreversible (spontaneous) process*.

````````````{important} Note the Pattern

The entropy of the universe increases during a spontaneous process.

````````````

As an example of an irreversible process, consider the entropy changes that accompany the spontaneous and irreversible transfer of heat from a hot object to a cold one, as occurs when lava spewed from a volcano flows into cold ocean water. The cold substance, the water, gains heat (*q* \> 0), so the change in the entropy of the water can be written as Δ*S*<sub>cold</sub> = *q*/*T*<sub>cold</sub>. Similarly, the hot substance, the lava, loses heat (*q* \< 0), so its entropy change can be written as Δ*S*<sub>hot</sub> = −*q*/*T*<sub>hot</sub>, where *T*<sub>cold</sub> and *T*<sub>hot</sub> are the temperatures of the cold and hot substances, respectively. The total entropy change of the universe accompanying this process is therefore

(src-averill-1-0-ch18-s03-s03-eq05)=

Equation 18.19

$$\Delta S_{\text{univ}} = \Delta S_{\text{cold}} + \Delta S_{\text{hot}} = \frac{q}{T_{\text{cold}}} + \left( {- \frac{q}{T_{\text{hot}}}} \right)$$

The numerators on the right side of [Equation 18.19](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-eq05) are the same in magnitude but opposite in sign. Whether Δ*S*<sub>univ</sub> is positive or negative depends on the relative magnitudes of the denominators. By definition, *T*<sub>hot</sub> \> *T*<sub>cold</sub>, so −*q*/*T*<sub>hot</sub> must be less than *q*/*T*<sub>cold</sub>, and Δ*S*<sub>univ</sub> must be positive. As predicted by the second law of thermodynamics, the entropy of the universe increases during this irreversible process. Any process for which Δ*S*<sub>univ</sub> is positive is, by definition, a spontaneous one that will occur as written. Conversely, any process for which Δ*S*<sub>univ</sub> approaches zero will not occur spontaneously as written but will occur spontaneously in the reverse direction. We see, therefore, that heat is spontaneously transferred from a hot substance, the lava, to a cold substance, the ocean water. In fact, if the lava is hot enough (e.g., if it is molten), so much heat can be transferred that the water is converted to steam ([Figure 18.12 \"Spontaneous Transfer of Heat from a Hot Substance to a Cold Substance\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-f03)).

(src-averill-1-0-ch18-s03-s03-f03)=

Figure 18.12 Spontaneous Transfer of Heat from a Hot Substance to a Cold Substance

![Figure 18.12 Spontaneous Transfer of Heat from a Hot Substance to a Cold Substance](/images/section_22/38a9391ec943f35f76c5118d7ffa13d4.jpg)

When molten lava flows into cold ocean water, so much heat is spontaneously transferred to the water that steam is produced.

### Example 6

Tin has two allotropes with different structures. Gray tin (α-tin) has a structure similar to that of diamond, whereas white tin (β-tin) is denser, with a unit cell structure that is based on a rectangular prism. At temperatures greater than 13.2°C, white tin is the more stable phase, but below that temperature, it slowly converts reversibly to the less dense, powdery gray phase. This phenomenon plagued Napoleon's army during his ill-fated invasion of Russia in 1812: the buttons on his soldiers' uniforms were made of tin and disintegrated during the Russian winter, adversely affecting the soldiers' health (and morale). The conversion of white tin to gray tin is exothermic, with Δ*H* = −2.1 kJ/mol at 13.2°C.

1.  What is Δ*S* for this process?
2.  Which is the more highly ordered form of tin---white or gray?

**Given:** Δ*H* and temperature

**Asked for:** Δ*S* and relative degree of order

**Strategy:**

Use [Equation 18.15](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-eq01) to calculate the change in entropy for the reversible phase transition. From the calculated value of Δ*S*, predict which allotrope has the more highly ordered structure.

**Solution:**

1.  We know from [Equation 18.15](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-eq01) that the entropy change for any reversible process is the heat transferred (in joules) divided by the temperature at which the process occurs. Because the conversion occurs at constant pressure, and Δ*H* and Δ*E* are essentially equal for reactions that involve only solids, we can calculate the change in entropy for the reversible phase transition where *q*<sub>rev</sub> = Δ*H*. Substituting the given values for Δ*H* and temperature in kelvins (in this case, *T* = 13.2°C = 286.4 K),

    $$\Delta S = \frac{q_{\text{rev}}}{T} = \frac{( - 2.1\ \cancel{\text{kJ}}\text{/mol})(1000\text{~J/}\cancel{\text{kJ}})}{286.4\text{~K}} = - 7.3\text{~J/}(\text{mol} \cdot \text{K})$$

2.  The fact that Δ*S* \< 0 means that entropy decreases when white tin is converted to gray tin. Thus gray tin must be the more highly ordered structure.

Exercise

Elemental sulfur exists in two forms: an orthorhombic form (S<sub>α</sub>), which is stable below 95.3°C, and a monoclinic form (S<sub>β</sub>), which is stable above 95.3°C. The conversion of orthorhombic sulfur to monoclinic sulfur is endothermic, with Δ*H* = 0.401 kJ/mol at 1 atm.

1.  What is Δ*S* for this process?
2.  Which is the more highly ordered form of sulfur---S<sub>α</sub> or S<sub>β</sub>?

**Answer:**

1.  1.09 J/(mol·K)
2.  S<sub>α</sub>

````````````{important} Summary

A measure of the disorder of a system is its **entropy (***S***)**, a state function whose value increases with an increase in the number of available microstates. A **reversible process** is one for which all intermediate states between extremes are equilibrium states; it can change direction at any time. In contrast, an **irreversible process** occurs in one direction only. The change in entropy of the system or the surroundings is the quantity of heat transferred divided by the temperature. The **second law of thermodynamics** states that in a reversible process, the entropy of the universe is constant, whereas in an irreversible process, such as the transfer of heat from a hot object to a cold object, the entropy of the universe increases.

````````````

````````````{important} Key Takeaways

- For a given system, the greater the number of microstates, the higher the entropy.
- During a spontaneous process, the entropy of the universe increases.

````````````

````````````{important} Key Equation

**Entropy change**

[Equation 18.15](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-eq01): $\Delta S = \frac{q_{\text{rev}}}{T}$

````````````

### Conceptual Problems

1.  A Russian space vehicle developed a leak, which resulted in an internal pressure drop from 1 atm to 0.85 atm. Is this an example of a reversible expansion? Has work been done?

2.  Which member of each pair do you expect to have a higher entropy? Why?

    1.  solid phenol or liquid phenol
    2.  1-butanol or butane
    3.  cyclohexane or cyclohexanol
    4.  1 mol of N<sub>2</sub> mixed with 2 mol of O<sub>2</sub> or 2 mol of NO<sub>2</sub>
    5.  1 mol of O<sub>2</sub> or 1 mol of O<sub>3</sub>
    6.  1 mol of propane at 1 atm or 1 mol of propane at 2 atm

3.  Determine whether each process is reversible or irreversible.

    1.  ice melting at 0°C
    2.  salt crystallizing from a saline solution
    3.  evaporation of a liquid in equilibrium with its vapor in a sealed flask
    4.  a neutralization reaction

4.  Determine whether each process is reversible or irreversible.

    1.  cooking spaghetti
    2.  the reaction between sodium metal and water
    3.  oxygen uptake by hemoglobin
    4.  evaporation of water at its boiling point

5.  Explain why increasing the temperature of a gas increases its entropy. What effect does this have on the internal energy of the gas?

6.  For a series of related compounds, does Δ*S*<sub>vap</sub> increase or decrease with an increase in the strength of intermolecular interactions in the liquid state? Why?

7.  Is the change in the enthalpy of reaction or the change in entropy of reaction more sensitive to changes in temperature? Explain your reasoning.

8.  Solid potassium chloride has a highly ordered lattice structure. Do you expect Δ*S*<sub>soln</sub> to be greater or less than zero? Why? What opposing factors must be considered in making your prediction?

9.  Aniline (C<sub>6</sub>H<sub>5</sub>NH<sub>2</sub>) is an oily liquid at 25°C that darkens on exposure to air and light. It is used in dying fabrics and in staining wood black. One gram of aniline dissolves in 28.6 mL of water, but aniline is completely miscible with ethanol. Do you expect Δ*S*<sub>soln</sub> in H<sub>2</sub>O to be greater than, less than, or equal to Δ*S*<sub>soln</sub> in CH<sub>3</sub>CH<sub>2</sub>OH? Why?

### Answers

1.  No, it is irreversible; no work is done because the external pressure is effectively zero.

2.  

3.  1.  reversible
    2.  irreversible
    3.  reversible
    4.  irreversible

4.  

5.  

6.  

7.  

8.  

9.  Water has a highly ordered, hydrogen-bonded structure that must reorganize to accommodate hydrophobic solutes like aniline. In contrast, we expect that aniline will be able to disperse randomly throughout ethanol, which has a significantly less ordered structure. We therefore predict that Δ*S*<sub>soln</sub> in ethanol will be more positive than Δ*S*<sub>soln</sub> in water.

### Numerical Problems

1.  Liquid nitrogen, which has a boiling point of −195.79°C, is used as a coolant and as a preservative for biological tissues. Is the entropy of nitrogen higher or lower at −200°C than at −190°C? Explain your answer. Liquid nitrogen freezes to a white solid at −210.00°C, with an enthalpy of fusion of 0.71 kJ/mol. What is its entropy of fusion? Is freezing biological tissue in liquid nitrogen an example of a reversible process or an irreversible process?

2.  Using the second law of thermodynamics, explain why heat flows from a hot body to a cold body but not from a cold body to a hot body.

3.  One test of the spontaneity of a reaction is whether the entropy of the universe increases: Δ*S*<sub>univ</sub> \> 0. Using an entropic argument, show that the following reaction is spontaneous at 25°C:

    4Fe(s) + 3O<sub>2</sub>(g) → 2Fe<sub>2</sub>O<sub>3</sub>(s)

    Why does the entropy of the universe increase in this reaction even though gaseous molecules, which have a high entropy, are consumed?

4.  Calculate the missing data in the following table.

    ````````{list-table}
    :header-rows: 1

    - - Compound
      - Δ*H*<sub>fus</sub> (kJ/mol)
      - Δ*S*<sub>fus</sub> \[J/(mol·K)\]
      - Melting Point (°C)
    - - acetic acid
      - 11.7
      -  
      - 16.6
    - - CH<sub>3</sub>CN
      - 8.2
      - 35.9
      -  
    - - CH<sub>4</sub>
      - 0.94
      -  
      - −182.5
    - - CH<sub>3</sub>OH
      -  
      - 18.2
      - −97.7
    - - formic acid
      - 12.7
      - 45.1
      -  

    ````````

    Based on this table, can you conclude that entropy is related to the nature of functional groups? Explain your reasoning.

5.  Calculate the missing data in the following table.

    ````````{list-table}
    :header-rows: 1

    - - Compound
      - Δ*H*<sub>vap</sub> (kJ/mol)
      - Δ*S*<sub>vap</sub> \[J/(mol·K)\]
      - Boiling Point (°C)
    - - hexanoic acid
      - 71.1
      -  
      - 105.7
    - - hexane
      - 28.9
      - 85.5
      -  
    - - formic acid
      -  
      - 60.7
      - 100.8
    - - 1-hexanol
      - 44.5
      -  
      - 157.5

    ````````

    The text states that the magnitude of Δ*S*<sub>vap</sub> tends to be similar for a wide variety of compounds. Based on the values in the table, do you agree?

(src-averill-1-0-ch18-s04)=

## 18.4 Entropy Changes and the Third Law of Thermodynamics

````````````{note} Learning Objective

1.  To use thermodynamic cycles to calculate changes in entropy.

````````````

The atoms, molecules, or ions that compose a chemical system can undergo several types of molecular motion, including translation, rotation, and vibration ([Figure 18.13 \"Molecular Motions\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-f01)). The greater the molecular motion of a system, the greater the number of possible microstates and the higher the entropy. A perfectly ordered system with only a single microstate available to it would have an entropy of zero. The only system that meets this criterion is a perfect crystal at a temperature of absolute zero (0 K), in which each component atom, molecule, or ion is fixed in place within a crystal lattice and exhibits no motion. Such a state of perfect order (or, conversely, zero disorder) corresponds to zero entropy. In practice, absolute zero is an ideal temperature that is unobtainable, and a perfect single crystal is also an ideal that cannot be achieved. Nonetheless, the combination of these two ideals constitutes the basis for the third law of thermodynamics[^chem-11]: *the entropy of any perfectly ordered, crystalline substance at absolute zero is zero*.

(src-averill-1-0-ch18-s04-f01)=

Figure 18.13 Molecular Motions

![Figure 18.13 Molecular Motions](/images/section_22/6042f2292e2c4c0f403b608bd294af3f.jpg)

Vibrational, rotational, and translational motions of a carbon dioxide molecule are illustrated here. Only a perfectly ordered, crystalline substance at absolute zero would exhibit no molecular motion and have zero entropy. In practice, this is an unattainable ideal.

The third law of thermodynamics has two important consequences: it defines the *sign* of the entropy of any substance at temperatures above absolute zero as positive, and it provides a fixed reference point that allows us to measure the *absolute entropy* of any substance at any temperature.[^chem-12] In contrast, other thermodynamic properties, such as internal energy and enthalpy, can be evaluated in only *relative* terms, not absolute terms. In this section, we examine two different ways to calculate Δ*S* for a reaction or a physical change. The first, based on the definition of absolute entropy provided by the third law of thermodynamics, uses tabulated values of absolute entropies of substances. The second, based on the fact that entropy is a state function, uses a thermodynamic cycle similar to those we first encountered in [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05).

### Calculating Δ*S* from Standard Molar Entropy Values

One way of calculating Δ*S* for a reaction is to use tabulated values of the standard molar entropy (*S*°)[^chem-13], which is the entropy of 1 mol of a substance at a standard temperature of 298 K; the units of *S*° are J/(mol·K). Unlike enthalpy or internal energy, it is possible to obtain absolute entropy values by measuring the entropy change that occurs between the reference point of 0 K \[corresponding to *S* = 0  J/(mol·K)\] and 298 K.

As shown in [Table 18.1 \"Standard Molar Entropy Values of Selected Substances at 25°C\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s01-t01), for substances with approximately the same molar mass and number of atoms, *S*° values fall in the order *S*°(gas) \> *S*°(liquid) \> *S*°(solid). For instance, *S*° for liquid water is 70.0 J/(mol·K), whereas *S*° for water vapor is 188.8 J/(mol·K). Likewise, *S*° is 260.7 J/(mol·K) for gaseous I<sub>2</sub> and 116.1 J/(mol·K) for solid I<sub>2</sub>. This order makes qualitative sense based on the kinds and extents of motion available to atoms and molecules in the three phases. The correlation between physical state and absolute entropy is illustrated in [Figure 18.14 \"A Generalized Plot of Entropy versus Temperature for a Single Substance\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s01-f01), which is a generalized plot of the entropy of a substance versus temperature.

(src-averill-1-0-ch18-s04-s01-t01)=

Table 18.1 Standard Molar Entropy Values of Selected Substances at 25°C

````````{list-table}
:header-rows: 1

- - Substance
  - *S*° \[J/(mol·K)\]
- - **Gases**
  -  
- - He
  - 126.2
- - H<sub>2</sub>
  - 130.7
- - Ne
  - 146.3
- - Ar
  - 154.8
- - Kr
  - 164.1
- - Xe
  - 169.7
- - H<sub>2</sub>O
  - 188.8
- - N<sub>2</sub>
  - 191.6
- - O<sub>2</sub>
  - 205.2
- - CO<sub>2</sub>
  - 213.8
- - I<sub>2</sub>
  - 260.7
- - **Liquids**
  -  
- - H<sub>2</sub>O
  - 70.0
- - CH<sub>3</sub>OH
  - 126.8
- - Br<sub>2</sub>
  - 152.2
- - CH<sub>3</sub>CH<sub>2</sub>OH
  - 160.7
- - C<sub>6</sub>H<sub>6</sub>
  - 173.4
- - CH<sub>3</sub>COCl
  - 200.8
- - C<sub>6</sub>H<sub>12</sub> (cyclohexane)
  - 204.4
- - C<sub>8</sub>H<sub>18</sub> (isooctane)
  - 329.3
- - **Solids**
  -  
- - C (diamond)
  - 2.4
- - C (graphite)
  - 5.7
- - LiF
  - 35.7
- - SiO<sub>2</sub> (quartz)
  - 41.5
- - Ca
  - 41.6
- - Na
  - 51.3
- - MgF<sub>2</sub>
  - 57.2
- - K
  - 64.7
- - NaCl
  - 72.1
- - KCl
  - 82.6
- - I<sub>2</sub>
  - 116.1

````````

(src-averill-1-0-ch18-s04-s01-f01)=

Figure 18.14 A Generalized Plot of Entropy versus Temperature for a Single Substance

![Figure 18.14 A Generalized Plot of Entropy versus Temperature for a Single Substance](/images/section_22/8bad6e4ce5fc3525a3b5538530398533.jpg)

Absolute entropy increases steadily with increasing temperature until the melting point is reached, where it jumps suddenly as the substance undergoes a phase change from a highly ordered solid to a disordered liquid (Δ*S*<sub>fus</sub>). The entropy again increases steadily with increasing temperature until the boiling point is reached, where it jumps suddenly as the liquid undergoes a phase change to a highly disordered gas (Δ*S*<sub>vap</sub>).

A closer examination of [Table 18.1 \"Standard Molar Entropy Values of Selected Substances at 25°C\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s01-t01) also reveals that substances with similar molecular structures tend to have similar *S*° values. Among crystalline materials, those with the lowest entropies tend to be rigid crystals composed of small atoms linked by strong, highly directional bonds, such as diamond \[*S*° = 2.4 J/(mol·K)\]. In contrast, graphite, the softer, less rigid allotrope of carbon, has a higher *S*° \[5.7 J/(mol·K)\] due to more disorder in the crystal. Soft crystalline substances and those with larger atoms tend to have higher entropies because of increased molecular motion and disorder. Similarly, the absolute entropy of a substance tends to increase with increasing molecular complexity because the number of available microstates increases with molecular complexity. For example, compare the *S*° values for CH<sub>3</sub>OH(l) and CH<sub>3</sub>CH<sub>2</sub>OH(l). Finally, substances with strong hydrogen bonds have lower values of *S*°, which reflects a more ordered structure.

To calculate Δ*S*° for a chemical reaction from standard molar entropies, we use the familiar "products minus reactants" rule, in which the absolute entropy of each reactant and product is multiplied by its stoichiometric coefficient in the balanced chemical equation. Example 7 illustrates this procedure for the combustion of the liquid hydrocarbon isooctane (C<sub>8</sub>H<sub>18</sub>; 2,2,4-trimethylpentane).

### Example 7

Use the data in [Table 18.1 \"Standard Molar Entropy Values of Selected Substances at 25°C\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s01-t01) to calculate Δ*S*° for the reaction of liquid isooctane with O<sub>2</sub>(g) to give CO<sub>2</sub>(g) and H<sub>2</sub>O(g) at 298 K.

**Given:** standard molar entropies, reactants, and products

**Asked for:** Δ*S*°

**Strategy:**

Write the balanced chemical equation for the reaction and identify the appropriate quantities in [Table 18.1 \"Standard Molar Entropy Values of Selected Substances at 25°C\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s01-t01). Subtract the sum of the absolute entropies of the reactants from the sum of the absolute entropies of the products, each multiplied by their appropriate stoichiometric coefficients, to obtain Δ*S*° for the reaction.

**Solution:**

The balanced chemical equation for the complete combustion of isooctane (C<sub>8</sub>H<sub>18</sub>) is as follows:

$$\left. \text{C}_{8}\text{H}_{18}\text{(l)} + \frac{25}{2}\text{O}_{2}\text{(g)}\rightarrow 8\text{CO}_{2}\text{(g)} + 9\text{H}_{2}\text{O(g)} \right.$$

We calculate Δ*S*° for the reaction using the "products minus reactants" rule, where *m* and *n* are the stoichiometric coefficients of each product and each reactant:

$$\begin{array}{rc}
{\Delta S{^\circ}_{\text{rxn}}} & {= \sum mS{^\circ}\text{(products)} - \sum nS{^\circ}\text{(reactants)}} \\
 & {= \lbrack 8S{^\circ}(\text{CO}_{2}) + 9S{^\circ}(\text{H}_{2}\text{O})\rbrack - \left\lbrack {S{^\circ}(\text{C}_{8}\text{H}_{18}) + \frac{25}{2}S{^\circ}(\text{O}_{2})} \right\rbrack} \\
 & {= \left\{ {\lbrack 8\ \cancel{\text{mol}}\text{~CO}_{2} \times 213.8\text{~J/}(\cancel{\text{mol}} \cdot \text{K})\rbrack + \lbrack 9\ \cancel{\text{mol}}\text{~H}_{2}\text{O} \times 188.8\text{~J/}(\cancel{\text{mol}} \cdot \text{K})\rbrack} \right\}} \\
 & {\quad - \left\{ {\lbrack 1\cancel{\text{mol}}\text{~C}_{8}\text{H}_{18} \times 329.3\text{~J/}(\cancel{\text{mol}} \cdot \text{K})\rbrack + \left\lbrack {\frac{25}{2}\cancel{\text{mol}}\text{~O}_{2} \times 205.2\text{~J/}(\cancel{\text{mol}} \cdot \text{K})} \right\rbrack} \right\}} \\
 & {= 515.3\text{~J/K}}
\end{array}$$

Δ*S*° is positive, as expected for a combustion reaction in which one large hydrocarbon molecule is converted to many molecules of gaseous products.

Exercise

Use the data in [Table 18.1 \"Standard Molar Entropy Values of Selected Substances at 25°C\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s01-t01) to calculate Δ*S*° for the reaction of H<sub>2</sub>(g) with liquid benzene (C<sub>6</sub>H<sub>6</sub>) to give cyclohexane (C<sub>6</sub>H<sub>12</sub>).

**Answer:** −361.1 J/K

````````````{important} Note the Pattern

Entropy increases with softer, less rigid solids, solids that contain larger atoms, and solids with complex molecular structures.

````````````

````````````{important} Note the Pattern

Δ*S*° for a reaction can be calculated from absolute entropy values using the same "products minus reactants" rule used to calculate Δ*H*°.

````````````

### Calculating Δ*S* from Thermodynamic Cycles

We can also calculate a change in entropy using a thermodynamic cycle. As you learned in [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05), the molar heat capacity (*C*<sub>p</sub>) is the amount of heat needed to raise the temperature of 1 mol of a substance by 1°C at constant pressure. Similarly, *C*<sub>v</sub> is the amount of heat needed to raise the temperature of 1 mol of a substance by 1°C at constant volume. The increase in entropy with increasing temperature in [Figure 18.14 \"A Generalized Plot of Entropy versus Temperature for a Single Substance\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s01-f01) is approximately proportional to the heat capacity of the substance.

Recall that the entropy change (Δ*S*) is related to heat flow (*q*<sub>rev</sub>) by Δ*S* = *q*<sub>rev</sub>/*T*. Because *q*<sub>rev</sub> = *nC*<sub>p</sub>Δ*T* at constant pressure or *nC*<sub>v</sub>Δ*T* at constant volume, where *n* is the number of moles of substance present, the change in entropy for a substance whose temperature changes from *T*<sub>1</sub> to *T*<sub>2</sub> is as follows:

$$\Delta S = \frac{q_{rev}}{T} = nC_{\text{p}}\frac{\Delta T}{T}\quad\left( \text{constant~pressure} \right)$$

As you will discover in more advanced math courses than is required here, it can be shown that this is equal to the following:[^chem-14]

(src-averill-1-0-ch18-s04-s02-eq01)=

Equation 18.20

$$\Delta S = nC_{\text{p}}\text{ln~}\frac{T_{2}}{T_{1}}\quad\left( \text{constant~pressure} \right)$$

Similarly,

(src-averill-1-0-ch18-s04-s02-eq02)=

Equation 18.21

$$\Delta S = nC_{\text{v}}\text{ln~}\frac{T_{2}}{T_{1}}\quad\left( \text{constant~volume} \right)$$

Thus we can use a combination of heat capacity measurements ([Equation 18.20](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s02-eq01) or [Equation 18.21](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s02-eq02)) and experimentally measured values of enthalpies of fusion or vaporization if a phase change is involved ([Equation 18.18](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-eq04)) to calculate the entropy change corresponding to a change in the temperature of a sample.

We can use a thermodynamic cycle to calculate the entropy change when the phase change for a substance such as sulfur cannot be measured directly. As noted in the exercise in Example 6, elemental sulfur exists in two forms (part (a) in [Figure 18.15 \"Two Forms of Elemental Sulfur and a Thermodynamic Cycle Showing the Transition from One to the Other\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s02-f01)): an orthorhombic form with a highly ordered structure (S<sub>α</sub>) and a less-ordered monoclinic form (S<sub>β</sub>). The orthorhombic (α) form is more stable at room temperature but undergoes a phase transition to the monoclinic (β) form at temperatures greater than 95.3°C (368.5 K). The transition from S<sub>α</sub> to S<sub>β</sub> can be described by the thermodynamic cycle shown in part (b) in [Figure 18.15 \"Two Forms of Elemental Sulfur and a Thermodynamic Cycle Showing the Transition from One to the Other\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s02-f01), in which liquid sulfur is an intermediate. The change in entropy that accompanies the conversion of liquid sulfur to S<sub>β</sub> (−Δ*S*<sub>fus(β)</sub> = Δ*S*<sub>3</sub> in the cycle) cannot be measured directly. Because entropy is a state function, however, Δ*S*<sub>3</sub> can be calculated from the overall entropy change (Δ*S*<sub>t</sub>) for the S<sub>α</sub>--S<sub>β</sub> transition, which equals the sum of the Δ*S* values for the steps in the thermodynamic cycle, using [Equation 18.20](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s02-eq01) and tabulated thermodynamic parameters (the heat capacities of S<sub>α</sub> and S<sub>β</sub>, Δ*H*<sub>fus(α)</sub>, and the melting point of S<sub>α</sub>.)

(src-averill-1-0-ch18-s04-s02-f01)=

Figure 18.15 Two Forms of Elemental Sulfur and a Thermodynamic Cycle Showing the Transition from One to the Other

![Figure 18.15 Two Forms of Elemental Sulfur and a Thermodynamic Cycle Showing the Transition from One to the Other](/images/section_22/13f703820796f96830ffbdb074383889.jpg)

\(a\) Orthorhombic sulfur (S<sub>α</sub>) has a highly ordered structure in which the S<sub>8</sub> rings are stacked in a "crankshaft" arrangement. Monoclinic sulfur (S<sub>β</sub>) is also composed of S<sub>8</sub> rings but has a less-ordered structure. (b) At 368.5 K, S<sub>α</sub> undergoes a phase transition to S<sub>β</sub>. Although Δ*S*<sub>3</sub> cannot be measured directly, it can be calculated using the values shown in this thermodynamic cycle.

If we know the melting point of S<sub>α</sub> (*T*<sub>m</sub> = 115.2°C = 388.4 K) and Δ*S*<sub>t</sub> for the overall phase transition \[calculated to be 1.09 J/(mol·K) in the exercise in Example 6\], we can calculate Δ*S*<sub>3</sub> from the values given in part (b) in [Figure 18.15 \"Two Forms of Elemental Sulfur and a Thermodynamic Cycle Showing the Transition from One to the Other\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s02-f01) where *C*<sub>p(α)</sub> = 22.70 J/mol·K and *C*<sub>p(β)</sub> = 24.77 J/mol·K (subscripts on Δ*S* refer to steps in the cycle):

$$\begin{aligned}
{\Delta S_{\text{t}}} & {= \Delta S_{1} + \Delta S_{2} + \Delta S_{3} + \Delta S_{4}} \\
{1.09\text{~J/}(\text{mol} \cdot \text{K})} & {= C_{\text{p}(\alpha)}\ln\left( \frac{T_{2}}{T_{1}} \right) + \frac{\Delta H_{\text{fus}}}{T_{\text{m}}} + \Delta S_{3} + C_{p(\beta)}\ln\left( \frac{T_{4}}{T_{3}} \right)} \\
 & {= 22.70\text{~J/}(\text{mol} \cdot \text{K})\ln\left( \frac{388.4}{368.5} \right) + \left( {\frac{1.722\ \cancel{\text{kJ}}\text{/mol}}{388.4\text{~K}} \times 1000\text{~J/}\cancel{\text{kJ}}} \right) + \Delta S_{3} + 24.77\text{~J/}(\text{mol} \cdot \text{K})\ln\left( \frac{368.5}{388.4} \right)} \\
 & {= \lbrack 1.194\text{~J/}(\text{mol} \cdot \text{K})\rbrack + \lbrack 4.434\text{~J/}(\text{mol} \cdot \text{K})\rbrack + \Delta S_{3} + \lbrack - 1.303\text{~J/}(\text{mol} \cdot \text{K})\rbrack}
\end{aligned}$$

Solving for Δ*S*<sub>3</sub> gives a value of −3.24 J/(mol·K). As expected for the conversion of a less ordered state (a liquid) to a more ordered one (a crystal), Δ*S*<sub>3</sub> is negative.

````````````{important} Summary

The **third law of thermodynamics** states that the entropy of any perfectly ordered, crystalline substance at absolute zero is zero. At temperatures greater than absolute zero, entropy has a positive value, which allows us to measure the *absolute entropy* of a substance. Measurements of the heat capacity of a substance and the enthalpies of fusion or vaporization can be used to calculate the changes in entropy that accompany a physical change. The entropy of 1 mol of a substance at a standard temperature of 298 K is its **standard molar entropy (***S***°)**. We can use the "products minus reactants" rule to calculate the standard entropy change (Δ*S*°) for a reaction using tabulated values of *S*° for the reactants and the products.

````````````

````````````{important} Key Takeaway

- Entropy changes can be calculated using the "products minus reactants" rule or from a combination of heat capacity measurements and measured values of enthalpies of fusion or vaporization.

````````````

````````````{important} Key Equations

**Temperature dependence of entropy at constant pressure**

[Equation 18.20](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s02-eq01): $\Delta S = nC_{\text{p}}\text{ln~}\frac{T_{2}}{T_{1}}$

**Temperature dependence of entropy at constant volume**

[Equation 18.21](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s02-eq02): $\Delta S = nC_{\text{v}}\text{ln~}\frac{T_{2}}{T_{1}}$

````````````

### Conceptual Problems

1.  Crystalline MgCl<sub>2</sub> has *S*° = 89.63 J/(mol·K), whereas aqueous MgCl<sub>2</sub> has *S*° = −25.1 J/(mol·K). Is this consistent with the third law of thermodynamics? Explain your answer.

2.  Why is it possible to measure absolute entropies but not absolute enthalpies?

3.  How many microstates are available to a system at absolute zero? How many are available to a substance in its liquid state?

4.  Substance A has a higher heat capacity than substance B. Do you expect the absolute entropy of substance A to be less than, similar to, or greater than that of substance B? Why? As the two substances are heated, for which substance do you predict the entropy to increase more rapidly?

5.  Phase transitions must be considered when calculating entropy changes. Why?

### Numerical Problems

1.  What is the final temperature of water when 5.20 g of ice at 0.0°C are added to 250 mL of water in an insulated thermos at 30.0°C? The value of Δ*H*<sub>fus</sub> for water is 6.01 kJ/mol, and the heat capacity of liquid water is 75.3 J/(mol·°C). What is the entropy change for this process?

2.  Calculate the change in both enthalpy and entropy when a 3.0 g block of ice melts at 0.0°C \[Δ*H*<sub>fus</sub>(H<sub>2</sub>O) = 6.01 kJ/mol\]. For the same block of ice, calculate the entropy change for the system when the ice is warmed from 0.0°C to 25°C. The heat capacity of liquid water over this temperature range is 75.3 J/(mol·°C).

3.  Use the data in [Table 18.1 \"Standard Molar Entropy Values of Selected Substances at 25°C\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s01-t01) and [Chapter 25 \"Appendix A: Standard Thermodynamic Quantities for Chemical Substances at 25°C\"](/appendices/appendix-a-standard-thermodyna.md#src-averill-1-0-ch96appa) to calculate Δ*S*° for each reaction.

    1.  $\left. \text{H}_{2}\text{(g)} + \frac{1}{2}\text{O}_{2}\text{(g)}\rightarrow\text{H}_{2}\text{O(l)} \right.$
    2.  CH<sub>3</sub>OH(l) + HCl(g) → CH<sub>3</sub>Cl(g) + H<sub>2</sub>O(l)
    3.  H<sub>2</sub>(g) + Br<sub>2</sub>(l) → 2HBr(g)
    4.  Zn(s) + 2HCl(aq) → ZnCl<sub>2</sub>(s) + H<sub>2</sub>(g)

4.  Calculate the entropy change (J/K) when 4.35 g of liquid bromine are heated from 30.0°C to 50.0°C if the molar heat capacity (*C*<sub>p</sub>) of liquid bromine is 75.1 kJ/(mol·K).

5.  Calculate the molar heat capacity (*C*<sub>p</sub>) of titanium tetrachloride if the change in entropy when a 6.00 g sample of TiCl<sub>4</sub>(l) is heated from 25.0°C to 40.0°C is 0.154 J/K.

6.  When a 1.00 g sample of lead is heated from 298.2 K to just below its melting temperature of 600.5 K, the change in entropy is 0.0891 J/K. Determine the molar heat capacity (*C*<sub>p</sub>) of lead over this temperature range.

7.  Phosphorus oxychloride (POCl<sub>3</sub>) is a chlorinating agent that is frequently used in organic chemistry to replace oxygen with chlorine. Given Δ*S*<sub>vap</sub> = 93.08 J/(mol·K) and Δ*H*<sub>vap</sub> = 35.2 kJ/mol, does POCl<sub>3</sub> spontaneously convert from a liquid to a gas at 110°C? Does it spontaneously crystallize at 0.0°C if Δ*H*<sub>fus</sub> = 34.3 kJ/mol and Δ*S*<sub>fus</sub> = 125 J/(mol·K)? Using the information provided, what is the melting point of POCl<sub>3</sub>?

8.  A useful reagent for the fluorination of alcohols, carboxylic acids, and carbonyl compounds is selenium tetrafluoride (SeF<sub>4</sub>). One must be careful when using this compound, however, because it is known to attack glass (such as the glass of a reaction vessel).

    1.  Is SeF<sub>4</sub> a liquid or a gas at 100°C given that Δ*H*<sub>vap</sub> = 46.9 kJ/mol and Δ*S*<sub>vap</sub> = 124 J/(mol·K)?
    2.  Determine the boiling point of SeF<sub>4</sub>.
    3.  Would you use SeF<sub>4</sub> for a solution reaction at 0°C if Δ*H*<sub>fus</sub> = 46 kJ/mol and Δ*S*<sub>fus</sub> = 178 J/(mol·K)?

### Answers

1.  27.8°C; 0.85 J.

2.  

3.  1.  −163.3 J/K
    2.  −9.1 J/K
    3.  114.5 J/K
    4.  −173.2 J/K

4.  

5.  25.0 J/(mol·K)

6.  

7.  yes; yes; 274 K

8.  

(src-averill-1-0-ch18-s05)=

## 18.5 Free Energy

````````````{note} Learning Objective

1.  To understand the relationship between Gibbs free energy and work.

````````````

One of the major goals of chemical thermodynamics is to establish criteria for predicting whether a particular reaction or process will occur spontaneously. We have developed one such criterion, the change in entropy of the universe: if Δ*S*<sub>univ</sub> \> 0 for a process or a reaction, then the process will occur spontaneously as written. Conversely, if Δ*S*<sub>univ</sub> \< 0, a process cannot occur spontaneously; if Δ*S*<sub>univ</sub> = 0, the system is at equilibrium. The sign of Δ*S*<sub>univ</sub> is a universally applicable and infallible indicator of the spontaneity of a reaction. Unfortunately, using Δ*S*<sub>univ</sub> requires that we calculate Δ*S* for *both* a system *and* its surroundings. This is not particularly useful for two reasons: we are normally much more interested in the system than in the surroundings, and it is difficult to make quantitative measurements of the surroundings (i.e., the rest of the universe). A criterion of spontaneity that is based solely on the state functions of a *system* would be much more convenient and is provided by a new state function: the Gibbs free energy.

### Gibbs Free Energy and the Direction of Spontaneous Reactions

The Gibbs free energy (*G*)[^chem-15], often called simply *free energy*, was named in honor of J. Willard Gibbs (1838--1903), an American physicist who first developed the concept. It is defined in terms of three other state functions with which you are already familiar: enthalpy, temperature, and entropy:

Equation 18.22

*G* = *H* − *TS*

Because it is a combination of state functions, *G* is also a state function.

````````````{important} J. Willard Gibbs (1839–1903)

Born in Connecticut, Josiah Willard Gibbs attended Yale, as did his father, a professor of sacred literature at Yale, who was involved in the *Amistad* trial. In 1863, Gibbs was awarded the first engineering doctorate granted in the United States. He was appointed professor of mathematical physics at Yale in 1871, the first such professorship in the United States. His series of papers entitled "On the Equilibrium of Heterogeneous Substances" was the foundation of the field of physical chemistry and is considered one of the great achievements of the 19th century. Gibbs, whose work was translated into French by Le Châtelier, lived with his sister and brother-in-law until his death in 1903, shortly before the inauguration of the Nobel Prizes.

````````````

The criterion for predicting spontaneity is based on Δ*G*, the change in *G*, at constant temperature and pressure. Although very few chemical reactions actually occur under conditions of constant temperature and pressure, most systems can be brought back to the initial temperature and pressure without significantly affecting the value of thermodynamic state functions such as *G*. At constant temperature and pressure,

(src-averill-1-0-ch18-s05-s01-eq02)=

Equation 18.23

Δ*G* = Δ*H* − *T*Δ*S*

where all thermodynamic quantities are those of the *system*. Recall that at constant pressure, Δ*H* = *q*, whether a process is reversible or irreversible, and *T*Δ*S* = *q*<sub>rev</sub>. Using these expressions, we can reduce [Equation 18.23](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s01-eq02) to Δ*G* = *q* − *q*<sub>rev</sub>. Thus Δ*G* is the difference between the heat released during a process (via a reversible or an irreversible path) and the heat released for the same process occurring in a reversible manner. Under the special condition in which a process occurs reversibly, *q* = *q*<sub>rev</sub> and Δ*G* = 0. As we shall soon see, if Δ*G* is zero, the system is at equilibrium, and there will be no net change.

What about processes for which Δ*G* ≠ 0? To understand how the sign of Δ*G* for a *system* determines the direction in which change is spontaneous, we can rewrite [Equation 18.15](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-eq01) (where *q*<sub>p</sub> = Δ*H*, [Equation 18.11](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s02-s01-eq04)) as follows:

Equation 18.24

$$\Delta S_{\text{surr}} = - \frac{\Delta H_{\text{sys}}}{T}$$

Thus the entropy change of the *surroundings* is related to the enthalpy change of the *system*. We have stated that for a spontaneous reaction, Δ*S*<sub>univ</sub> \> 0, so substituting we obtain

$$\begin{aligned}
{\Delta S_{\text{univ}}} & {= \Delta S_{\text{sys}} + \Delta S_{\text{surr}} > 0} \\
 & {= \Delta S_{\text{sys}} - \frac{\Delta H_{\text{sys}}}{T} > 0}
\end{aligned}$$

Multiplying both sides of the inequality by −*T* reverses the sign of the inequality; rearranging,

$$\Delta H_{\text{sys}} - T\Delta S_{\text{sys}} < 0$$

which is equal to Δ*G* ([Equation 18.23](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s01-eq02)). We can therefore see that for a spontaneous process, Δ*G* \< 0.

The relationship between the entropy change of the *surroundings* and the heat gained or lost by the *system* provides the key connection between the thermodynamic properties of the system and the change in entropy of the universe. The relationship shown in [Equation 18.23](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s01-eq02) allows us to predict spontaneity by focusing exclusively on the thermodynamic properties and temperature of the system. We predict that highly exothermic processes (Δ*H* \<\< 0) that increase the disorder of a *system* (Δ*S*<sub>sys</sub> \>\> 0) would therefore occur spontaneously. An example of such a process is the decomposition of ammonium nitrate fertilizer. (This substance destroyed Texas City, Texas, in 1947; see [Chapter 3 \"Chemical Reactions\"](/chapters/ch-03-chemical-reactions.md#src-averill-1-0-ch03), [Section 3.3.1 \"Interpreting Chemical Equations\"](/chapters/ch-03-chemical-reactions.md#src-averill-1-0-ch03-s03-s01).) Ammonium nitrate was also used to destroy the Murrah Federal Building in Oklahoma City, Oklahoma, in 1995. For a system at constant temperature and pressure, we can summarize the following results:

- If Δ*G* \< 0, the process occurs spontaneously.
- If Δ*G* = 0, the system is at equilibrium.
- If Δ*G* \> 0, the process is not spontaneous as written but occurs spontaneously in the reverse direction.

To further understand how the various components of Δ*G* dictate whether a process occurs spontaneously, we now look at a simple and familiar physical change: the conversion of liquid water to water vapor. If this process is carried out at 1 atm and the normal boiling point of 100.00°C (373.15 K), we can calculate Δ*G* from the experimentally measured value of Δ*H*<sub>vap</sub> (40.657 kJ/mol). For vaporizing 1 mol of water, Δ*H* = 40,657 J, so the process is highly endothermic. From the definition of Δ*S* ([Equation 18.15](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s03-s03-eq01)), we know that for 1 mol of water,

$$\Delta S_{\text{vap}} = \frac{\Delta H_{\text{vap}}}{T_{\text{b}}} = \frac{40,657\text{~J}}{373.15\text{~K}} = 108.96\text{~J/K}$$

Hence there is an increase in the disorder of the system. At the normal boiling point of water,

$$\Delta G_{\text{100°C}} = \Delta H_{\text{100°C}} - T\Delta S_{\text{100°C}} = 40,657\text{~J} - \lbrack(373.15\ \cancel{\text{K}})(108.96\text{~J/}\cancel{\text{K}})\rbrack = \text{0~J}$$

The energy required for vaporization offsets the increase in disorder of the system. Thus Δ*G* = 0, and the liquid and vapor are in equilibrium, as is true of any liquid at its boiling point under standard conditions. (For more information on standard conditions, see [Chapter 11 \"Liquids\"](/chapters/ch-11-liquids.md#src-averill-1-0-ch11).)

Now suppose we were to superheat 1 mol of liquid water to 110°C. The value of Δ*G* for the vaporization of 1 mol of water at 110°C, assuming that Δ*H* and Δ*S* do not change significantly with temperature, becomes

$$\Delta G_{\text{110°C}} = \Delta H - T\Delta S = 40,657\text{~J} - \lbrack(383.15\ \cancel{\text{K}})(108.96\text{~J/}\cancel{\text{K}})\rbrack = - 1\text{091~J}$$

At 110°C, Δ*G* \< 0, and vaporization is predicted to occur spontaneously and irreversibly.

We can also calculate Δ*G* for the vaporization of 1 mol of water at a temperature below its normal boiling point---for example, 90°C---making the same assumptions:

$$\Delta G_{\text{90°C}} = \Delta H - T\Delta S = 40,657\text{~J} - \lbrack(363.15\ \cancel{\text{K}})(108.96\text{~J/}\cancel{\text{K}})\rbrack = 1\text{088~J}$$

At 90°C, Δ*G* \> 0, and water does not spontaneously convert to water vapor. When using all the digits in the calculator display in carrying out our calculations, Δ*G*<sub>110°C</sub> = 1090 J = −Δ*G*<sub>90°C</sub>, as we would predict. (For more information on using a calculator, see Essential Skills 1 in [Chapter 1 \"Introduction to Chemistry\"](/chapters/ch-01-introduction-to-chemistry.md#src-averill-1-0-ch01).)

````````````{important} Note the Pattern

Δ*G* = 0 only if Δ*H* = *T*Δ*S*.

````````````

We can also calculate the temperature at which liquid water is in equilibrium with water vapor. Inserting the values of Δ*H* and Δ*S* into the definition of Δ*G* ([Equation 18.23](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s01-eq02)), setting Δ*G* = 0, and solving for *T*,

$$\begin{aligned}
{0\text{~J}} & {= 40,657\text{~J} - T(108.96\text{~J/K})} \\
T & {= 373.15\text{~K}}
\end{aligned}$$

Thus Δ*G* = 0 at *T* = 373.15 K and 1 atm, which indicates that liquid water and water vapor are in equilibrium; this temperature is called the *normal boiling point* of water. At temperatures greater than 373.15 K, Δ*G* is negative, and water evaporates spontaneously and irreversibly. Below 373.15 K, Δ*G* is positive, and water does not evaporate spontaneously. Instead, water vapor at a temperature less than 373.15 K and 1 atm will spontaneously and irreversibly condense to liquid water. [Figure 18.16 \"Temperature Dependence of Δ\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s01-f01) shows how the Δ*H* and *T*Δ*S* terms vary with temperature for the vaporization of water. When the two lines cross, Δ*G* = 0, and Δ*H* = *T*Δ*S*.

(src-averill-1-0-ch18-s05-s01-f01)=

Figure 18.16 Temperature Dependence of Δ*H* and *T*Δ*S* for the Vaporization of Water

![Figure 18.16 Temperature Dependence of Δ H and T Δ S for the Vaporization of Water](/images/section_22/fe1815006be0d86076e42639ab129b81.jpg)

Both Δ*H* and *T*Δ*S* are temperature dependent, but the lines have opposite slopes and cross at 373.15 K at 1 atm, where Δ*H* = *T*Δ*S*. Because Δ*G* = Δ*H* − *T*Δ*S*, at this temperature Δ*G* = 0, indicating that the liquid and vapor phases are in equilibrium. The normal boiling point of water is therefore 373.15 K. Above the normal boiling point, the *T*Δ*S* term is greater than Δ*H*, making Δ*G* \< 0; hence, liquid water evaporates spontaneously. Below the normal boiling point, the Δ*H* term is greater than *T*Δ*S*, making Δ*G* \> 0. Thus liquid water does not evaporate spontaneously, but water vapor spontaneously condenses to liquid.

A similar situation arises in the conversion of liquid egg white to a solid when an egg is boiled. The major component of egg white is a protein called albumin, which is held in a compact, ordered structure by a large number of hydrogen bonds. Breaking them requires an input of energy (Δ*H* \> 0), which converts the albumin to a highly disordered structure in which the molecules aggregate as a disorganized solid (Δ*S* \> 0). At temperatures greater than 373 K, the *T*Δ*S* term dominates, and Δ*G* \< 0, so the conversion of a raw egg to a hard-boiled egg is an irreversible and spontaneous process above 373 K.

### The Relationship between Δ*G* and Work

In the previous subsection, we learned that the value of Δ*G* allows us to predict the spontaneity of a physical or a chemical change. In addition, the magnitude of Δ*G* for a process provides other important information. The change in free energy (Δ*G*) is equal to the maximum amount of work that a system can perform on the surroundings while undergoing a spontaneous change (at constant temperature and pressure): Δ*G* = *w*<sub>max</sub>. To see why this is true, let's look again at the relationships among free energy, enthalpy, and entropy expressed in [Equation 18.23](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s01-eq02). We can rearrange this equation as follows:

Equation 18.25

Δ*H* = Δ*G* + *T*Δ*S*

This equation tells us that when energy is released during an exothermic process (Δ*H* \< 0), such as during the combustion of a fuel, some of that energy can be used to do work (Δ*G* \< 0), while some is used to increase the entropy of the universe (*T*Δ*S* \> 0). Only if the process occurs infinitely slowly in a perfectly reversible manner will the entropy of the universe be unchanged. (For more information on entropy and reversibility, see [Section 18.4 \"Entropy Changes and the Third Law of Thermodynamics\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04).) Because no real system is perfectly reversible, the entropy of the universe increases during all processes that produce energy. As a result, no process that uses stored energy can ever be 100% efficient; that is, Δ*H* will never equal Δ*G* because Δ*S* has a positive value.

One of the major challenges facing engineers is to maximize the efficiency of converting stored energy to useful work or converting one form of energy to another. As indicated in [Table 18.2 \"Approximate Thermodynamic Efficiencies of Various Devices\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s02-t01), the efficiencies of various energy-converting devices vary widely. For example, an internal combustion engine typically uses only 25%--30% of the energy stored in the hydrocarbon fuel to perform work; the rest of the stored energy is released in an unusable form as heat. In contrast, gas--electric hybrid engines, now used in several models of automobiles, deliver approximately 50% greater fuel efficiency. A large electrical generator is highly efficient (approximately 99%) in converting mechanical to electrical energy, but a typical incandescent light bulb is one of the least efficient devices known (only approximately 5% of the electrical energy is converted to light). In contrast, a mammalian liver cell is a relatively efficient machine and can use fuels such as glucose with an efficiency of 30%--50%.

(src-averill-1-0-ch18-s05-s02-t01)=

Table 18.2 Approximate Thermodynamic Efficiencies of Various Devices

````````{list-table}
:header-rows: 1

- - Device
  - Energy Conversion
  - Approximate Efficiency (%)
- - large electrical generator
  - mechanical → electrical
  - 99
- - chemical battery
  - chemical → electrical
  - 90
- - home furnace
  - chemical → heat
  - 65
- - small electric tool
  - electrical → mechanical
  - 60
- - space shuttle engine
  - chemical → mechanical
  - 50
- - mammalian liver cell
  - chemical → chemical
  - 30--50
- - spinach cell
  - light → chemical
  - 30
- - internal combustion engine
  - chemical → mechanical
  - 25--30
- - fluorescent light
  - electrical → light
  - 20
- - solar cell
  - light → electricity
  - 10
- - incandescent light bulb
  - electricity → light
  - 5
- - yeast cell
  - chemical → chemical
  - 2--4

````````

### Standard Free-Energy Change

We have seen that there is no way to measure absolute enthalpies, although we can measure *changes* in enthalpy (Δ*H*) during a chemical reaction. Because enthalpy is one of the components of Gibbs free energy, we are consequently unable to measure absolute free energies; we can measure only changes in free energy. The standard free-energy change (Δ*G*°)[^chem-16] is the change in free energy when one substance or a set of substances in their standard states is converted to one or more other substances, also in their standard states. The standard free-energy change can be calculated from the definition of free energy, if the standard enthalpy and entropy changes are known, using [Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01):

(src-averill-1-0-ch18-s05-s03-eq01)=

Equation 18.26

Δ*G*° = Δ*H*° − *T*Δ*S*°

If Δ*S*° and Δ*H*° for a reaction have the same sign, then the sign of Δ*G*° depends on the relative magnitudes of the Δ*H*° and *T*Δ*S*° terms. It is important to recognize that a positive value of Δ*G*° for a reaction does *not* mean that no products will form if the reactants in their standard states are mixed; it means only that at equilibrium the concentrations of the products will be less than the concentrations of the reactants.

````````````{important} Note the Pattern

A positive Δ*G*° means that the equilibrium constant is less than 1.

````````````

### Example 8

Calculate the standard free-energy change (Δ*G*°) at 25°C for the reaction $\left. \text{H}_{2}\text{(g)} + \text{O}_{2}\text{(g)}\rightleftharpoons\text{H}_{2}\text{O}_{2}\text{(l)}\text{.} \right.$ At 25°C, the standard enthalpy change (Δ*H*°) is −187.78 kJ/mol, and the absolute entropies of the products and reactants are *S*°(H<sub>2</sub>O<sub>2</sub>) = 109.6 J/(mol·K), *S*°(O<sub>2</sub>) = 205.2 J/(mol·K), and *S*°(H<sub>2</sub>) = 130.7 J/(mol·K). Is the reaction spontaneous as written?

**Given:** balanced chemical equation, Δ*H*° and *S*° for reactants and products

**Asked for:** spontaneity of reaction as written

**Strategy:**

**A** Calculate Δ*S*° from the absolute molar entropy values given.

**B** Use [Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01), the calculated value of Δ*S*°, and other data given to calculate Δ*G*° for the reaction. Use the value of Δ*G*° to determine whether the reaction is spontaneous as written.

**Solution:**

**A** To calculate Δ*G*° for the reaction, we need to know Δ*H*°, Δ*S*°, and *T*. We are given Δ*H*°, and we know that *T* = 298.15 K. We can calculate Δ*S*° from the absolute molar entropy values provided using the "products minus reactants" rule:

$$\begin{array}{rc}
{\Delta S{^\circ}} & {= S{^\circ}(\text{H}_{2}\text{O}_{2}) - \left\lbrack {S{^\circ}(\text{O}_{2}) + S{^\circ}(\text{H}_{2})} \right\rbrack} \\
 & {= \lbrack 1\ \cancel{\text{mol}}\text{~H}_{2}\text{O}_{2} \times 109.6\text{~J/}(\cancel{\text{mol}} \cdot \text{K})\rbrack} \\
 & {\quad - \left\{ {\lbrack 1\cancel{\text{mol}}\text{~H}_{2} \times 130.7\text{~J/}(\cancel{\text{mol}} \cdot \text{K})\rbrack + \lbrack 1\cancel{\text{mol}}\text{~O}_{2} \times 205.2\text{~J/}(\cancel{\text{mol}} \cdot \text{K})\rbrack} \right\}} \\
 & {= - 226.3\text{~J/K~}(\text{per~mole~of~H}_{2}\text{O}_{2})}
\end{array}$$

As we might expect for a reaction in which 2 mol of gas is converted to 1 mol of a much more ordered liquid, Δ*S*° is very negative for this reaction.

**B** Substituting the appropriate quantities into [Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01),

$$\begin{aligned}
{\Delta G{^\circ} = \Delta H{^\circ} - T\Delta S{^\circ}} & {= - 187.78\text{~kJ/mol} - (298.15\ \cancel{\text{K}})\lbrack - 226.3\ \cancel{\text{J}}\text{/}(\text{mol~} \cdot \cancel{\text{K}}) \times 1\text{~kJ/1000}\cancel{\text{~J}}\rbrack} \\
 & {= - 187.78\text{~kJ/mol} + 67.47\text{~kJ/mol} = - 120.31\text{~kJ/mol}}
\end{aligned}$$

The negative value of Δ*G*° indicates that the reaction is spontaneous as written. Because Δ*S*° and Δ*H*° for this reaction have the same sign, the sign of Δ*G*° depends on the relative magnitudes of the Δ*H*° and *T*Δ*S*° terms. In this particular case, the enthalpy term dominates, indicating that the strength of the bonds formed in the product more than compensates for the unfavorable Δ*S*° term and for the energy needed to break bonds in the reactants.

Exercise

Calculate the standard free-energy change (Δ*G*°) at 25°C for the reaction $\left. 2\text{H}_{2}\text{(g)} + \text{N}_{2}\text{(g)}\rightleftharpoons\text{N}_{2}\text{H}_{4}\text{(l)}\text{.} \right.$ At 25°C, the standard enthalpy change (Δ*H*°) is 50.6 kJ/mol, and the absolute entropies of the products and reactants are *S*°(N<sub>2</sub>H<sub>4</sub>) = 121.2 J/(mol·K), *S*°(N<sub>2</sub>) = 191.6 J/(mol·K), and *S*°(H<sub>2</sub>) = 130.7 J/(mol·K). Is the reaction spontaneous as written?

**Answer:** 149.5 kJ/mol; no

Tabulated values of standard free energies of formation allow chemists to calculate the values of Δ*G*° for a wide variety of chemical reactions rather than having to measure them in the laboratory. The standard free energy of formation $\left( {\Delta G_{\text{f}}^{{^\circ}}} \right)$[^chem-17] of a compound is the change in free energy that occurs when 1 mol of a substance in its standard state is formed from the component elements in their standard states. By definition, the standard free energy of formation of an element in its standard state is zero at 298.15 K. One mole of Cl<sub>2</sub> gas at 298.15 K, for example, has $\Delta G_{\text{f}}^{{^\circ}}$ = 0. The standard free energy of formation of a compound can be calculated from the standard enthalpy of formation $\left( {\Delta H_{\text{f}}^{{^\circ}}} \right)$ and the standard entropy of formation $\left( {\Delta S_{\text{f}}^{{^\circ}}} \right)$ using the definition of free energy:

Equation 18.27

$\Delta G_{\text{f}}^{{^\circ}} = \Delta H_{\text{f}}^{{^\circ}} - T\Delta S_{\text{f}}^{{^\circ}}$

Using standard free energies of formation to calculate the standard free energy of a reaction is analogous to calculating standard enthalpy changes from standard enthalpies of formation using the familiar "products minus reactants" rule:

Equation 18.28

$\Delta G_{\text{rxn}}^{{^\circ}} = \sum m\Delta G_{\text{f}}^{{^\circ}}\text{~(products)} - \sum n\Delta G_{\text{f}}^{{^\circ}}\text{~(reactants)}$

where *m* and *n* are the stoichiometric coefficients of each product and reactant in the balanced chemical equation. A very large negative Δ*G*° indicates a strong tendency for products to form spontaneously from reactants; *it does not, however, necessarily indicate that the reaction will occur rapidly*. To make this determination, we need to evaluate the kinetics of the reaction. (For more information on chemical kinetics, see [Chapter 14 \"Chemical Kinetics\"](/chapters/ch-14-chemical-kinetics.md#src-averill-1-0-ch14).)

````````````{important} Note the Pattern

The Δ*G*° of a reaction can be calculated from tabulated $\Delta G_{\text{f}}^{{^\circ}}$ values using the "products minus reactants" rule.

````````````

### Example 9

Calculate Δ*G*° for the reaction of isooctane with oxygen gas to give carbon dioxide and water (described in Example 7). Use the following data:

$\Delta G_{\text{f}}^{{^\circ}}$(isooctane) = −353.2 kJ/mol,

$\Delta G_{\text{f}}^{{^\circ}}$(CO<sub>2</sub>) = −394.4 kJ/mol, and

$\Delta G_{\text{f}}^{{^\circ}}$(H<sub>2</sub>O) = −237.1 kJ/mol. Is the reaction spontaneous as written?

**Given:** balanced chemical equation and values of $\Delta G_{\text{f}}^{{^\circ}}$ for isooctane, CO<sub>2</sub>, and H<sub>2</sub>O

**Asked for:** spontaneity of reaction as written

**Strategy:**

Use the "products minus reactants" rule to obtain $\Delta G_{\text{rxn}}^{{^\circ}}$, remembering that $\Delta G_{\text{f}}^{{^\circ}}$ for an element in its standard state is zero. From the calculated value, determine whether the reaction is spontaneous as written.

**Solution:**

From Example 7, we know that the balanced chemical equation for the reaction is as follows: $\left. \text{C}_{8}\text{H}_{18}\text{(l)} + \frac{25}{2}\text{O}_{2}\text{(g)}\rightarrow 8\text{CO}_{2}\text{(g)} + 9\text{H}_{2}\text{O(l)}\text{.} \right.$ We are given $\Delta G_{\text{f}}^{{^\circ}}$ values for all the products and reactants except O<sub>2</sub>(g). Because oxygen gas is an element in its standard state, $\Delta G_{\text{f}}^{{^\circ}}$ (O<sub>2</sub>) is zero. Using the "products minus reactants" rule,

$$\begin{array}{rc}
{\Delta G{^\circ}} & {= \left\lbrack {8\Delta G_{\text{f}}^{{^\circ}}(\text{CO}_{2}) + 9\Delta G_{\text{f}}^{{^\circ}}(\text{H}_{2}\text{O})} \right\rbrack - \left\lbrack {1\Delta G_{\text{f}}^{{^\circ}}(\text{C}_{8}\text{H}_{18}) + \frac{25}{2}\Delta G_{\text{f}}^{{^\circ}}(\text{O}_{2})} \right\rbrack} \\
 & {= \lbrack(8\ \cancel{\text{mol}})( - 394.4\text{~kJ/}\cancel{\text{mol}}) + (9\ \cancel{\text{mol}})( - 237.1\text{~kJ/}\cancel{\text{mol}})\rbrack} \\
 & {\quad - \left\lbrack {(1\ \cancel{\text{mol}})( - 353.2\text{~kJ/}\cancel{\text{mol}}) + \left( {\frac{25}{2}\cancel{\text{mol}}} \right)(0\text{~kJ/}\cancel{\text{mol}})} \right\rbrack} \\
 & {= - 4935.9\text{~kJ~}(\text{per~mol~of~C}_{8}\text{H}_{18})}
\end{array}$$

Because Δ*G*° is a large negative number, there is a strong tendency for the spontaneous formation of products from reactants (though not necessarily at a rapid rate). Also notice that the magnitude of Δ*G*° is largely determined by the $\Delta G_{\text{f}}^{{^\circ}}$ of the stable products: water and carbon dioxide.

Exercise

Calculate Δ*G*° for the reaction of benzene with hydrogen gas to give cyclohexane using the data

$\Delta G_{\text{f}}^{{^\circ}}$ (benzene) = 124.5 kJ/mol and

$\Delta G_{\text{f}}^{{^\circ}}$ (cyclohexane) = 217.3 kJ/mol. Is the reaction spontaneous as written?

**Answer:** 92.8 kJ; no

Calculated values of Δ*G*° are extremely useful in predicting whether a reaction will occur spontaneously if the reactants and products are mixed under standard conditions. We should note, however, that very few reactions are actually carried out under standard conditions, and calculated values of Δ*G*° may not tell us whether a given reaction will occur spontaneously under nonstandard conditions. What determines whether a reaction will occur spontaneously is the free-energy change (Δ*G*) under the actual experimental conditions, which are usually different from Δ*G*°. If the Δ*H* and *T*Δ*S* terms for a reaction have the same sign, for example, then it may be possible to reverse the sign of Δ*G* by changing the temperature, thereby converting a reaction that is not thermodynamically spontaneous, having *K*<sub>eq</sub> \< 1, to one that is, having a *K*<sub>eq</sub> \> 1, or vice versa. Because Δ*H* and Δ*S* usually do not vary greatly with temperature in the absence of a phase change, we can use tabulated values of Δ*H*° and Δ*S*° to calculate Δ*G*° at various temperatures, as long as no phase change occurs over the temperature range being considered.

````````````{important} Note the Pattern

In the absence of a phase change, neither Δ*H* nor Δ*S* vary greatly with temperature.

````````````

### Example 10

Calculate (a) Δ*G*° and (b) Δ*G*<sub>300°C</sub> for the reaction $\left. \text{N}_{2}\text{(g)} + 3\text{H}_{2}\text{(g)}\rightleftharpoons 2\text{NH}_{3}\text{(g),} \right.$ assuming that Δ*H* and Δ*S* do not change between 25°C and 300°C. Use these data:

*S*°(N<sub>2</sub>) = 191.6 J/(mol·K),

*S*°(H<sub>2</sub>) = 130.7 J/(mol·K),

*S*°(NH<sub>3</sub>) = 192.8 J/(mol·K), and

$\Delta H_{\text{f}}^{{^\circ}}$ (NH<sub>3</sub>) = −45.9 kJ/mol.

**Given:** balanced chemical equation, temperatures, *S*° values, and $\Delta H_{\text{f}}^{{^\circ}}$ for NH<sub>3</sub>

**Asked for:** Δ*G*° and Δ*G* at 300°C

**Strategy:**

**A** Convert each temperature to kelvins. Then calculate Δ*S*° for the reaction. Calculate Δ*H*° for the reaction, recalling that $\Delta H_{\text{f}}^{{^\circ}}$ for any element in its standard state is zero.

**B** Substitute the appropriate values into [Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01) to obtain Δ*G*° for the reaction.

**C** Assuming that Δ*H* and Δ*S* are independent of temperature, substitute values into [Equation 18.23](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s01-eq02) to obtain Δ*G* for the reaction at 300°C.

**Solution:**

1.  **A** To calculate Δ*G*° for the reaction using [Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01), we must know the temperature as well as the values of Δ*S*° and Δ*H*°. At standard conditions, the temperature is 25°C, or 298 K. We can calculate Δ*S*° for the reaction from the absolute molar entropy values given for the reactants and the products using the "products minus reactants" rule:

    $$\begin{array}{rc}
    {\Delta S_{\text{rxn}}^{{^\circ}}} & {= 2S{^\circ}(\text{NH}_{3}) - \lbrack S{^\circ}(\text{N}_{2}) + 3S{^\circ}(\text{H}_{2})\rbrack} \\
     & {= \lbrack 2\cancel{\text{mol}}\text{~NH}_{3} \times 192.8\text{~J/}(\cancel{\text{mol}} \cdot \text{K})\rbrack} \\
     & {\quad - \left\{ {\lbrack 1\cancel{\text{mol}}\text{~N}_{2} \times 191.6\text{~J/}(\cancel{\text{mol}} \cdot \text{K})\rbrack + \lbrack 3\cancel{\text{mol}}\text{~H}_{2} \times 130.7\text{~J/}(\cancel{\text{mol}} \cdot \text{K})\rbrack} \right\}} \\
     & {= - 198.1\text{~J/K~}(\text{per~mole~of~}Ν_{2})}
    \end{array}$$

    We can also calculate Δ*H*° for the reaction using the "products minus reactants" rule. The value of $\Delta H_{\text{f}}^{{^\circ}}$ (NH<sub>3</sub>) is given, and $\Delta H_{\text{f}}^{{^\circ}}$ is zero for both N<sub>2</sub> and H<sub>2</sub>:

    $$\begin{aligned}
    {\Delta H_{\text{rxn}}^{{^\circ}}} & {= 2\Delta H_{\text{f}}^{{^\circ}}(\text{NH}_{3}) - \lbrack\Delta H_{\text{f}}^{{^\circ}}(\text{N}_{2}) + 3\Delta H_{\text{f}}^{{^\circ}}(\text{H}_{2})\rbrack} \\
     & {= \lbrack 2 \times ( - 45.9\text{~kJ/mol)}\rbrack - \lbrack(1 \times 0\text{~kJ/mol}) + (3 \times 0\text{~kJ/mol})\rbrack} \\
     & {= - 91.8\text{~kJ}(\text{per~mole~of}\text{N}_{2})}
    \end{aligned}$$

    **B** Inserting the appropriate values into [Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01),

    $$\Delta G_{\text{rxn}}^{{^\circ}} = \Delta H{^\circ} - T\Delta S{^\circ} = ( - 91.8\text{~kJ}) - (298\ \cancel{\text{K}})( - 198.1\ \cancel{\text{J}}\text{/}\cancel{\text{K}})(1\text{~kJ/1000}\cancel{\text{~J}}) = - 32.7\text{~kJ~}(\text{per~mole~of~N}_{2})$$

2.  **C** To calculate Δ*G* for this reaction at 300°C, we assume that Δ*H* and Δ*S* are independent of temperature (i.e., Δ*H*<sub>300°C</sub> = *H*° and ΔS<sub>300°C</sub> = Δ*S*°) and insert the appropriate temperature (573 K) into [Equation 18.23](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s01-eq02):

    $$\begin{aligned}
    {\Delta G_{300{^\circ}\text{C}}} & {= \Delta H_{300{^\circ}\text{C}} - (573\text{~K})(\Delta S_{300{^\circ}\text{C}}) = \Delta H{^\circ} - (573\text{~K})\Delta S{^\circ}} \\
     & {= ( - 91.8\text{~kJ}) - (573\ \cancel{\text{K}})( - 198.1~\cancel{\text{J}}\text{/}\cancel{\text{K}})(1\text{~kJ/1000}\cancel{\text{~J}}) = 21.7\text{~kJ~}(\text{per~mole~of~N}_{2})}
    \end{aligned}$$

    In this example, changing the temperature has a major effect on the thermodynamic spontaneity of the reaction. Under standard conditions, the reaction of nitrogen and hydrogen gas to produce ammonia is thermodynamically spontaneous, but in practice, it is too slow to be useful industrially. Increasing the temperature in an attempt to make this reaction occur more rapidly also changes the thermodynamics by causing the −*T*Δ*S*° term to dominate, and the reaction is no longer spontaneous at high temperatures; that is, its *K*<sub>eq</sub> is less than one. This is a classic example of the conflict encountered in real systems between thermodynamics and kinetics, which is often unavoidable.

Exercise

Calculate (a) Δ*G*° and (b) Δ*G*<sub>750°C</sub> for the reaction $\left. 2\text{NO(g)} + \text{O}_{2}\text{(g)}\rightleftharpoons 2\text{NO}_{2}\text{(g),} \right.$ which is important in the formation of urban smog. Assume that Δ*H* and Δ*S* do not change between 25.0°C and 750°C and use these data:

*S*°(NO) = 210.8 J/(mol·K),

*S*°(O<sub>2</sub>) = 205.2 J/(mol·K),

*S*°(NO<sub>2</sub>) = 240.1 J/(mol·K),

$\Delta H_{\text{f}}^{{^\circ}}$(NO<sub>2</sub>) = 33.2 kJ/mol, and

$\Delta H_{\text{f}}^{{^\circ}}$ (NO) = 91.3 kJ/mol.

**Answer**

1.  −72.5 kJ/mol of O<sub>2</sub>
2.  33.8 kJ/mol of O<sub>2</sub>

The effect of temperature on the spontaneity of a reaction, which is an important factor in the design of an experiment or an industrial process, depends on the sign and magnitude of both Δ*H*° and Δ*S*°. The temperature at which a given reaction is at equilibrium can be calculated by setting Δ*G*° = 0 in [Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01), as illustrated in Example 11.

### Example 11

As you saw in Example 10, the reaction of nitrogen and hydrogen gas to produce ammonia is one in which Δ*H*° and Δ*S*° are both negative. Such reactions are predicted to be thermodynamically spontaneous at low temperatures but nonspontaneous at high temperatures. Use the data in Example 10 to calculate the temperature at which this reaction changes from spontaneous to nonspontaneous, assuming that Δ*H*° and Δ*S*° are independent of temperature.

**Given:** Δ*H*° and Δ*S*°

**Asked for:** temperature at which reaction changes from spontaneous to nonspontaneous

**Strategy:**

Set Δ*G*° equal to zero in [Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01) and solve for *T*, the temperature at which the reaction becomes nonspontaneous.

**Solution:**

In Example 10, we calculated that Δ*H*° is −91.8 kJ/mol of N<sub>2</sub> and Δ*S*° is −198.1 J/K per mole of N<sub>2</sub>, corresponding to Δ*G*° = −32.7 kJ/mol of N<sub>2</sub> at 25°C. Thus the reaction is indeed spontaneous at low temperatures, as expected based on the signs of Δ*H*° and Δ*S*°. The temperature at which the reaction becomes nonspontaneous is found by setting Δ*G*° equal to zero and rearranging [Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01) to solve for *T*:

$$\begin{aligned}
{\Delta G{^\circ}} & {= \Delta H{^\circ} - T\Delta S{^\circ} = 0} \\
{\Delta H{^\circ}} & {= T\Delta S{^\circ}} \\
{T = \frac{\Delta H{^\circ}}{\Delta S{^\circ}}} & {= \frac{( - 91.8\ \cancel{\text{kJ}})(1000\ \cancel{\text{J}}\text{/}\cancel{\text{kJ}})}{- 198.1\ \cancel{\text{J}}\text{/K}} = 463\text{~K}}
\end{aligned}$$

This is a case in which a chemical engineer is severely limited by thermodynamics. Any attempt to increase the rate of reaction of nitrogen with hydrogen by increasing the temperature will cause reactants to be favored over products above 463 K.

Exercise

As you found in the exercise in Example 10, Δ*H*° and Δ*S*° are both negative for the reaction of nitric oxide and oxygen to form nitrogen dioxide. Use those data to calculate the temperature at which this reaction changes from spontaneous to nonspontaneous.

**Answer:** 792.6 K

````````````{important} Summary

We can predict whether a reaction will occur spontaneously by combining the entropy, enthalpy, and temperature of a system in a new state function called **Gibbs free energy (***G***)**. The change in free energy (Δ*G*) is the difference between the heat released during a process and the heat released for the same process occurring in a reversible manner. If a system is at equilibrium, Δ*G* = 0. If the process is spontaneous, Δ*G* \< 0. If the process is not spontaneous as written but is spontaneous in the reverse direction, Δ*G* \> 0. At constant temperature and pressure, Δ*G* is equal to the maximum amount of work a system can perform on its surroundings while undergoing a spontaneous change. The **standard free-energy change (Δ***G***°)** is the change in free energy when one substance or a set of substances in their standard states is converted to one or more other substances, also in their standard states. The **standard free energy of formation (**$\Delta G_{\text{f}}^{{^\circ}}$), is the change in free energy that occurs when 1 mol of a substance in its standard state is formed from the component elements in their standard states. Tabulated values of standard free energies of formation are used to calculate Δ*G*° for a reaction.

````````````

````````````{important} Key Takeaway

- The change in Gibbs free energy, which is based solely on changes in state functions, is the criterion for predicting the spontaneity of a reaction.

````````````

````````````{important} Key Equations

**Free-energy change**

[Equation 18.23](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s01-eq02): Δ*G* = Δ*H* − *T*Δ*S*

**Standard free-energy change**

[Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01): Δ*G*° = Δ*H*° − *T*Δ*S*°

````````````

### Conceptual Problems

1.  How does each example illustrate the fact that no process is 100% efficient?

    1.  burning a log to stay warm
    2.  the respiration of glucose to provide energy
    3.  burning a candle to provide light

2.  Neither the change in enthalpy nor the change in entropy is, by itself, sufficient to determine whether a reaction will occur spontaneously. Why?

3.  If a system is at equilibrium, what must be the relationship between Δ*H* and Δ*S*?

4.  The equilibrium $\left. 2\text{AB}\rightleftharpoons\text{A}_{2}\text{B}_{2} \right.$ is exothermic in the forward direction. Which has the higher entropy---the products or the reactants? Why? Which is favored at high temperatures?

5.  Is Δ*G* a state function that describes a system or its surroundings? Do its components---Δ*H* and Δ*S*---describe a system or its surroundings?

6.  How can you use Δ*G* to determine the temperature of a phase transition, such as the boiling point of a liquid or the melting point of a solid?

7.  Occasionally, an inventor claims to have invented a "perpetual motion" machine, which requires no additional input of energy once the machine has been put into motion. Using your knowledge of thermodynamics, how would you respond to such a claim? Justify your arguments.

8.  Must the entropy of the universe increase in a spontaneous process? If not, why is no process 100% efficient?

9.  The reaction of methyl chloride with water produces methanol and hydrogen chloride gas at room temperature, despite the fact that $\Delta H_{\text{rxn}}^{{^\circ}}$ = 7.3 kcal/mol. Using thermodynamic arguments, propose an explanation as to why methanol forms.

### Answer

1.  

2.  

3.  

4.  

5.  

6.  

7.  

8.  

9.  In order for the reaction to occur spontaneously, Δ*G* for the reaction must be less than zero. In this case, Δ*S* must be positive, and the *T*Δ*S* term outweighs the positive value of Δ*H.*

### Numerical Problems

1.  Use the tables in the text to determine whether each reaction is spontaneous under standard conditions. If a reaction is not spontaneous, write the corresponding spontaneous reaction.

    1.  $\left. \text{H}_{2}\text{(g)} + \frac{1}{2}\text{O}_{2}\text{(g)}\rightarrow\text{H}_{2}\text{O(l)} \right.$
    2.  2H<sub>2</sub>(g) + C<sub>2</sub>H<sub>2</sub>(g) → C<sub>2</sub>H<sub>6</sub>(g)
    3.  (CH<sub>3</sub>)<sub>2</sub>O(g) + H<sub>2</sub>O(g) → 2CH<sub>3</sub>OH(l)
    4.  CH<sub>4</sub>(g) + H<sub>2</sub>O(g) → CO(g) + 3H<sub>2</sub>(g)

2.  Use the tables in the text to determine whether each reaction is spontaneous under standard conditions. If a reaction is not spontaneous, write the corresponding spontaneous reaction.

    1.  K<sub>2</sub>O<sub>2</sub>(s) → 2K(s) + O<sub>2</sub>(g)
    2.  PbCO<sub>3</sub>(s) → PbO(s) + CO<sub>2</sub>(g)
    3.  P<sub>4</sub>(s) + 6H<sub>2</sub>(g) → 4PH<sub>3</sub>(g)
    4.  2AgCl(s) + H<sub>2</sub>S(g) → Ag<sub>2</sub>S(s) + 2HCl(g)

3.  Nitrogen fixation is the process by which nitrogen in the atmosphere is reduced to NH<sub>3</sub> for use by organisms. Several reactions are associated with this process; three are listed in the following table. Which of these are spontaneous at 25°C? If a reaction is not spontaneous, at what temperature does it become spontaneous?

    ````````{list-table}
    :header-rows: 1

    - - Reaction
      - $\Delta H_{\text{298}}^{{^\circ}}$ (kcal/mol)
      - $\Delta S_{\text{298}}^{{^\circ}}$ \[cal/(°·mol)\]
    - - \(a\) $\left. \frac{1}{2}\text{N}_{2} + \text{O}_{2}\rightarrow\text{NO}_{2} \right.$
      - 8.0
      - −14.4
    - - \(b\) $\left. \frac{1}{2}\text{N}_{2} + \frac{1}{2}\text{O}_{2}\rightarrow\text{NO} \right.$
      - 21.6
      - 2.9
    - - \(c\) $\left. \frac{1}{2}\text{N}_{2} + \frac{3}{2}\text{H}_{2}\rightarrow\text{NH}_{3} \right.$
      - −11.0
      - −23.7

    ````````

4.  A student was asked to propose three reactions for the oxidation of carbon or a carbon compound to CO or CO<sub>2</sub>. The reactions are listed in the following table. Are any of these reactions spontaneous at 25°C? If a reaction does not occur spontaneously at 25°C, at what temperature does it become spontaneous?

    ````````{list-table}
    :header-rows: 1

    - - Reaction
      - $\Delta H_{\text{298}}^{{^\circ}}$ (kcal/mol)
      - $\Delta S_{\text{298}}^{{^\circ}}$ \[cal/(°·mol)\]
    - - C(s) + H<sub>2</sub>O(g) → CO(g) + H<sub>2</sub>(g)
      - 42
      - 32
    - - CO(g) + H<sub>2</sub>O(g) → CO<sub>2</sub>(g) + H<sub>2</sub>(g)
      - −9.8
      - −10.1
    - - CH<sub>4</sub>(g) + H<sub>2</sub>O(g) → CO(g) + 3H<sub>2</sub>(g)
      - 49.3
      - 51.3

    ````````

5.  Tungsten trioxide (WO<sub>3</sub>) is a dense yellow powder that, because of its bright color, is used as a pigment in oil paints and water colors (although cadmium yellow is more commonly used in artists' paints). Tungsten metal can be isolated by the reaction of WO<sub>3</sub> with H<sub>2</sub> at 1100°C according to the equation WO<sub>3</sub>(s) + 3H<sub>2</sub>(g) → W(s) + 3H<sub>2</sub>O(g). What is the lowest temperature at which the reaction occurs spontaneously? Δ*H*° = 27.4 kJ/mol and Δ*S*° = 29.8 J/K.

6.  Sulfur trioxide (SO<sub>3</sub>) is produced in large quantities in the industrial synthesis of sulfuric acid. Sulfur dioxide is converted to sulfur trioxide by reaction with oxygen gas.

    1.  Write a balanced chemical equation for the reaction of SO<sub>2</sub> with O<sub>2</sub>(g) and determine its Δ*G*°.
    2.  What is the value of the equilibrium constant at 600°C?
    3.  If you had to rely on the equilibrium concentrations alone, would you obtain a higher yield of product at 400°C or at 600°C?

7.  Calculate Δ*G*° for the general reaction MCO<sub>3</sub>(s) → MO(s) + CO<sub>2</sub>(g) at 25°C, where M is Mg or Ba. At what temperature does each of these reactions become spontaneous?

    ````````{list-table}
    :header-rows: 1

    - - Compound
      - $\Delta H_{\text{f}}^{{^\circ}}$ (kJ/mol)
      - *S*° \[J/(mol·K)\]
    - - **MCO** <sub>**3**</sub>
      -  
      -  
    - - Mg
      - −1111
      - 65.85
    - - Ba
      - −1213.0
      - 112.1
    - - **MO**
      -  
      -  
    - - Mg
      - −601.6
      - 27.0
    - - Ba
      - −548.0
      - 72.1
    - - **CO** <sub>**2**</sub>
      - −393.5
      - 213.8

    ````````

8.  The reaction of aqueous solutions of barium nitrate with sodium iodide is described by the following equation:

    Ba(NO<sub>3</sub>)<sub>2</sub>(aq) + 2NaI(aq) → BaI<sub>2</sub>(aq) + 2NaNO<sub>3</sub>(aq)

    You want to determine the absolute entropy of BaI<sub>2</sub>, but that information is not listed in your tables. However, you have been able to obtain the following information:

    ````````{list-table}
    :header-rows: 1

    - -  
      - Ba(NO<sub>3</sub>)<sub>2</sub>
      - NaI
      - BaI<sub>2</sub>
      - NaNO<sub>3</sub>
    - - $\Delta H_{\text{f}}^{{^\circ}}$ (kJ/mol)
      - −952.36
      - −295.31
      - −605.4
      - −447.5
    - - *S*° \[J/(mol·K)\]
      - 302.5
      - 170.3
      -  
      - 205.4

    ````````

    You know that Δ*G*° for the reaction at 25°C is 22.64 kJ/mol. What is Δ*H*° for this reaction? What is *S*° for BaI<sub>2</sub>?

### Answers

1.  1.  −237.1 kJ/mol; spontaneous as written
    2.  −241.9 kJ/mol; spontaneous as written
    3.  8.0 kJ/mol; spontaneous in reverse direction.
    4.  141.9 kJ/mol; spontaneous in reverse direction.

2.  

3.  1.  Not spontaneous at any *T*
    2.  Not spontaneous at 25°C; spontaneous above 7400 K
    3.  Spontaneous at 25°C

4.  

5.  919 K

6.  

7.  MgCO<sub>3</sub>: Δ*G*° = 63 kJ/mol, spontaneous above 663 K; BaCO<sub>3</sub>: Δ*G*° = 220 kJ/mol, spontaneous above 1562 K

8.  

## 18.6 Spontaneity and Equilibrium

````````````{note} Learning Objective

1.  To know the relationship between free energy and the equilibrium constant.

````````````

We have identified three criteria for whether a given reaction will occur spontaneously: Δ*S*<sub>univ</sub> \> 0, Δ*G*<sub>sys</sub> \< 0, and the relative magnitude of the reaction quotient *Q* versus the equilibrium constant *K*. (For more information on the reaction quotient and the equilibrium constant, see [Chapter 15 \"Chemical Equilibrium\"](/chapters/ch-15-chemical-equilibrium.md#src-averill-1-0-ch15).) Recall that if *Q* \< *K*, then the reaction proceeds spontaneously to the right as written, resulting in the net conversion of reactants to products. Conversely, if *Q* \> *K*, then the reaction proceeds spontaneously to the left as written, resulting in the net conversion of products to reactants. If *Q* = *K*, then the system is at equilibrium, and no net reaction occurs. [Table 18.3 \"Criteria for the Spontaneity of a Process as Written\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-t01) summarizes these criteria and their relative values for spontaneous, nonspontaneous, and equilibrium processes. Because all three criteria are assessing the same thing---the spontaneity of the process---it would be most surprising indeed if they were not related. The relationship between Δ*S*<sub>univ</sub> and Δ*G*<sub>sys</sub> was described in [Section 18.5 \"Free Energy\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05). In this section, we explore the relationship between the standard free energy of reaction (Δ*G*°) and the equilibrium constant (*K*).

(src-averill-1-0-ch18-s06-t01)=

Table 18.3 Criteria for the Spontaneity of a Process as Written

````````{list-table}
:header-rows: 1

- - Spontaneous
  - Equilibrium
  - Nonspontaneous\*
- - Δ*S*<sub>univ</sub> \> 0
  - Δ*S*<sub>univ</sub> = 0
  - Δ*S*<sub>univ</sub> \< 0
- - Δ*G*<sub>sys</sub> \< 0
  - Δ*G*<sub>sys</sub> = 0
  - Δ*G*<sub>sys</sub> \> 0
- - *Q* \< *K*
  - *Q* = *K*
  - *Q* \> *K*
- - \*Spontaneous in the *reverse* direction.
  - \*Spontaneous in the *reverse* direction.
  - \*Spontaneous in the *reverse* direction.

````````

### Free Energy and the Equilibrium Constant

Because Δ*H*° and Δ*S*° determine the magnitude of Δ*G*° ([Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01)), and because *K* is a measure of the ratio of the concentrations of products to the concentrations of reactants, we should be able to express *K* in terms of Δ*G*° and vice versa. As you learned in [Section 18.5 \"Free Energy\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05), Δ*G* is equal to the maximum amount of work a system can perform on its surroundings while undergoing a spontaneous change. For a reversible process that does not involve external work, we can express the change in free energy in terms of volume, pressure, entropy, and temperature, thereby eliminating Δ*H* from the equation for Δ*G*. Using higher math, the general relationship can be shown as follows:

(src-averill-1-0-ch18-s06-s01-eq01)=

Equation 18.29

Δ*G* = *V*Δ*P* − *S*Δ*T*

If a reaction is carried out at constant temperature (Δ*T* = 0), then [Equation 18.29](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq01) simplifies to

(src-averill-1-0-ch18-s06-s01-eq02)=

Equation 18.30

Δ*G* = *V*Δ*P*

Under normal conditions, the pressure dependence of free energy is not important for solids and liquids because of their small molar volumes. For reactions that involve gases, however, the effect of pressure on free energy is very important.

Assuming ideal gas behavior, we can replace the *V* in [Equation 18.30](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq02) by *nRT*/*P* (where *n* is the number of moles of gas and *R* is the ideal gas constant) and express Δ*G* in terms of the initial and final pressures (*P*<sub>i</sub> and *P*<sub>f</sub>, respectively) as in [Equation 18.20](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s02-eq01):

Equation 18.31

$$\Delta G = \left( \frac{nRT}{P} \right)\Delta P = nRT\frac{\Delta P}{P} = nRT\ln\left( \frac{P_{\text{f}}}{P_{\text{i}}} \right)$$

If the initial state is the standard state with *P*<sub>i</sub> = 1 atm, then the change in free energy of a substance when going from the standard state to any other state with a pressure *P* can be written as follows:

*G* − *G*° = *nRT*ln *P*

This can be rearranged as follows:

(src-averill-1-0-ch18-s06-s01-eq04)=

Equation 18.32

*G* = *G*° + *nRT*ln *P*

As you will soon discover, [Equation 18.32](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq04) allows us to relate Δ*G*° and *K*<sub>p</sub>. Any relationship that is true for *K*<sub>p</sub> must also be true for *K* because *K*<sub>p</sub> and *K* are simply different ways of expressing the equilibrium constant using different units.

Let's consider the following hypothetical reaction, in which all the reactants and the products are ideal gases and the lowercase letters correspond to the stoichiometric coefficients for the various species:

Equation 18.33

$$\left. a\text{A} + bB\rightleftharpoons c\text{C} + d\text{D} \right.$$

Because the free-energy change for a reaction is the difference between the sum of the free energies of the products and the reactants, we can write the following expression for Δ*G*:

(src-averill-1-0-ch18-s06-s01-eq06)=

Equation 18.34

$$\Delta G = \sum mG_{\text{products}} - \sum nG_{\text{reactants}} = (cG_{\text{C}} + dG_{\text{D}}) - (aG_{\text{A}} + bG_{\text{B}})$$

Substituting [Equation 18.32](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq04) for each term into [Equation 18.34](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq06),

$$\Delta G = \lbrack(cG{^\circ}_{\text{C}} + cRT\text{ln~}P_{\text{C}}) + (dG{^\circ}_{\text{D}} + dRT\text{ln~}P_{\text{D}})\rbrack - \lbrack(aG{^\circ}_{\text{A}} + aRT\text{ln~}P_{\text{A}}) + (bG{^\circ}_{\text{B}} + bRT\text{ln~}P_{\text{B}})\rbrack$$

Combining terms gives the following relationship between Δ*G* and the reaction quotient *Q*:

(src-averill-1-0-ch18-s06-s01-eq07)=

Equation 18.35

$$\Delta G = \Delta G{^\circ} + RT\ln\left( \frac{P_{\text{C}}^{c}P_{\text{D}}^{d}}{P_{\text{A}}^{a}P_{\text{B}}^{b}} \right) = \Delta G{^\circ} + RT\text{ln~}Q$$

where Δ*G*° indicates that all reactants and products are in their standard states. In [Chapter 15 \"Chemical Equilibrium\"](/chapters/ch-15-chemical-equilibrium.md#src-averill-1-0-ch15), you learned that for gases *Q* = *K*<sub>p</sub> at equilibrium, and as you've learned in this chapter, Δ*G* = 0 for a system at equilibrium. Therefore, we can describe the relationship between Δ*G*° and *K*<sub>p</sub> for gases as follows:

(src-averill-1-0-ch18-s06-s01-eq08)=

Equation 18.36

$$\begin{aligned}
0 & {= \Delta G{^\circ} + RT\text{ln~}K_{\text{p}}} \\
{\Delta G{^\circ}} & {= - RT\text{ln~}K_{\text{p}}}
\end{aligned}$$

If the products and reactants are in their standard states and Δ*G*° \< 0, then *K*<sub>p</sub> \> 1, and products are favored over reactants. Conversely, if Δ*G*° \> 0, then *K*<sub>p</sub> \< 1, and reactants are favored over products. If Δ*G*° = 0, then *K*<sub>p</sub> = 1, and neither reactants nor products are favored: the system is at equilibrium.

````````````{important} Note the Pattern

For a spontaneous process under standard conditions, *K*<sub>eq</sub> and *K*<sub>p</sub> are greater than 1.

````````````

### Example 12

In Example 10, we calculated that Δ*G*° = −32.7 kJ/mol of N<sub>2</sub> for the reaction $\left. \text{N}_{2}\text{(g)} + 3\text{H}_{2}\text{(g)}\rightleftharpoons 2\text{NH}_{3}\text{(g)}\text{.} \right.$ This calculation was for the reaction under standard conditions---that is, with all gases present at a partial pressure of 1 atm and a temperature of 25°C. Calculate Δ*G* for the same reaction under the following nonstandard conditions: $P_{\text{N}_{2}}$ = 2.00 atm, $P_{\text{H}_{2}}$ = 7.00 atm, $P_{\text{NH}_{3}}$ = 0.021 atm, and *T* = 100°C. Does the reaction favor products or reactants?

**Given:** balanced chemical equation, partial pressure of each species, temperature, and Δ*G*°

**Asked for:** whether products or reactants are favored

**Strategy:**

**A** Using the values given and [Equation 18.35](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq07), calculate *Q*.

**B** Substitute the values of Δ*G*° and *Q* into [Equation 18.35](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq07) to obtain Δ*G* for the reaction under nonstandard conditions.

**Solution:**

**A** The relationship between Δ*G*° and Δ*G* under nonstandard conditions is given in [Equation 18.35](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq07). Substituting the partial pressures given, we can calculate *Q*:

$$Q = \frac{P_{\text{NH}_{3}}^{2}}{P_{\text{N}_{2}}P_{\text{H}_{2}}^{3}} = \frac{{(0.021)}^{2}}{(2.00){(7.00)}^{3}} = 6.4 \times 10^{- 7}$$

**B** Substituting the values of Δ*G*° and *Q* into [Equation 18.35](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq07),

$$\begin{array}{rc}
{\Delta G = \Delta G{^\circ} + RT\text{ln~}Q} & {= - 32.7\text{~kJ} + \left\lbrack {(8.314\cancel{\text{J}}\text{/}\cancel{\text{K}})(373\ \cancel{\text{K}})\left( \frac{1\text{~kJ}}{1000\ \cancel{\text{J}}} \right)\ln(6.4 \times 10^{- 7})} \right\rbrack} \\
 & \begin{array}{r}
{= - 32.7\text{~kJ} + ( - 44\text{~kJ})} \\
{= - 77\text{~kJ/mol~of~N}_{2}}
\end{array}
\end{array}$$

Because Δ*G* \< 0 and *Q* \< 1.0, the reaction is spontaneous to the right as written, so products are favored over reactants.

Exercise

Calculate Δ*G* for the reaction of nitric oxide with oxygen to give nitrogen dioxide under these conditions: *T* = 50°C, *P*<sub>NO</sub> = 0.0100 atm, $P_{\text{O}_{2}}$ = 0.200 atm, and $P_{\text{NO}_{2}}$ = 1.00 × 10<sup>−4</sup> atm. The value of Δ*G*° for this reaction is −72.5 kJ/mol of O<sub>2</sub>. Are products or reactants favored?

**Answer:** −92.9 kJ/mol of O<sub>2</sub>; the reaction is spontaneous to the right as written, so products are favored.

### Example 13

Calculate *K*<sub>p</sub> for the reaction of H<sub>2</sub> with N<sub>2</sub> to give NH<sub>3</sub> at 25°C. As calculated in Example 10, Δ*G*° for this reaction is −32.7 kJ/mol of N<sub>2</sub>.

**Given:** balanced chemical equation from Example 10, Δ*G*°, and temperature

**Asked for:** *K* <sub>p</sub>

**Strategy:**

Substitute values for Δ*G*° and *T* (in kelvins) into [Equation 18.36](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq08) to calculate *K*<sub>p</sub>, the equilibrium constant for the formation of ammonia.

**Solution:**

In Example 10, we used tabulated values of $\Delta G_{\text{f}}^{{^\circ}}$ to calculate Δ*G*° for this reaction (−32.7 kJ/mol of N<sub>2</sub>). For equilibrium conditions, rearranging [Equation 18.36](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq08),

$$\begin{aligned}
{\Delta G{^\circ}} & {= - RT\text{ln~}K_{\text{p}}} \\
\frac{- \Delta G{^\circ}}{RT} & {= \text{ln~}K_{\text{p}}}
\end{aligned}$$

Inserting the value of Δ*G*° and the temperature (25°C = 298 K) into this equation,

$$\begin{aligned}
{\text{ln~}K_{\text{p}}} & {= - \frac{( - 32.7\cancel{\text{kJ}})(1000\ \cancel{\text{J}}\text{/}\cancel{\text{kJ}})}{(8.314\ \cancel{\text{J}}\text{/}\cancel{\text{K}})(298\ \cancel{\text{K}})} = 13.2} \\
K_{\text{p}} & {= 5.4 \times 10^{5}}
\end{aligned}$$

Thus the equilibrium constant for the formation of ammonia at room temperature is favorable. As we saw in [Chapter 15 \"Chemical Equilibrium\"](/chapters/ch-15-chemical-equilibrium.md#src-averill-1-0-ch15), however, the *rate* at which the reaction occurs at room temperature is too slow to be useful.

Exercise

Calculate *K*<sub>p</sub> for the reaction of NO with O<sub>2</sub> to give NO<sub>2</sub> at 25°C. As calculated in the exercise in Example 10, Δ*G*° for this reaction is −70.5 kJ/mol of O<sub>2</sub>.

**Answer:** 2.2 × 10<sup>12</sup>

Although *K*<sub>p</sub> is defined in terms of the partial pressures of the reactants and the products, the equilibrium constant *K* is defined in terms of the concentrations of the reactants and the products. We described the relationship between the numerical magnitude of *K*<sub>p</sub> and *K* in [Chapter 15 \"Chemical Equilibrium\"](/chapters/ch-15-chemical-equilibrium.md#src-averill-1-0-ch15) and showed that they are related:

Equation 18.37

*K*<sub>p</sub> = *K*(*RT*)<sup>Δ*n*</sup>

where Δ*n* is the number of moles of gaseous product minus the number of moles of gaseous reactant. For reactions that involve only solutions, liquids, and solids, Δ*n* = 0, so *K*<sub>p</sub> = *K*. For all reactions that do not involve a change in the number of moles of gas present, the relationship in [Equation 18.36](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq08) can be written in a more general form:

(src-averill-1-0-ch18-s06-s01-eq10)=

Equation 18.38

Δ*G*° = −*RT* ln *K*

Only when a reaction results in a net production or consumption of gases is it necessary to correct [Equation 18.38](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq10) for the difference between *K*<sub>p</sub> and *K*.[^chem-18]

Combining [Equation 18.26](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s05-s03-eq01) and [Equation 18.38](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq10) provides insight into how the components of Δ*G*° influence the magnitude of the equilibrium constant:

(src-averill-1-0-ch18-s06-s01-eq11)=

Equation 18.39

Δ*G*° = Δ*H*° − *T*Δ*S*° = −*RT* ln *K*

Notice that *K* becomes larger as Δ*S*° becomes more positive, indicating that the magnitude of the equilibrium constant is directly influenced by the tendency of a system to move toward maximum disorder. Moreover, *K* increases as Δ*H*° decreases. Thus the magnitude of the equilibrium constant is also directly influenced by the tendency of a system to seek the lowest energy state possible.

````````````{important} Note the Pattern

The magnitude of the equilibrium constant is directly influenced by the tendency of a system to move toward maximum disorder and seek the lowest energy state possible.

````````````

### Temperature Dependence of the Equilibrium Constant

The fact that Δ*G*° and *K* are related provides us with another explanation of why equilibrium constants are temperature dependent. This relationship is shown explicitly in [Equation 18.39](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq11), which can be rearranged as follows:

(src-averill-1-0-ch18-s06-s02-eq01)=

Equation 18.40

$$\text{ln~}K = - \frac{\Delta H{^\circ}}{RT} + \frac{\Delta S{^\circ}}{R}$$

Assuming Δ*H*° and Δ*S*° are temperature independent, for an exothermic reaction (Δ*H*° \< 0), the magnitude of *K* decreases with increasing temperature, whereas for an endothermic reaction (Δ*H*° \> 0), the magnitude of *K* increases with increasing temperature. The quantitative relationship expressed in [Equation 18.40](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s02-eq01) agrees with the qualitative predictions made by applying Le Châtelier's principle, which we discussed in [Chapter 15 \"Chemical Equilibrium\"](/chapters/ch-15-chemical-equilibrium.md#src-averill-1-0-ch15). Because heat is produced in an exothermic reaction, adding heat (by increasing the temperature) will shift the equilibrium to the left, favoring the reactants and decreasing the magnitude of *K*. Conversely, because heat is consumed in an endothermic reaction, adding heat will shift the equilibrium to the right, favoring the products and increasing the magnitude of *K*. [Equation 18.40](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s02-eq01) also shows that the *magnitude* of Δ*H*° dictates how rapidly *K* changes as a function of temperature. In contrast, the magnitude and sign of Δ*S*° affect the magnitude of *K* but not its temperature dependence.

If we know the value of *K* at a given temperature and the value of Δ*H*° for a reaction, we can estimate the value of *K* at any other temperature, even in the absence of information on Δ*S*°. Suppose, for example, that *K*<sub>1</sub> and *K*<sub>2</sub> are the equilibrium constants for a reaction at temperatures *T*<sub>1</sub> and *T*<sub>2</sub>, respectively. Applying [Equation 18.40](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s02-eq01) gives the following relationship at each temperature:

$$\begin{aligned}
{\text{ln~}K_{1}} & {= \frac{- \Delta H{^\circ}}{RT_{1}} + \frac{\Delta S{^\circ}}{R}} \\
{\text{ln~}K_{2}} & {= \frac{- \Delta H{^\circ}}{RT_{2}} + \frac{\Delta S{^\circ}}{R}}
\end{aligned}$$

Subtracting ln *K*<sub>1</sub> from ln *K*<sub>2</sub>,

(src-averill-1-0-ch18-s06-s02-eq02)=

Equation 18.41

$$\text{ln~}K_{2} - \text{ln~}K_{1} = \text{ln~}\frac{K_{2}}{K_{1}} = \frac{\Delta H{^\circ}}{R}\left( {\frac{1}{T_{1}} - \frac{1}{T_{2}}} \right)$$

Thus calculating Δ*H*° from tabulated enthalpies of formation and measuring the equilibrium constant at one temperature (*K*<sub>1</sub>) allow us to calculate the value of the equilibrium constant at any other temperature (*K*<sub>2</sub>), assuming that Δ*H*° and Δ*S*° are independent of temperature.

### Example 14

The equilibrium constant for the formation of NH<sub>3</sub> from H<sub>2</sub> and N<sub>2</sub> at 25°C was calculated to be *K*<sub>p</sub> = 5.4 × 10<sup>5</sup> in Example 13. What is *K*<sub>p</sub> at 500°C? (Use the data from Example 10.)

**Given:** balanced chemical equation, Δ*H*°, initial and final *T*, and *K*<sub>p</sub> at 25°C

**Asked for:** *K*<sub>p</sub> at 500°C

**Strategy:**

Convert the initial and final temperatures to kelvins. Then substitute appropriate values into [Equation 18.41](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s02-eq02) to obtain *K*<sub>2</sub>, the equilibrium constant at the final temperature.

**Solution:**

The value of Δ*H*° for the reaction obtained using Hess's law is −91.8 kJ/mol of N<sub>2</sub>. If we set *T*<sub>1</sub> = 25°C = 298.K and *T*<sub>2</sub> = 500°C = 773 K, then from [Equation 18.41](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s02-eq02) we obtain the following:

$$\begin{aligned}
{\text{ln~}\frac{K_{2}}{K_{1}}} & {= \frac{\Delta H{^\circ}}{R}\left( {\frac{1}{T_{1}} - \frac{1}{T_{2}}} \right)} \\
 & {= \frac{( - 91.8\ \cancel{\text{kJ}})(1000\ \cancel{\text{J}}\text{/}\cancel{\text{kJ}})}{8.314\ \cancel{\text{J}}\text{/}\cancel{\text{K}}}\left( {\frac{1}{298\ \cancel{\text{K}}} - \frac{1}{773\ \cancel{\text{K}}}} \right) = - 22.8} \\
\frac{K_{2}}{K_{1}} & {= 1.3 \times 10^{- 10}} \\
K_{2} & {= (5.4 \times 10^{5})(1.3 \times 10^{- 10}) = 7.0 \times 10^{- 5}}
\end{aligned}$$

Thus at 500°C, the equilibrium strongly favors the reactants over the products.

Exercise

In the exercise in Example 13, you calculated *K*<sub>p</sub> = 2.2 × 10<sup>12</sup> for the reaction of NO with O<sub>2</sub> to give NO<sub>2</sub> at 25°C. Use the $\Delta H_{\text{f}}^{{^\circ}}$ values in the exercise in Example 10 to calculate *K*<sub>p</sub> for this reaction at 1000°C.

**Answer:** 5.6 × 10<sup>−4</sup>

````````````{important} Summary

For a reversible process that does not involve external work, we can express the change in free energy in terms of volume, pressure, entropy, and temperature. If we assume ideal gas behavior, the ideal gas law allows us to express Δ*G* in terms of the partial pressures of the reactants and products, which gives us a relationship between Δ*G* and *K*<sub>p</sub>, the equilibrium constant of a reaction involving gases, or *K*, the equilibrium constant expressed in terms of concentrations. If Δ*G*° \< 0, then *K* or *K*<sub>p</sub> \> 1, and products are favored over reactants. If Δ*G*° \> 0, then *K* or *K*<sub>p</sub> \< 1, and reactants are favored over products. If Δ*G*° = 0, then *K* or *K*<sub>p</sub> = 1, and the system is at equilibrium. We can use the measured equilibrium constant *K* at one temperature and Δ*H*° to estimate the equilibrium constant for a reaction at any other temperature.

````````````

````````````{important} Key Takeaway

- The change in free energy of a reaction can be expressed in terms of the standard free-energy change and the equilibrium constant *K* or *K*<sub>p</sub> and indicates whether a reaction will occur spontaneously under a given set of conditions.

````````````

````````````{important} Key Equations

**Relationship between standard free-energy change and equilibrium constant**

[Equation 18.38](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq10): Δ*G*° = −*RT* ln *K*

**Temperature dependence of equilibrium constant**

[Equation 18.40](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s02-eq01): $\text{ln~}K = \frac{- \Delta H{^\circ}}{RT} + \frac{\Delta S{^\circ}}{R}$

**Calculation of** *K* **at second temperature**

[Equation 18.41](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s02-eq02): $\text{ln~}\frac{K_{2}}{K_{1}} = \frac{\Delta H{^\circ}}{R}\left( {\frac{1}{T_{1}} - \frac{1}{T_{2}}} \right)$

````````````

### Conceptual Problems

1.  Do you expect products or reactants to dominate at equilibrium in a reaction for which Δ*G*° is equal to

    1.  1.4 kJ/mol?
    2.  105 kJ/mol?
    3.  −34 kJ/mol?

2.  The change in free energy enables us to determine whether a reaction will proceed spontaneously. How is this related to the extent to which a reaction proceeds?

3.  What happens to the change in free energy of the reaction N<sub>2</sub>(g) + 3F<sub>2</sub>(g) → 2NF<sub>3</sub>(g) if the pressure is increased while the temperature remains constant? if the temperature is increased at constant pressure? Why are these effects not so important for reactions that involve liquids and solids?

4.  Compare the expressions for the relationship between the change in free energy of a reaction and its equilibrium constant where the reactants are gases versus liquids. What are the differences between these expressions?

### Numerical Problems

1.  Carbon monoxide, a toxic product from the incomplete combustion of fossil fuels, reacts with water to form CO<sub>2</sub> and H<sub>2</sub>, as shown in the equation $\left. \text{CO(g)} + \text{H}_{2}\text{O(g)}\rightleftharpoons\text{CO}_{2}\text{(g)} + \text{H}_{2}\text{(g),} \right.$ for which Δ*H*° = −41.0 kJ/mol and Δ*S*° = −42.3 J cal/(mol·K) at 25°C and 1 atm.

    1.  What is Δ*G*° for this reaction?
    2.  What is Δ*G* if the gases have the following partial pressures: *P*<sub>CO</sub> = 1.3 atm, $P_{\text{H}_{2}\text{O}}$ = 0.8 atm, $P_{\text{CO}_{2}}$ = 2.0 atm, and $P_{\text{H}_{2}}$ = 1.3 atm?
    3.  What is Δ*G* if the temperature is increased to 150°C assuming no change in pressure?

2.  Methane and water react to form carbon monoxide and hydrogen according to the equation $\left. \text{CH}_{4}\text{(g)} + \text{H}_{2}\text{O(g)}\rightleftharpoons\text{CO(g)} + 3\text{H}_{2}\text{(g)}\text{.} \right.$

    1.  What is the standard free energy change for this reaction?
    2.  What is *K*<sub>p</sub> for this reaction?
    3.  What is the carbon monoxide pressure if 1.3 atm of methane reacts with 0.8 atm of water, producing 1.8 atm of hydrogen gas?
    4.  What is the hydrogen gas pressure if 2.0 atm of methane is allowed to react with 1.1 atm of water?
    5.  At what temperature does the reaction become spontaneous?

3.  Calculate the equilibrium constant at 25°C for each equilibrium reaction and comment on the extent of the reaction.

    1.  $\left. \text{CCl}_{4}\text{(g)} + 6\text{H}_{2}\text{O(l)}\rightleftharpoons\text{CO}_{2}\text{(g)} + 4\text{HCl(aq);~} \right.$ Δ*G*° = −377 kJ/mol
    2.  $\left. \text{Xe(g)} + 2\text{F}_{2}\text{(g)}\rightleftharpoons\text{XeF}_{4}\text{(s);~} \right.$ Δ*H*° = −66.3 kJ/mol, Δ*S*° = −102.3 J/(mol·K)
    3.  $\left. \text{PCl}_{3}\text{(g)} + \text{S}\rightleftharpoons\text{PSCl}_{3}\text{(l);~} \right.$$\Delta G_{\text{f}}^{{^\circ}}$(PCl<sub>3</sub>) = −272.4 kJ/mol, $\Delta G_{\text{f}}^{{^\circ}}$(PSCl<sub>3</sub>) = −363.2 kJ/mol

4.  Calculate the equilibrium constant at 25°C for each equilibrium reaction and comment on the extent of the reaction.

    1.  $\left. 2\text{KClO}_{3}\text{(s)}\rightleftharpoons 2\text{KCl(s)} + 3\text{O}_{2}\text{(g);~} \right.$ Δ*G*° = −225.8 kJ/mol
    2.  $\left. \text{CoCl}_{2}\text{(s)} + 6\text{H}_{2}\text{O(g)}\rightleftharpoons\text{CoCl}_{2}\text{}\cdot \text{}6\text{H}_{2}\text{O(s);} \right.$$\Delta H_{\text{rxn}}^{{^\circ}}$ = −352 kJ/mol, $\Delta S_{\text{rxn}}^{{^\circ}}$ = −899 J/(mol·K)
    3.  $\left. 2\text{PCl}_{3}\text{(g)} + \text{O}_{2}\text{(g)}\rightleftharpoons 2\text{POCl}_{3}\text{(g);} \right.$ $\Delta G_{\text{f}}^{{^\circ}}$(PCl<sub>3</sub>) = −272.4 kJ/mol, $\Delta G_{\text{f}}^{{^\circ}}$(POCl<sub>3</sub>) = −558.5 kJ/mol

5.  The gas-phase decomposition of N<sub>2</sub>O<sub>4</sub> to NO<sub>2</sub> is an equilibrium reaction with *K*<sub>p</sub> = 4.66 × 10<sup>−3</sup>. Calculate the standard free-energy change for the equilibrium reaction between N<sub>2</sub>O<sub>4</sub> and NO<sub>2</sub>.

6.  The standard free-energy change for the dissolution $\left. \text{K}_{4}\text{Fe(CN)}_{6}\text{}\cdot \text{}\text{H}_{2}\text{O(s)}\rightleftharpoons 4\text{K}^{+}\text{(aq)} + \text{Fe(CN)}_{6}{}^{4 -}\text{(aq)} + \text{H}_{2}\text{O(l)} \right.$ is 26.1 kJ/mol. What is the equilibrium constant for this process at 25°C?

7.  Ammonia reacts with water in liquid ammonia solution (am) according to the equation $\left. \text{NH}_{3}\text{(g)} + \text{H}_{2}\text{O(am)}\rightleftharpoons\text{NH}_{4}{}^{+}\text{(am)} + \text{OH}^{-}\text{(am)}\text{.} \right.$ The change in enthalpy for this reaction is 21 kJ/mol, and Δ*S*° = −303 J/(mol·K). What is the equilibrium constant for the reaction at the boiling point of liquid ammonia (−31°C)?

8.  At 25°C, a saturated solution of barium carbonate is found to have a concentration of \[Ba<sup>2+</sup>\] = \[CO<sub>3</sub><sup>2−</sup>\] = 5.08 × 10<sup>−5</sup> M. Determine Δ*G*° for the dissolution of BaCO<sub>3</sub>.

9.  Lead phosphates are believed to play a major role in controlling the overall solubility of lead in acidic soils. One of the dissolution reactions is $\left. \text{Pb}_{3}{(\text{PO}_{4})}_{2}\text{(s)} + 4\text{H}^{+}\text{(aq)}\rightleftharpoons 3\text{Pb}^{2 +}\text{(aq)} + 2\text{H}_{2}\text{PO}_{4}{}^{-}\text{(aq),} \right.$ for which log *K* = −1.80. What is Δ*G*° for this reaction?

10. The conversion of butane to 2-methylpropane is an equilibrium process with Δ*H*° = −2.05 kcal/mol and Δ*G*° = −0.89 kcal/mol.

    1.  What is the change in entropy for this conversion?
    2.  Based on structural arguments, are the sign and magnitude of the entropy change what you would expect? Why?
    3.  What is the equilibrium constant for this reaction?

11. The reaction of CaCO<sub>3</sub>(s) to produce CaO(s) and CO<sub>2</sub>(g) has an equilibrium constant at 25°C of 2 × 10<sup>−23</sup>. Values of $\Delta H_{\text{f}}^{{^\circ}}$ are as follows: CaCO<sub>3</sub>, −1207.6 kJ/mol; CaO, −634.9 kJ/mol; and CO<sub>2</sub>, −393.5 kJ/mol.

    1.  What is Δ*G*° for this reaction?
    2.  What is the equilibrium constant at 900°C?
    3.  What is the partial pressure of CO<sub>2</sub>(g) in equilibrium with CaO and CaCO<sub>3</sub> at this temperature?
    4.  Are reactants or products favored at the lower temperature? at the higher temperature?

12. In acidic soils, dissolved Al<sup>3+</sup> undergoes a complex formation reaction with SO<sub>4</sub><sup>2−</sup> to form \[AlSO<sub>4</sub><sup>+</sup>\]. The equilibrium constant at 25°C for the reaction $\left. \text{Al}^{3 +}\text{(aq)} + \text{SO}_{4}{}^{2 -}\text{(aq)}\rightleftharpoons\text{AlSO}_{4}{}^{+}\text{(aq)} \right.$ is 1585.

    1.  What is Δ*G*° for this reaction?
    2.  How does this value compare with Δ*G*° for the reaction $\left. \text{Al}^{3 +}\text{(aq)} + \text{F}^{-}\text{(aq)}\rightleftharpoons\text{AlF}^{2 +}\text{(aq),} \right.$ for which *K* = 10<sup>7</sup> at 25°C?
    3.  Which is the better ligand to use to trap Al<sup>3+</sup> from the soil?

### Answers

1.  1.  −28.4 kJ/mol
    2.  −26.1 kJ/mol
    3.  −19.9 kJ/mol

2.  

3.  1.  1.21 × 10<sup>66</sup>; equilibrium lies far to the right.
    2.  1.89 × 10<sup>6</sup>; equilibrium lies to the right.
    3.  5.28 × 10<sup>16</sup>; equilibrium lies far to the right.

4.  

5.  13.3 kJ/mol

6.  

7.  5.1 × 10<sup>−21</sup>

8.  

9.  10.3 kJ/mol

10. 

11. 1.  129.5 kJ/mol
    2.  6
    3.  6.0 atm
    4.  Products are favored at high *T*; reactants are favored at low *T*.

12. 

## 18.7 Comparing Thermodynamics and Kinetics

````````````{note} Learning Objective

1.  To understand the differences between the information that thermodynamics and kinetics provide about a system.

````````````

Because thermodynamics deals with state functions, it can be used to describe the overall properties, behavior, and equilibrium composition of a system. It is *not* concerned with the particular pathway by which physical or chemical changes occur, however, so it cannot address the *rate* at which a particular process will occur. Although thermodynamics provides a significant constraint on what *can* occur during a reaction process, it does not describe the detailed steps of what *actually* occurs on an atomic or a molecular level.

````````````{important} Note the Pattern

Thermodynamics focuses on the energetics of the products and the reactants, whereas kinetics focuses on the pathway from reactants to products.

````````````

[Table 18.4 \"The Relationship between \"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s07-t01) gives the numerical values of the equilibrium constant (*K*) that correspond to various approximate values of Δ*G*°. Note that Δ*G*° ≥ +10 kJ/mol or Δ*G*° ≤ −10 kJ/mol ensures that an equilibrium lies essentially all the way to the left or to the right, respectively, under standard conditions, corresponding to a reactant-to-product ratio of approximately 10,000:1 (or vice versa). Only if Δ*G*° is quite small (±10 kJ/mol) are significant amounts of both products and reactants present at equilibrium. Most reactions that we encounter have equilibrium constants substantially greater or less than 1, with the equilibrium strongly favoring either products or reactants. In many cases, we will encounter reactions that are strongly favored by thermodynamics but do not occur at a measurable rate. In contrast, we may encounter reactions that are not thermodynamically favored under standard conditions but nonetheless do occur under certain nonstandard conditions.

(src-averill-1-0-ch18-s07-t01)=

Table 18.4 The Relationship between *K* and Δ*G*° at 25°C

````````{list-table}
:header-rows: 1

- - Δ*G*° (kJ/mol)
  - *K*
  - Physical Significance
- - 500
  - 3 × 10<sup>−88</sup>
  - For all intents and purposes, the reaction does not proceed in the forward direction: only reactants are present at equilibrium.
- - 100
  - 3 × 10<sup>−18</sup>
  - For all intents and purposes, the reaction does not proceed in the forward direction: only reactants are present at equilibrium.
- - 10
  - 2 × 10<sup>−2</sup>
  - Both forward and reverse reactions occur: significant amounts of both products and reactants are present at equilibrium.
- - 0
  - 1
  - Both forward and reverse reactions occur: significant amounts of both products and reactants are present at equilibrium.
- - −10
  - 60
  - Both forward and reverse reactions occur: significant amounts of both products and reactants are present at equilibrium.
- - −100
  - 3 × 10<sup>17</sup>
  - For all intents and purposes, the forward reaction proceeds to completion: only products are present at equilibrium.
- - −500
  - 4 × 10<sup>87</sup>
  - For all intents and purposes, the forward reaction proceeds to completion: only products are present at equilibrium.

````````

A typical challenge in industrial processes is a reaction that has a large negative value of Δ*G*° and hence a large value of *K* but that is too slow to be practically useful. In such cases, mixing the reactants results in only a physical mixture, not a chemical reaction. An example is the reaction of carbon tetrachloride with water to produce carbon dioxide and hydrochloric acid, for which Δ*G*° is −232 kJ/mol:

Equation 18.42

$$\left. \text{CCl}_{4}\text{(l)} + 2\text{H}_{2}\text{O(l)}\rightleftharpoons\text{CO}_{2}\text{(g)} + 2\text{HCl(g)} \right.$$

The value of *K* for this reaction is 5 × 10<sup>40</sup> at 25°C, yet when CCl<sub>4</sub> and water are shaken vigorously at 25°C, nothing happens: the two immiscible liquids form separate layers, with the denser CCl<sub>4</sub> on the bottom. In comparison, the analogous reaction of SiCl<sub>4</sub> with water to give SiO<sub>2</sub> and HCl, which has a similarly large equilibrium constant, occurs almost explosively. Although the two reactions have comparable thermodynamics, they have very different kinetics!

There are also many reactions for which Δ*G*° \<\< 0 but that do not occur as written because another possible reaction occurs more rapidly. For example, consider the reaction of lead sulfide with hydrogen peroxide. One possible reaction is as follows:

(src-averill-1-0-ch18-s07-eq02)=

Equation 18.43

$$\left. \text{PbS(s)~} + 4\text{H}_{2}\text{O}_{2}\text{(l)}\rightleftharpoons\text{PbO}_{2}\text{(s)} + \text{SO}_{2}\text{(g)} + 4\text{H}_{2}\text{O(l)} \right.$$

for which Δ*G*° is −886 kJ/mol and *K* is 10<sup>161</sup>. Yet when lead sulfide is mixed with hydrogen peroxide, the ensuing vigorous reaction does *not* produce PbO<sub>2</sub> and SO<sub>2</sub>. Instead, the reaction that actually occurs is as follows:

Equation 18.44

$$\left. \text{PbS(s)~} + 4\text{H}_{2}\text{O}_{2}\text{(l)}\rightleftharpoons\text{PbSO}_{4}\text{(s)} + 4\text{H}_{2}\text{O(l)} \right.$$

This reaction has a Δ*G*° value of −1181 kJ/mol, within the same order of magnitude as the reaction in [Equation 18.43](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s07-eq02), but it occurs much more rapidly.

Now consider reactions with Δ*G*° \> 0. Thermodynamically, such reactions do not occur spontaneously under standard conditions. Nonetheless, these reactions can be made to occur under nonstandard conditions. An example is the reduction of chromium(III) chloride by hydrogen gas:

Equation 18.45

$$\left. \text{CrCl}_{3}\text{(s)} + \frac{1}{2}\text{H}_{2}\left( \text{g} \right)\rightleftharpoons\text{CrCl}_{2}\text{(s)} + \text{HCl(g)} \right.$$

At 25°C, Δ*G*° = 35 kJ/mol and *K*<sub>p</sub> = 7 × 10<sup>−7</sup>. However, at 730°C, Δ*G*° = −52 kJ/mol and *K*<sub>p</sub> = 5 × 10<sup>2</sup>; at this elevated temperature, the reaction is a convenient way of preparing chromium(II) chloride in the laboratory. Moreover, removing HCl gas from the system drives the reaction to completion, as predicted by Le Châtelier's principle. Although the reaction is not thermodynamically spontaneous under standard conditions, it becomes spontaneous under nonstandard conditions.

There are also cases in which a compound whose formation appears to be thermodynamically prohibited can be prepared using a different reaction. The reaction for the preparation of chlorine monoxide from its component elements, for example, is as follows:

Equation 18.46

$$\left. \frac{1}{2}\text{O}_{2}\text{(g)} + \text{Cl}_{2}\text{(g)}\rightleftharpoons\text{Cl}_{2}\text{O(g)} \right.$$

for which $\Delta G_{\text{f}}^{{^\circ}}$ is 97.9 kJ/mol. The large positive value of $\Delta G_{\text{f}}^{{^\circ}}$ for this reaction indicates that mixtures of chlorine and oxygen do not react to any extent to form Cl<sub>2</sub>O. Nonetheless, Cl<sub>2</sub>O is easily prepared using the reaction

(src-averill-1-0-ch18-s07-eq06)=

Equation 18.47

$$\left. \text{HgO(s)} + 2\text{Cl}_{2}\text{(g)}\rightleftharpoons\text{Cl}_{2}\text{O(g)} + \text{HgCl}_{2}\text{(s)} \right.$$

which has a Δ*G*° of −22.2 kJ/mol and a *K*<sub>p</sub> of approximately 1 × 10<sup>4</sup>.

Finally, the Δ*G*° values for some reactions are so positive that the only way to make them proceed in the desired direction is to supply external energy, often in the form of electricity. Consider, for example, the formation of metallic lithium from molten lithium chloride:

Equation 18.48

$$\left. \text{LiCl(l)}\rightleftharpoons\text{Li(l)} + \frac{1}{2}\text{Cl}_{2}\text{(g)} \right.$$

Even at 1000°C, Δ*G* is very positive (324 kJ/mol), and there is no obvious way to obtain lithium metal using a different reaction. Hence in the industrial preparation of metallic lithium, electrical energy is used to drive the reaction to the right, as described in [Chapter 19 \"Electrochemistry\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19).

````````````{important} Note the Pattern

A reaction that does not occur under standard conditions can be made to occur under nonstandard conditions, such as by driving the reaction to completion using Le Châtelier's principle or by providing external energy.

````````````

Often reactions that are not thermodynamically spontaneous under standard conditions can be made to occur spontaneously if coupled, or connected, in some way to another reaction for which Δ*G*° \<\< 0. Because the overall value of Δ*G*° for a series of reactions is the sum of the Δ*G*° values for the individual reactions, virtually any unfavorable reaction can be made to occur by chemically coupling it to a sufficiently favorable reaction or reactions. In the preparation of chlorine monoxide from mercuric oxide and chlorine ([Equation 18.47](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s07-eq06)), we have already encountered one example of this phenomenon of *coupled reactions*, although we did not describe it as such at the time. We can see how the chemical coupling works if we write [Equation 18.47](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s07-eq06) as the sum of three separate reactions:

$$\begin{array}{rlclc}
{\cancel{\frac{1}{2}\text{O}_{2}\text{(g)}} + \text{Cl}_{2}\text{(g)}} & \left. \rightleftharpoons\text{Cl}_{2}\text{O(g)} \right. & {\Delta G{^\circ}} & {= 97.9\text{~kJ/mol}} & {(1)} \\
\text{HgO(s)} & \left. \rightleftharpoons\cancel{\text{Hg(l)}} + \cancel{\frac{1}{2}\text{O}_{2}\text{(g)}} \right. & {\Delta G{^\circ}} & {= 58.5\text{~kJ/mol}} & {(2)} \\
{\cancel{\text{Hg(l)}} + \text{Cl}_{2}\text{(g)}} & \left. \rightleftharpoons\text{HgCl}_{2}\text{(s)} \right. & {\Delta G{^\circ}} & {= - 178.6\text{~kJ/mol}} & {(3)} \\
{\text{HgO(s)} + 2\text{Cl}_{2}\text{(g)}} & \left. \rightleftharpoons\text{Cl}_{2}\text{O(g)} + \text{HgCl}_{2}\text{(s)} \right. & {\Delta G_{\text{rxn}}^{{^\circ}}} & {= - 22.2\text{~kJ/mol}} & 
\end{array}$$

Comparing the Δ*G*° values for the three reactions shows that reaction 3 is so energetically favorable that it more than compensates for the other two energetically unfavorable reactions. Hence the overall reaction is indeed thermodynamically spontaneous as written.

````````````{important} Note the Pattern

By coupling reactions, a reaction that is thermodynamically nonspontaneous can be made spontaneous.

````````````

### Example 15

Bronze Age metallurgists were accomplished practical chemists who unknowingly used coupled reactions to obtain metals from their ores. Realizing that different ores of the same metal required different treatments, they heated copper oxide ore in the presence of charcoal (carbon) to obtain copper metal, whereas they pumped air into the reaction system if the ore was copper sulfide. Assume that a particular copper ore consists of pure cuprous oxide (Cu<sub>2</sub>O). Using the $\Delta G_{\text{f}}^{{^\circ}}$ values given for each, calculate

1.  Δ*G*° and *K*<sub>p</sub> for the decomposition of Cu<sub>2</sub>O to metallic copper and oxygen gas $\left\lbrack {\Delta G_{\text{f}}^{{^\circ}}\left( {\text{Cu}_{2}\text{O}} \right) = - 146.0\text{~kJ/mol}} \right\rbrack\text{.}$
2.  Δ*G*° and *K*<sub>p</sub> for the reaction of Cu<sub>2</sub>O with carbon to produce metallic copper and carbon monoxide $\left\lbrack {\Delta G_{\text{f}}^{{^\circ}}\left( \text{CO} \right) = - 137.2\text{~kJ/mol}} \right\rbrack\text{.}$

**Given:** reactants and products, $\Delta G_{\text{f}}^{{^\circ}}$ values for Cu<sub>2</sub>O and CO, and temperature

**Asked for:** Δ*G*° and *K*<sub>p</sub> for the formation of metallic copper from Cu<sub>2</sub>O in the absence and presence of carbon

**Strategy:**

**A** Write the balanced equilibrium equation for each reaction. Using the "products minus reactants" rule, calculate Δ*G*° for the reaction.

**B** Substitute appropriate values into [Equation 18.36](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq08) to obtain *K*<sub>p</sub>.

**Solution:**

1.  **A** The chemical equation for the decomposition of cuprous oxide is as follows:

    $$\left. \text{Cu}_{2}\text{O(s)}\rightleftharpoons 2\text{Cu(s)} + \frac{1}{2}\text{O}_{2}\text{(g)} \right.$$

    The substances on the right side of this equation are pure elements in their standard states, so their $\Delta G_{\text{f}}^{{^\circ}}$ values are zero. Δ*G*° for the reaction is therefore

    $$\begin{aligned}
    {\Delta G{^\circ}} & {= \left\lbrack {2\Delta G_{\text{f}}^{{^\circ}}\text{(Cu)} + \frac{1}{2}\Delta G_{\text{f}}^{{^\circ}}(\text{O}_{2})} \right\rbrack - \Delta G_{\text{f}}^{{^\circ}}(\text{Cu}_{2}\text{O})} \\
     & {= \left\lbrack {(2\ \cancel{\text{mol}})(0\text{~kJ/}\cancel{\text{mol}}) + \left( {\frac{1}{2}\cancel{\text{mol}}} \right)(0\text{~kJ/}\cancel{\text{mol}})} \right\rbrack - \lbrack(1\ \cancel{\text{mol}})( - 146.0\text{~kJ/}\cancel{\text{mol}})\rbrack} \\
     & {= 146.0\text{~kJ}}
    \end{aligned}$$

    **B** Rearranging and substituting the appropriate values into [Equation 18.36](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s06-s01-eq08),

    $$\begin{aligned}
    {\text{ln~}K_{\text{p}}} & {= - \frac{\Delta G{^\circ}}{RT} = - \frac{(146.0\ \cancel{\text{kJ}})(1000\ \cancel{\text{J}}\text{/}\cancel{\text{kJ}})}{(8.314\ \cancel{\text{J}}\text{/}\cancel{\text{K}})(298.15\ \cancel{\text{K}})} = - 58.90} \\
    K_{\text{p}} & {= 2.6 \times 10^{- 26}}
    \end{aligned}$$

    This is a very small number, indicating that Cu<sub>2</sub>O does not spontaneously decompose to a significant extent at room temperature.

2.  **A** The O<sub>2</sub> produced in the decomposition of Cu<sub>2</sub>O can react with carbon to form CO:

    $$\left. \frac{1}{2}\text{O}_{2}\text{(g)} + \text{C(s)}\rightleftharpoons\text{CO(g)} \right.$$

    Because Δ*G*° for this reaction is equal to $\Delta G_{\text{f}}^{{^\circ}}$ for CO (−137.2 kJ/mol), it is energetically more feasible to produce metallic copper from cuprous oxide by coupling the two reactions:

    $$\begin{array}{rlcl}
    {\text{Cu}_{2}\text{O(s)}} & \left. \rightleftharpoons 2\text{Cu(s)} + \cancel{\frac{1}{2}\text{O}_{2}\text{(g)}} \right. & {\Delta G{^\circ}} & {= 146.0\text{~kJ/mol}} \\
    {\cancel{\frac{1}{2}\text{O}_{2}\text{(g)}} + \text{C(s)}} & \left. \rightleftharpoons\text{~CO(g)} \right. & {\Delta G{^\circ}} & {= - 137.2\text{~kJ/mol}} \\
    {\text{Cu}_{2}\text{O(s)} + \text{C(s)}} & \left. \rightleftharpoons 2\text{Cu(s)} + \text{CO(g)} \right. & {\Delta G_{\text{f}}^{{^\circ}}} & {= 8.8\text{~kJ/mol}}
    \end{array}$$

    **B** We can find the corresponding value of *K*<sub>p</sub>:

    $$\begin{aligned}
    {\text{ln~}K_{\text{p}}} & {= - \frac{\Delta G{^\circ}}{RT} = - \frac{(8.8\cancel{\text{kJ}})(1000\ \cancel{\text{J}}\text{/}\cancel{\text{kJ}})}{(8.314\ \cancel{\text{J}}\text{/}\cancel{\text{K}})(298.15\ \cancel{\text{K}})} = - 3.6} \\
    K_{\text{p}} & {= 0.03}
    \end{aligned}$$

    Although this value is still less than 1, indicating that reactants are favored over products at room temperature, it is about 24 orders of magnitude greater than *K*<sub>p</sub> for the production of copper metal in the absence of carbon. Because both Δ*H*° and Δ*S*° are positive for this reaction, it becomes thermodynamically feasible at slightly elevated temperatures (greater than about 80°C). At temperatures of a few hundred degrees Celsius, the reaction occurs spontaneously, proceeding smoothly and rapidly to the right as written and producing metallic copper and carbon monoxide from cuprous oxide and carbon.

Exercise

Use the $\Delta G_{\text{f}}^{{^\circ}}$ values given to calculate Δ*G*° and *K*<sub>p</sub> for each reaction.

1.  the decomposition of cuprous sulfide to copper metal and elemental sulfur \[$\Delta G_{\text{f}}^{{^\circ}}\left( {\text{Cu}_{\text{2}}\text{S}} \right) = - \text{86}.\text{2~kJ/mol}\rbrack$
2.  the reaction of cuprous sulfide with oxygen gas to produce sulfur dioxide and copper metal \[$\Delta G_{\text{f}}^{{^\circ}}$ \[SO<sub>2</sub>(g)\] = −300.1 kJ/mol\]

**Answer:**

1.  Δ*G*° = 86.2 kJ/mol; *K*<sub>p</sub> = 7.90 × 10<sup>−16</sup>
2.  Δ*G*° = −213.9 kJ/mol; *K*<sub>p</sub> = 2.99 × 10<sup>37</sup>

````````````{important} Summary

Thermodynamics describes the overall properties, behavior, and equilibrium composition of a system; kinetics describes the rate at which a particular process will occur and the pathway by which it will occur. Whereas thermodynamics tells us what can occur during a reaction process, kinetics tells us what actually occurs on an atomic or a molecular level. A reaction that is not thermodynamically spontaneous under standard conditions can often be made to occur spontaneously by varying the reaction conditions; using a different reaction to obtain the same product; supplying external energy, such as electricity; or coupling the unfavorable reaction to another reaction for which Δ*G*° \<\< 0.

````````````

````````````{important} Key Takeaway

- Thermodynamics describes the overall properties, behavior, and equilibrium composition of a system, whereas kinetics describes the particular pathway by which a physical or a chemical change actually occurs.

````````````

### Conceptual Problem

1.  You are in charge of finding conditions to make the reaction A(l) + B(l) → C(l) + D(g) favorable because it is a critical step in the synthesis of your company's key product. You have calculated that Δ*G*° for the reaction is negative, yet the ratio of products to reactants is very small. What have you overlooked in your scheme? What can you do to drive the reaction to increase your product yield?

## 18.8 Thermodynamics and Life

````````````{note} Learning Objective

1.  To understand the importance of thermodynamics in biochemical systems.

````````````

In a thermodynamic sense, a living cell can be viewed as a low-entropy system that is *not* in equilibrium with its surroundings and is capable of replicating itself. A constant input of energy is needed to maintain the cell's highly organized structure, its wide array of precisely folded biomolecules, and its intricate system of thousands of chemical reactions. A cell also needs energy to synthesize complex molecules from simple precursors (e.g., to make proteins from amino acids), create and maintain differences in the concentrations of various substances inside and outside the cell, and do mechanical work (e.g., muscle contraction). In this section, we examine the nature of the energy flow between a cell and its environment as well as some of the chemical strategies cells use to extract energy from their surroundings and store that energy.

### Energy Flow between a Cell and Its Surroundings

One implication of the first and second laws of thermodynamics is that any closed system must eventually reach equilibrium. With no external input, a clock will run down, a battery will lose its charge, and a mixture of an aqueous acid and an aqueous base will achieve a uniform intermediate pH value. In contrast, a cell is an open system that can exchange matter with its surroundings as well as absorb energy from its environment in the form of heat or light. Cells use the energy obtained in these ways to maintain the nonequilibrium state that is essential for life.

Because cells are open systems, they cannot be described using the concepts of classical thermodynamics that we have discussed in this chapter, which have focused on reversible processes occurring in closed chemical systems that can exchange energy---but not matter---with their surroundings. Consequently, a relatively new subdiscipline called *nonequilibrium thermodynamics* has been developed to quantitatively describe open systems such as living cells.

Because a cell cannot violate the second law of thermodynamics, the only way it can maintain a low-entropy, nonequilibrium state characterized by a high degree of structural organization is to increase the entropy of its surroundings. A cell releases some of the energy that it obtains from its environment as heat that is transferred to its surroundings, thereby resulting in an increase in *S*<sub>surr</sub> ([Figure 18.17 \"Life and Entropy\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s08-s01-f01)). As long as Δ*S*<sub>surr</sub> is positive and greater than Δ*S*<sub>sys</sub>, the entropy of the universe increases, so the second law of thermodynamics is not violated. Releasing heat to the surroundings is necessary but not sufficient for life: the release of energy must be coupled to processes that increase the degree of order within a cell. For example, a wood fire releases heat to its surroundings, but unless energy from the burning wood is also used to do work, there is no increase in order of any portion of the universe.

(src-averill-1-0-ch18-s08-s01-f01)=

Figure 18.17 Life and Entropy

![Figure 18.17 Life and Entropy](/images/section_22/35393b221c5e9e0bebd1bb2cf0504ab3.jpg)

A living cell is in a low-entropy, nonequilibrium state characterized by a high degree of structural organization. To maintain this state, a cell must release some of the energy it obtains from its environment as heat, thereby increasing *S*<sub>surr</sub> sufficiently that the second law of thermodynamics is not violated. In this example, the cell combines smaller components into larger, more ordered structures; the accompanying release of heat increases the entropy of the surrounding environment so that *S*<sub>univ</sub> \> 0.

````````````{important} Note the Pattern

Any organism in equilibrium with its environment is dead.

````````````

### Extracting Energy from the Environment

Although organisms employ a wide range of specific strategies to obtain the energy they need to live and reproduce, they can generally be divided into two categories: organisms are either *phototrophs* (from the Greek *photos*, meaning "light," and *trophos*, meaning "feeder"), whose energy source is sunlight, or *chemotrophs*, whose energy source is chemical compounds, usually obtained by consuming or breaking down other organisms. Phototrophs, such as plants, algae, and photosynthetic bacteria, use the radiant energy of the sun directly, converting water and carbon dioxide to energy-rich organic compounds, whereas chemotrophs, such as animals, fungi, and many nonphotosynthetic bacteria, obtain energy-rich organic compounds from their environment. Regardless of the nature of their energy and carbon sources, all organisms use oxidation--reduction, or redox, reactions to drive the synthesis of complex biomolecules. Organisms that can use only O<sub>2</sub> as the oxidant (a group that includes most animals) are *aerobic organisms* that cannot survive in the absence of O<sub>2</sub>. Many organisms that use other oxidants (such as SO<sub>4</sub><sup>2−</sup>, NO<sub>3</sub><sup>−</sup>, or CO<sub>3</sub><sup>2−</sup>) or oxidized organic compounds can live only in the absence of O<sub>2</sub>, which is a deadly poison for them; such species are called *anaerobic organisms*.

The fundamental reaction by which all green plants and algae obtain energy from sunlight is photosynthesis[^chem-19], the photochemical reduction of CO<sub>2</sub> to a carbon compound such as glucose. Concurrently, oxygen in water is oxidized to O<sub>2</sub> (recall that *h*ν is energy from light):

Equation 18.49

$$6\text{CO}_{2} + \underset{\text{photosynthesis}}{6\text{H}_{2}\text{O}\overset{hv}{\rightarrow}\text{C}_{6}\text{H}_{12}\text{O}_{6}} + 6\text{O}_{2}$$

This reaction is not a spontaneous process as written, so energy from sunlight is used to drive the reaction. Photosynthesis is critical to life on Earth; it produces all the oxygen in our atmosphere.

In many ways, chemotrophs are more diverse than phototrophs because the nature of both the reductant (the nutrient) and the oxidant can vary. The most familiar chemotrophic strategy uses compounds such as glucose as the reductant and molecular oxygen as the oxidant in a process called respiration[^chem-20]. (For more information on respiration, see [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05).) The overall reaction of respiration is the reverse of photosynthesis:

(src-averill-1-0-ch18-s08-s02-eq02)=

Equation 18.50

$$\text{C}_{6}\text{H}_{12}\text{O}_{6} + \underset{\text{respiration}}{\left. 6\text{O}_{2}\rightarrow 6\text{CO}_{2} \right.} + 6\text{H}_{2}\text{O}$$

An alternative strategy uses fermentation[^chem-21] reactions, in which an organic compound is simultaneously oxidized and reduced. Common examples are alcohol fermentation, used in making wine, beer, and bread, and lactic acid fermentation, used in making yogurt:

Equation 18.51

$$\underset{\text{alcohol~fermentation}}{\left. \text{C}_{6}\text{H}_{12}\text{O}_{6}\rightarrow 2\text{CO}_{2} + 2\text{CH}_{3}\text{CH}_{2}\text{OH} \right.}$$

Equation 18.52

$$\underset{\text{lactic~acid~fermentation}}{\left. \text{C}_{6}\text{H}_{12}\text{O}_{6}\rightarrow 2\text{CH}_{3}\text{CH}\left( \text{OH} \right)\text{CO}_{2}\text{H} \right.}$$

In these reactions, some of the carbon atoms of glucose are oxidized, while others are reduced. Recall that a reaction in which a single species is both oxidized and reduced is called a *disproportionation* reaction.

### The Role of NADH and ATP in Metabolism

Regardless of the identity of the substances from which an organism obtains energy, the energy must be released in very small increments if it is to be useful to the cell. Otherwise, the temperature of the cell would rise to lethal levels. Cells store part of the energy that is released as ATP (adenosine triphosphate), a compound that is the universal energy currency of all living organisms ([Figure 18.18 \"ATP, the Universal Energy Currency of All Cells\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s08-s03-f01)).

(src-averill-1-0-ch18-s08-s03-f01)=

Figure 18.18 ATP, the Universal Energy Currency of All Cells

![Figure 18.18 ATP, the Universal Energy Currency of All Cells](/images/section_22/4c472e40bbb8daf25916b0c16b33db08.jpg)

The ATP molecule contains a nitrogen-containing base, a sugar, and three phosphate groups, as well as two high-energy phosphoric acid anhydride bonds.

Most organisms use several intermediate species to shuttle electrons between the terminal reductant (such as glucose) and the terminal oxidant (such as O<sub>2</sub>). In virtually all cases, an intermediate species oxidizes the energy-rich reduced compound, and the now-reduced intermediate then migrates to another site where *it* is oxidized. The most important of these electron-carrying intermediates is NAD<sup>+</sup> (nicotinamide adenine dinucleotide; [Figure 18.19 \"NAD\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s08-s03-f02)), whose reduced form, formally containing H<sup>−</sup>, is NADH (reduced nicotinamide adenine dinucleotide). The reduction of NAD<sup>+</sup> to NADH can be written as follows:

Equation 18.53

NAD<sup>+</sup> + H<sup>+</sup> + 2e<sup>−</sup> → NADH

(src-averill-1-0-ch18-s08-s03-f02)=

Figure 18.19 NAD<sup>+</sup> and Its Reduced Form (NADH)

![Figure 18.19 NAD + and Its Reduced Form (NADH)](/images/section_22/3cb8533019a71e9a540d14d7b44576b2.jpg)

This electron carrier is used by biological systems to transfer electrons from one species to another. The oxidized form (NAD<sup>+</sup>) is reduced to NADH by energy-rich nutrients such as glucose, and the reduced form (NADH), is then oxidized to NAD<sup>+</sup> by O<sub>2</sub> during respiration.

Most organisms use NAD<sup>+</sup> to oxidize energy-rich nutrients such as glucose to CO<sub>2</sub> and water; NADH is then oxidized to NAD<sup>+</sup> using an oxidant such as O<sub>2</sub>. During oxidation, a fraction of the energy obtained from the oxidation of the nutrient is stored as ATP. The phosphoric acid anhydride bonds in ATP can then be hydrolyzed by water, releasing energy and forming ADP (adenosine diphosphate). It is through this sequence of reactions that energy from the oxidation of nutrients is made available to cells. Thus ATP has a central role in metabolism: it is synthesized by the oxidation of nutrients, and its energy is then used by cells to drive synthetic reactions and perform work ([Figure 18.20 \"The ATP Cycle\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s08-s03-f03)).

(src-averill-1-0-ch18-s08-s03-f03)=

Figure 18.20 The ATP Cycle

![Figure 18.20 The ATP Cycle](/images/section_22/4d63af61c4222e206af1bbb7ff53a6c5.jpg)

The high-energy phosphoric acid anhydride bond in ATP stores energy released during the oxidation of nutrients. Hydrolysis of the high-energy bond in ATP releases energy, forming adenosine diphosphate (ADP) and phosphate.

Under standard conditions in biochemical reactions, all reactants are present in aqueous concentrations of 1 M at a pressure of 1 atm. For H<sup>+</sup>, this corresponds to a pH of zero, but very little biochemistry occurs at pH = 0. For biochemical reactions, chemists have therefore defined a new standard state in which the H<sup>+</sup> concentration is 1 × 10<sup>−7</sup> M (pH 7.0), and all other reactants and products are present in their usual standard-state conditions (1 M or 1 atm). The free-energy change and corresponding equilibrium constant for a reaction under these new standard conditions are denoted by the addition of a prime sign (′) to the conventional symbol: Δ*G*°′ and *K*′. If protons do not participate in a biological reaction, then Δ*G*°′ = Δ*G*°. Otherwise, the relationship between Δ*G*°′ and Δ*G*° is as follows:

Equation 18.54

Δ*G*°′ = Δ*G*° + *RT* ln(10<sup>−7</sup>)<sup>*n*</sup>

where Δ*G*°′ and Δ*G*° are in kilojoules per mole and *n* is the number of protons produced in the reaction. At 298 K, this simplifies to

Equation 18.55

Δ*G*°′ = Δ*G*° − 39.96*n*

Thus any reaction that involves the release of protons is thermodynamically more favorable at pH 7 than at pH 0.

The chemical equation that corresponds to the hydrolysis of ATP to ADP and phosphate is as follows:

Equation 18.56

$$\left. \text{ATP}^{4 -} + \text{H}_{2}\text{O}\rightleftharpoons\text{ADP}^{3 -} + \text{HPO}_{4}{}^{2 -} + \text{H}^{+} \right.$$

This reaction has a Δ*G*°′ of −34.54 kJ/mol, but under typical physiological (or biochemical) conditions, the actual value of Δ*G*′ for the hydrolysis of ATP is about −50 kJ/mol. Organisms use this energy to drive reactions that are energetically uphill, thereby coupling the reactions to the hydrolysis of ATP. One example is found in the biochemical pathway of *glycolysis*, in which the 6-carbon sugar glucose (C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>) is split into two 3-carbon fragments that are then used as the fuel for the cell. Initially, a phosphate group is added to glucose to form a phosphate ester, glucose-6-phosphate (abbreviated glucose-6-P), in a reaction analogous to that of an alcohol and phosphoric acid:

(src-averill-1-0-ch18-s08-s03-eq05)=

Equation 18.57

$$\begin{array}{llll}
\text{glucose(aq)} & {+ \text{HPO}_{4}{}^{2 -}\text{(aq)}} & \left. \rightleftharpoons\text{glucose-6-P}^{2 -}\text{(aq)} \right. & {+ \text{H}_{2}\text{O(l)}} \\
\text{ROH} & {+ \text{HOPO}_{3}{}^{2 -}} & \left. \rightleftharpoons\text{ROPO}_{3}{}^{2 -} \right. & {+ \text{H}_{2}\text{O}}
\end{array}$$

Due to its electrical charge, the phosphate ester is unable to escape from the cell by diffusing back through the membrane surrounding the cell, ensuring that it remains available for further reactions. For the reaction in [Equation 18.57](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s08-s03-eq05), Δ*G*° is 17.8 kJ/mol and *K* is 7.6 × 10<sup>−4</sup>, indicating that the equilibrium lies far to the left. To force this reaction to occur as written, it is coupled to a thermodynamically favorable reaction, the hydrolysis of ATP to ADP:

$$\begin{array}{rlclcl}
{\text{glucose}\operatorname{~+~}\cancel{\text{HPO}_{4}{}^{2 -}}} & \left. \rightleftharpoons\text{glucose-6-P}^{2 -} + \cancel{\text{H}_{2}\text{O}} \right. & {\Delta G{^\circ}'} & {= 17.8\text{~kJ/mol}} & K_{1} & {= 7.6 \times 10^{- 4}} \\
{\text{ATP}^{4 -} + \cancel{\text{H}_{2}\text{O}}} & \left. \rightleftharpoons\text{ADP}^{3 -} + \cancel{\text{HPO}_{4}{}^{2 -}} + \text{H}^{+} \right. & {\Delta G{^\circ}'} & {= - 34.54\text{~kJ/mol}} & K_{2} & {= 2.2 \times 10^{5}} \\
{\text{glucose}\operatorname{~+~}\text{ATP}^{4 -}} & \left. \rightleftharpoons\text{glucose-6-P}^{2 -} + \text{ADP}^{3 -} + \text{H}^{+} \right. & {\Delta G{^\circ}'} & {= - 16.7\text{~kJ/mol}} & K_{3} & {= 1.7 \times 10^{2}}
\end{array}$$

Thus the formation of glucose-6-phosphate is thermodynamically spontaneous if ATP is used as the source of phosphate.

````````````{important} Note the Pattern

Organisms use energy from the hydrolysis of ATP to drive reactions that are thermodynamically nonspontaneous.

````````````

The formation of glucose-6-phosphate is only one of many examples of how cells use ATP to drive an otherwise nonspontaneous biochemical reaction. Under nonstandard physiological conditions, each ATP hydrolyzed actually results in approximately a 10<sup>8</sup> increase in the magnitude of the equilibrium constant, compared with the equilibrium constant of the reaction in the absence of ATP. Thus a reaction in which two ATP molecules are converted to ADP increases *K* by about 10<sup>16</sup>, three ATP molecules by 10<sup>24</sup>, and so forth. Virtually any energetically unfavorable reaction or sequence of reactions can be made to occur spontaneously by coupling it to the hydrolysis of a sufficiently large number of ATP molecules.

### Energy Storage in Cells

Although all organisms use ATP as the *immediate* free-energy source in biochemical reactions, ATP is not an efficient form in which to store energy on a long-term basis. If the caloric intake of an average resting adult human were stored as ATP, two-thirds of the body weight would have to consist of ATP. Instead, a typical 70 kg adult human has a total of only about 50 g of both ATP and ADP, and, far from being used for long-term storage, each molecule of ATP is turned over about 860 times per day. The entire ATP supply would be exhausted in less than 2 minutes if it were not continuously regenerated.

How does the body store energy for the eventual production of ATP? Three primary means are as sugars, proteins, and fats. The combustion of sugars and proteins yields about 17 kJ of energy per gram, whereas the combustion of fats yields more than twice as much energy per gram, about 39 kJ/g. Moreover, sugars and proteins are hydrophilic and contain about 2 g of water per gram of fuel, even in very concentrated form. In contrast, fats are hydrophobic and can be stored in essentially anhydrous form. As a result, organisms can store about six times more energy per gram as fats than in any other form. A typical 70 kg adult human has about 170 kJ of energy in the form of glucose circulating in the blood, about 2600 kJ of energy stored in the muscles and liver as glycogen (a polymeric form of glucose), about 100,000 kJ stored in the form of protein (primarily muscle tissue), and almost 500,000 kJ in the form of fats ([Figure 18.21 \"Percentages of Forms of Energy Storage in Adult Humans\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s08-s04-f01)). Thus fats constitute by far the greatest energy reserve, while accounting for only about 12 kg of the 70 kg body mass. To store this amount of energy in the form of sugars would require a total body mass of about 144 kg, more than half of which would be sugar.

(src-averill-1-0-ch18-s08-s04-f01)=

Figure 18.21 Percentages of Forms of Energy Storage in Adult Humans

![Figure 18.21 Percentages of Forms of Energy Storage in Adult Humans](/images/section_22/78804cc01878ffaaa106267751e3619e.jpg)

An average 70 kg adult stores about 6 × 10<sup>5</sup> kJ of energy in glucose, glycogen, protein, and fats. Fats are the most abundant and most efficient form for storing energy.

### Example 16

Glucose is one form in which the body stores energy.

1.  Calculate Δ*G*°′ for the respiration of glucose to CO<sub>2</sub> and H<sub>2</sub>O using these values of $\Delta G_{\text{f}}^{{^\circ}}$: −910.4 kJ/mol for glucose, −394.4 kJ/mol for CO<sub>2</sub>(g), and −237.1 kJ/mol for H<sub>2</sub>O(l).
2.  Assuming 50% efficiency in the conversion of the released energy to ATP, how many molecules of ATP can be synthesized by the combustion of one molecule of glucose? At 298.15 K, Δ*G*°′ for the hydrolysis of ATP is −34.54 kJ/mol.

**Given:** balanced chemical equation ([Equation 18.50](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s08-s02-eq02)), values of $\Delta G_{\text{f}}^{{^\circ}}$, conversion efficiency, and Δ*G*°′ for hydrolysis of ATP

**Asked for:** Δ*G*°′ for the combustion reaction and the number of molecules of ATP that can be synthesized

**Strategy:**

**A** Using the "products minus reactants" rule, calculate $\Delta G_{\text{rxn}}^{{^\circ}}$ for the respiration reaction.

**B** Multiply the calculated value of $\Delta G_{\text{rxn}}^{{^\circ}}$ by the efficiency to obtain the number of kilojoules available for ATP synthesis. Then divide this value by Δ*G*°′ for the hydrolysis of ATP to find the maximum number of ATP molecules that can be synthesized.

**Solution:**

1.  **A** Protons are not released or consumed in the reaction, so Δ*G*°′ = Δ*G*°. We begin by using the balanced chemical equation in [Equation 18.50](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s08-s02-eq02):

    C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6O<sub>2</sub> → 6CO<sub>2</sub> + 6H<sub>2</sub>O

    From the given values of $\Delta G_{\text{f}}^{{^\circ}}$ (remember that $\Delta G_{\text{f}}^{{^\circ}}$ is zero for an element such as O<sub>2</sub> in its standard state), we can calculate $\Delta G_{\text{rxn}}^{{^\circ}}$:

    $$\begin{aligned}
    {\Delta G_{\text{rxn}}^{{^\circ}}} & {= \sum m\Delta G_{\text{f}}^{{^\circ}}\text{(products)} - \sum n\Delta G_{\text{f}}^{{^\circ}}\text{(reactants)}} \\
     & {= \lbrack 6( - 394.4) + 6( - 237.1)\rbrack - \lbrack( - 910.4) + 0\rbrack} \\
     & {= - 2879\text{~kJ/mol~of~glucose}}
    \end{aligned}$$

2.  **B** If we assume that only 50% of the available energy is used, then about 1440 kJ/mol of glucose is available for ATP synthesis. The value of Δ*G*°′ for the hydrolysis of ATP under biochemical conditions is −34.54 kJ/mol, so in principle an organism could synthesize

    $$\frac{1440\ \cancel{\text{kJ/mol}}\text{~glucose}}{34.54\ \cancel{\text{kJ/mol}}\text{~ATP~~}} = 41.7 \approx 42\text{~ATP/glucose}$$

    Most aerobic organisms actually synthesize about 32 molecules of ATP per molecule of glucose, for an efficiency of about 45%.

Exercise

Some bacteria synthesize methane using the following redox reaction:

CO<sub>2</sub>(g) + 4H<sub>2</sub>(g) → CH<sub>4</sub>(g) + 2H<sub>2</sub>O(g)

1.  Calculate Δ*G*°′ for this reaction using values of $\Delta G_{\text{f}}^{{^\circ}}$ in [Chapter 25 \"Appendix A: Standard Thermodynamic Quantities for Chemical Substances at 25°C\"](/appendices/appendix-a-standard-thermodyna.md#src-averill-1-0-ch96appa).
2.  Calculate how many ATP molecules could be synthesized per mol of CO<sub>2</sub> reduced if the efficiency of the process were 100%.

**Answer:**

1.  −86.6 kJ/mol CO<sub>2</sub>
2.  2.5 ATP/mol CO<sub>2</sub>

````````````{important} Summary

A living cell is a system that is not in equilibrium with its surroundings; it requires a constant input of energy to maintain its nonequilibrium state. Cells maintain a low-entropy state by increasing the entropy of their surroundings. *Aerobic organisms* cannot survive in the absence of O<sub>2</sub>, whereas *anaerobic organisms* can live only in the absence of O<sub>2</sub>. Green plants and algae are *phototrophs*, which extract energy from the environment through a process called **photosynthesis**, the photochemical reduction of CO<sub>2</sub> to a reduced carbon compound. Other species, called *chemotrophs*, extract energy from chemical compounds. One of the main processes chemotrophs use to obtain energy is **respiration**, which is the reverse of photosynthesis. Alternatively, some chemotrophs obtain energy by **fermentation**, in which an organic compound is both the oxidant and the reductant. Intermediates used by organisms to shuttle electrons between the reductant and the oxidant include NAD<sup>+</sup> and NADH. Energy from the oxidation of nutrients is made available to cells through the synthesis of ATP, the energy currency of the cell. Its energy is used by cells to synthesize substances through coupled reactions and to perform work. The body stores energy as sugars, protein, or fats before using it to produce ATP.

````````````

### Conceptual Problem

1.  The tricarboxylic acid (TCA) cycle in aerobic organisms is one of four pathways responsible for the stepwise oxidation of organic intermediates. The final reaction in the TCA cycle has Δ*G*° = 29.7 kJ/mol, so it should not occur spontaneously. Suggest an explanation for why this reaction proceeds in the forward direction in living cells.

### Answer

1.  It is coupled to another reaction that is spontaneous, which drives this reaction forward (Le Châtelier's principle).

## 18.9 End-of-Chapter Material

### Application Problems

*Problems marked with a* ♦ *involve multiple concepts.*

1.  Electric utilities have been exploring thermal energy storage as a potentially attractive energy-storage solution for peak use. Thermal energy is extracted as steam and stored in rock, oil, or water for later conversion to electricity via heat exchangers. Which steps involve heat transfer? Which involve work done?

2.  ♦ During World War II, German scientists developed the first rocket-powered airplane to be flown in combat, the *Messerschmitt 163 Komet*. The *Komet* was powered by the reaction of liquid hydrogen peroxide (H<sub>2</sub>O<sub>2</sub>) and hydrazine (N<sub>2</sub>H<sub>4</sub>) as follows:

    2H<sub>2</sub>O<sub>2</sub>(l) + N<sub>2</sub>H<sub>4</sub>(l) → N<sub>2</sub>(g) + 4H<sub>2</sub>O(g)

    1.  Determine the standard molar enthalpy of reaction.
    2.  What amount of work can be done by the reaction of 1.00 kg of hydrazine with a stoichiometric amount of hydrogen peroxide at 25°C at a constant pressure of 1.00 atm?
    3.  What is the change in internal energy under these conditions?

3.  ♦ During the 1950s, pentaborane-9 was tested as a potential rocket fuel. However, the idea was abandoned when it was discovered that B<sub>2</sub>O<sub>3</sub>, the product of the reaction of pentaborane-9 with O<sub>2</sub>, was an abrasive that destroyed rocket nozzles. The reaction is represented by the equation

    2B<sub>5</sub>H<sub>9</sub>(l) + 12O<sub>2</sub>(g) → 5B<sub>2</sub>O<sub>3</sub>(s) + 9H<sub>2</sub>O(g)

    1.  Determine the standard molar enthalpy of reaction.
    2.  How much work is done against a pressure of 1.0 atm when 50 lb of fuel are allowed to react with sufficient oxygen to cause the reaction to go to completion at 25°C?
    3.  What is Δ*E* for the reaction?

4.  ♦ Polar explorers must be particularly careful to keep their clothes from becoming damp because the resulting heat loss could be fatal. If a polar explorer's clothes absorbed 1.0 kg of water and the clothes dried from the polar wind, what would be the heat loss \[Δ*H*<sub>vap</sub>(H<sub>2</sub>O) = 44 kJ/mol\]? How much glucose must be consumed to make up for this heat loss to prevent death \[Δ*H*<sub>comb</sub>(glucose) = −802 kJ/mol\]?

5.  Propane gas is generally preferred to kerosene as a fuel for stoves in the boating industry because kerosene stoves require more maintenance. Propane, however, is much more flammable than kerosene and imposes an added risk because it is denser than air and can collect in the bottom of a boat and ignite. The complete combustion of propane produces CO<sub>2</sub> gas and H<sub>2</sub>O vapor and has a value of Δ*H* = −2044 kJ/mol at 25°C. What is Δ*E*?

6.  The propane in Problem 5 can be produced from the hydrogenation of propene according to the following reaction: C<sub>3</sub>H<sub>6</sub>(g) + H<sub>2</sub>(g) → C<sub>3</sub>H<sub>8</sub>(g); Δ*H* = −124 kJ/mol. Given that the reaction $\left. \text{H}_{2}\text{(g)} + \frac{1}{2}\text{O}_{2}\text{(g)}\rightarrow\text{H}_{2}\text{O(g)} \right.$ has Δ*H* = −241.8 kJ/mol, what is the

    1.  standard enthalpy of combustion of propene?
    2.  value of Δ*E* for the combustion of propene?

7.  ♦ The anaerobic conversion of sucrose, a sweetening agent, to lactic acid, which is associated with sour milk, can be described as follows:

    $$\left. \underset{\text{sucrose}}{\text{C}_{12}\text{H}_{22}\text{O}_{11} + \text{H}_{2}\text{O}}\rightarrow\underset{\text{lactic~acid}}{4\text{CH}_{3}\text{CH}\left( \text{OH} \right)\text{CO}_{2}\text{H}} \right.$$

    The combustion of sucrose, however, occurs as follows:

    C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>(s) + 12O<sub>2</sub>(g) → 12CO<sub>2</sub>(g) + 11H<sub>2</sub>O(l)

    1.  Which reaction is thermodynamically more favorable---the anaerobic conversion of sucrose to lactic acid or the aerobic oxidation to CO<sub>2</sub> and H<sub>2</sub>O? The values of Δ*H*<sub>f</sub> are as follows: lactic acid, −694.1 kJ/mol; sucrose, −222 kJ/mol; CO<sub>2</sub>, −393.5 kJ/mol; and H<sub>2</sub>O, −285.8 kJ/mol.
    2.  What is Δ*E* for the combustion of 12.0 g of sucrose at normal body temperature (37°C)?

8.  Phosphorus exists as several allotropes, the most common being red, black, and white phosphorus. White phosphorus consists of tetrahedral P<sub>4</sub> molecules and melts at 44.15°C; it is converted to red phosphorus by heating at 400°C for several hours. The chemical differences between red and white phosphorus are considerable: white phosphorus burns in air, whereas red phosphorus is stable; white phosphorus is soluble in organic compounds, whereas red phosphorus is not; white phosphorus melts at 44.15°C, whereas red phosphorus melts at 597°C. If the enthalpy of fusion of white phosphorus is 0.659 kJ/mol, what is its Δ*S*? Black phosphorus is even less reactive than red. Based on this information, which allotrope would you predict to have the highest entropy? the lowest? Why?

9.  ♦ Ruby and sapphire have a common mineral name: corundum (Al<sub>2</sub>O<sub>3</sub>). Although they are crystalline versions of the same compound, the nature of the imperfections determines the identity of the gem. Outline a method for measuring and comparing the entropy of a ruby with the entropy of a sapphire. How would you expect the entropies to compare with the entropy of a perfect corundum crystal?

10. ♦ Tin has two crystalline forms---α and β---represented in the following equilibrium equation:

    $$\underset{\text{gray}}{\alpha\text{-tin}}\overset{18{^\circ}\text{C}}{\rightleftharpoons}\underset{\text{white}}{\beta\text{-tin}}\overset{232{^\circ}\text{C}}{\rightleftharpoons}\text{Sn(l)}$$

    The earliest known tin artifacts were discovered in Egyptian tombs of the 18th dynasty (1580--1350 BC), although archaeologists are surprised that so few tin objects exist from earlier eras. It has been suggested that many early tin objects were either oxidized to a mixture of stannous and stannic oxides or transformed to powdery, gray tin. Sketch a thermodynamic cycle similar to part (b) in [Figure 18.15 \"Two Forms of Elemental Sulfur and a Thermodynamic Cycle Showing the Transition from One to the Other\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18-s04-s02-f01) to show the conversion of liquid tin to gray tin. Then calculate the change in entropy that accompanies the conversion of Sn(l) to α-Sn using the following data: *C*<sub>p</sub>(white) = 26.99, *C*<sub>p</sub>(gray) = 25.77 J/(mol·K), Δ*H*<sub>fus</sub> = 7.0 kJ/mol, Δ*H*<sub>β\ →\ α</sub> = −2.2 kJ/mol.

11. The reaction of SO<sub>2</sub> with O<sub>2</sub> to produce SO<sub>3</sub> has great industrial significance because SO<sub>3</sub> is converted to H<sub>2</sub>SO<sub>4</sub> by reaction with water. Unfortunately, the reaction is also environmentally important because SO<sub>3</sub> from industrial smokestacks is a primary source of acid rain. Δ*H* for the reaction of SO<sub>2</sub> with O<sub>2</sub> to form SO<sub>3</sub> is −23.49 kJ/mol, and Δ*S* is −22.66 J/(mol·K). Does this reaction occur spontaneously at 25°C? Does it occur spontaneously at 800°C assuming no change in Δ*H* and Δ*S*? Why is this reaction usually carried out at elevated temperatures?

12. Pollutants from industrial societies pose health risks to individuals from exposure to metals such as lead, mercury, and cadmium. The biological effects of a toxic metal may be reduced by removing it from the system using a chelating agent, which binds to the metal and forms a complex that is eliminated from the system without causing more damage. In designing a suitable chelating agent, one must be careful, however, because some chelating agents form metal complexes that are more toxic than the metal itself. Both methylamine (CH<sub>3</sub>NH<sub>2</sub>) and ethylenediamine (H<sub>2</sub>NCH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub>, abbreviated en) could, in principle, be used to treat heavy metal poisoning. In the case of cadmium, the reactions are as follows:

    $$\begin{array}{ll}
     & \left. \text{Cd}^{2 +} + 2\text{CH}_{3}\text{NH}_{2}\rightarrow\text{Cd}{(\text{CH}_{3}\text{NH}_{2})}_{2}{}^{2 +} \right. \\
    {\Delta H} & {= - 7.03\text{~kcal/mol,~}\Delta S = - 1.58\text{~cal/}(\text{mol} \cdot \text{K})} \\
     & \left. \text{Cd}^{2 +} + \text{en}\rightarrow\text{Cd(en)}^{2 +} \right. \\
    {\Delta H} & {= - 7.02\text{~kcal/mol,~}\Delta S = 3.15\text{~cal/}(\text{mol} \cdot \text{K})}
    \end{array}$$

    Based strictly on thermodynamic arguments, which would you choose to administer to a patient suffering from cadmium toxicity? Why? Assume a body temperature of 37°C.

13. ♦ Explosive reactions often have a large negative enthalpy change and a large positive entropy change, but the reaction must also be kinetically favorable. For example, the following equation represents the reaction between hydrazine, a rocket propellant, and the oxidizer dinitrogen tetroxide:

    2N<sub>2</sub>H<sub>4</sub>(l) + N<sub>2</sub>O<sub>4</sub>(l) → 4H<sub>2</sub>O(g) + 3N<sub>2</sub>(g) Δ*H*° = −249 kJ/mol, Δ*S*° = 218 J/(mol·K)

    1.  How much free energy is produced from this reaction at 25°C?
    2.  Is the reaction thermodynamically favorable?
    3.  What is *K*?
    4.  This reaction requires thermal ignition. Why?

14. ♦ Cesium, a silvery-white metal used in the manufacture of vacuum tubes, is produced industrially by the reaction of CsCl with CaC<sub>2</sub>:

    2CsCl(l) + CaC<sub>2</sub>(s) → CaCl<sub>2</sub>(l) + 2C(s) + 2Cs(g)

    Compare the free energy produced from this reaction at 25°C and at 1227°C, the temperature at which it is normally run, given these values: $\Delta H_{298\text{~K}}^{{^\circ}}$

    = 32.0 kJ/mol, $\Delta S_{298\text{~K}}^{{^\circ}}$ = 8.0 J/(mol·K); $\Delta H_{1500\text{~K}}^{{^\circ}}$ = −0.6 kJ/mol, $\Delta S_{1500\text{~K}}^{{^\circ}}$ = 3.6 J/(mol·K).

    1.  If you wanted to minimize energy costs in your production facility by reducing the temperature of the reaction, what is the lowest temperature at which products are favored over reactants (assuming the reaction is kinetically favorable at the lower temperature)? Assume Δ*H*° and Δ*S*° vary linearly with temperature.
    2.  What is the ratio *K*<sub>1500\ K</sub>/*K*<sub>298\ K</sub>?

15. Dessicants (drying agents) can often be regenerated by heating, although it is generally not economically worthwhile to do so. A dessicant that is commonly regenerated is CaSO<sub>4</sub>·2H<sub>2</sub>O:

    $$\begin{array}{l}
    \left. \text{CaSO}_{4} \cdot 2\text{H}_{2}\text{O(s)}\rightarrow\text{CaSO}_{4}\text{(s)} + 2\text{H}_{2}\text{O(g)} \right. \\
    {\Delta H_{298\ }^{{^\circ}} = 25.1\text{~kJ/mol,~}\Delta S_{298\ }^{{^\circ}} = 69.3\text{~J/}\left( {\text{mol} \cdot \text{K}} \right)}
    \end{array}$$

    Regeneration is carried out at 250°C.

    1.  What is Δ*G*° for this reaction?
    2.  What is the equilibrium constant at 25°C?
    3.  What is the ratio *K*<sub>250°C</sub>/*K*<sub>25°C</sub>?
    4.  What is the equilibrium constant at 250°C?
    5.  Is regeneration of CaSO<sub>4</sub>(s)·2H<sub>2</sub>O an enthalpy- or entropy-driven process? Explain your answer.

16. The nitrogen triiodide complex with ammonia (NI<sub>3</sub>·NH<sub>3</sub>) is a simple explosive that can be synthesized from common household products. When detonated, it produces N<sub>2</sub> and I<sub>2</sub>. It can be painted on surfaces when wet, but it is shock sensitive when dry (even touching it with a feather can cause an explosion). Do you expect Δ*G* for the explosion reaction to be positive or negative? Why doesn't NI<sub>3</sub>·NH<sub>3</sub> explode spontaneously?

17. Adenosine triphosphate (ATP) contains high-energy phosphate bonds that are used in energy metabolism, coupling energy-yielding and energy-requiring processes. Cleaving a phosphate link by hydrolysis (ATP hydrolysis) can be described by the reaction $\left. \text{ATP~} + \text{~H}_{2}\text{O}\rightleftharpoons\text{ADP} + \text{P}_{\text{i}} + \text{H}^{+}\text{,} \right.$ where P<sub>i</sub> symbolizes phosphate. Glycerol and ATP react to form glycerol-3-phosphate, ADP, and H<sup>+</sup>, with an overall *K* = 6.61 × 10<sup>5</sup> at 37°C. The reaction of glycerol with phosphate to form glycerol-3-phosphate and water has an equilibrium constant of 2.82 × 10<sup>−2</sup>. What is the equilibrium constant for ATP hydrolysis? How much free energy is released from the hydrolysis of ATP?

18. ♦ Consider the biological reduction of molecular nitrogen, for which the following is the minimal reaction stoichiometry under optimal conditions (P<sub>i</sub> = phosphate):

    8H<sup>+</sup> + 8e<sup>−</sup> + N<sub>2</sub> + 16ATP → H<sub>2</sub> + 2NH<sub>3</sub> + 16ADP + 16P<sub>i</sub>

    1.  What is the approximate ratio of *K*<sub>eq</sub> for this reaction and for the same reaction in the absence of ATP?
    2.  Given the fact that at pH 7 both the reaction of protons and electrons to give H<sub>2</sub> and the reaction of H<sub>2</sub> with N<sub>2</sub> to give ammonia are thermodynamically spontaneous (i.e., *K* \>\> 1), suggest a reason that nitrogen-fixing bacteria use such a large energy input to drive a reaction that is already spontaneous.

### Answers

1.  

2.  

3.  1.  −4315 kJ/mol B<sub>5</sub>H<sub>9</sub>
    2.  1340 kJ
    3.  −1.55 × 10<sup>6</sup> kJ per 50 lb of B<sub>5</sub>H<sub>9</sub>

4.  

5.  −2046 kJ/mol

6.  

7.  1.  aerobic conversion
    2.  −268 kJ

8.  

9.  

10. 

11. Yes, the reaction is spontaneous at 25°C, but its rate is *very* slow. The reaction is not spontaneous at 800°C (Δ*G* = 0.82 kJ/mol), but the reaction rate is much greater.

12. 

13. 1.  −314 kJ/mol
    2.  yes
    3.  2.10 × 10<sup>45</sup>
    4.  Ignition is required to overcome the high activation energy to reaction.

14. 

15. 1.  4.4 kJ/mol
    2.  0.17
    3.  78.3
    4.  13
    5.  entropy-driven; Δ*H*° \> 0, so Δ*S*° must be positive for the reaction to be spontaneous.

16. 

17. 2.34 × 10<sup>7</sup>; −43.7 kJ/mol

18. 

[^chem-1]: The study of the interrelationships among heat, work, and the energy content of a system at equilibrium.

[^chem-2]: A property of a system whose magnitude depends on only the present state of the system, not its previous history.

[^chem-3]: A state function that is the sum of the kinetic and potential energies of all a system's components.

[^chem-4]: This is an arbitrary convention and one that is not universally used. Some engineering disciplines are more interested in the work done *on* the surroundings than in the work done *by* the system and therefore use the opposite convention.

[^chem-5]: The energy of the universe is constant: $\Delta E_{\text{universe}}$ = $\Delta E_{\text{system}}$ + $\Delta E_{\text{surroundings}}$ = 0.

[^chem-6]: A state function that is the sum of the system's internal energy $E$ and the product of its pressure $P$ and volume $V\text{:}$ $H = E + PV\text{.}$

[^chem-7]: The degree of disorder in a thermodynamic system, which is directly proportional to the possible number of microstates.

[^chem-8]: A process in which every intermediate state between the extremes is an equilibrium state, regardless of the direction of the change.

[^chem-9]: A process in which the intermediate states between the extremes are not equilibrium states, so change occurs spontaneously in only one direction.

[^chem-10]: The entropy of the universe remains constant in a reversible process, whereas the entropy of the universe increases in an irreversible (spontaneous) process.

[^chem-11]: The entropy of any perfectly ordered, crystalline substance at absolute zero is zero.

[^chem-12]: In practice, chemists determine the absolute entropy of a substance by measuring the molar heat capacity (*C*<sub>p</sub>) as a function of temperature and then plotting the quantity *C*<sub>p</sub>/*T* versus *T*. The *area* under the curve between 0 K and any temperature *T* is the absolute entropy of the substance at *T*.

[^chem-13]: The entropy of 1 mol of a substance at a standard temperature of 298 K.

[^chem-14]: For a review of natural logarithms, see Essential Skills 6 in [Chapter 11 \"Liquids\"](/chapters/ch-11-liquids.md#src-averill-1-0-ch11).

[^chem-15]: A state function that is defined in terms of three other state functions---namely, enthalpy $(H)\text{,}$ entropy $(S),$ and temperature $(T)\text{:}$ $G = H - TS\text{.}$

[^chem-16]: The change in free energy when one substance or a set of substances in their standard states is converted to one or more other sustances, also in their standard states: $\Delta G{^\circ} = \Delta H{^\circ} - T\Delta S{^\circ}\text{.}$

[^chem-17]: The change in free energy that occurs when 1 mol of a substance in its standard state is formed from the component elements in their standard states: $\Delta G{^\circ}_{\text{f}} = \Delta H{^\circ}_{\text{f}} - T\Delta S{^\circ}_{\text{f}}\text{.}$

[^chem-18]: Although we typically use concentrations or pressures in our equilibrium calculations, recall that equilibrium constants are generally expressed as unitless numbers because of the use of activities or fugacities in precise thermodynamic work. Systems that contain gases at high pressures or concentrated solutions that deviate substantially from ideal behavior require the use of fugacities or activities, respectively.

[^chem-19]: The fundamental reaction by which all green plants and algae obtain energy from sunlight in which $\text{CO}_{2}$ is photochemically reduced to a carbon compound such as glucose. Oxygen in water is concurrently oxidized to $\text{O}_{2}\text{.}$

[^chem-20]: A process by which chemotrophs obtain energy from their environment; the overall reaction of respiration is the reverse of photosynthesis. Respiration is the combustion of a carbon compound such as glucose to $\text{CO}_{2}$ and water.

[^chem-21]: A process used by some chemotrophs to obtain energy from their environment; a chemical reaction in which both the oxidant and the reductant are organic compounds.
