(src-averill-1-0-ch19)=

# Chapter 19 Electrochemistry

In oxidation--reduction (redox) reactions, electrons are transferred from one species (the reductant) to another (the oxidant). This transfer of electrons provides a means for converting chemical energy to electrical energy or vice versa. The study of the relationship between electricity and chemical reactions is called electrochemistry[^chem-1], an area of chemistry we introduced in [Chapter 4 \"Reactions in Aqueous Solution\"](/chapters/ch-04-reactions-in-aqueous-solution.md#src-averill-1-0-ch04) and [Chapter 5 \"Energy Changes in Chemical Reactions\"](/chapters/ch-05-energy-changes-in-chemical-rea.md#src-averill-1-0-ch05). In this chapter, we describe electrochemical reactions in more depth and explore some of their applications.

In the first three sections, we review redox reactions; describe how they can be used to generate an electrical potential, or *voltage*; and discuss factors that affect the magnitude of the potential. We then explore the relationships among the electrical potential, the change in free energy, and the equilibrium constant for a redox reaction, which are all measures of the thermodynamic driving force for a reaction. Finally, we examine two kinds of applications of electrochemical principles: (1) those in which a spontaneous reaction is used to provide electricity and (2) those in which electrical energy is used to drive a thermodynamically nonspontaneous reaction. By the end of this chapter, you will understand why different kinds of batteries are used in cars, flashlights, cameras, and portable computers; how rechargeable batteries operate; and why corrosion occurs and how to slow---if not prevent---it. You will also discover how metal objects can be plated with silver or chromium for protection; how silver polish removes tarnish; and how to calculate the amount of electricity needed to produce aluminum, chlorine, copper, and sodium on an industrial scale.

![A view from the top of the Statue of Liberty, showing the green patina coating the statue. The patina is formed by corrosion of the copper skin of the statue, which forms a thin layer of an insoluble compound that contains copper(II), sulfate, and hydroxide ions.](/images/section_23/ae04f36c0ee23bf0beb5f1069d60783b.jpg)

**A view from the top of the Statue of Liberty, showing the green patina coating the statue.** The patina is formed by corrosion of the copper skin of the statue, which forms a thin layer of an insoluble compound that contains copper(II), sulfate, and hydroxide ions.

## 19.1 Describing Electrochemical Cells

````````````{note} Learning Objective

1.  To distinguish between galvanic and electrolytic cells.

````````````

In any electrochemical process, electrons flow from one chemical substance to another, driven by an oxidation--reduction (redox) reaction. As we described in [Chapter 3 \"Chemical Reactions\"](/chapters/ch-03-chemical-reactions.md#src-averill-1-0-ch03), a redox reaction occurs when electrons are transferred from a substance that is oxidized to one that is being reduced. The reductant[^chem-2] is the substance that loses electrons and is oxidized in the process; the oxidant[^chem-3] is the species that gains electrons and is reduced in the process. The associated potential energy is determined by the potential difference between the valence electrons in atoms of different elements. (For more information on valence electrons, see [Chapter 7 \"The Periodic Table and Periodic Trends\"](/chapters/ch-07-the-periodic-table-and-periodi.md#src-averill-1-0-ch07), [Section 7.3 \"Energetics of Ion Formation\"](/chapters/ch-07-the-periodic-table-and-periodi.md#src-averill-1-0-ch07-s03).)

Because it is impossible to have a reduction without an oxidation and vice versa, a redox reaction can be described as two half-reactions[^chem-4], one representing the oxidation process and one the reduction process. For the reaction of zinc with bromine, the overall chemical reaction is as follows:

(src-averill-1-0-ch19-s01-eq01)=

Equation 19.1

Zn(s) + Br<sub>2</sub>(aq) → Zn<sup>2+</sup>(aq) + 2Br<sup>−</sup>(aq)

The half-reactions are as follows:

Equation 19.2

reduction half-reaction: Br<sub>2</sub>(aq) + 2e<sup>−</sup> → 2Br<sup>−</sup>(aq)

Equation 19.3

oxidation half-reaction: Zn(s) → Zn<sup>2+</sup>(aq) + 2e<sup>−</sup>

Each half-reaction is written to show what is actually occurring in the system; Zn is the reductant in this reaction (it loses electrons), and Br<sub>2</sub> is the oxidant (it gains electrons). Adding the two half-reactions gives the overall chemical reaction ([Equation 19.1](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s01-eq01)). A redox reaction is balanced when *the number of electrons lost by the reductant equals the number of electrons gained by the oxidant*. Like any balanced chemical equation, the overall process is electrically neutral; that is, the net charge is the same on both sides of the equation.

````````````{important} Note the Pattern

In any redox reaction, the number of electrons lost by the reductant equals the number of electrons gained by the oxidant.

````````````

In most of our discussions of chemical reactions, we have assumed that the reactants are in intimate physical contact with one another. Acid--base reactions, for example, are usually carried out with the acid and the base dispersed in a single phase, such as a liquid solution. With redox reactions, however, it is possible to physically separate the oxidation and reduction half-reactions in space, as long as there is a complete circuit, including an external electrical connection, such as a wire, between the two half-reactions. As the reaction progresses, the electrons flow from the reductant to the oxidant over this electrical connection, producing an electric current that can be used to do work. An apparatus that is used to generate electricity from a spontaneous redox reaction or, conversely, that uses electricity to drive a nonspontaneous redox reaction is called an electrochemical cell[^chem-5].

There are two types of electrochemical cells: galvanic cells and electrolytic cells. A galvanic (voltaic) cell[^chem-6][^chem-7] uses the energy released during a spontaneous redox reaction (Δ*G* \< 0) to *generate* electricity. This type of electrochemical cell is often called a *voltaic cell* after its inventor, the Italian physicist Alessandro Volta (1745--1827). In contrast, an electrolytic cell[^chem-8] *consumes* electrical energy from an external source, using it to cause a nonspontaneous redox reaction to occur (Δ*G* \> 0). Both types contain two electrodes[^chem-9], which are solid metals connected to an external circuit that provides an electrical connection between the two parts of the system ([Figure 19.1 \"Electrochemical Cells\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s01-f01)). The oxidation half-reaction occurs at one electrode (the anode[^chem-10]), and the reduction half-reaction occurs at the other (the cathode[^chem-11]). When the circuit is closed, electrons flow from the anode to the cathode. The electrodes are also connected by an *electrolyte*, an ionic substance or solution that allows ions to transfer between the electrode compartments, thereby maintaining the system's electrical neutrality. In this section, we focus on reactions that occur in galvanic cells. We discuss electrolytic cells in [Section 19.7 \"Electrolysis\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07).

(src-averill-1-0-ch19-s01-f01)=

Figure 19.1 Electrochemical Cells

![Figure 19.1 Electrochemical Cells](/images/section_23/6e3746e90855da01a5790e5f329b359c.jpg)

A galvanic cell (left) transforms the energy released by a spontaneous redox reaction into electrical energy that can be used to perform work. The oxidative and reductive half-reactions usually occur in separate compartments that are connected by an external electrical circuit; in addition, a second connection that allows ions to flow between the compartments (shown here as a vertical dashed line to represent a porous barrier) is necessary to maintain electrical neutrality. The potential difference between the electrodes (voltage) causes electrons to flow from the reductant to the oxidant through the external circuit, generating an electric current. In an electrolytic cell (right), an external source of electrical energy is used to generate a potential difference between the electrodes that forces electrons to flow, driving a nonspontaneous redox reaction; only a single compartment is employed in most applications. In both kinds of electrochemical cells, the anode is the electrode at which the oxidation half-reaction occurs, and the cathode is the electrode at which the reduction half-reaction occurs.

(src-averill-1-0-ch19-s01-s01)=

### Galvanic (Voltaic) Cells

To illustrate the basic principles of a galvanic cell, let's consider the reaction of metallic zinc with cupric ion (Cu<sup>2+</sup>) to give copper metal and Zn<sup>2+</sup> ion. The balanced chemical equation is as follows:

Equation 19.4

Zn(s) + Cu<sup>2+</sup>(aq) → Zn<sup>2+</sup>(aq) + Cu(s)

We can cause this reaction to occur by inserting a zinc rod into an aqueous solution of copper(II) sulfate. As the reaction proceeds, the zinc rod dissolves, and a mass of metallic copper forms ([Figure 19.2 \"The Reaction of Metallic Zinc with Aqueous Copper(II) Ions in a Single Compartment\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s01-s01-f01)). These changes occur spontaneously, but all the energy released is in the form of heat rather than in a form that can be used to do work.

(src-averill-1-0-ch19-s01-s01-f01)=

Figure 19.2 The Reaction of Metallic Zinc with Aqueous Copper(II) Ions in a Single Compartment

![A zinc strip stands in blue copper(II) sulfate solution in one beaker and becomes coated with fine black copper particles. A particle view shows zinc atoms leaving as zinc ions while copper(II) ions gain electrons directly at the zinc surface and deposit as copper.](/images/replacements/fig-19-02-zinc-copper-sulfate.svg)

When a zinc rod is inserted into a beaker that contains an aqueous solution of copper(II) sulfate, a spontaneous redox reaction occurs: the zinc electrode dissolves to give Zn<sup>2+</sup>(aq) ions, while Cu<sup>2+</sup>(aq) ions are simultaneously reduced to metallic copper. The reaction occurs so rapidly that the copper is deposited as very fine particles that appear black, rather than the usual reddish color of copper.

*Diagram credit:* original diagram for this edition ([CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)).

This same reaction can be carried out using the galvanic cell illustrated in part (a) in [Figure 19.3 \"The Reaction of Metallic Zinc with Aqueous Copper(II) Ions in a Galvanic Cell\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s01-s01-f02). To assemble the cell, a copper strip is inserted into a beaker that contains a 1 M solution of Cu<sup>2+</sup> ions, and a zinc strip is inserted into a different beaker that contains a 1 M solution of Zn<sup>2+</sup> ions. The two metal strips, which serve as electrodes, are connected by a wire, and the compartments are connected by a salt bridge[^chem-12], a U-shaped tube inserted into both solutions that contains a concentrated liquid or gelled electrolyte. The ions in the salt bridge are selected so that they do not interfere with the electrochemical reaction by being oxidized or reduced themselves or by forming a precipitate or complex; commonly used cations and anions are Na<sup>+</sup> or K<sup>+</sup> and NO<sub>3</sub><sup>−</sup> or SO<sub>4</sub><sup>2−</sup>, respectively. (The ions in the salt bridge do *not* have to be the same as those in the redox couple in either compartment.) When the circuit is closed, a spontaneous reaction occurs: zinc metal is oxidized to Zn<sup>2+</sup> ions at the zinc electrode (the anode), and Cu<sup>2+</sup> ions are reduced to Cu metal at the copper electrode (the cathode). As the reaction progresses, the zinc strip dissolves, and the concentration of Zn<sup>2+</sup> ions in the Zn<sup>2+</sup> solution increases; simultaneously, the copper strip gains mass, and the concentration of Cu<sup>2+</sup> ions in the Cu<sup>2+</sup> solution decreases (part (b) in [Figure 19.3 \"The Reaction of Metallic Zinc with Aqueous Copper(II) Ions in a Galvanic Cell\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s01-s01-f02)). Thus we have carried out the same reaction as we did using a single beaker, but this time the oxidative and reductive half-reactions are physically separated from each other. The electrons that are released at the anode flow through the wire, producing an electric current. Galvanic cells therefore transform chemical energy into electrical energy that can then be used to do work.

(src-averill-1-0-ch19-s01-s01-f02)=

Figure 19.3 The Reaction of Metallic Zinc with Aqueous Copper(II) Ions in a Galvanic Cell

![Figure 19.3 The Reaction of Metallic Zinc with Aqueous Copper(II) Ions in a Galvanic Cell](/images/section_23/b45fb1f467be4a8e28df94c7d3af4503.jpg)

\(a\) A galvanic cell can be constructed by inserting a copper strip into a beaker that contains an aqueous 1 M solution of Cu<sup>2+</sup> ions and a zinc strip into a different beaker that contains an aqueous 1 M solution of Zn<sup>2+</sup> ions. The two metal strips are connected by a wire that allows electricity to flow, and the beakers are connected by a salt bridge. When the switch is closed to complete the circuit, the zinc electrode (the anode) is spontaneously oxidized to Zn<sup>2+</sup> ions in the left compartment, while Cu<sup>2+</sup> ions are simultaneously reduced to copper metal at the copper electrode (the cathode). (b) As the reaction progresses, the Zn anode loses mass as it dissolves to give Zn<sup>2+</sup>(aq) ions, while the Cu cathode gains mass as Cu<sup>2+</sup>(aq) ions are reduced to copper metal that is deposited on the cathode.

The electrolyte in the salt bridge serves two purposes: it completes the circuit by carrying electrical charge and maintains electrical neutrality in both solutions by allowing ions to migrate between them. The identity of the salt in a salt bridge is unimportant, as long as the component ions do not react or undergo a redox reaction under the operating conditions of the cell. Without such a connection, the total positive charge in the Zn<sup>2+</sup> solution would increase as the zinc metal dissolves, and the total positive charge in the Cu<sup>2+</sup> solution would decrease. The salt bridge allows charges to be neutralized by a flow of anions into the Zn<sup>2+</sup> solution and a flow of cations into the Cu<sup>2+</sup> solution. In the absence of a salt bridge or some other similar connection, the reaction would rapidly cease because electrical neutrality could not be maintained.

![A zinc electrode in zinc ion solution and a copper electrode in copper(II) ion solution are joined by a wire through a voltmeter and by a salt bridge. Electrons flow through the wire from zinc to copper; in the salt bridge, anions move toward the zinc compartment and cations toward the copper compartment.](/images/replacements/fig-19-galvanic-cell.svg)

**A galvanic cell.** This galvanic cell illustrates the use of a salt bridge to connect two solutions.

*Diagram credit:* original diagram for this edition ([CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)).

A *voltmeter* can be used to measure the difference in electrical potential between the two compartments. Opening the switch that connects the wires to the anode and the cathode prevents a current from flowing, so no chemical reaction occurs. With the switch closed, however, the external circuit is closed, and an electric current can flow from the anode to the cathode. The potential (*E*<sub>cell</sub>)[^chem-13] of the cell, measured in volts, is the difference in electrical potential between the two half-reactions and is related to the energy needed to move a charged particle in an electric field. In the cell we have described, the voltmeter indicates a potential of 1.10 V (part (a) in [Figure 19.3 \"The Reaction of Metallic Zinc with Aqueous Copper(II) Ions in a Galvanic Cell\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s01-s01-f02)). Because electrons from the oxidation half-reaction are released at the anode, the anode in a galvanic cell is negatively charged. The cathode, which attracts electrons, is positively charged.

Not all electrodes undergo a chemical transformation during a redox reaction. The electrode can be made from an inert, highly conducting metal such as platinum to prevent it from reacting during a redox process, where it does not appear in the overall electrochemical reaction. This phenomenon is illustrated in Example 1.

````````````{important} Note the Pattern

A galvanic (voltaic) cell converts the energy released by a spontaneous chemical reaction to electrical energy. An electrolytic cell consumes electrical energy from an external source to drive a nonspontaneous chemical reaction.

````````````

### Example 1

A chemist has constructed a galvanic cell consisting of two beakers. One beaker contains a strip of tin immersed in aqueous sulfuric acid, and the other contains a platinum electrode immersed in aqueous nitric acid. The two solutions are connected by a salt bridge, and the electrodes are connected by a wire. Current begins to flow, and bubbles of a gas appear at the platinum electrode. The spontaneous redox reaction that occurs is described by the following balanced chemical equation:

3Sn(s) + 2NO<sub>3</sub><sup>−</sup>(aq) + 8H<sup>+</sup>(aq) → 3Sn<sup>2+</sup>(aq) + 2NO(g) + 4H<sub>2</sub>O(l)

For this galvanic cell,

1.  write the half-reaction that occurs at each electrode.
2.  indicate which electrode is the cathode and which is the anode.
3.  indicate which electrode is the positive electrode and which is the negative electrode.

**Given:** galvanic cell and redox reaction

**Asked for:** half-reactions, identity of anode and cathode, and electrode assignment as positive or negative

**Strategy:**

**A** Identify the oxidation half-reaction and the reduction half-reaction. Then identify the anode and cathode from the half-reaction that occurs at each electrode.

**B** From the direction of electron flow, assign each electrode as either positive or negative.

**Solution:**

1.  **A** In the reduction half-reaction, nitrate is reduced to nitric oxide. (The nitric oxide would then react with oxygen in the air to form NO<sub>2</sub>, with its characteristic red-brown color.) In the oxidation half-reaction, metallic tin is oxidized. The half-reactions corresponding to the actual reactions that occur in the system are as follows:

    reduction: NO<sub>3</sub><sup>−</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>−</sup> → NO(g) + 2H<sub>2</sub>O(l) oxidation: Sn(s) → Sn<sup>2+</sup>(aq) + 2e<sup>−</sup>

    Thus nitrate is reduced to NO, while the tin electrode is oxidized to Sn<sup>2+</sup>.

2.  Because the reduction reaction occurs at the Pt electrode, it is the cathode. Conversely, the oxidation reaction occurs at the tin electrode, so it is the anode.

3.  **B** Electrons flow from the tin electrode through the wire to the platinum electrode, where they transfer to nitrate. The electric circuit is completed by the salt bridge, which permits the diffusion of cations toward the cathode and anions toward the anode. Because electrons flow *from* the tin electrode, it must be electrically negative. In contrast, electrons flow *toward* the Pt electrode, so that electrode must be electrically positive.

Exercise

Consider a simple galvanic cell consisting of two beakers connected by a salt bridge. One beaker contains a solution of MnO<sub>4</sub><sup>−</sup> in dilute sulfuric acid and has a Pt electrode. The other beaker contains a solution of Sn<sup>2+</sup> in dilute sulfuric acid, also with a Pt electrode. When the two electrodes are connected by a wire, current flows and a spontaneous reaction occurs that is described by the following balanced chemical equation:

2MnO<sub>4</sub><sup>−</sup>(aq) + 5Sn<sup>2+</sup>(aq) + 16H<sup>+</sup>(aq) → 2Mn<sup>2+</sup>(aq) + 5Sn<sup>4+</sup>(aq) + 8H<sub>2</sub>O(l)

For this galvanic cell,

1.  write the half-reaction that occurs at each electrode.
2.  indicate which electrode is the cathode and which is the anode.
3.  indicate which electrode is positive and which is negative.

**Answer:**

1.  MnO<sub>4</sub><sup>−</sup>(aq) + 8H<sup>+</sup>(aq) + 5e<sup>−</sup> → Mn<sup>2+</sup>(aq) + 4H<sub>2</sub>O(l); Sn<sup>2+</sup>(aq) → Sn<sup>4+</sup>(aq) + 2e<sup>−</sup>
2.  The Pt electrode in the permanganate solution is the cathode; the one in the tin solution is the anode.
3.  The cathode (electrode in beaker that contains the permanganate solution) is positive, and the anode (electrode in beaker that contains the tin solution) is negative.

### Constructing a Cell Diagram

Because it is somewhat cumbersome to describe any given galvanic cell in words, a more convenient notation has been developed. In this line notation, called a *cell diagram*, the identity of the electrodes and the chemical contents of the compartments are indicated by their chemical formulas, with the anode written on the far left and the cathode on the far right. Phase boundaries are shown by single vertical lines, and the salt bridge, which has two phase boundaries, by a double vertical line. Thus the cell diagram for the Zn/Cu cell shown in part (a) in [Figure 19.3 \"The Reaction of Metallic Zinc with Aqueous Copper(II) Ions in a Galvanic Cell\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s01-s01-f02) is written as follows:

Figure 19.4

![Figure 19.4](/images/section_23/ad967decb98fbe3ead0614b0f65194c4.jpg)

 

A cell diagram includes solution concentrations when they are provided.

Galvanic cells can have arrangements other than the examples we have seen so far. For example, the voltage produced by a redox reaction can be measured more accurately using two electrodes immersed in a single beaker containing an electrolyte that completes the circuit. This arrangement reduces errors caused by resistance to the flow of charge at a boundary, called the *junction potential*. One example of this type of galvanic cell is as follows:

Equation 19.5

Pt(s)∣H<sub>2</sub>(g)∣HCl(aq)∣AgCl(s)∣Ag(s)

This cell diagram does not include a double vertical line representing a salt bridge because there is no salt bridge providing a junction between two dissimilar solutions. Moreover, solution concentrations have not been specified, so they are not included in the cell diagram. The half-reactions and the overall reaction for this cell are as follows:

Equation 19.6

cathode reaction: AgCl(s) + e<sup>−</sup> → Ag(s) + Cl<sup>−</sup>(aq)

Equation 19.7

$$\left. \text{anode~reaction:~}\frac{1}{2}\text{H}_{2}\text{(g)}\rightarrow\text{H}^{+}\text{(aq)} + \text{e}^{-} \right.$$

Equation 19.8

$$\text{overall:~}\left. \text{AgCl(s)~} + \ \frac{1}{2}\text{H}_{2}\text{(g)}\rightarrow\text{Ag(s)} + \text{Cl}^{-}\text{(aq)} + \text{H}^{+}\text{(aq)} \right.$$

A single-compartment galvanic cell will initially exhibit the same voltage as a galvanic cell constructed using separate compartments, but it will discharge rapidly because of the direct reaction of the reactant at the anode with the oxidized member of the cathodic redox couple. Consequently, cells of this type are not particularly useful for producing electricity.

### Example 2

Draw a cell diagram for the galvanic cell described in Example 1. The balanced chemical reaction is as follows:

3Sn(s) + 2NO<sub>3</sub><sup>−</sup>(aq) + 8H<sup>+</sup>(aq) → 3Sn<sup>2+</sup>(aq) + 2NO(g) + 4H<sub>2</sub>O(l)

**Given:** galvanic cell and redox reaction

**Asked for:** cell diagram

**Strategy:**

Using the symbols described, write the cell diagram beginning with the oxidation half-reaction on the left.

**Solution:**

The anode is the tin strip, and the cathode is the Pt electrode. Beginning on the left with the anode, we indicate the phase boundary between the electrode and the tin solution by a vertical bar. The anode compartment is thus Sn(s)∣Sn<sup>2+</sup>(aq). We could include H<sub>2</sub>SO<sub>4</sub>(aq) with the contents of the anode compartment, but the sulfate ion (as HSO<sub>4</sub><sup>−</sup>) does not participate in the overall reaction, so it does not need to be specifically indicated. The cathode compartment contains aqueous nitric acid, which does participate in the overall reaction, together with the product of the reaction (NO) and the Pt electrode. These are written as HNO<sub>3</sub>(aq)∣NO(g)∣Pt(s), with single vertical bars indicating the phase boundaries. Combining the two compartments and using a double vertical bar to indicate the salt bridge,

Sn(s)∣Sn<sup>2+</sup>(aq)∥HNO<sub>3</sub>(aq)∣NO(g)∣Pt(s)

The solution concentrations were not specified, so they are not included in this cell diagram.

Exercise

Draw a cell diagram for the following reaction, assuming the concentration of Ag<sup>+</sup> and Mg<sup>2+</sup> are each 1 M:

Mg(s) + 2Ag<sup>+</sup>(aq) → Mg<sup>2+</sup>(aq) + 2Ag(s)

**Answer:** Mg(s)∣Mg<sup>2+</sup>(aq, 1 M)∥Ag<sup>+</sup>(aq, 1 M)∣Ag(s)

````````````{important} Summary

**Electrochemistry** is the study of the relationship between electricity and chemical reactions. The oxidation--reduction reaction that occurs during an electrochemical process consists of two **half-reactions**, one representing the oxidation process and one the reduction process. The sum of the half-reactions gives the overall chemical reaction. The overall redox reaction is balanced when the number of electrons lost by the **reductant** equals the number of electrons gained by the **oxidant**. An electric current is produced from the flow of electrons from the reductant to the oxidant. An **electrochemical cell** can either generate electricity from a spontaneous redox reaction or consume electricity to drive a nonspontaneous reaction. In a **galvanic (voltaic) cell**, the energy from a spontaneous reaction generates electricity, whereas in an **electrolytic cell**, electrical energy is consumed to drive a nonspontaneous redox reaction. Both types of cells use two **electrodes** that provide an electrical connection between systems that are separated in space. The oxidative half-reaction occurs at the **anode**, and the reductive half-reaction occurs at the **cathode**. A **salt bridge** connects the separated solutions, allowing ions to migrate to either solution to ensure the system's electrical neutrality. A voltmeter is a device that measures the flow of electric current between two half-reactions. The **potential** of a cell, measured in volts, is the energy needed to move a charged particle in an electric field. An electrochemical cell can be described using line notation called a cell diagram, in which vertical lines indicate phase boundaries and the location of the salt bridge. Resistance to the flow of charge at a boundary is called the junction potential.

````````````

````````````{important} Key Takeaway

- A galvanic (voltaic) cell uses the energy released during a spontaneous redox reaction to generate electricity, whereas an electrolytic cell consumes electrical energy from an external source to force a reaction to occur.

````````````

### Conceptual Problems

1.  Is 2NaOH(aq) + H<sub>2</sub>SO<sub>4</sub>(aq) → Na<sub>2</sub>SO<sub>4</sub>(aq) + 2H<sub>2</sub>O(l) an oxidation--reduction reaction? Why or why not?

2.  If two half-reactions are physically separated, how is it possible for a redox reaction to occur? What is the name of the apparatus in which two half-reactions are carried out simultaneously?

3.  What is the difference between a galvanic cell and an electrolytic cell? Which would you use to generate electricity?

4.  What is the purpose of a salt bridge in a galvanic cell? Is it always necessary to use a salt bridge in a galvanic cell?

5.  One criterion for a good salt bridge is that it contains ions that have similar rates of diffusion in aqueous solution, as K<sup>+</sup> and Cl<sup>−</sup> ions do. What would happen if the diffusion rates of the anions and cations differed significantly?

6.  It is often more accurate to measure the potential of a redox reaction by immersing two electrodes in a single beaker rather than in two beakers. Why?

### Answer

1.  

2.  

3.  

4.  

5.  A large difference in cation/anion diffusion rates would increase resistance in the salt bridge and limit electron flow through the circuit.

6.  

### Numerical Problems

1.  Copper(I) sulfate forms a bright blue solution in water. If a piece of zinc metal is placed in a beaker of aqueous CuSO<sub>4</sub> solution, the blue color fades with time, the zinc strip begins to erode, and a black solid forms around the zinc strip. What is happening? Write half-reactions to show the chemical changes that are occurring. What will happen if a piece of copper metal is placed in a colorless aqueous solution of ZnCl<sub>2</sub>?

2.  Consider the following spontaneous redox reaction: NO<sub>3</sub><sup>−</sup>(aq) + H<sup>+</sup>(aq) + SO<sub>3</sub><sup>2−</sup>(aq) → SO<sub>4</sub><sup>2−</sup>(aq) + HNO<sub>2</sub>(aq).

    1.  Write the two half-reactions for this overall reaction.
    2.  If the reaction is carried out in a galvanic cell using an inert electrode in each compartment, which electrode corresponds to which half-reaction?
    3.  Which electrode is negatively charged, and which is positively charged?

3.  The reaction Pb(s) + 2VO<sup>2+</sup>(aq) + 4H<sup>+</sup>(aq) → Pb<sup>2+</sup>(aq) + 2V<sup>3+</sup>(aq) + 2H<sub>2</sub>O(l) occurs spontaneously.

    1.  Write the two half-reactions for this redox reaction.
    2.  If the reaction is carried out in a galvanic cell using an inert electrode in each compartment, which reaction occurs at the cathode and which occurs at the anode?
    3.  Which electrode is positively charged, and which is negatively charged?

4.  Phenolphthalein is an indicator that turns pink under basic conditions. When an iron nail is placed in a gel that contains \[Fe(CN)<sub>6</sub>\]<sup>3−</sup>, the gel around the nail begins to turn pink. What is occurring? Write the half-reactions and then write the overall redox reaction.

5.  Sulfate is reduced to HS<sup>−</sup> in the presence of glucose, which is oxidized to bicarbonate. Write the two half-reactions corresponding to this process. What is the equation for the overall reaction?

6.  Write the spontaneous half-reactions and the overall reaction for each proposed cell diagram. State which half-reaction occurs at the anode and which occurs at the cathode.

    1.  Pb(s)∣PbSO<sub>4</sub>(s)∣SO<sub>4</sub><sup>2−</sup>(aq)∥Cu<sup>2+</sup>(aq)∣Cu(s)
    2.  Hg(l)∣Hg<sub>2</sub>Cl<sub>2</sub>(s)∣Cl<sup>−</sup>(aq) ∥ Cd<sup>2+</sup>(aq)∣Cd(s)

7.  For each galvanic cell represented by these cell diagrams, determine the spontaneous half-reactions and the overall reaction. Indicate which reaction occurs at the anode and which occurs at the cathode.

    1.  Zn(s)∣Zn<sup>2+</sup>(aq) ∥ H<sup>+</sup>(aq)∣H<sub>2</sub>(g), Pt(s)
    2.  Ag(s)∣AgCl(s)∣Cl<sup>−</sup>(aq) ∥ H<sup>+</sup>(aq)∣H<sub>2</sub>(g)∣Pt(s)
    3.  Pt(s)∣H<sub>2</sub>(g)∣H<sup>+</sup>(aq) ∥ Fe<sup>2+</sup>(aq), Fe<sup>3+</sup>(aq)∣Pt(s)

8.  For each redox reaction, write the half-reactions and draw the cell diagram for a galvanic cell in which the overall reaction occurs spontaneously. Identify each electrode as either positive or negative.

    1.  Ag(s) + Fe<sup>3+</sup>(aq) → Ag<sup>+</sup>(aq) + Fe<sup>2+</sup>(aq)
    2.  Fe<sup>3+</sup>(aq) + 1/2H<sub>2</sub>(g) → Fe<sup>2+</sup>(aq) + H<sup>+</sup>(aq)

9.  Write the half-reactions for each overall reaction, decide whether the reaction will occur spontaneously, and construct a cell diagram for a galvanic cell in which a spontaneous reaction will occur.

    1.  2Cl<sup>−</sup>(aq) + Br<sub>2</sub>(l) → Cl<sub>2</sub>(g) + 2Br<sup>−</sup>(aq)
    2.  2NO<sub>2</sub>(g) + 2OH<sup>−</sup>(aq) → NO<sub>2</sub><sup>−</sup>(aq) + NO<sub>3</sub><sup>−</sup>(aq) + H<sub>2</sub>O(l)
    3.  2H<sub>2</sub>O(l) + 2Cl<sup>−</sup>(aq) → H<sub>2</sub>(g) + Cl<sub>2</sub>(g) + 2OH<sup>−</sup>(aq)
    4.  C<sub>3</sub>H<sub>8</sub>(g) + 5O<sub>2</sub>(g) → 3CO<sub>2</sub>(g) + 4H<sub>2</sub>O(g)

10. Write the half-reactions for each overall reaction, decide whether the reaction will occur spontaneously, and construct a cell diagram for a galvanic cell in which a spontaneous reaction will occur.

    1.  Co(s) + Fe<sup>2+</sup>(aq) → Co<sup>2+</sup>(aq) + Fe(s)
    2.  O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4Fe<sup>2+</sup>(aq) → 2H<sub>2</sub>O(l) + 4Fe<sup>3+</sup>(aq)
    3.  6Hg<sup>2+</sup>(aq) + 2NO<sub>3</sub><sup>−</sup>(aq) + 8H<sup>+</sup> → 3Hg<sub>2</sub><sup>2+</sup>(aq) + 2NO(g) + 4H<sub>2</sub>O(l)
    4.  CH<sub>4</sub>(g) + 2O<sub>2</sub>(g) → CO<sub>2</sub>(g) + 2H<sub>2</sub>O(g)

### Answers

1.  

2.  

3.  

4.  

5.   

    reduction: SO<sub>4</sub><sup>2−</sup>(aq) + 9H<sup>+</sup>(aq) + 8e<sup>−</sup> → HS<sup>−</sup>(aq) + 4H<sub>2</sub>O(l) oxidation: C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>(aq) + 12H<sub>2</sub>O(l) → 6HCO<sub>3</sub><sup>−</sup>(g) + 30H<sup>+</sup>(aq) + 24e<sup>−</sup> overall: C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>(aq) + 3SO<sub>4</sub><sup>2−</sup>(aq) → 6HCO<sub>3</sub><sup>−</sup>(g) + 3H<sup>+</sup>(aq) + 3HS<sup>−</sup>(aq)

6.  

7.  1.  reduction: 2H<sup>+</sup>(aq) + 2e<sup>−</sup> → H<sub>2</sub>(aq); cathode;

        oxidation: Zn(s) → Zn<sup>2+</sup>(aq) + 2e<sup>−</sup>; anode;

        overall: Zn(s) + 2H<sup>+</sup>(aq) → Zn<sup>2+</sup>(aq) + H<sub>2</sub>(aq)

    2.  reduction: AgCl(s) + e<sup>−</sup> → Ag(s) + Cl<sup>−</sup>(aq); cathode;

        oxidation: H<sub>2</sub>(g) → 2H<sup>+</sup>(aq) + 2e<sup>−</sup>; anode;

        overall: AgCl(s) + H<sub>2</sub>(g) → 2H<sup>+</sup>(aq) + Ag(s) + Cl<sup>−</sup>(aq)

    3.  reduction: Fe<sup>3+</sup>(aq) + e<sup>−</sup> → Fe<sup>2+</sup>(aq); cathode;

        oxidation: H<sub>2</sub>(g) → 2H<sup>+</sup>(aq) + 2e<sup>−</sup>; anode;

        overall: 2Fe<sup>3+</sup>(aq) + H<sub>2</sub>(g) → 2H<sup>+</sup>(aq) + 2Fe<sup>2+</sup>(aq)

8.  

9.  

10. 

(src-averill-1-0-ch19-s02)=

## 19.2 Standard Potentials

````````````{note} Learning Objectives

1.  To use redox potentials to predict whether a reaction is spontaneous.
2.  To balance redox reactions using half-reactions.

````````````

In a galvanic cell, current is produced when electrons flow externally through the circuit from the anode to the cathode because of a difference in potential energy between the two electrodes in the electrochemical cell. In the Zn/Cu system, the valence electrons in zinc have a substantially higher potential energy than the valence electrons in copper because of shielding of the *s* electrons of zinc by the electrons in filled *d* orbitals. (For more information on atomic orbitals, see [Chapter 6 \"The Structure of Atoms\"](/chapters/ch-06-the-structure-of-atoms.md#src-averill-1-0-ch06), [Section 6.5 \"Atomic Orbitals and Their Energies\"](/chapters/ch-06-the-structure-of-atoms.md#src-averill-1-0-ch06-s05).) Hence electrons flow spontaneously from zinc to copper(II) ions, forming zinc(II) ions and metallic copper ([Figure 19.5 \"Potential Energy Difference in the Zn/Cu System\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-f01)). Just like water flowing spontaneously downhill, which can be made to do work by forcing a waterwheel, the flow of electrons from a higher potential energy to a lower one can also be harnessed to perform work.

(src-averill-1-0-ch19-s02-f01)=

Figure 19.5 Potential Energy Difference in the Zn/Cu System

![Figure 19.5 Potential Energy Difference in the Zn/Cu System](/images/section_23/cb91471e7dff8e2c77249fb7a859291a.jpg)

The potential energy of a system consisting of metallic Zn and aqueous Cu<sup>2+</sup> ions is greater than the potential energy of a system consisting of metallic Cu and aqueous Zn<sup>2+\ ions</sup>. Much of this potential energy difference is because the valence electrons of metallic Zn are higher in energy than the valence electrons of metallic Cu. Because the Zn(s) + Cu<sup>2+</sup>(aq) system is higher in energy by 1.10 V than the Cu(s) + Zn<sup>2+</sup>(aq) system, energy is released when electrons are transferred from Zn to Cu<sup>2+</sup> to form Cu and Zn<sup>2+</sup>.

Because the potential energy of valence electrons differs greatly from one substance to another, the voltage of a galvanic cell depends partly on the identity of the reacting substances. If we construct a galvanic cell similar to the one in part (a) in [Figure 19.3 \"The Reaction of Metallic Zinc with Aqueous Copper(II) Ions in a Galvanic Cell\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s01-s01-f02) but instead of copper use a strip of cobalt metal and 1 M Co<sup>2+</sup> in the cathode compartment, the measured voltage is not 1.10 V but 0.51 V. Thus we can conclude that the difference in potential energy between the valence electrons of cobalt and zinc is less than the difference between the valence electrons of copper and zinc by 0.59 V.

The measured potential of a cell also depends strongly on the *concentrations* of the reacting species and the *temperature* of the system. To develop a scale of relative potentials that will allow us to predict the direction of an electrochemical reaction and the magnitude of the driving force for the reaction, the potentials for oxidations and reductions of different substances must be measured under comparable conditions. To do this, chemists use the standard cell potential[^chem-14] (*E*°<sub>cell</sub>), defined as the potential of a cell measured under standard conditions---that is, with all species in their standard states (1 M for solutions,[^chem-15] 1 atm for gases, pure solids or pure liquids for other substances) and at a fixed temperature, usually 25°C.

````````````{important} Note the Pattern

Measured redox potentials depend on the potential energy of valence electrons, the concentrations of the species in the reaction, and the temperature of the system.

````````````

### Measuring Standard Electrode Potentials

It is physically impossible to measure the potential of a single electrode: only the *difference* between the potentials of two electrodes can be measured. (This is analogous to measuring absolute enthalpies or free energies. Recall from [Chapter 18 \"Chemical Thermodynamics\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18) that only *differences* in enthalpy and free energy can be measured.) We can, however, compare the standard cell potentials for two different galvanic cells that have one kind of electrode in common. This allows us to measure the potential difference between two dissimilar electrodes. For example, the measured standard cell potential (*E*°) for the Zn/Cu system is 1.10 V, whereas *E*° for the corresponding Zn/Co system is 0.51 V. This implies that the potential difference between the Co and Cu electrodes is 1.10 V − 0.51 V = 0.59 V. In fact, that is exactly the potential measured under standard conditions if a cell is constructed with the following cell diagram:

Equation 19.9

$$\text{Co(s)~}\mid \text{~Co}^{\text{2+}}\text{(aq,~1~M)} \parallel \text{Cu}^{\text{2+}}\text{(aq,~1~M)~}\mid \text{~Cu~(s)}\quad E{^\circ} = 0.59\text{~V}$$

This cell diagram corresponds to the oxidation of a cobalt anode and the reduction of Cu<sup>2+</sup> in solution at the copper cathode.

All tabulated values of *standard electrode potentials* by convention are listed for a reaction written as a reduction, not as an oxidation, to be able to compare standard potentials for different substances. (Standard electrode potentials for various reduction reactions are given in [Chapter 29 \"Appendix E: Standard Reduction Potentials at 25°C\"](/appendices/appendix-e-standard-reduction-.md#src-averill-1-0-ch96appe).) The standard cell potential (*E*°<sub>cell</sub>) is therefore the *difference* between the tabulated reduction potentials of the two half-reactions, not their sum:

(src-averill-1-0-ch19-s02-s01-eq02)=

Equation 19.10

*E*°<sub>cell</sub> = *E*°<sub>cathode</sub> − *E*°<sub>anode</sub>

In contrast, recall that half-reactions are written to show the reduction and oxidation reactions that actually occur in the cell, so the overall cell reaction is written as the *sum* of the two half-reactions. According to [Equation 19.10](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s01-eq02), when we know the standard potential for any single half-reaction, we can obtain the value of the standard potential of many other half-reactions by measuring the standard potential of the corresponding cell.

````````````{important} Note the Pattern

The overall cell reaction is the sum of the two half-reactions, but the cell potential is the difference between the reduction potentials: *E*°<sub>cell</sub> = *E*°<sub>cathode</sub> − *E*°<sub>anode</sub>.

````````````

Although it is impossible to measure the potential of any electrode directly, we can choose a reference electrode whose potential is defined as 0 V under standard conditions. The standard hydrogen electrode (SHE)[^chem-16] is universally used for this purpose and is assigned a standard potential of 0 V. It consists of a strip of platinum wire in contact with an aqueous solution containing 1 M H<sup>+</sup>. The \[H<sup>+</sup>\] in solution is in equilibrium with H<sub>2</sub> gas at a pressure of 1 atm at the Pt-solution interface ([Figure 19.6 \"The Standard Hydrogen Electrode\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s01-f01)). Protons are reduced or hydrogen molecules are oxidized at the Pt surface according to the following equation:

Equation 19.11

$$\left. 2\text{H}^{+}\text{(aq)} + 2\text{e}^{-}\rightleftharpoons\text{H}_{2}\text{(g)} \right.$$

One especially attractive feature of the SHE is that the Pt metal electrode is not consumed during the reaction.

(src-averill-1-0-ch19-s02-s01-f01)=

Figure 19.6 The Standard Hydrogen Electrode

![Figure 19.6 The Standard Hydrogen Electrode](/images/section_23/af6801ed39947e4483186d5add6f3e62.jpg)

The SHE consists of platinum wire that is connected to a Pt surface in contact with an aqueous solution containing 1 M H<sup>+</sup> in equilibrium with H<sub>2</sub> gas at a pressure of 1 atm. In the molecular view, the Pt surface catalyzes the oxidation of hydrogen molecules to protons or the reduction of protons to hydrogen gas. (Water is omitted for clarity.) The standard potential of the SHE is arbitrarily assigned a value of 0 V.

[Figure 19.7 \"Determining a Standard Electrode Potential Using a Standard Hydrogen Electrode\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s01-f02) shows a galvanic cell that consists of a SHE in one beaker and a Zn strip in another beaker containing a solution of Zn<sup>2+</sup> ions. When the circuit is closed, the voltmeter indicates a potential of 0.76 V. The zinc electrode begins to dissolve to form Zn<sup>2+</sup>, and H<sup>+</sup> ions are reduced to H<sub>2</sub> in the other compartment. Thus the hydrogen electrode is the cathode, and the zinc electrode is the anode. The diagram for this galvanic cell is as follows:

Equation 19.12

Zn(s)∣Zn<sup>2+</sup>(aq)∥H<sup>+</sup>(aq, 1 M)∣H<sub>2</sub>(g, 1 atm)∣Pt(s)

The half-reactions that actually occur in the cell and their corresponding electrode potentials are as follows:

Equation 19.13

$$\left. \text{cathode:~}2\text{H}^{+}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{H}_{2}\text{(g)}\quad E_{\text{cathode}}^{{^\circ}} = 0\text{~V} \right.$$

Equation 19.14

$$\left. \text{anode:~}Ζ\text{n(s)}\rightarrow Ζ\text{n}^{2 +}\text{(aq)} + 2\text{e}^{-}\quad E_{\text{anode}}^{{^\circ}} = - 0.76\text{~V} \right.$$

Equation 19.15

$$\begin{array}{r}
\left. \text{overall:~}Ζ\text{n(s)} + 2\text{H}^{+}\text{(aq)}\rightarrow Ζ\text{n}^{2 +}\text{(aq)} + \text{H}_{2}\text{(g)} \right. \\
{\quad\quad E_{\text{cell}}^{{^\circ}} = E_{\text{cathode}}^{{^\circ}} - E_{\text{anode}}^{{^\circ}} = 0.76\text{~V}}
\end{array}$$

(src-averill-1-0-ch19-s02-s01-f02)=

Figure 19.7 Determining a Standard Electrode Potential Using a Standard Hydrogen Electrode

![Figure 19.7 Determining a Standard Electrode Potential Using a Standard Hydrogen Electrode](/images/section_23/cd25120da9ca8d305139003206878a7c.jpg)

The voltmeter shows that the standard cell potential of a galvanic cell consisting of a SHE and a Zn/Zn<sup>2+</sup> couple is *E*°<sub>cell</sub> = 0.76 V. Because the zinc electrode in this cell dissolves spontaneously to form Zn<sup>2+</sup>(aq) ions while H<sup>+</sup>(aq) ions are reduced to H<sub>2</sub> at the platinum surface, the standard electrode potential of the Zn<sup>2+</sup>/Zn couple is −0.76 V.

Although the reaction at the anode is an oxidation, by convention its tabulated *E*° value is reported as a *reduction* potential. The potential of a half-reaction measured against the SHE under standard conditions is called the standard electrode potential[^chem-17] for that half-reaction.In this example, the standard reduction potential for Zn<sup>2+</sup>(aq) + 2e<sup>−</sup> → Zn(s) is −0.76 V, which means that the standard electrode potential for the reaction that occurs at the anode, the *oxidation* of Zn to Zn<sup>2+</sup>, often called the Zn/Zn<sup>2+</sup> *redox couple*, or the Zn/Zn<sup>2+</sup> *couple*, is −(−0.76 V) = 0.76 V. We must therefore subtract *E*°<sub>anode</sub> from *E*°<sub>cathode</sub> to obtain *E*°<sub>cell</sub>: 0 − (−0.76 V) = 0.76 V.

Because electrical potential is the energy needed to move a charged particle in an electric field, standard electrode potentials for half-reactions are intensive properties and do not depend on the amount of substance involved. Consequently, *E*° *values are independent of the stoichiometric coefficients for the half-reaction*, and, most important, the coefficients used to produce a balanced overall reaction do not affect the value of the cell potential.

````````````{important} Note the Pattern

*E*° values do not depend on the stoichiometric coefficients for a half-reaction.

````````````

To measure the potential of the Cu/Cu<sup>2+</sup> couple, we can construct a galvanic cell analogous to the one shown in [Figure 19.7 \"Determining a Standard Electrode Potential Using a Standard Hydrogen Electrode\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s01-f02) but containing a Cu/Cu<sup>2+</sup> couple in the sample compartment instead of Zn/Zn<sup>2+</sup>. When we close the circuit this time, the measured potential for the cell is negative (−0.34 V) rather than positive. The negative value of *E*°<sub>cell</sub> indicates that the direction of spontaneous electron flow is the opposite of that for the Zn/Zn<sup>2+</sup> couple. Hence the reactions that occur spontaneously, indicated by a positive *E*°<sub>cell</sub>, are the reduction of Cu<sup>2+</sup> to Cu at the copper electrode. The copper electrode gains mass as the reaction proceeds, and H<sub>2</sub> is oxidized to H<sup>+</sup> at the platinum electrode. In this cell, the copper strip is the *cathode*, and the hydrogen electrode is the *anode*. The cell diagram therefore is written with the SHE on the left and the Cu<sup>2+</sup>/Cu couple on the right:

Equation 19.16

Pt(s)∣H<sub>2</sub>(g, 1 atm)∣H<sup>+</sup>(aq, 1 M)∥Cu<sup>2+</sup>(aq, 1 M)∣Cu(s)

The half-cell reactions and potentials of the spontaneous reaction are as follows:

Equation 19.17

$$\begin{array}{lll}
\text{Cathode:} & \left. \text{Cu}^{2 +}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{~Cu(g)} \right. & {E_{\text{cathode}}^{{^\circ}} = 0.34\text{~V}}
\end{array}$$

Equation 19.18

$$\begin{array}{lll}
\text{Anode:} & \left. \text{H}_{2}\text{(g)}\rightarrow 2\text{H}^{+}\text{(aq)} + 2\text{e}^{-} \right. & {E_{\text{anode}}^{{^\circ}} = 0\text{~V}}
\end{array}$$

Equation 19.19

$$\begin{array}{rc}
\text{Overall:} & \left. \text{H}_{2}\text{(g)} + \text{Cu}^{2 +}\text{(aq)}\rightarrow 2\text{H}^{+}\text{(aq)} + \text{Cu(s)} \right. \\
 & {E_{\text{cell}}^{{^\circ}} = E_{\text{cathode}}^{{^\circ}} - E_{\text{anode}}^{{^\circ}} = 0.34\text{~V}}
\end{array}$$

Thus the standard electrode potential for the Cu<sup>2+</sup>/Cu couple is 0.34 V.

### Balancing Redox Reactions Using the Half-Reaction Method

In [Chapter 4 \"Reactions in Aqueous Solution\"](/chapters/ch-04-reactions-in-aqueous-solution.md#src-averill-1-0-ch04), we described a method for balancing redox reactions using oxidation numbers. Oxidation numbers were assigned to each atom in a redox reaction to identify any changes in the oxidation states. Here we present an alternative approach to balancing redox reactions, the half-reaction method, in which the overall redox reaction is divided into an oxidation half-reaction and a reduction half-reaction, each balanced for mass and charge. This method more closely reflects the events that take place in an electrochemical cell, where the two half-reactions may be physically separated from each other.

We can illustrate how to balance a redox reaction using half-reactions with the reaction that occurs when Drano, a commercial solid drain cleaner, is poured into a clogged drain. Drano contains a mixture of sodium hydroxide and powdered aluminum, which in solution reacts to produce hydrogen gas:

(src-averill-1-0-ch19-s02-s02-eq01)=

Equation 19.20

Al(s) + OH<sup>−</sup>(aq) → Al(OH)<sub>4</sub><sup>−</sup>(aq) + H<sub>2</sub>(g)

In this reaction, Al(s) is oxidized to Al<sup>3+</sup>, and H<sup>+</sup> in water is reduced to H<sub>2</sub> gas, which bubbles through the solution, agitating it and breaking up the clogs.

The overall redox reaction is composed of a reduction half-reaction and an oxidation half-reaction. From the standard electrode potentials listed in [Chapter 29 \"Appendix E: Standard Reduction Potentials at 25°C\"](/appendices/appendix-e-standard-reduction-.md#src-averill-1-0-ch96appe), we find the corresponding half-reactions that describe the reduction of H<sup>+</sup> ions in water to H<sub>2</sub> and the oxidation of Al to Al<sup>3+</sup> in basic solution:

(src-averill-1-0-ch19-s02-s02-eq02)=

Equation 19.21

reduction: 2H<sub>2</sub>O(l) + 2e<sup>−</sup> → 2OH<sup>−</sup>(aq) + H<sub>2</sub>(g)

(src-averill-1-0-ch19-s02-s02-eq03)=

Equation 19.22

oxidation: Al(s) + 4OH<sup>−</sup>(aq) → Al(OH)<sub>4</sub><sup>−</sup>(aq) + 3e<sup>−</sup>

The half-reactions chosen must exactly reflect the reaction conditions, such as the basic conditions shown here. Moreover, the physical states of the reactants and the products must be identical to those given in the overall reaction, whether gaseous, liquid, solid, or in solution.

In [Equation 19.21](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-eq02), two H<sup>+</sup> ions gain one electron each in the reduction; in [Equation 19.22](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-eq03), the aluminum atom loses three electrons in the oxidation. The charges are balanced by multiplying the reduction half-reaction ([Equation 19.21](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-eq02)) by 3 and the oxidation half-reaction ([Equation 19.22](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-eq03)) by 2 to give the same number of electrons in both half-reactions:

Equation 19.23

reduction: 6H<sub>2</sub>O(l) + 6e<sup>−</sup> → 6OH<sup>−</sup>(aq) + 3H<sub>2</sub>(g)

Equation 19.24

oxidation: 2Al(s) + 8OH<sup>−</sup>(aq) → 2Al(OH)<sub>4</sub><sup>−</sup>(aq) + 6e<sup>−</sup>

Adding the two half-reactions,

Equation 19.25

6H<sub>2</sub>O(l) + 2Al(s) + 8OH<sup>−</sup>(aq) → 2Al(OH)<sub>4</sub><sup>−</sup>(aq) + 3H<sub>2</sub>(g) + 6OH<sup>−</sup>(aq)

Simplifying by canceling substances that appear on both sides of the equation,

(src-averill-1-0-ch19-s02-s02-eq07)=

Equation 19.26

6H<sub>2</sub>O(l) + 2Al(s) + 2OH<sup>−</sup>(aq) → 2Al(OH)<sub>4</sub><sup>−</sup>(aq) + 3H<sub>2</sub>(g)

We have a −2 charge on the left side of the equation and a −2 charge on the right side. Thus the charges are balanced, but we must also check that atoms are balanced:

Equation 19.27

2Al + 8O + 14H = 2Al + 8O + 14H

The atoms also balance, so [Equation 19.26](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-eq07) is a balanced chemical equation for the redox reaction depicted in [Equation 19.20](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-eq01).

````````````{important} Note the Pattern

The half-reaction method requires that half-reactions exactly reflect reaction conditions, and the physical states of the reactants and the products must be identical to those in the overall reaction.

````````````

We can also balance a redox reaction by first balancing the atoms in each half-reaction and then balancing the charges. With this alternative method, we do not need to use the half-reactions listed in [Chapter 29 \"Appendix E: Standard Reduction Potentials at 25°C\"](/appendices/appendix-e-standard-reduction-.md#src-averill-1-0-ch96appe) but instead focus on the atoms whose oxidation states change, as illustrated in the following steps:

**Step 1:** Write the reduction half-reaction and the oxidation half-reaction.

For the reaction shown in [Equation 19.20](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-eq01), hydrogen is reduced from H<sup>+</sup> in OH<sup>−</sup> to H<sub>2</sub>, and aluminum is oxidized from Al<sup>0</sup> to Al<sup>3+</sup>:

Equation 19.28

reduction: OH<sup>−</sup>(aq) → H<sub>2</sub>(g)

Equation 19.29

oxidation: Al(s) → Al(OH)<sub>4</sub><sup>−</sup>(aq)

**Step 2:** Balance the atoms by balancing elements other than O and H. Then balance O atoms by adding H<sub>2</sub>O and balance H atoms by adding H<sup>+</sup>.

Elements other than O and H in the previous two equations are balanced as written, so we proceed with balancing the O atoms. We can do this by adding water to the appropriate side of each half-reaction:

Equation 19.30

reduction: OH<sup>−</sup>(aq) → H<sub>2</sub>(g) + H<sub>2</sub>O(l)

Equation 19.31

oxidation: Al(s) + 4H<sub>2</sub>O(l) → Al(OH)<sub>4</sub><sup>−</sup>(aq)

Balancing H atoms by adding H<sup>+</sup>, we obtain the following:

Equation 19.32

reduction: OH<sup>−</sup>(aq) + 3H<sup>+</sup>(aq) → H<sub>2</sub>(g) + H<sub>2</sub>O(l)

Equation 19.33

oxidation: Al(s) + 4H<sub>2</sub>O(l) → Al(OH)<sub>4</sub><sup>−</sup>(aq) + 4H<sup>+</sup>(aq)

We have now balanced the atoms in each half-reaction, but the charges are not balanced.

**Step 3:** Balance the charges in each half-reaction by adding electrons.

Two electrons are gained in the reduction of H<sup>+</sup> ions to H<sub>2</sub>, and three electrons are lost during the oxidation of Al<sup>0</sup> to Al<sup>3+</sup>:

(src-averill-1-0-ch19-s02-s02-eq15)=

Equation 19.34

reduction: OH<sup>−</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>−</sup> → H<sub>2</sub>(g) + H<sub>2</sub>O(l)

(src-averill-1-0-ch19-s02-s02-eq16)=

Equation 19.35

oxidation: Al(s) + 4H<sub>2</sub>O(l) → Al(OH)<sub>4</sub><sup>−</sup>(aq) + 4H<sup>+</sup>(aq) + 3e<sup>−</sup>

**Step 4:** Multiply the reductive and oxidative half-reactions by appropriate integers to obtain the same number of electrons in both half-reactions.

In this case, we multiply [Equation 19.34](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-eq15) (the reductive half-reaction) by 3 and [Equation 19.35](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-eq16) (the oxidative half-reaction) by 2 to obtain the same number of electrons in both half-reactions:

Equation 19.36

reduction: 3OH<sup>−</sup>(aq) + 9H<sup>+</sup>(aq) + 6e<sup>−</sup> → 3H<sub>2</sub>(g) + 3H<sub>2</sub>O(l)

Equation 19.37

oxidation: 2Al(s) + 8H<sub>2</sub>O(l) → 2Al(OH)<sub>4</sub><sup>−</sup>(aq) + 8H<sup>+</sup>(aq) + 6e<sup>−</sup>

**Step 5:** Add the two half-reactions and cancel substances that appear on both sides of the equation.

Adding and, in this case, canceling 8H<sup>+</sup>, 3H<sub>2</sub>O, and 6e<sup>−</sup>,

Equation 19.38

2Al(s) + 5H<sub>2</sub>O(l) + 3OH<sup>−</sup>(aq) + H<sup>+</sup>(aq) → 2Al(OH)<sub>4</sub><sup>−</sup>(aq) + 3H<sub>2</sub>(g)

We have three OH<sup>−</sup> and one H<sup>+</sup> on the left side. Neutralizing the H<sup>+</sup> gives us a total of 5H<sub>2</sub>O + H<sub>2</sub>O = 6H<sub>2</sub>O and leaves 2OH<sup>−</sup> on the left side:

(src-averill-1-0-ch19-s02-s02-eq20)=

Equation 19.39

2Al(s) + 6H<sub>2</sub>O(l) + 2OH<sup>−</sup>(aq) → 2Al(OH)<sub>4</sub><sup>−</sup>(aq) + 3H<sub>2</sub>(g)

**Step 6:** Check to make sure that all atoms and charges are balanced.

[Equation 19.39](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-eq20) is identical to [Equation 19.26](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-eq07), obtained using the first method, so the charges and numbers of atoms on each side of the equation balance.

(src-averill-1-0-ch19-s02-s02-f01)=

Figure 19.8 The Reaction of Dichromate with Iodide

![A yellow sodium dichromate solution and a colorless sodium iodide solution are combined under acidic conditions to give a deep amber mixture containing green chromium(III) and brown iodine. Iodide is oxidized to iodine and chromium is reduced from +6 to +3.](/images/replacements/fig-19-08-dichromate-iodide.svg)

The reaction of a yellow solution of sodium dichromate with a colorless solution of sodium iodide produces a deep amber solution that contains a green Cr<sup>3+</sup>(aq) complex and brown I<sub>2</sub>(aq).

*Diagram credit:* original diagram for this edition ([CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)).

### Example 3

In acidic solution, the redox reaction of dichromate ion (Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>) and iodide (I<sup>−</sup>) can be monitored visually. The yellow dichromate solution reacts with the colorless iodide solution to produce a solution that is deep amber due to the presence of a green Cr<sup>3+</sup>(aq) complex and brown I<sub>2</sub>(aq) ions ([Figure 19.8 \"The Reaction of Dichromate with Iodide\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s02-f01)):

Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>(aq) + I<sup>−</sup>(aq) → Cr<sup>3+</sup>(aq) + I<sub>2</sub>(aq)

Balance this equation using half-reactions.

**Given:** redox reaction and [Chapter 29 \"Appendix E: Standard Reduction Potentials at 25°C\"](/appendices/appendix-e-standard-reduction-.md#src-averill-1-0-ch96appe)

**Asked for:** balanced chemical equation using half-reactions

**Strategy:**

Follow the steps to balance the redox reaction using the half-reaction method.

**Solution:**

From the standard electrode potentials listed in [Chapter 29 \"Appendix E: Standard Reduction Potentials at 25°C\"](/appendices/appendix-e-standard-reduction-.md#src-averill-1-0-ch96appe), we find the half-reactions corresponding to the overall reaction:

reduction: Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>−</sup> → 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l) oxidation: 2I<sup>−</sup>(aq) → I<sub>2</sub>(aq) + 2e<sup>−</sup>

Balancing the number of electrons by multiplying the oxidation reaction by 3,

oxidation: 6I<sup>−</sup>(aq) → 3I<sub>2</sub>(aq) + 6e<sup>−</sup>

Adding the two half-reactions and canceling electrons,

Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>(aq) + 14H<sup>+</sup>(aq) + 6I<sup>−</sup>(aq) → 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l) + 3I<sub>2</sub>(aq)

We must now check to make sure the charges and atoms on each side of the equation balance:

$$\begin{aligned}
{( - 2) + 14 + ( - 6)} & {= + 6} \\
{+ 6} & {= + 6} \\
{2\text{Cr} + 7\text{O} + 14\text{H} + 6\text{I}} & {= 2\text{Cr} + 7\text{O} + 14\text{H} + 6\text{I}}
\end{aligned}$$

The charges and atoms balance, so our equation is balanced.

We can also use the alternative procedure, which does not require the half-reactions listed in [Chapter 29 \"Appendix E: Standard Reduction Potentials at 25°C\"](/appendices/appendix-e-standard-reduction-.md#src-averill-1-0-ch96appe).

**Step 1:** Chromium is reduced from Cr<sup>6+</sup> in Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>to Cr<sup>3+</sup>, and I<sup>−</sup> ions are oxidized to I<sub>2</sub>. Dividing the reaction into two half-reactions,

reduction: Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>(aq) → Cr<sup>3+</sup>(aq) oxidation: I<sup>−</sup>(aq) → I<sub>2</sub>(aq)

**Step 2:** Balancing the atoms other than oxygen and hydrogen,

reduction: Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>(aq) → 2Cr<sup>3+</sup>(aq) oxidation: 2I<sup>−</sup>(aq) → I<sub>2</sub>(aq)

We now balance the O atoms by adding H<sub>2</sub>O---in this case, to the right side of the reduction half-reaction. Because the oxidation half-reaction does not contain oxygen, it can be ignored in this step.

reduction: Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>(aq) → 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l)

Next we balance the H atoms by adding H<sup>+</sup> to the left side of the reduction half-reaction. Again, we can ignore the oxidation half-reaction.

reduction: Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>(aq) + 14H<sup>+</sup>(aq) → + 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l)

**Step 3:** We must now add electrons to balance the charges. The reduction half-reaction (2Cr<sup>+6</sup> to 2Cr<sup>+3</sup>) has a +12 charge on the left and a +6 charge on the right, so six electrons are needed to balance the charge. The oxidation half-reaction (2I<sup>−</sup> to I<sub>2</sub>) has a −2 charge on the left side and a 0 charge on the right, so it needs two electrons to balance the charge:

reduction: Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>−</sup> → 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l) oxidation: 2I<sup>−</sup>(aq) → I<sub>2</sub>(aq) + 2e<sup>−</sup>

**Step 4:** To have the same number of electrons in both half-reactions, we must multiply the oxidation half-reaction by 3:

oxidation: 6I<sup>−</sup>(aq) → 3I<sub>2</sub>(s) + 6e<sup>−</sup>

**Step 5:** Adding the two half-reactions and canceling substances that appear in both reactions,

Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>(aq) + 14H<sup>+</sup>(aq) + 6I<sup>−</sup>(aq) → 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l) + 3I<sub>2</sub>(aq)

**Step 6:** This is the same equation we obtained using the first method. Thus the charges and atoms on each side of the equation balance.

Exercise

Copper is commonly found as the mineral covellite (CuS). The first step in extracting the copper is to dissolve the mineral in nitric acid (HNO<sub>3</sub>), which oxidizes sulfide to sulfate and reduces nitric acid to NO:

CuS(s) + HNO<sub>3</sub>(aq) → NO(g) + CuSO<sub>4</sub>(aq)

Balance this equation using the half-reaction method.

**Answer:** 3CuS(s) + 8HNO<sub>3</sub>(aq) → 8NO(g) + 3CuSO<sub>4</sub>(aq) + 4H<sub>2</sub>O(l)

### Calculating Standard Cell Potentials

The standard cell potential for a redox reaction (*E*°<sub>cell</sub>) is a measure of the tendency of reactants in their standard states to form products in their standard states; consequently, it is a measure of the driving force for the reaction, which earlier we called *voltage*. We can use the two standard electrode potentials we found earlier to calculate the standard potential for the Zn/Cu cell represented by the following cell diagram:

Equation 19.40

Zn(s)∣Zn<sup>2+</sup>(aq, 1 M)∥Cu<sup>2+</sup>(aq, 1 M)∣Cu(s)

We know the values of *E*°<sub>anode</sub> for the reduction of Zn<sup>2+</sup> and *E*°<sub>cathode</sub> for the reduction of Cu<sup>2+</sup>, so we can calculate *E*°<sub>cell</sub>:

Equation 19.41

$$\left. \text{cathode:~Cu}^{2 +}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{Cu(s)}\quad E_{\text{cathode}}^{{^\circ}} = 0.34\text{~V} \right.$$

Equation 19.42

$$\left. \text{anode:~}Ζ\text{n(s)}\rightarrow\text{Zn}^{2 +}\text{(aq,~1~M)} + 2\text{e}^{-}\quad E_{\text{anode}}^{{^\circ}} = - 0.76\text{~V} \right.$$

Equation 19.43

$$\begin{array}{r}
\left. \text{overall:~Zn(s)} + \text{Cu}^{2 +}\text{(aq)}\rightarrow Ζ\text{n}^{2 +}\text{(aq)} + \text{Cu(s)} \right. \\
{\quad\quad E_{\text{cell}}^{{^\circ}} = E_{\text{cathode}}^{{^\circ}} - E_{\text{anode}}^{{^\circ}} = 1.10\text{~V}}
\end{array}$$

This is the same value that is observed experimentally. If the value of *E*°<sub>cell</sub> is positive, the reaction will occur spontaneously as written. If the value of *E*°<sub>cell</sub> is negative, then the reaction is not spontaneous, and it will not occur as written under standard conditions; it will, however, proceed spontaneously in the opposite direction.[^chem-18] Example 4 and its corresponding exercise illustrate how we can use measured cell potentials to calculate standard potentials for redox couples.

````````````{important} Note the Pattern

A positive *E*°<sub>cell</sub> means that the reaction will occur spontaneously as written. A negative *E*°<sub>cell</sub> means that the reaction will proceed spontaneously in the opposite direction.

````````````

### Example 4

A galvanic cell with a measured standard cell potential of 0.27 V is constructed using two beakers connected by a salt bridge. One beaker contains a strip of gallium metal immersed in a 1 M solution of GaCl<sub>3</sub>, and the other contains a piece of nickel immersed in a 1 M solution of NiCl<sub>2</sub>. The half-reactions that occur when the compartments are connected are as follows:

cathode: Ni<sup>2+</sup>(aq) + 2e<sup>−</sup> → Ni(s) anode: Ga(s) → Ga<sup>3+</sup>(aq) + 3e<sup>−</sup>

If the potential for the oxidation of Ga to Ga<sup>3+</sup> is 0.55 V under standard conditions, what is the potential for the oxidation of Ni to Ni<sup>2+</sup>?

**Given:** galvanic cell, half-reactions, standard cell potential, and potential for the oxidation half-reaction under standard conditions

**Asked for:** standard electrode potential of reaction occurring at the cathode

**Strategy:**

**A** Write the equation for the half-reaction that occurs at the anode along with the value of the standard electrode potential for the half-reaction.

**B** Use [Equation 19.10](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s01-eq02) to calculate the standard electrode potential for the half-reaction that occurs at the cathode. Then reverse the sign to obtain the potential for the corresponding oxidation half-reaction under standard conditions.

**Solution:**

**A** We have been given the potential for the oxidation of Ga to Ga<sup>3+</sup> under standard conditions, but to report the standard electrode potential, we must reverse the sign. For the reduction reaction Ga<sup>3+</sup>(aq) + 3e<sup>−</sup> → Ga(s), *E*°<sub>anode</sub> = −0.55 V.

**B** Using the value given for *E*°<sub>cell</sub> and the calculated value of *E*°<sub>anode</sub>, we can calculate the standard potential for the reduction of Ni<sup>2+</sup> to Ni from [Equation 19.10](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s01-eq02):

$$\begin{array}{ll}
E_{\text{cell}}^{{^\circ}} & {= E_{\text{cathode}}^{{^\circ}} - E_{\text{anode}}^{{^\circ}}} \\
{0.27\text{~V}} & {= E_{\text{cathode}}^{{^\circ}} - ( - 0.55\text{~V})} \\
E_{\text{cathode}}^{{^\circ}} & {= - 0.28\text{~V}}
\end{array}$$

This is the standard electrode potential for the reaction Ni<sup>2+</sup>(aq) + 2e<sup>−</sup> → Ni(s). Because we are asked for the potential for the *oxidation* of Ni to Ni<sup>2+</sup> under standard conditions, we must reverse the sign of *E*°<sub>cathode</sub>. Thus *E*° = −(−0.28 V) = 0.28 V for the oxidation. With three electrons consumed in the reduction and two produced in the oxidation, the overall reaction is not balanced. Recall, however, that standard potentials are *independent* of stoichiometry.

Exercise

A galvanic cell is constructed with one compartment that contains a mercury electrode immersed in a 1 M aqueous solution of mercuric acetate \[Hg(CH<sub>3</sub>CO<sub>2</sub>)<sub>2</sub>\] and one compartment that contains a strip of magnesium immersed in a 1 M aqueous solution of MgCl<sub>2</sub>. When the compartments are connected, a potential of 3.22 V is measured and the following half-reactions occur:

cathode: Hg<sup>2+</sup>(aq) + 2e<sup>−</sup> → Hg(l) anode: Mg(s) → Mg<sup>2+</sup>(aq) + 2e<sup>−</sup>

If the potential for the oxidation of Mg to Mg<sup>2+</sup> is 2.37 V under standard conditions, what is the standard electrode potential for the reaction that occurs at the anode?

**Answer:** 0.85 V

### Reference Electrodes and Measuring Concentrations

When using a galvanic cell to measure the concentration of a substance, we are generally interested in the potential of only one of the electrodes of the cell, the so-called indicator electrode[^chem-19], whose potential is related to the concentration of the substance being measured. To ensure that any change in the measured potential of the cell is due to only the substance being analyzed, the potential of the other electrode, the reference electrode[^chem-20], must be constant. You are already familiar with one example of a reference electrode: the SHE. The potential of a reference electrode must be unaffected by the properties of the solution, and if possible, it should be physically isolated from the solution of interest. To measure the potential of a solution, we select a reference electrode and an appropriate indicator electrode. Whether reduction or oxidation of the substance being analyzed occurs depends on the potential of the half-reaction for the substance of interest (the sample) and the potential of the reference electrode.

````````````{important} Note the Pattern

The potential of any reference electrode should not be affected by the properties of the solution to be analyzed, and it should also be physically isolated.

````````````

There are many possible choices of reference electrode other than the SHE. The SHE requires a constant flow of highly flammable hydrogen gas, which makes it inconvenient to use. Consequently, two other electrodes are commonly chosen as reference electrodes. One is the silver--silver chloride electrode[^chem-21], which consists of a silver wire coated with a very thin layer of AgCl that is dipped into a chloride ion solution with a fixed concentration. The cell diagram and reduction half-reaction are as follows:

(src-averill-1-0-ch19-s02-s04-eq01)=

Equation 19.44

$$\begin{array}{r}
{\text{Cl}^{-}\text{(aq)} \mid \text{AgCl(s)} \mid \text{Ag(s)}} \\
\left. \text{AgCl(s)} + \text{e}^{-}\rightarrow\text{Ag(s)} + \text{Cl}^{-}\text{(aq)} \right.
\end{array}$$

If a saturated solution of KCl is used as the chloride solution, the potential of the silver--silver chloride electrode is 0.197 V versus the SHE. That is, 0.197 V must be subtracted from the measured value to obtain the standard electrode potential measured against the SHE.

A second common reference electrode is the saturated calomel electrode (SCE)[^chem-22], which has the same general form as the silver--silver chloride electrode. The SCE consists of a platinum wire inserted into a moist paste of liquid mercury (Hg<sub>2</sub>Cl<sub>2</sub>; called *calomel* in the old chemical literature) and KCl. This interior cell is surrounded by an aqueous KCl solution, which acts as a salt bridge between the interior cell and the exterior solution (part (a) in [Figure 19.9 \"Three Common Types of Electrodes\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s04-f01)). Although it sounds and looks complex, this cell is actually easy to prepare and maintain, and its potential is highly reproducible. The SCE cell diagram and corresponding half-reaction are as follows:

Equation 19.45

Pt(s)∣Hg<sub>2</sub>Cl<sub>2</sub>(s)∣KCl(aq, sat)

Equation 19.46

Hg<sub>2</sub>Cl<sub>2</sub>(s) + 2e<sup>−</sup> → 2Hg(l) + 2Cl<sup>−</sup>(aq)

(src-averill-1-0-ch19-s02-s04-f01)=

Figure 19.9 Three Common Types of Electrodes

![Figure 19.9 Three Common Types of Electrodes](/images/section_23/502acee270b6333872101f77e2093437.jpg)

\(a\) The SCE is a reference electrode that consists of a platinum wire inserted into a moist paste of liquid mercury (calomel; Hg<sub>2</sub>Cl<sub>2</sub>) and KCl. The interior cell is surrounded by an aqueous KCl solution, which acts as a salt bridge between the interior cell and the exterior solution. (b) In a glass electrode, an internal Ag/AgCl electrode is immersed in a 1 M HCl solution that is separated from the sample solution by a very thin glass membrane. The potential of the electrode depends on the H<sup>+</sup> ion concentration of the sample. (c) The potential of an ion-selective electrode depends on the concentration of only a single ionic species in solution.

At 25°C, the potential of the SCE is 0.2415 V versus the SHE, which means that 0.2415 V must be subtracted from the potential versus an SCE to obtain the standard electrode potential.

One of the most common uses of electrochemistry is to measure the H<sup>+</sup> ion concentration of a solution. A glass electrode[^chem-23] is generally used for this purpose, in which an internal Ag/AgCl electrode is immersed in a 0.10 M HCl solution that is separated from the solution by a very thin glass membrane (part (b) in [Figure 19.9 \"Three Common Types of Electrodes\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s04-f01)). The glass membrane absorbs protons, which affects the measured potential. The extent of the adsorption on the inner side is fixed because \[H<sup>+</sup>\] is fixed inside the electrode, but the adsorption of protons on the outer surface depends on the pH of the solution. The potential of the glass electrode depends on \[H<sup>+</sup>\] as follows (recall that pH = −log\[H<sup>+</sup>\]:

Equation 19.47

*E*<sub>glass</sub> = *E*′ + (0.0591 V × log\[H<sup>+</sup>\]) = *E*′ − 0.0591 V × pH

The voltage *E*′ is a constant that depends on the exact construction of the electrode. Although it can be measured, in practice, a glass electrode is *calibrated*; that is, it is inserted into a solution of known pH, and the display on the pH meter is adjusted to the known value. Once the electrode is properly calibrated, it can be placed in a solution and used to determine an unknown pH.

Ion-selective electrodes[^chem-24] are used to measure the concentration of a particular species in solution; they are designed so that their potential depends on only the concentration of the desired species (part (c) in [Figure 19.9 \"Three Common Types of Electrodes\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s04-f01)). These electrodes usually contain an internal reference electrode that is connected by a solution of an electrolyte to a crystalline inorganic material or a membrane, which acts as the sensor. For example, one type of ion-selective electrode uses a single crystal of Eu-doped LaF<sub>3</sub> as the inorganic material. When fluoride ions in solution diffuse to the surface of the solid, the potential of the electrode changes, resulting in a so-called *fluoride electrode*. Similar electrodes are used to measure the concentrations of other species in solution. Some of the species whose concentrations can be determined in aqueous solution using ion-selective electrodes and similar devices are listed in [Table 19.1 \"Some Species Whose Aqueous Concentrations Can Be Measured Using Electrochemical Methods\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s04-t01).

(src-averill-1-0-ch19-s02-s04-t01)=

Table 19.1 Some Species Whose Aqueous Concentrations Can Be Measured Using Electrochemical Methods

````````{list-table}
:header-rows: 1

- - Species
  - Type of Sample
- - H<sup>+</sup>
  - laboratory samples, blood, soil, and ground and surface water
- - NH<sub>3</sub>/NH<sub>4</sub><sup>+</sup>
  - wastewater and runoff water
- - K<sup>+</sup>
  - blood, wine, and soil
- - CO<sub>2</sub>/HCO<sub>3</sub><sup>−</sup>
  - blood and groundwater
- - F<sup>−</sup>
  - groundwater, drinking water, and soil
- - Br<sup>−</sup>
  - grains and plant extracts
- - I<sup>−</sup>
  - milk and pharmaceuticals
- - NO<sub>3</sub><sup>−</sup>
  - groundwater, drinking water, soil, and fertilizer

````````

````````````{important} Summary

The flow of electrons in an electrochemical cell depends on the identity of the reacting substances, the difference in the potential energy of their valence electrons, and their concentrations. The potential of the cell under standard conditions (1 M for solutions, 1 atm for gases, pure solids or liquids for other substances) and at a fixed temperature (25°C) is called the **standard cell potential (***E***°**<sub>**cell**</sub>**)**. Only the *difference* between the potentials of two electrodes can be measured. By convention, all tabulated values of *standard electrode potentials* are listed as standard reduction potentials. The overall cell potential is the reduction potential of the reductive half-reaction minus the reduction potential of the oxidative half-reaction (*E*°<sub>cell</sub> = *E*°<sub>cathode</sub> − *E*°<sub>anode</sub>). The potential of the **standard hydrogen electrode (SHE)** is defined as 0 V under standard conditions. The potential of a half-reaction measured against the SHE under standard conditions is called its **standard electrode potential**. The standard cell potential is a measure of the driving force for a given redox reaction. All *E*° values are independent of the stoichiometric coefficients for the half-reaction. Redox reactions can be balanced using the half-reaction method, in which the overall redox reaction is divided into an oxidation half-reaction and a reduction half-reaction, each balanced for mass and charge. The half-reactions selected from tabulated lists must exactly reflect reaction conditions. In an alternative method, the atoms in each half-reaction are balanced, and then the charges are balanced. Whenever a half-reaction is reversed, the sign of *E*° corresponding to that reaction must also be reversed. If *E*°<sub>cell</sub> is positive, the reaction will occur spontaneously under standard conditions. If *E*°<sub>cell</sub> is negative, then the reaction is not spontaneous under standard conditions, although it will proceed spontaneously in the opposite direction. The potential of an **indicator electrode** is related to the concentration of the substance being measured, whereas the potential of the **reference electrode** is held constant. Whether reduction or oxidation occurs depends on the potential of the sample versus the potential of the reference electrode. In addition to the SHE, other reference electrodes are the **silver--silver chloride electrode**; the **saturated calomel electrode (SCE)**; the **glass electrode**, which is commonly used to measure pH; and **ion-selective electrodes**, which depend on the concentration of a single ionic species in solution. Differences in potential between the SHE and other reference electrodes must be included when calculating values for *E*°.

````````````

````````````{important} Key Takeaways

- Redox reactions can be balanced using the half-reaction method.
- The standard cell potential is a measure of the driving force for the reaction.

````````````

````````````{important} Key Equation

**Standard cell potential**

[Equation 19.10](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s01-eq02): *E*°<sub>cell</sub> = *E*°<sub>cathode</sub>− *E*°<sub>anode</sub>

````````````

### Conceptual Problems

1.  Is a hydrogen electrode chemically inert? What is the major disadvantage to using a hydrogen electrode?

2.  List two factors that affect the measured potential of an electrochemical cell and explain their impact on the measurements.

3.  What is the relationship between electron flow and the potential energy of valence electrons? If the valence electrons of substance A have a higher potential energy than those of substance B, what is the direction of electron flow between them in a galvanic cell?

4.  If the components of a galvanic cell include aluminum and bromine, what is the predicted direction of electron flow? Why?

5.  Write a cell diagram representing a cell that contains the Ni/Ni<sup>2+</sup> couple in one compartment and the SHE in the other compartment. What are the values of *E*°<sub>cathode</sub>, *E*°<sub>anode</sub>, and *E*°<sub>cell</sub>?

6.  Explain why *E*° values are independent of the stoichiometric coefficients in the corresponding half-reaction.

7.  Identify the oxidants and the reductants in each redox reaction.

    1.  Cr(s) + Ni<sup>2+</sup>(aq) → Cr<sup>2+</sup>(aq) + Ni(s)
    2.  Cl<sub>2</sub>(g) + Sn<sup>2+</sup>(aq) → 2Cl<sup>−</sup>(aq) + Sn<sup>4+</sup>(aq)
    3.  H<sub>3</sub>AsO<sub>4</sub>(aq) + 8H<sup>+</sup>(aq) + 4Zn(s) → AsH<sub>3</sub>(g) + 4H<sub>2</sub>O(l) + 4Zn<sup>2+</sup>(aq)
    4.  2NO<sub>2</sub>(g) + 2OH<sup>−</sup>(aq) → NO<sub>2</sub><sup>−</sup>(aq) + NO<sub>3</sub><sup>−</sup>(aq) + H<sub>2</sub>O(l)

8.  Identify the oxidants and the reductants in each redox reaction.

    1.  Br<sub>2</sub>(l) + 2I<sup>−</sup>(aq) → 2Br<sup>−</sup>(aq) + I<sub>2</sub>(s)
    2.  Cu<sup>2+</sup>(aq) + 2Ag(s) → Cu(s) + 2Ag<sup>+</sup>(aq)
    3.  H<sup>+</sup>(aq) + 2MnO<sub>4</sub><sup>−</sup>(aq) + 5H<sub>2</sub>SO<sub>3</sub>(aq) → 2Mn<sup>2+</sup>(aq) + 3H<sub>2</sub>O(l) + 5HSO<sub>4</sub><sup>−</sup>(aq)
    4.  IO<sub>3</sub><sup>−</sup>(aq) + 5I<sup>−</sup>(aq) + 6H<sup>+</sup>(aq) → 3I<sub>2</sub>(s) + 3H<sub>2</sub>O(l)

9.  All reference electrodes must conform to certain requirements. List the requirements and explain their significance.

10. For each application, describe the reference electrode you would use and explain why. In each case, how would the measured potential compare with the corresponding *E*°?

    1.  measuring the potential of a Cl<sup>−</sup>/Cl<sub>2</sub> couple
    2.  measuring the pH of a solution
    3.  measuring the potential of a MnO<sub>4−</sub>/Mn<sup>2+</sup> couple

### Answers

1.  

2.  

3.  

4.  

5.   

    Ni(s)∣Ni<sup>2+</sup>(aq)∥H<sup>+</sup>(aq, 1 M)∣H<sub>2</sub>(g, 1 atm)∣Pt(s) $$\begin{array}{ll}
    E_{\text{anode}}^{{^\circ}} & \left. \text{Ni}^{2 +}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{Ni(s);~} - 0.257\text{~V} \right. \\
    E_{\text{cathode}}^{{^\circ}} & \left. 2\text{H}^{+}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{H}_{2}\text{(g);~0}\text{.000~V} \right. \\
    E_{\text{cell}}^{{^\circ}} & \left. 2\text{H}^{+}\text{(aq)} + \text{Ni(s)}\rightarrow\text{H}_{2}\text{(g)} + \text{Ni}^{2 +}\text{(aq);~0}\text{.257~V} \right.
    \end{array}$$

6.  

7.  1.  oxidant: Ni<sup>2+</sup>(aq); reductant: Cr(s)
    2.  oxidant: Cl<sub>2</sub>(g); reductant: Sn<sup>2+</sup>(aq)
    3.  oxidant: H<sub>3</sub>AsO<sub>4</sub>(aq); reductant: Zn(s)
    4.  oxidant: NO<sub>2</sub>(g); reductant: NO<sub>2</sub>(g)

8.  

9.  

10. 

### Numerical Problems

1.  Draw the cell diagram for a galvanic cell with an SHE and a copper electrode that carries out this overall reaction: H<sub>2</sub>(g) + Cu<sup>2+</sup>(aq) → 2H<sup>+</sup>(aq) + Cu(s).

2.  Draw the cell diagram for a galvanic cell with an SHE and a zinc electrode that carries out this overall reaction: Zn(s) + 2H<sup>+</sup>(aq) → Zn<sup>2+</sup>(aq) + H<sub>2</sub>(g).

3.  Balance each reaction and calculate the standard electrode potential for each. Be sure to include the physical state of each product and reactant.

    1.  Cl<sub>2</sub>(g) + H<sub>2</sub>(g) → 2Cl<sup>−</sup>(aq) + 2H<sup>+</sup>(aq)
    2.  Br<sub>2</sub>(aq) + Fe<sup>2+</sup>(aq) → 2Br<sup>−</sup>(aq) + Fe<sup>3+</sup>(aq)
    3.  Fe<sup>3+</sup>(aq) + Cd(s) → Fe<sup>2+</sup>(aq) + Cd<sup>2+</sup>(aq)

4.  Balance each reaction and calculate the standard reduction potential for each. Be sure to include the physical state of each product and reactant.

    1.  Cu<sup>+</sup>(aq) + Ag<sup>+</sup>(aq) → Cu<sup>2+</sup>(aq) + Ag(s)
    2.  Sn(s) + Fe<sup>3+</sup>(aq) → Sn<sup>2+</sup>(aq) + Fe<sup>2+</sup>(aq)
    3.  Mg(s) + Br<sub>2</sub>(l) → 2Br<sup>−</sup>(aq) + Mg<sup>2+</sup>(aq)

5.  Write a balanced chemical equation for each redox reaction.

    1.  H<sub>2</sub>PO<sub>2</sub><sup>−</sup>(aq) + SbO<sub>2</sub><sup>−</sup>(aq) → HPO<sub>3</sub><sup>2−</sup>(aq) + Sb(s) in basic solution
    2.  HNO<sub>2</sub>(aq) + I<sup>−</sup>(aq) → NO(g) + I<sub>2</sub>(s) in acidic solution
    3.  N<sub>2</sub>O(g) + ClO<sup>−</sup>(aq) → Cl<sup>−</sup>(aq) + NO<sub>2</sub><sup>−</sup>(aq) in basic solution
    4.  Br<sub>2</sub>(l) → Br<sup>−</sup>(aq) + BrO<sub>3</sub><sup>−</sup>(aq) in basic solution
    5.  Cl(CH<sub>2</sub>)<sub>2</sub>OH(aq) + K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub>(aq) → ClCH<sub>2</sub>CO<sub>2</sub>H(aq) + Cr<sup>3+</sup>(aq) in acidic solution

6.  Write a balanced chemical equation for each redox reaction.

    1.  I<sup>−</sup>(aq) + HClO<sub>2</sub>(aq) → IO<sub>3</sub><sup>−</sup>(aq) + Cl<sub>2</sub>(g) in acidic solution
    2.  Cr<sup>2+</sup>(aq) + O<sub>2</sub>(g) → Cr<sup>3+</sup>(aq) + H<sub>2</sub>O(l) in acidic solution
    3.  CrO<sub>2</sub><sup>−</sup>(aq) + ClO<sup>−</sup>(aq) → CrO<sub>4</sub><sup>2−</sup>(aq) + Cl<sup>−</sup>(aq) in basic solution
    4.  S(s) + HNO<sub>2</sub>(aq) → H<sub>2</sub>SO<sub>3</sub>(aq) + N<sub>2</sub>O(g) in acidic solution
    5.  F(CH<sub>2</sub>)<sub>2</sub>OH(aq) + K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub>(aq) → FCH<sub>2</sub>CO<sub>2</sub>H(aq) + Cr<sup>3+</sup>(aq) in acidic solution

7.  The standard cell potential for the oxidation of Pb to Pb<sup>2+</sup> with the concomitant reduction of Cu<sup>+</sup> to Cu is 0.39 V. You know that *E*° for the Pb<sup>2+</sup>/Pb couple is −0.13 V. What is *E*° for the Cu<sup>+</sup>/Cu couple?

8.  You have built a galvanic cell similar to the one in [Figure 19.7 \"Determining a Standard Electrode Potential Using a Standard Hydrogen Electrode\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s01-f02) using an iron nail, a solution of FeCl<sub>2</sub>, and an SHE. When the cell is connected, you notice that the iron nail begins to corrode. What else do you observe? Under standard conditions, what is *E*<sub>cell</sub>?

9.  Carbon is used to reduce iron ore to metallic iron. The overall reaction is as follows:

    2Fe<sub>2</sub>O<sub>3</sub>·*x*H<sub>2</sub>O(s) + 3C(s) → 4Fe(l) + 3CO<sub>2</sub>(g) + 2*x*H<sub>2</sub>O(g)

    Write the two half-reactions for this overall reaction.

10. Will each reaction occur spontaneously under standard conditions?

    1.  Cu(s) + 2H<sup>+</sup>(aq) → Cu<sup>2+</sup>(aq) + H<sub>2</sub>(g)
    2.  Zn<sup>2+</sup>(aq) + Pb(s) → Zn(s) + Pb<sup>2+</sup>(aq)

11. Each reaction takes place in acidic solution. Balance each reaction and then determine whether it occurs spontaneously as written under standard conditions.

    1.  Se(s) + Br<sub>2</sub>(l) → H<sub>2</sub>SeO<sub>3</sub>(aq) + Br<sup>−</sup>(aq)
    2.  NO<sub>3</sub><sup>−</sup>(aq) + S(s) → HNO<sub>2</sub>(aq) + H<sub>2</sub>SO<sub>3</sub>(aq)
    3.  Fe<sup>3+</sup>(aq) + Cr<sup>3+</sup>(aq) → Fe<sup>2+</sup>(aq) + Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>(aq)

12. Calculate *E*°<sub>cell</sub> and Δ*G*° for the redox reaction represented by the cell diagram Pt(s)∣Cl<sub>2</sub>(g, 1 atm)∥ZnCl<sub>2</sub>(aq, 1 M)∣Zn(s). Will this reaction occur spontaneously?

13. If you place Zn-coated (galvanized) tacks in a glass and add an aqueous solution of iodine, the brown color of the iodine solution fades to a pale yellow. What has happened? Write the two half-reactions and the overall balanced chemical equation for this reaction. What is *E*°<sub>cell</sub>?

14. Your lab partner wants to recover solid silver from silver chloride by using a 1.0 M solution of HCl and 1 atm H<sub>2</sub> under standard conditions. Will this plan work?

### Answers

1.  Pt(s)∣H<sub>2</sub>(g, 1 atm) \| H<sup>+</sup>(aq, 1M)∥Cu<sup>2+</sup>(aq)∣Cu(s)

2.  

3.  1.  Cl<sub>2</sub>(g) + H<sub>2</sub>(g) → 2Cl<sup>−</sup>(aq) + 2H<sup>+</sup>(aq); *E*° = 1.358 V
    2.  Br<sub>2</sub>(l) + 2Fe<sup>2+</sup>(aq) → 2Br<sup>−</sup>(aq) + 2Fe<sup>3+</sup>(aq); *E*° = 0.316 V
    3.  2Fe<sup>3+</sup>(aq) + Cd(s) → 2Fe<sup>2+</sup>(aq) + Cd<sup>2+</sup>(aq); *E*° = 1.174 V

4.  

5.  

6.  

7.  

8.  

9.  

10. 

11. 

12. 

13. 

14. 

## 19.3 Comparing Strengths of Oxidants and Reductants

````````````{note} Learning Objective

1.  To know how to predict the relative strengths of various oxidants and reductants.

````````````

We can use the procedure described in [Section 19.2 \"Standard Potentials\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02) to measure the standard potentials for a wide variety of chemical substances, some of which are listed in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01). ([Chapter 29 \"Appendix E: Standard Reduction Potentials at 25°C\"](/appendices/appendix-e-standard-reduction-.md#src-averill-1-0-ch96appe) contains a more extensive listing.) These data allow us to compare the oxidative and reductive strengths of a variety of substances. The half-reaction for the standard hydrogen electrode (SHE) lies more than halfway down the list in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01). All reactants that lie *above* the SHE in the table are stronger oxidants than H<sup>+</sup>, and all those that lie below the SHE are weaker. The strongest oxidant in the table is F<sub>2</sub>, with a standard electrode potential of 2.87 V. This high value is consistent with the high electronegativity of fluorine and tells us that fluorine has a stronger tendency to accept electrons (it is a stronger oxidant) than any other element.

(src-averill-1-0-ch19-s03-t01)=

Table 19.2 Standard Potentials for Selected Reduction Half-Reactions at 25°C

````````{list-table}
:header-rows: 1

- - Half-Reaction
  - *E*° (V)
- - F<sub>2</sub>(g) + 2e<sup>−</sup>→ 2F<sup>−</sup>(aq)
  - 2.87
- - H<sub>2</sub>O<sub>2</sub>(aq) + 2H<sup>+</sup>(aq) + 2e<sup>−</sup> → 2H<sub>2</sub>O(l)
  - 1.78
- - Ce<sup>4+</sup>(aq) + e<sup>−</sup> → Ce<sup>3+</sup>(aq)
  - 1.72
- - PbO<sub>2</sub>(s) + HSO<sub>4</sub><sup>−</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>−</sup> → PbSO<sub>4</sub>(s) + 2H<sub>2</sub>O(l)
  - 1.69
- - Cl<sub>2</sub>(g) + 2e<sup>−</sup> → 2Cl<sup>−</sup>(aq)
  - 1.36
- - Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>(aq) + 14H<sup>+</sup>(aq) + 6e<sup>−</sup> → 2Cr<sup>3+</sup>(aq) + 7H<sub>2</sub>O(l)
  - 1.23
- - O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>−</sup> → 2H<sub>2</sub>O(l)
  - 1.23
- - MnO<sub>2</sub>(s) + 4H<sup>+</sup>(aq) + 2e<sup>−</sup> → Mn<sup>2+</sup>(aq) + 2H<sub>2</sub>O(l)
  - 1.22
- - Br<sub>2</sub>(aq) + 2e<sup>−</sup> → 2Br<sup>−</sup>(aq)
  - 1.09
- - NO<sub>3</sub><sup>−</sup>(aq) + 3H<sup>+</sup>(aq) + 2e<sup>−</sup> → HNO<sub>2</sub>(aq) + H<sub>2</sub>O(l)
  - 0.93
- - Ag<sup>+</sup>(aq) + e<sup>−</sup> → Ag(s)
  - 0.80
- - Fe<sup>3+</sup>(aq) + e<sup>−</sup> → Fe<sup>2+</sup>(aq)
  - 0.77
- - H<sub>2</sub>SeO<sub>3</sub>(aq) + 4H<sup>+</sup> + 4e<sup>−</sup> → Se(s) + 3H<sub>2</sub>O(l)
  - 0.74
- - O<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>−</sup> → H<sub>2</sub>O<sub>2</sub>(aq)
  - 0.70
- - MnO<sub>4</sub><sup>−</sup>(aq) + 2H<sub>2</sub>O(l) + 3e<sup>−</sup> → MnO<sub>2</sub>(s) + 4OH<sup>−</sup>(aq)
  - 0.60
- - MnO<sub>4</sub><sup>2−</sup>(aq) + 2H<sub>2</sub>O(l) + 2e<sup>−</sup> → MnO<sub>2</sub>(s) + 4OH<sup>−</sup>(aq)
  - 0.60
- - I<sub>2</sub>(s) + 2e<sup>−</sup> → 2I<sup>−</sup>(aq)
  - 0.54
- - H<sub>2</sub>SO<sub>3</sub>(aq) + 4H<sup>+</sup>(aq) + 4e<sup>−</sup> → S(s) + 3H<sub>2</sub>O(l)
  - 0.45
- - O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>−</sup> → 4OH<sup>−</sup>(aq)
  - 0.40
- - Cu<sup>2+</sup>(aq) + 2e<sup>−</sup> → Cu(s)
  - 0.34
- - AgCl(s) + e<sup>−</sup> → Ag(s) + Cl<sup>−</sup>(aq)
  - 0.22
- - Cu<sup>2+</sup>(aq) + e<sup>−</sup> → Cu<sup>+</sup>(aq)
  - 0.15
- - Sn<sup>4+</sup>(aq) + 2e<sup>−</sup> → Sn<sup>2+</sup>(aq)
  - 0.15
- - 2H<sup>+</sup>(aq) + 2e<sup>−</sup> → H<sub>2</sub>(g)
  - 0.00
- - Sn<sup>2+</sup>(aq) + 2e<sup>−</sup> → Sn(s)
  - −0.14
- - 2SO<sub>4</sub><sup>2−</sup>(aq) + 4H+(aq) + 2e<sup>−</sup> → S<sub>2</sub>O<sub>6</sub><sup>2−</sup>(aq) + 2H<sub>2</sub>O(l)
  - −0.22
- - Ni<sup>2+</sup>(aq) + 2e<sup>−</sup> → Ni(s)
  - −0.26
- - PbSO<sub>4</sub>(s) + 2e<sup>−</sup> → Pb(s) + SO<sub>4</sub><sup>2−</sup>(aq)
  - −0.36
- - Cd<sup>2+</sup>(aq) + 2e<sup>−</sup> → Cd(s)
  - −0.40
- - Cr<sup>3+</sup>(aq) + e<sup>−</sup> → Cr<sup>2+</sup>(aq)
  - −0.41
- - Fe<sup>2+</sup>(aq) + 2e<sup>−</sup> → Fe(s)
  - −0.45
- - Ag<sub>2</sub>S(s) + 2e<sup>−</sup> → 2Ag(s) + S<sup>2−</sup>(aq)
  - −0.69
- - Zn<sup>2+</sup>(aq) + 2e<sup>−</sup> → Zn(s)
  - −0.76
- - Al<sup>3+</sup>(aq) + 3e<sup>−</sup> → Al(s)
  - −1.662
- - Be<sup>2+</sup>(aq) + 2e<sup>−</sup> → Be(s)
  - −1.85
- - Li<sup>+</sup>(aq) + e<sup>−</sup> → Li(s)
  - −3.04

````````

Similarly, all species in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) that lie *below* H<sub>2</sub> are stronger reductants than H<sub>2</sub>, and those that lie above H<sub>2</sub> are weaker. The strongest reductant in the table is thus metallic lithium, with a standard electrode potential of −3.04 V. This fact might be surprising because cesium, not lithium, is the least electronegative element. The apparent anomaly can be explained by the fact that electrode potentials are measured in aqueous solution, where intermolecular interactions are important, whereas ionization potentials and electron affinities are measured in the gas phase. Due to its small size, the Li<sup>+</sup> ion is stabilized in aqueous solution by strong electrostatic interactions with the negative dipole end of water molecules. These interactions result in a significantly greater Δ*H*<sub>hydration</sub> for Li<sup>+</sup> compared with Cs<sup>+</sup>. Lithium metal is therefore the strongest reductant (most easily oxidized) of the alkali metals in aqueous solution.

````````````{important} Note the Pattern

Species in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) that lie below H<sub>2</sub> are stronger reductants (more easily oxidized) than H<sub>2</sub>. Species that lie above H<sub>2</sub> are stronger oxidants.

````````````

Because the half-reactions shown in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) are arranged in order of their *E*° values, we can use the table to quickly predict the relative strengths of various oxidants and reductants. Any species on the left side of a half-reaction will spontaneously oxidize any species on the right side of another half-reaction that lies *below* it in the table. Conversely, any species on the right side of a half-reaction will spontaneously reduce any species on the left side of another half-reaction that lies *above* it in the table. We can use these generalizations to predict the spontaneity of a wide variety of redox reactions (*E*°<sub>cell</sub> \> 0), as illustrated in Example 5.

![Chemical illustration from Chapter 19: Electrochemistry](/images/section_23/ba414bd42846ac0a34aab2643b08b859.jpg)

### Example 5

The black tarnish that forms on silver objects is primarily Ag<sub>2</sub>S. The half-reaction for reversing the tarnishing process is as follows:

$$\left. \text{Ag}_{\text{2}}\text{S(s)} + \text{2e}^{-}\rightarrow\text{2Ag(s)} + \text{S}^{\text{2} -}\text{(aq)}\quad E{^\circ} = - 0.\text{69~V} \right.$$

1.  Referring to [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01), predict which species---H<sub>2</sub>O<sub>2</sub>(aq), Zn(s), I<sup>−</sup>(aq), Sn<sup>2+</sup>(aq)---can reduce Ag<sub>2</sub>S to Ag under standard conditions.
2.  Of these species---H<sub>2</sub>O<sub>2</sub>(aq), Zn(s), I<sup>−</sup>(aq), Sn<sup>2+</sup>(aq), identify which is the strongest reducing agent in aqueous solution and thus the best candidate for a commercial product.
3.  From the data in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01), suggest an alternative reducing agent that is readily available, inexpensive, and possibly more effective at removing tarnish.

**Given:** reduction half-reaction, standard electrode potential, and list of possible reductants

**Asked for:** reductants for Ag<sub>2</sub>S, strongest reductant, and potential reducing agent for removing tarnish

**Strategy:**

**A** From their positions in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01), decide which species can reduce Ag<sub>2</sub>S. Determine which species is the strongest reductant.

**B** Use [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) to identify a reductant for Ag<sub>2</sub>S that is a common household product.

**Solution:**

We can solve the problem in one of two ways: (1) compare the relative positions of the four possible reductants with that of the Ag<sub>2</sub>S/Ag couple in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) or (2) compare *E*° for each species with *E*° for the Ag<sub>2</sub>S/Ag couple (−0.69 V).

1.  **A** The species in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) are arranged from top to bottom in order of increasing reducing strength. Of the four species given in the problem, I<sup>−</sup>(aq), Sn<sup>2+</sup>(aq), and H<sub>2</sub>O<sub>2</sub>(aq) lie above Ag<sub>2</sub>S, and one \[Zn(s)\] lies below it. We can therefore conclude that Zn(s) can reduce Ag<sub>2</sub>S(s) under standard conditions, whereas I<sup>−</sup>(aq), Sn<sup>2+</sup>(aq), and H<sub>2</sub>O<sub>2</sub>(aq) cannot. Sn<sup>2+</sup>(aq) and H<sub>2</sub>O<sub>2</sub>(aq) appear twice in the table: on the left side (oxidant) in one half-reaction and on the right side (reductant) in another.
2.  The strongest reductant is Zn(s), the species on the right side of the half-reaction that lies closer to the bottom of [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) than the half-reactions involving I<sup>−</sup>(aq), Sn<sup>2+</sup>(aq), and H<sub>2</sub>O<sub>2</sub>(aq). (Commercial products that use a piece of zinc are often marketed as a "miracle product" for removing tarnish from silver. All that is required is to add warm water and salt for electrical conductivity.)
3.  **B** Of the reductants that lie below Zn(s) in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01), and therefore are stronger reductants, only one is commonly available in household products: Al(s), which is sold as aluminum foil for wrapping foods.

Exercise

Refer to [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) to predict

1.  which species---Sn<sup>4+</sup>(aq), Cl<sup>−</sup>(aq), Ag<sup>+</sup>(aq), Cr<sup>3+</sup>(aq), and/or H<sub>2</sub>O<sub>2</sub>(aq)---can oxidize MnO<sub>2</sub>(s) to MNO<sub>4</sub><sup>−</sup> under standard conditions.
2.  which species---Sn<sup>4+</sup>(aq), Cl<sup>−</sup>(aq), Ag<sup>+</sup>(aq), Cr<sup>3+</sup>(aq), and/or H<sub>2</sub>O<sub>2</sub>(aq)---is the strongest oxidizing agent in aqueous solution.

**Answer:**

1.  Ag<sup>+</sup>(aq); H<sub>2</sub>O<sub>2</sub>(aq)
2.  H<sub>2</sub>O<sub>2</sub>(aq)

### Example 6

Use the data in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) to determine whether each reaction is likely to occur spontaneously under standard conditions:

1.  Sn(s) + Be<sup>2+</sup>(aq) → Sn<sup>2+</sup>(aq) + Be(s)
2.  MnO<sub>2</sub>(s) + H<sub>2</sub>O<sub>2</sub>(aq) + 2H<sup>+</sup>(aq) → O<sub>2</sub>(g) + Mn<sup>2+</sup>(aq) + 2H<sub>2</sub>O(l)

**Given:** redox reaction and list of standard electrode potentials ([Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01))

**Asked for:** reaction spontaneity

**Strategy:**

**A** Identify the half-reactions in each equation. Using [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01), determine the standard potentials for the half-reactions in the appropriate direction.

**B** Use [Equation 19.10](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s01-eq02) to calculate the standard cell potential for the overall reaction. From this value, determine whether the overall reaction is spontaneous.

**Solution:**

1.  **A** Metallic tin is oxidized to Sn<sup>2+</sup>(aq), and Be<sup>2+</sup>(aq) is reduced to elemental beryllium. We can find the standard electrode potentials for the latter (reduction) half-reaction (−1.85 V) and for the former (oxidation) half-reaction (−0.14 V) directly from [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01).

    **B** Adding the two half-reactions gives the overall reaction:

    $$\begin{array}{lll}
    \text{cathode:} & \left. \text{MnO}_{2}\text{(s)} + 4\text{H}^{+}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{Mn}^{2 +}\text{(aq)} + 2\text{H}_{2}\text{O(l)} \right. & {E{^\circ}_{\text{cathode}} = 1.22\text{~V}} \\
    \text{anode:} & \left. \text{H}_{2}\text{O}_{2}\text{(aq)}\rightarrow\text{O}_{2}\text{(g)} + 2\text{H}^{+}\text{(aq)} + 2\text{e}^{-} \right. & {E{^\circ}_{\text{anode}} = 0.70\text{~V}} \\
    \text{overall:} & \left. \text{MnO}_{2}\text{(s)} + \text{H}_{2}\text{O}_{2}\text{(aq)} + 2\text{H}^{+}\text{(aq)}\rightarrow \right. & {E{^\circ}_{\text{cell}} = E{^\circ}_{\text{cathode}} - E{^\circ}_{\text{anode}}} \\
     & {\quad\text{O}_{2}\left( \text{g} \right) + \text{Mn}^{2 +}\text{(aq)} + 2\text{H}_{2}\text{O(l)}} & {\quad = - 0.53\text{~V}}
    \end{array}$$

    The standard cell potential is quite negative, so the reaction will *not* occur spontaneously as written. That is, metallic tin cannot be used to reduce Be<sup>2+</sup> to beryllium metal under standard conditions. Instead, the reverse process, the reduction of stannous ions (Sn<sup>2+</sup>) by metallic beryllium, which has a positive value of *E*°<sub>cell</sub>, will occur spontaneously.

2.  **A** MnO<sub>2</sub> is the oxidant (Mn<sup>4+</sup> is reduced to Mn<sup>2+</sup>), while H<sub>2</sub>O<sub>2</sub> is the reductant (O<sup>2−</sup> is oxidized to O<sub>2</sub>). We can obtain the standard electrode potentials for the reduction and oxidation half-reactions directly from [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01).

    **B** The two half-reactions and their corresponding potentials are as follows:

    $$\begin{array}{lll}
    \text{cathode:} & \left. \text{MnO}_{2}\text{(s)} + 4\text{H}^{+}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{Mn}^{2 +}\text{(aq)} + 2\text{H}_{2}\text{O(l)} \right. & {E{^\circ}_{\text{cathode}} = 1.22\text{~V}} \\
    \text{anode:} & \left. \text{H}_{2}\text{O}_{2}\text{(aq)}\rightarrow\text{O}_{2}\text{(g)} + 2\text{H}^{+}\text{(aq)} + 2\text{e}^{-} \right. & {E{^\circ}_{\text{anode}} = 0.70\text{~V}} \\
    \text{overall:} & \left. \text{MnO}_{2}\text{(s)} + \text{H}_{2}\text{O}_{2}\text{(aq)} + 2\text{H}^{+}\text{(aq)}\rightarrow \right. & {E{^\circ}_{\text{cell}} = E{^\circ}_{\text{cathode}} - E{^\circ}_{\text{anode}}} \\
     & {\quad\text{O}_{2}\left( \text{g} \right) + \text{Mn}^{2 +}\text{(aq)} + 2\text{H}_{2}\text{O(l)}} & {\quad = - 0.53\text{~V}}
    \end{array}$$

    The standard potential for the reaction is positive, indicating that under standard conditions, it will occur spontaneously as written. Hydrogen peroxide will reduce MnO<sub>2</sub>, and oxygen gas will evolve from the solution.

Exercise

Use the data in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) to determine whether each reaction is likely to occur spontaneously under standard conditions:

1.  2Ce<sup>4+</sup>(aq) + 2Cl<sup>−</sup>(aq) → 2Ce<sup>3+</sup>(aq) + Cl<sub>2</sub>(g)
2.  4MnO<sub>2</sub>(s) + 3O<sub>2</sub>(g) + 4OH<sup>−</sup>(aq) → 4MnO<sub>4</sub><sup>−</sup>(aq) + 2H<sub>2</sub>O

**Answer:**

1.  spontaneous (*E*°<sub>cell</sub> = 0.36 V)
2.  nonspontaneous (*E*°<sub>cell</sub> = −0.20 V)

Although the sign of *E*°<sub>cell</sub> tells us whether a particular redox reaction will occur spontaneously under standard conditions, it does not tell us to what *extent* the reaction proceeds, and it does not tell us what will happen under nonstandard conditions. To answer these questions requires a more quantitative understanding of the relationship between electrochemical cell potential and chemical thermodynamics, as described in [Section 19.4 \"Electrochemical Cells and Thermodynamics\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04).

````````````{important} Summary

The oxidative and reductive strengths of a variety of substances can be compared using standard electrode potentials. Apparent anomalies can be explained by the fact that electrode potentials are measured in aqueous solution, which allows for strong intermolecular electrostatic interactions, and not in the gas phase.

````````````

````````````{important} Key Takeaway

- The relative strengths of various oxidants and reductants can be predicted using *E*° values.

````````````

### Conceptual Problems

1.  The order of electrode potentials cannot always be predicted by ionization potentials and electron affinities. Why? Do you expect sodium metal to have a higher or a lower electrode potential than predicted from its ionization potential? What is its approximate electrode potential?

2.  Without referring to tabulated data, of Br<sub>2</sub>/Br<sup>−</sup>, Ca<sup>2+</sup>/Ca, O<sub>2</sub>/OH<sup>−</sup>, and Al<sup>3+</sup>/Al, which would you expect to have the *least* negative electrode potential and which the *most* negative? Why?

3.  Because of the sulfur-containing amino acids present in egg whites, eating eggs with a silver fork will tarnish the fork. As a chemist, you have all kinds of interesting cleaning products in your cabinet, including a 1 M solution of oxalic acid (H<sub>2</sub>C<sub>2</sub>O<sub>4</sub>). Would you choose this solution to clean the fork that you have tarnished from eating scrambled eggs?

4.  The electrode potential for the reaction Cu<sup>2+</sup>(aq) + 2e<sup>−</sup> → Cu(s) is 0.34 V under standard conditions. Is the potential for the oxidation of 0.5 mol of Cu equal to −0.34/2 V? Explain your answer.

### Answer

1.  

2.  

3.  No; *E*° = −0.691 V for Ag<sub>2</sub>S(s) + 2e<sup>−</sup> → Ag(s) + S<sup>2−</sup>(aq), which is too negative for Ag<sub>2</sub>S to be spontaneously reduced by oxalic acid \[*E*° = 0.49 V for 2CO<sub>2</sub>(g) + 2H<sup>+</sup>(aq) + 2e<sup>−</sup> → H<sub>2</sub>C<sub>2</sub>O<sub>4</sub>(aq)\]

4.  

(src-averill-1-0-ch19-s04)=

## 19.4 Electrochemical Cells and Thermodynamics

````````````{note} Learning Objectives

1.  To understand the relationship between cell potential and the equilibrium constant.
2.  To use cell potentials to calculate solution concentrations.

````````````

Changes in reaction conditions can have a tremendous effect on the course of a redox reaction. For example, under standard conditions, the reaction of Co(s) with Ni<sup>2+</sup>(aq) to form Ni(s) and Co<sup>2+</sup>(aq) occurs spontaneously, but if we reduce the concentration of Ni<sup>2+</sup> by a factor of 100, so that \[Ni<sup>2+</sup>\] is 0.01 M, then the reverse reaction occurs spontaneously instead. The relationship between voltage and concentration is one of the factors that must be understood to predict whether a reaction will be spontaneous.

### The Relationship between Cell Potential and Free Energy

Electrochemical cells convert chemical energy to electrical energy and vice versa. The total amount of energy produced by an electrochemical cell, and thus the amount of energy available to do electrical work, depends on both the cell potential and the total number of electrons that are transferred from the reductant to the oxidant during the course of a reaction. The resulting electric current is measured in coulombs (C)[^chem-25], an SI unit that measures the number of electrons passing a given point in 1 s. A coulomb relates energy (in joules) to electrical potential (in volts). Electric current is measured in amperes (A)[^chem-26]; 1 A is defined as the flow of 1 C/s past a given point (1 C = 1 A·s):

Equation 19.48

$$\frac{1\text{~J}}{1\text{~V}} = 1\text{~C} = \text{A} \cdot \text{s}$$

In chemical reactions, however, we need to relate the coulomb to the charge on a *mole* of electrons. Multiplying the charge on the electron by Avogadro's number gives us the charge on 1 mol of electrons, which is called the faraday (*F*)[^chem-27], named after the English physicist and chemist Michael Faraday (1791--1867):

(src-averill-1-0-ch19-s04-s01-eq02)=

Equation 19.49

$$\begin{array}{ll}
F & {= (1.60218 \times 10^{- 19}\text{~C})\left( \frac{6.02214 \times 10^{23}}{1\text{~mol~e}^{-}} \right)} \\
 & {= 9.64855 \times 10^{4}\text{~C/mol~e}^{-} \simeq 96,486\text{/}(\text{V} \cdot \text{mol~e}^{-})}
\end{array}$$

The total charge transferred from the reductant to the oxidant is therefore *nF*, where *n* is the number of moles of electrons.

````````````{important} Michael Faraday (1791–1867)

Faraday was a British physicist and chemist who was arguably one of the greatest experimental scientists in history. The son of a blacksmith, Faraday was self-educated and became an apprentice bookbinder at age 14 before turning to science. His experiments in electricity and magnetism made electricity a routine tool in science and led to both the electric motor and the electric generator. He discovered the phenomenon of electrolysis and laid the foundations of electrochemistry. In fact, most of the specialized terms introduced in this chapter (electrode, anode, cathode, and so forth) are due to Faraday. In addition, he discovered benzene and invented the system of oxidation state numbers that we use today. Faraday is probably best known for "The Chemical History of a Candle," a series of public lectures on the chemistry and physics of flames.

````````````

The maximum amount of work that can be produced by an electrochemical cell (*w*<sub>max</sub>) is equal to the product of the cell potential (*E*<sub>cell</sub>) and the total charge transferred during the reaction (*nF*):

(src-averill-1-0-ch19-s04-s01-eq03)=

Equation 19.50

*w*<sub>max</sub> = *nFE*<sub>cell</sub>

Work is expressed as a negative number because work is being done *by* a system (an electrochemical cell with a positive potential) *on* its surroundings.

As you learned in [Chapter 18 \"Chemical Thermodynamics\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18), the change in free energy (Δ*G*) is also a measure of the maximum amount of work that can be performed during a chemical process (Δ*G* = *w*<sub>max</sub>). Consequently, there must be a relationship between the potential of an electrochemical cell and Δ*G*, the most important thermodynamic quantity discussed in [Chapter 18 \"Chemical Thermodynamics\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18). This relationship is as follows:

Equation 19.51

Δ*G* = −*nFE*<sub>cell</sub>

A spontaneous redox reaction is therefore characterized by a *negative* value of Δ*G* and a *positive* value of *E*<sub>cell</sub>, consistent with our earlier discussions. When both reactants and products are in their standard states, the relationship between Δ*G*° and *E*°<sub>cell</sub> is as follows:

(src-averill-1-0-ch19-s04-s01-eq05)=

Equation 19.52

Δ*G*° = −*nFE*°<sub>cell</sub>

````````````{important} Note the Pattern

A spontaneous redox reaction is characterized by a negative value of Δ*G*°, which corresponds to a positive value of *E*°<sub>cell</sub>.

````````````

### Example 7

Suppose you want to prepare elemental bromine from bromide using the dichromate ion as an oxidant. Using the data in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01), calculate the free-energy change (Δ*G*°) for this redox reaction under standard conditions. Is the reaction spontaneous?

**Given:** redox reaction

**Asked for:** Δ*G*° for the reaction and spontaneity

**Strategy:**

**A** From the relevant half-reactions and the corresponding values of *E*°, write the overall reaction and calculate *E*°<sub>cell</sub> using [Equation 19.10](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s01-eq02).

**B** Determine the number of electrons transferred in the overall reaction. Then use [Equation 19.52](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s01-eq05) to calculate Δ*G*°. If Δ*G*° is negative, then the reaction is spontaneous.

**Solution:**

**A** As always, the first step is to write the relevant half-reactions and use them to obtain the overall reaction and the magnitude of *E*°. From [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01), we can find the reduction and oxidation half-reactions and corresponding *E*° values:

$$\begin{array}{lll}
\text{cathode:} & \left. \text{Cr}_{2}\text{O}_{7}{}^{2 -}\text{(aq)} + 14\text{H}^{+}\text{(aq)} + 6\text{e}^{-}\rightarrow 2\text{Cr}^{3 +}\text{(aq)} + 7\text{H}_{2}\text{O(l)} \right. & {E_{\text{cathode}}^{{^\circ}} = 1.23\text{~V}} \\
\text{anode:} & \left. \text{2Br}^{-}\text{(aq)}\rightarrow\text{Br}_{2}\text{(aq)} + 2\text{e}^{-} \right. & {E_{\text{anode}}^{{^\circ}} = 1.09\text{~V}}
\end{array}$$

To obtain the overall balanced chemical equation, we must multiply both sides of the oxidation half-reaction by 3 to obtain the same number of electrons as in the reduction half-reaction, remembering that the magnitude of *E*° is not affected:

$$\begin{array}{lll}
\text{cathode:} & \left. \text{Cr}_{2}\text{O}_{7}{}^{2 -}\text{(aq)} + 14\text{H}^{+}\text{(aq)} + 6\text{e}^{-}\rightarrow 2\text{Cr}^{3 +}\text{(aq)} + 7\text{H}_{2}\text{O(l)} \right. & {E{^\circ}_{\text{cathode}} = 1.23\text{~V}} \\
\text{anode:} & \left. \text{6Br}^{-}\text{(aq)}\rightarrow 3\text{Br}_{2}\text{(aq)} + 6\text{e}^{-} \right. & {E{^\circ}_{\text{anode}} = 1.09\text{~V}} \\
\text{overall:} & \left. \text{Cr}_{2}\text{O}_{7}{}^{2 -}\text{(aq)} + 6\text{Br}^{-}\text{(aq)} + 14\text{H}^{+}\text{(aq)}\rightarrow \right. & {E{^\circ}_{\text{cell}} = 0.14\text{~V}} \\
 & {\quad 2\text{Cr}^{3 +}\text{(aq)} + 3\text{Br}_{2}\text{(aq)} + 7\text{H}_{2}\text{O(l)}} & 
\end{array}$$

**B** We can now calculate Δ*G*° using [Equation 19.52](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s01-eq05). Because six electrons are transferred in the overall reaction, the value of *n* is 6:

$$\begin{aligned}
{\Delta G{^\circ} = - (n)(F)(E_{\text{cell}}^{{^\circ}})} & {= - (6\ \cancel{\text{mole}})\lbrack 96,468\text{~J/}(\cancel{\text{V}} \cdot \cancel{\text{mol}})(0.14\ \cancel{\text{V}})\rbrack} \\
 & {= - 8.1\, \times \, 10^{4}\text{~J}} \\
 & {= - 81\text{~kJ/mol~Cr}_{2}\text{O}_{7}{}^{2 -}}
\end{aligned}$$

Thus Δ*G*° is −81 kJ for the reaction as written, and the reaction is spontaneous.

Exercise

Use the data in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) to calculate Δ*G*° for the reduction of ferric ion by iodide:

2Fe<sup>3+</sup>(aq) + 2I<sup>−</sup>(aq) → 2Fe<sup>2+</sup>(aq) + I<sub>2</sub>(s)

Is the reaction spontaneous?

**Answer:** −44 kJ/mol I<sub>2</sub>; yes

### Potentials for the Sums of Half-Reactions

Although [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) and [Chapter 29 \"Appendix E: Standard Reduction Potentials at 25°C\"](/appendices/appendix-e-standard-reduction-.md#src-averill-1-0-ch96appe) list several half-reactions, many more are known. When the standard potential for a half-reaction is not available, we can use relationships between standard potentials and free energy to obtain the potential of any other half-reaction that can be written as the sum of two or more half-reactions whose standard potentials are available. For example, the potential for the reduction of Fe<sup>3+</sup>(aq) to Fe(s) is not listed in the table, but two related reductions are given:

Equation 19.53

$$\begin{array}{rc}
\left. \text{Fe}^{3 +}\text{(aq)} + \text{e}^{-}\rightarrow\text{Fe}^{2 +}\text{(aq)} \right. & {E{^\circ} = 0.77\text{~V}}
\end{array}$$

Equation 19.54

$$\begin{array}{rc}
\left. \text{Fe}^{2 +}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{Fe(aq)} \right. & {E{^\circ} = - 0.45\text{~V}}
\end{array}$$

Although the sum of these two half-reactions gives the desired half-reaction, we cannot simply add the potentials of two reductive half-reactions to obtain the potential of a third reductive half-reaction *because E*° *is not a state function*. However, because Δ*G*° is a state function, the sum of the Δ*G*° values for the individual reactions gives us Δ*G*° for the overall reaction, which is proportional to *both* the potential *and* the number of electrons (*n*) transferred. To obtain the value of *E*° for the overall half-reaction, we first must add the values of Δ*G*° (= −*nFE*°) for each individual half-reaction to obtain Δ*G*° for the overall half-reaction:

(src-averill-1-0-ch19-s04-s02-eq03)=

Equation 19.55

$$\begin{array}{rccl}
{\text{Fe}^{3 +}\text{(aq)} + \text{e}^{-}} & \left. \rightarrow\cancel{\text{Fe}^{2 +}\text{(aq)}} \right. & {\Delta G{^\circ}} & {= - (1)(F)(0.77\text{~V})} \\
{\cancel{\text{Fe}^{2 +}\text{(aq)}} + 2\text{e}^{-}} & \left. \rightarrow\text{Fe(s)} \right. & {\Delta G{^\circ}} & {= - (2)(F)( - .045\text{~V})} \\
{\text{Fe}^{3 +}\text{(aq)} + 3\text{e}^{-}} & \left. \rightarrow\text{Fe(s)} \right. & {\Delta G{^\circ}} & {= \lbrack - (1)(F)(0.77\text{~V})\rbrack + \lbrack - (2)(F)( - 0.45\text{~V})\rbrack}
\end{array}$$

Solving the last expression for Δ*G*° for the overall half-reaction,

Equation 19.56

Δ*G*° = *F*\[(−0.77 V) + (−2)(−0.45 V)\] = *F*(0.13 V)

Three electrons (*n* = 3) are transferred in the overall reaction ([Equation 19.55](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s02-eq03)), so substituting into [Equation 19.52](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s01-eq05) and solving for *E*° gives the following:

$$\begin{aligned}
{\Delta G{^\circ}} & {= - nFE_{\text{cell}}^{{^\circ}}} \\
{F(0.13\text{~V})} & {= - (3)(F)(E_{\text{cell}}^{{^\circ}})} \\
{E{^\circ}} & {= - \frac{0.13\text{~V}}{3} = - 0.043\text{~V}}
\end{aligned}$$

This value of *E*° is *very* different from the value that is obtained by simply adding the potentials for the two half-reactions (0.32 V) and even has the opposite sign.

````````````{important} Note the Pattern

Values of *E*° for half-reactions cannot be added to give *E*° for the sum of the half-reactions; only values of Δ*G*° = −*nFE*°<sub>cell</sub> for half-reactions can be added.

````````````

### The Relationship between Cell Potential and the Equilibrium Constant

We can use the relationship between Δ*G*° and the equilibrium constant *K*, defined in [Chapter 18 \"Chemical Thermodynamics\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18), to obtain a relationship between *E*°<sub>cell</sub> and *K*. Recall that for a general reaction of the type *a*A + *b*B → *c*C + *d*D, the standard free-energy change and the equilibrium constant are related by the following equation:

(src-averill-1-0-ch19-s04-s03-eq01)=

Equation 19.57

Δ*G*° = −*RT* ln *K*

Given the relationship between the standard free-energy change and the standard cell potential ([Equation 19.52](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s01-eq05)), we can write

Equation 19.58

−*nFE*°<sub>cell</sub> = −*RT* ln *K*

Rearranging this equation,

(src-averill-1-0-ch19-s04-s03-eq03)=

Equation 19.59

$$E_{\text{cell}}^{{^\circ}} = \left( \frac{RT}{nF} \right)\text{ln~}K$$

For *T* = 298 K, [Equation 19.59](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s03-eq03) can be simplified as follows:

(src-averill-1-0-ch19-s04-s03-eq04)=

Equation 19.60

$$E_{\text{cell}}^{{^\circ}} = \left( \frac{RT}{nF} \right)\text{ln~}K = \left\lbrack \frac{\lbrack 8.314\ \cancel{\text{J}}\text{/}(\cancel{\text{mol}} \cdot \cancel{\text{K}})(298\cancel{\text{K}})\rbrack}{n\lbrack 96,486\ \cancel{\text{J}}\text{/}(\text{V} \cdot \cancel{\text{mol}})\rbrack} \right\rbrack 2.303\text{~log~}K = \left( \frac{0.0591\text{~V}}{n} \right)\log\ K$$

Thus *E*°<sub>cell</sub> is directly proportional to the logarithm of the equilibrium constant. This means that large equilibrium constants correspond to large positive values of *E*°<sub>cell</sub> and vice versa.

### Example 8

Use the data in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) to calculate the equilibrium constant for the reaction of metallic lead with PbO<sub>2</sub> in the presence of sulfate ions to give PbSO<sub>4</sub> under standard conditions. (This reaction occurs when a car battery is discharged.) Report your answer to two significant figures.

**Given:** redox reaction

**Asked for:** *K*

**Strategy:**

**A** Write the relevant half-reactions and potentials. From these, obtain the overall reaction and *E*°<sub>cell</sub>.

**B** Determine the number of electrons transferred in the overall reaction. Use [Equation 19.60](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s03-eq04) to solve for log *K* and then *K*.

**Solution:**

**A** The relevant half-reactions and potentials from [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) are as follows:

$$\begin{array}{lll}
\text{cathode:} & \left. \text{PbO}_{2}\text{(s)} + \text{SO}_{4}{}^{2 -}\text{(aq)} + 4\text{H}^{+}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{PbSO}_{4}\text{(s)} + 2\text{H}_{2}\text{O(l)} \right. & {E_{\text{cathode}}^{{^\circ}} = 1.69\text{~V}} \\
\text{anode:} & \left. \text{Pb(s)} + \text{SO}_{4}{}^{2 -}\text{(aq)}\rightarrow\text{PbSO}_{4}\text{(s)} + 2\text{e}^{-} \right. & {E_{\text{anode}}^{{^\circ}} = - 0.36\text{~V}} \\
\text{overall:} & \left. \text{Pb(s)} + \text{PbO}_{2}\text{(s)} + 2\text{SO}_{4}{}^{2 -}\text{(aq)} + 4\text{H}^{+}\text{(aq)}\rightarrow 2\text{PbSO}_{4}\text{(s)} + 2\text{H}_{2}\text{O(l)} \right. & {E_{\text{cell}}^{{^\circ}} = 2.05\text{~V}}
\end{array}$$

**B** Two electrons are transferred in the overall reaction, so *n* = 2. Solving [Equation 19.60](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s03-eq04) for log *K* and inserting the values of *n* and *E*°,

$$\begin{aligned}
{\log\ K} & {= \frac{nE{^\circ}}{0.0591\text{~V}} = \frac{2(2.05\ \cancel{\text{V}})}{0.0591\ \cancel{\text{V}}} = 69.37} \\
K & {= 2.3 \times 10^{69}}
\end{aligned}$$

Thus the equilibrium lies far to the right, favoring a discharged battery (as anyone who has ever tried unsuccessfully to start a car after letting it sit for a long time will know).

Exercise

Use the data in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) to calculate the equilibrium constant for the reaction of Sn<sup>2+</sup>(aq) with oxygen to produce Sn<sup>4+</sup>(aq) and water under standard conditions. Report your answer to two significant figures. The reaction is as follows:

$$\left. 2\text{Sn}^{2 +}\text{(aq)} + \text{O}_{2}\text{(g)} + 4\text{H}^{+}\text{(aq)}\rightleftharpoons 2\text{Sn}^{4 +}\text{(aq)} + 2\text{H}_{2}\text{O(l)} \right.$$

**Answer:** 1.2 × 10<sup>73</sup>

[Figure 19.10 \"The Relationships among Criteria for Thermodynamic Spontaneity\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s03-f01) summarizes the relationships that we have developed based on properties of the *system*---that is, based on the equilibrium constant, standard free-energy change, and standard cell potential---and the criteria for spontaneity (Δ*G*° \< 0). Unfortunately, these criteria apply only to systems in which all reactants and products are present in their standard states, a situation that is seldom encountered in the real world. A more generally useful relationship between cell potential and reactant and product concentrations, as we are about to see, uses the relationship between Δ*G* and the reaction quotient *Q* developed in [Chapter 18 \"Chemical Thermodynamics\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18).

(src-averill-1-0-ch19-s04-s03-f01)=

Figure 19.10 The Relationships among Criteria for Thermodynamic Spontaneity

![Figure 19.10 The Relationships among Criteria for Thermodynamic Spontaneity](/images/section_23/a4aacd07d282552c4098dbfebc4314ec.jpg)

The three properties of a system that can be used to predict the spontaneity of a redox reaction under standard conditions are *K*, Δ*G*°, and *E*°<sub>cell</sub>. If we know the value of one of these quantities, then these relationships enable us to calculate the value of the other two. The signs of Δ*G*° and *E*°<sub>cell</sub> and the magnitude of *K* determine the direction of spontaneous reaction under standard conditions.

### The Effect of Concentration on Cell Potential: The Nernst Equation

Recall from [Chapter 18 \"Chemical Thermodynamics\"](/chapters/ch-18-chemical-thermodynamics.md#src-averill-1-0-ch18) that the *actual* free-energy change for a reaction under nonstandard conditions, Δ*G*, is given as follows:

(src-averill-1-0-ch19-s04-s04-eq01)=

Equation 19.61

Δ*G* = Δ*G*° + *RT* ln *Q*

We also know that Δ*G* = −*nFE*<sub>cell</sub> and Δ*G*° = −*nFE*°<sub>cell</sub>. Substituting these expressions into [Equation 19.61](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-eq01), we obtain

Equation 19.62

−*nFE*<sub>cell</sub> = −*nFE*°<sub>cell</sub> + *RT* ln *Q*

Dividing both sides of this equation by −*nF*,

Equation 19.63

$$E_{\text{cell}} = E_{\text{cell}}^{{^\circ}} - \left( \frac{RT}{nF} \right)\text{ln~}Q$$

[Equation 19.44](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s04-eq01) is called the Nernst equation[^chem-28], after the German physicist and chemist Walter Nernst (1864--1941), who first derived it. The Nernst equation is arguably the most important relationship in electrochemistry. When a redox reaction is at equilibrium (Δ*G* = 0), [Equation 19.44](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s04-eq01) reduces to [Equation 19.59](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s03-eq03) because *Q* = *K*, and there is no net transfer of electrons (i.e., *E*<sub>cell</sub> = 0).

Substituting the values of the constants into [Equation 19.44](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s04-eq01) with *T* = 298 K and converting to base-10 logarithms give the relationship of the actual cell potential (*E*<sub>cell</sub>), the standard cell potential (*E*°<sub>cell</sub>), and the reactant and product concentrations at room temperature (contained in *Q*):

(src-averill-1-0-ch19-s04-s04-eq04)=

Equation 19.64

$$E_{\text{cell}} = E_{\text{cell}}^{{^\circ}} - \left( \frac{0.0591\text{~V}}{n} \right)\log\ Q$$

````````````{important} Note the Pattern

The Nernst equation can be used to determine the value of *E*<sub>cell</sub>, and thus the direction of spontaneous reaction, for any redox reaction under any conditions.

````````````

[Equation 19.64](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-eq04) allows us to calculate the potential associated with any electrochemical cell at 298 K for any combination of reactant and product concentrations under any conditions. We can therefore determine the spontaneous direction of any redox reaction under any conditions, as long as we have tabulated values for the relevant standard electrode potentials. Notice in [Equation 19.64](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-eq04) that the cell potential changes by 0.0591/*n* V for each 10-fold change in the value of *Q* because log 10 = 1.

### Example 9

In the exercise in Example 6, you determined that the following reaction proceeds spontaneously under standard conditions because *E*°<sub>cell</sub> \> 0 (which you now know means that Δ*G*° \< 0):

$$\left. 2\text{Ce}^{4 +}\text{(aq)} + 2\text{Cl}^{-}\text{(aq)}\rightarrow 2\text{Ce}^{3 +}\text{(aq)} + \text{Cl}_{2}\text{(g)}\quad E_{\text{cell}}^{{^\circ}} = 0.\text{25~V} \right.$$

Calculate *E* for this reaction under the following nonstandard conditions and determine whether it will occur spontaneously: \[Ce<sup>4+</sup>\] = 0.013 M, \[Ce<sup>3+</sup>\] = 0.60 M, \[Cl<sup>−</sup>\] = 0.0030 M, $P_{\text{Cl}_{2}}$ = 1.0 atm, and *T* = 25°C.

**Given:** balanced redox reaction, standard cell potential, and nonstandard conditions

**Asked for:** cell potential

**Strategy:**

Determine the number of electrons transferred during the redox process. Then use the Nernst equation to find the cell potential under the nonstandard conditions.

**Solution:**

We can use the information given and the Nernst equation to calculate *E*<sub>cell</sub>. Moreover, because the temperature is 25°C (298 K), we can use [Equation 19.64](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-eq04) instead of 19.46. The overall reaction involves the net transfer of two electrons:

2Ce<sup>4+</sup>(aq) + 2e<sup>−</sup> → 2Ce<sup>3+</sup>(aq) 2Cl<sup>−</sup>(aq) → Cl<sub>2</sub>(g) + 2e<sup>−</sup>

so *n* = 2. Substituting the concentrations given in the problem, the partial pressure of Cl<sub>2</sub>, and the value of *E*°<sub>cell</sub> into [Equation 19.64](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-eq04),

$$\begin{aligned}
E_{\text{cell}} & {= E_{\text{cell}}^{{^\circ}} - \left( \frac{0.0591\text{~V}}{n} \right)\log\ Q} \\
 & {= 0.25\text{~V} - \left( \frac{0.0591\text{~V}}{2} \right)\log\left( \frac{{\lbrack\text{Ce}^{3 +}\rbrack}^{2}P_{\text{Cl}_{2}}}{{\lbrack\text{Ce}^{4 +}\rbrack}^{2}{\lbrack\text{Cl}^{-}\rbrack}^{2}} \right)} \\
 & {= 0.25\text{~V} - \lbrack(0.0296\text{~V})(8.37)\rbrack = 0.00\text{~V}}
\end{aligned}$$

Thus the reaction will *not* occur spontaneously under these conditions (because *E* = 0 V and Δ*G* = 0). The composition specified is that of an equilibrium mixture.

Exercise

In the exercise in Example 6, you determined that molecular oxygen will not oxidize MnO<sub>2</sub> to permanganate via the reaction

$$\begin{array}{rc}
\left. 4\text{MnO}_{2}\text{(s)} + 3\text{O}_{2}\text{(g)} + 4\text{OH}^{-}\text{(aq)}\rightarrow 4\text{MnO}_{4}{}^{-}\text{(aq)} + 2\text{H}_{2}\text{O(l)} \right. & {E_{\text{cell}}^{{^\circ}} = - 0.20\text{~V}}
\end{array}$$

Calculate *E*<sub>cell</sub> for the reaction under the following nonstandard conditions and decide whether the reaction will occur spontaneously: pH 10, $P_{\text{O}_{2}}$ = 0.20 atm, \[MNO<sub>4</sub><sup>−</sup>\] = 1.0 × 10<sup>−4</sup> M, and *T* = 25°C.

**Answer:** *E*<sub>cell</sub> = −0.22 V; the reaction will not occur spontaneously.

Applying the Nernst equation to a simple electrochemical cell such as the Zn/Cu cell discussed in [Section 19.2 \"Standard Potentials\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02) allows us to see how the cell voltage varies as the reaction progresses and the concentrations of the dissolved ions change. Recall that the overall reaction for this cell is as follows:

Equation 19.65

$$\begin{array}{rc}
\left. \text{Zn(s)} + \text{Cu}^{2 +}\text{(aq)}\rightarrow\text{Zn}^{2 +}\text{(aq)} + \text{Cu(s)} \right. & {E_{\text{cell}}^{{^\circ}} = 1.10\text{~V}}
\end{array}$$

The reaction quotient is therefore *Q* = \[Zn<sup>2+</sup>\]/\[Cu<sup>2+</sup>\]. Suppose that the cell initially contains 1.0 M Cu<sup>2+</sup> and 1.0 × 10<sup>−6</sup> M Zn<sup>2+</sup>. The initial voltage measured when the cell is connected can then be calculated from [Equation 19.64](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-eq04):

Equation 19.66

$$\begin{aligned}
E_{\text{cell}} & {= E_{\text{cell}}^{{^\circ}} - \left( \frac{0.0591\text{~V}}{n} \right)\log\frac{\lbrack\text{Zn}^{2 +}\rbrack}{\lbrack\text{Cu}^{2 +}\rbrack}} \\
 & {= 1.10\text{~V} - \left( \frac{0.0591\text{~V}}{2} \right)\log\left( \frac{1.0 \times 10^{- 6}}{1.0} \right) = 1.28\text{~V}}
\end{aligned}$$

Thus the initial voltage is *greater* than *E*° because *Q* \< 1. As the reaction proceeds, \[Zn<sup>2+</sup>\] in the anode compartment increases as the zinc electrode dissolves, while \[Cu<sup>2+</sup>\] in the cathode compartment decreases as metallic copper is deposited on the electrode. During this process, the ratio *Q* = \[Zn<sup>2+</sup>\]/\[Cu<sup>2+</sup>\] steadily increases, and the cell voltage therefore steadily decreases. Eventually, \[Zn<sup>2+</sup>\] = \[Cu<sup>2+</sup>\], so *Q* = 1 and *E*<sub>cell</sub> = *E*°<sub>cell</sub>. Beyond this point, \[Zn<sup>2+</sup>\] will continue to increase in the anode compartment, and \[Cu<sup>2+</sup>\] will continue to decrease in the cathode compartment. Thus the value of *Q* will increase further, leading to a further decrease in *E*<sub>cell</sub>. When the concentrations in the two compartments are the opposite of the initial concentrations (i.e., 1.0 M Zn<sup>2+</sup> and 1.0 × 10<sup>−6</sup> M Cu<sup>2+</sup>), *Q* = 1.0 × 10<sup>6</sup>, and the cell potential will be reduced to 0.92 V.

The variation of *E*<sub>cell</sub> with log *Q* over this range is linear with a slope of −0.0591/*n*, as illustrated in [Figure 19.11 \"The Variation of \"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-f01). As the reaction proceeds still further, *Q* continues to increase, and *E*<sub>cell</sub> continues to decrease. If neither of the electrodes dissolves completely, thereby breaking the electrical circuit, the cell voltage will eventually reach zero. This is the situation that occurs when a battery is "dead." The value of *Q* when *E*<sub>cell</sub> = 0 is calculated as follows:

Equation 19.67

$$\begin{aligned}
E_{\text{cell}} & {= E_{\text{cell}}^{{^\circ}} - \left( \frac{0.0591\text{~V}}{n} \right)\log Q = 0} \\
{E{^\circ}} & {= \left( \frac{0.0591\text{~V}}{n} \right)\log\ Q} \\
{\log\ Q} & {= \frac{E{^\circ}n}{0.0591\text{~V}} = \frac{(1.10\ \cancel{\text{V}})(2)}{0.0591\ \cancel{\text{V}}} = 37.23} \\
Q & {= 10^{37.23} = 1.7 \times 10^{37}}
\end{aligned}$$

(src-averill-1-0-ch19-s04-s04-f01)=

Figure 19.11 The Variation of *E*<sub>cell</sub> with Log *Q* for a Zn/Cu Cell

![Figure 19.11 The Variation of E cell with Log Q for a Zn/Cu Cell](/images/section_23/d5ecb74a29e2c5f208defc391be185e0.jpg)

Initially, log *Q* \< 0, and the voltage of the cell is greater than *E*°<sub>cell</sub>. As the reaction progresses, log *Q* increases, and *E*<sub>cell</sub> decreases. When \[Zn<sup>2+</sup>\] = \[Cu<sup>2+</sup>\], log *Q* = 0 and *E*<sub>cell</sub> = *E*°<sub>cell</sub> = 1.10 V. As long as the electrical circuit remains intact, the reaction will continue, and log *Q* will increase until *Q* = *K* and the cell voltage reaches zero. At this point, the system will have reached equilibrium.

Recall that at equilibrium, *Q* = *K*. Thus the equilibrium constant for the reaction of Zn metal with Cu<sup>2+</sup> to give Cu metal and Zn<sup>2+</sup> is 1.7 × 10<sup>37</sup> at 25°C.

### Concentration Cells

A voltage can also be generated by constructing an electrochemical cell in which each compartment contains the same redox active solution but at different concentrations. The voltage is produced as the concentrations equilibrate. Suppose, for example, we have a cell with 0.010 M AgNO<sub>3</sub> in one compartment and 1.0 M AgNO<sub>3</sub> in the other. The cell diagram and corresponding half-reactions are as follows:

Equation 19.68

Ag(s)∣Ag<sup>+</sup>(aq, 0.010 M)∥Ag<sup>+</sup>(aq, 1.0 M)∣Ag(s)

Equation 19.69

cathode: Ag<sup>+</sup>(aq, 1.0 M) + e<sup>−</sup> → Ag(s)

Equation 19.70

anode: Ag(s) → Ag<sup>+</sup>(aq, 0.010 M) + e<sup>−</sup>

Equation 19.71

$$\text{overall:~}\left. \text{Ag}^{+}\text{(aq,~1}.0\text{~M)}\rightarrow\text{Ag}^{+}\text{(aq,~0}.010\text{~M)} \right.$$

As the reaction progresses, the concentration of Ag<sup>+</sup> will increase in the left (oxidation) compartment as the silver electrode dissolves, while the Ag<sup>+</sup> concentration in the right (reduction) compartment decreases as the electrode in that compartment gains mass. The *total* mass of Ag(s) in the cell will remain constant, however. We can calculate the potential of the cell using the Nernst equation, inserting 0 for *E*°<sub>cell</sub> because *E*°<sub>cathode</sub> = −*E*°<sub>anode</sub>:

$$E_{\text{cell}} = E_{\text{cell}}^{{^\circ}} - \left( \frac{0.0591\text{~V}}{n} \right)\log\ Q = 0 - \left( \frac{0.0591\text{~V}}{1} \right)\log\left( \frac{0.010}{1.0} \right) = 0.12\text{~V}$$

An electrochemical cell of this type, in which the anode and cathode compartments are identical except for the concentration of a reactant, is called a concentration cell[^chem-29]. As the reaction proceeds, the difference between the concentrations of Ag<sup>+</sup> in the two compartments will decrease, as will *E*<sub>cell</sub>. Finally, when the concentration of Ag<sup>+</sup> is the same in both compartments, equilibrium will have been reached, and the measured potential difference between the two compartments will be zero (*E*<sub>cell</sub> = 0).

### Example 10

Calculate the voltage in a galvanic cell that contains a manganese electrode immersed in a 2.0 M solution of MnCl<sub>2</sub> as the cathode, and a manganese electrode immersed in a 5.2 × 10<sup>−2</sup> M solution of MnSO<sub>4</sub> as the anode (*T* = 25°C).

**Given:** galvanic cell, identities of the electrodes, and solution concentrations

**Asked for:** voltage

**Strategy:**

**A** Write the overall reaction that occurs in the cell.

**B** Determine the number of electrons transferred. Substitute this value into the Nernst equation to calculate the voltage.

**Solution:**

**A** This is a concentration cell, in which the electrode compartments contain the same redox active substance but at different concentrations. The anions (Cl<sup>−</sup> and SO<sub>4</sub><sup>2−</sup>) do not participate in the reaction, so their identity is not important. The overall reaction is as follows:

Mn<sup>2+</sup>(aq, 2.0 M) → Mn<sup>2+</sup>(aq, 5.2 × 10<sup>−2</sup> M)

**B** For the reduction of Mn<sup>2+</sup>(aq) to Mn(s), *n* = 2. We substitute this value and the given Mn<sup>2+</sup> concentrations into [Equation 19.64](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-eq04):

$$E_{\text{cell}} = E_{\text{cell}}^{{^\circ}} - \left( \frac{0.0591\text{~V}}{n} \right)\log\ Q = 0\text{~V} - \left( \frac{0.0591\text{~V}}{2} \right)\log\left( \frac{5.2 \times 10^{- 2}}{2.0} \right) = 0.047\text{~V}$$

Thus manganese will dissolve from the electrode in the compartment that contains the more dilute solution and will be deposited on the electrode in the compartment that contains the more concentrated solution.

Exercise

Suppose we construct a galvanic cell by placing two identical platinum electrodes in two beakers that are connected by a salt bridge. One beaker contains 1.0 M HCl, and the other a 0.010 M solution of Na<sub>2</sub>SO<sub>4</sub> at pH 7.00. Both cells are in contact with the atmosphere, with $P_{\text{O}_{2}}$ = 0.20 atm. If the relevant electrochemical reaction in both compartments is the four-electron reduction of oxygen to water, O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>−</sup> → 2H<sub>2</sub>O(l), what will be the potential when the circuit is closed?

**Answer:** 0.41 V

### Using Cell Potentials to Measure Solubility Products

Because voltages are relatively easy to measure accurately using a voltmeter, electrochemical methods provide a convenient way to determine the concentrations of very dilute solutions and the solubility products (*K*<sub>sp</sub>) of sparingly soluble substances. As you learned in [Chapter 17 \"Solubility and Complexation Equilibriums\"](/chapters/ch-17-solubility-and-complexation-eq.md#src-averill-1-0-ch17), solubility products can be very small, with values of less than or equal to 10<sup>−30</sup>. Equilibrium constants of this magnitude are virtually impossible to measure accurately by direct methods, so we must use alternative methods that are more sensitive, such as electrochemical methods.

To understand how an electrochemical cell is used to measure a solubility product, consider the cell shown in [Figure 19.12 \"A Galvanic Cell for Measuring the Solubility Product of AgCl\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s06-f01), which is designed to measure the solubility product of silver chloride: *K*<sub>sp</sub> = \[Ag<sup>+</sup>\]\[Cl<sup>−</sup>\]. In one compartment, the cell contains a silver wire inserted into a 1.0 M solution of Ag<sup>+</sup>; the other compartment contains a silver wire inserted into a 1.0 M Cl<sup>−</sup> solution saturated with AgCl. In this system, the Ag<sup>+</sup> ion concentration in the first compartment equals *K*<sub>sp</sub>. We can see this by dividing both sides of the equation for *K*<sub>sp</sub> by \[Cl<sup>−</sup>\] and substituting: \[Ag<sup>+</sup>\] = *K*<sub>sp</sub>/\[Cl<sup>−</sup>\] = *K*<sub>sp</sub>/1.0 = *K*<sub>sp</sub>. The overall cell reaction is as follows:

Ag<sup>+</sup>(aq, concentrated) → Ag<sup>+</sup>(aq, dilute)

Thus the voltage of the concentration cell due to the difference in \[Ag<sup>+</sup>\] between the two cells is as follows:

(src-averill-1-0-ch19-s04-s06-eq01)=

Equation 19.72

$$E_{\text{cell}} = 0\text{~V} - \left( \frac{0.0591\text{~V}}{1} \right)\log\left( \frac{{\lbrack\text{Ag}^{+}\rbrack}_{\text{dilute}}}{{\lbrack\text{Ag}^{+}\rbrack}_{\text{concentrated}}} \right) = - 0.0591\text{~V~log}\left( \frac{K_{\text{sp}}}{1.0} \right) = - 0.0591\text{~V~log~}K_{\text{sp}}$$

(src-averill-1-0-ch19-s04-s06-f01)=

Figure 19.12 A Galvanic Cell for Measuring the Solubility Product of AgCl

![Figure 19.12 A Galvanic Cell for Measuring the Solubility Product of AgCl](/images/section_23/6b00017f10bbc22f61ecadb2f59aa3b9.jpg)

One compartment contains a silver wire inserted into a 1.0 M solution of Ag<sup>+</sup>, and the other compartment contains a silver wire inserted into a 1.0 M Cl<sup>−</sup> solution saturated with AgCl. The potential due to the difference in \[Ag<sup>+</sup>\] between the two cells can be used to determine *K*<sub>sp</sub>.

By closing the circuit, we can measure the potential caused by the difference in \[Ag<sup>+</sup>\] in the two cells. In this case, the experimentally measured voltage of the concentration cell at 25°C is 0.580 V. Solving [Equation 19.72](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s06-eq01) for *K*<sub>sp</sub>,

Equation 19.73

$$\begin{aligned}
{\log\ K_{\text{sp}}} & {= \frac{- E_{\text{cell}}}{0.0591\text{~V}} = \frac{- 0.580\ \cancel{\text{V}}}{0.0591\ \cancel{\text{V}}} = - 9.81} \\
K_{\text{sp}} & {= 1.5 \times 10^{- 10}}
\end{aligned}$$

Thus a single potential measurement can provide the information we need to determine the value of the solubility product of a sparingly soluble salt.

### Example 11

To measure the solubility product of lead(II) sulfate (PbSO<sub>4</sub>) at 25°C, you construct a galvanic cell like the one shown in [Figure 19.12 \"A Galvanic Cell for Measuring the Solubility Product of AgCl\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s06-f01), which contains a 1.0 M solution of a very soluble Pb<sup>2+</sup> salt \[lead(II) acetate trihydrate\] in one compartment that is connected by a salt bridge to a 1.0 M solution of Na<sub>2</sub>SO<sub>4</sub> saturated with PbSO<sub>4</sub> in the other. You then insert a Pb electrode into each compartment and close the circuit. Your voltmeter shows a voltage of 230 mV. What is *K*<sub>sp</sub> for PbSO<sub>4</sub>? Report your answer to two significant figures.

**Given:** galvanic cell, solution concentrations, electrodes, and voltage

**Asked for:** *K* <sub>sp</sub>

**Strategy:**

**A** From the information given, write the equation for *K*<sub>sp</sub>. Express this equation in terms of the concentration of Pb<sup>2+</sup>.

**B** Determine the number of electrons transferred in the electrochemical reaction. Substitute the appropriate values into [Equation 19.72](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s06-eq01) and solve for *K*<sub>sp</sub>.

**Solution:**

**A** You have constructed a concentration cell, with one compartment containing a 1.0 M solution of Pb<sup>2+</sup> and the other containing a dilute solution of Pb<sup>2+</sup> in 1.0 M Na<sub>2</sub>SO<sub>4</sub>. As for any concentration cell, the voltage between the two compartments can be calculated using the Nernst equation. The first step is to relate the concentration of Pb<sup>2+</sup> in the dilute solution to *K*<sub>sp</sub>:

$$\begin{aligned}
{\lbrack\text{Pb}^{2 +}\rbrack\lbrack\text{SO}_{4}{}^{2 -}\rbrack} & {= K_{\text{sp}}} \\
{\lbrack\text{Pb}^{2 +}\rbrack} & {= \frac{K_{\text{sp}}}{\lbrack\text{SO}_{4}{}^{2 -}\rbrack} = \frac{K_{\text{sp}}}{1.0\text{~M}} = K_{\text{sp}}}
\end{aligned}$$

**B** The reduction of Pb<sup>2+</sup> to Pb is a two-electron process and proceeds according to the following reaction:

Pb<sup>2+</sup>(aq, concentrated) → Pb<sup>2+</sup>(aq, dilute)

so

$$\begin{array}{ll}
E_{\text{cell}} & {= E_{\text{cell}}^{{^\circ}} - \left( \frac{0.0591}{n} \right)\log\ Q} \\
{0.230\text{~V}} & {= 0\text{~V} - \left( \frac{0.0591\text{~V}}{2} \right)\log\left( \frac{{\lbrack\text{Pb}^{2 +}\rbrack}_{\text{dilute}}}{{\lbrack\text{Pb}^{2 +}\rbrack}_{\text{concentrated}}} \right) = - 0.0296\text{~V~log}\left( \frac{K_{\text{sp}}}{1.0} \right)} \\
{- 7.77} & {= \text{log~}K_{\text{sp}}} \\
{1.7 \times 10^{- 8}} & {= K_{\text{sp}}}
\end{array}$$

Exercise

A concentration cell similar to the one described in Example 11 contains a 1.0 M solution of lanthanum nitrate \[La(NO<sub>3</sub>)<sub>3</sub>\] in one compartment and a 1.0 M solution of sodium fluoride saturated with LaF<sub>3</sub> in the other. A metallic La strip is inserted into each compartment, and the circuit is closed. The measured potential is 0.32 V. What is the *K*<sub>sp</sub> for LaF<sub>3</sub>? Report your answer to two significant figures.

**Answer:** 5.7 × 10<sup>−17</sup>

### Using Cell Potentials to Measure Concentrations

Another use for the Nernst equation is to calculate the concentration of a species given a measured potential and the concentrations of all the other species. We saw an example of this in Example 11, in which the experimental conditions were defined in such a way that the concentration of the metal ion was equal to *K*<sub>sp</sub>. Potential measurements can be used to obtain the concentrations of dissolved species under other conditions as well, which explains the widespread use of electrochemical cells in many analytical devices. Perhaps the most common application is in the determination of \[H<sup>+</sup>\] using a pH meter, as illustrated in Example 12.

### Example 12

Suppose a galvanic cell is constructed with a standard Zn/Zn<sup>2+</sup> couple in one compartment and a modified hydrogen electrode in the second compartment ([Figure 19.7 \"Determining a Standard Electrode Potential Using a Standard Hydrogen Electrode\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s02-s01-f02)). The pressure of hydrogen gas is 1.0 atm, but \[H<sup>+</sup>\] in the second compartment is unknown. The cell diagram is as follows:

Zn(s)∣Zn<sup>2+</sup>(aq, 1.0 M) ∥ H<sup>+</sup>(aq, ? M)∣H<sub>2</sub>(g, 1.0 atm)∣Pt(s)

What is the pH of the solution in the second compartment if the measured potential in the cell is 0.26 V at 25°C?

**Given:** galvanic cell, cell diagram, and cell potential

**Asked for:** pH of the solution

**Strategy:**

**A** Write the overall cell reaction.

**B** Substitute appropriate values into the Nernst equation and solve for −log\[H<sup>+</sup>\] to obtain the pH.

**Solution:**

**A** Under standard conditions, the overall reaction that occurs is the reduction of protons by zinc to give H<sub>2</sub> (note that Zn lies below H<sub>2</sub> in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01)):

$$\left. \text{Zn(s)} + 2\text{H}^{2 +}\text{(aq)}\rightarrow\text{Zn}^{2 +}\text{(aq)} + \text{H}_{\text{2}}\text{(g)}\quad E{^\circ} = 0.76\text{~V} \right.$$

**B** By substituting the given values into the simplified Nernst equation ([Equation 19.64](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-eq04)), we can calculate \[H<sup>+</sup>\] under nonstandard conditions:

$$\begin{aligned}
E_{\text{cell}} & {= E_{\text{cell}}^{{^\circ}} - \left( \frac{0.0591\text{~V}}{n} \right)\log\left( \frac{\lbrack\text{Zn}^{2 +}\rbrack P_{\text{H}_{2}}}{{\lbrack\text{H}^{+}\rbrack}^{2}} \right)} \\
{0.26\text{~V}} & {= 0.76\text{~V} - \left( \frac{0.0591\text{~V}}{2} \right)\log\left( \frac{(1.0)(1.0)}{{\lbrack\text{H}^{+}\rbrack}^{2}} \right)} \\
16.9 & {= \log\left( \frac{1}{{\lbrack\text{H}^{+}\rbrack}^{2}} \right) = \log{\lbrack\text{H}^{+}\rbrack}^{- 2} = \left( {- 2} \right)\log\lbrack\text{H}^{+}\rbrack} \\
8.46 & {= - \log\lbrack\text{H}^{+}\rbrack} \\
{\text{8}\text{.5}} & {= \text{pH}}
\end{aligned}$$

Thus the potential of a galvanic cell can be used to measure the pH of a solution.

Exercise

Suppose you work for an environmental laboratory and you want to use an electrochemical method to measure the concentration of Pb<sup>2+</sup> in groundwater. You construct a galvanic cell using a standard oxygen electrode in one compartment (*E*°<sub>cathode</sub> = 1.23 V). The other compartment contains a strip of lead in a sample of groundwater to which you have added sufficient acetic acid, a weak organic acid, to ensure electrical conductivity. The cell diagram is as follows"

Pb(s) ∣Pb<sup>2+</sup>(aq, ? M)∥H<sup>+</sup>(aq), 1.0 M∣O<sub>2</sub>(g, 1.0 atm)∣Pt(s)

When the circuit is closed, the cell has a measured potential of 1.62 V. Use [Table 19.3 \"Comparison of Galvanic and Electrolytic Cells\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07-s01-t01) and [Chapter 29 \"Appendix E: Standard Reduction Potentials at 25°C\"](/appendices/appendix-e-standard-reduction-.md#src-averill-1-0-ch96appe) to determine the concentration of Pb<sup>2+</sup> in the groundwater.

**Answer:** 1.2 × 10<sup>−9</sup> M

````````````{important} Summary

A **coulomb (C)** relates electrical potential, expressed in volts, and energy, expressed in joules. The current generated from a redox reaction is measured in **amperes (A)**, where 1 A is defined as the flow of 1 C/s past a given point. The **faraday (***F***)** is Avogadro's number multiplied by the charge on an electron and corresponds to the charge on 1 mol of electrons. The product of the cell potential and the total charge is the maximum amount of energy available to do work, which is related to the change in free energy that occurs during the chemical process. Adding together the Δ*G* values for the half-reactions gives Δ*G* for the overall reaction, which is proportional to *both* the potential *and* the number of electrons (*n*) transferred. Spontaneous redox reactions have a negative Δ*G* and therefore a positive *E*<sub>cell</sub>. Because the equilibrium constant *K* is related to Δ*G*, *E*°<sub>cell</sub> and *K* are also related. Large equilibrium constants correspond to large positive values of *E*°. The **Nernst equation** allows us to determine the spontaneous direction of any redox reaction under any reaction conditions from values of the relevant standard electrode potentials. **Concentration cells** consist of anode and cathode compartments that are identical except for the concentrations of the reactant. Because Δ*G* = 0 at equilibrium, the measured potential of a concentration cell is zero at equilibrium (the concentrations are equal). A galvanic cell can also be used to measure the solubility product of a sparingly soluble substance and calculate the concentration of a species given a measured potential and the concentrations of all the other species.

````````````

````````````{important} Key Takeaway

- The Nernst equation can be used to determine the direction of spontaneous reaction for any redox reaction in aqueous solution.

````````````

````````````{important} Key Equations

**Charge on a mole of electrons (faraday)**

[Equation 19.49](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s01-eq02): *F* ≈ 96,486 J/(V·mol)

**Maximum work from an electrochemical cell**

[Equation 19.50](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s01-eq03): *w*<sub>max</sub> = −*nFE*<sub>cell</sub>

**Relationship between Δ** *G* **° and Δ** *E* **°**

[Equation 19.52](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s01-eq05): Δ*G*° = −*nFE*°<sub>cell</sub>

**Relationship between Δ** *G* **° and** *K* **for a redox reaction**

[Equation 19.57](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s03-eq01): Δ*G*° = −*RT* ln *K*

**Relationship between Δ** *E* **° and** *K* **for a redox reaction at 25°C**

[Equation 19.59](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s03-eq03): $E_{\text{cell}}^{{^\circ}} = \left( \frac{RT}{nF} \right)\text{ln~}K$

[Equation 19.60](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s03-eq04): $E_{\text{cell}}^{{^\circ}} = \left( \frac{0.0591\text{~V}}{n} \right)\log K$

**Relationship between Δ** *G* **° and** *Q*

[Equation 19.61](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-eq01): Δ*G* = Δ*G*° + *RT* ln *Q*

**Relationship between** *E* **<sub>cell</sub> and** *Q* **at 25°C**

[Equation 19.64](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-eq04): $E_{\text{cell}}^{{^\circ}} = E_{\text{cell}}^{{^\circ}} - \left( \frac{0.0591\text{~V}}{n} \right)\log Q$

````````````

### Conceptual Problems

1.  State whether you agree or disagree with this reasoning and explain your answer: Standard electrode potentials arise from the number of electrons transferred. The greater the number of electrons transferred, the greater the measured potential difference. If 1 mol of a substance produces 0.76 V when 2 mol of electrons are transferred---as in Zn(s) → Zn<sup>2+</sup>(aq) + 2e<sup>−</sup>---then 0.5 mol of the substance will produce 0.76/2 V because only 1 mol of electrons is transferred.

2.  What is the relationship between the *measured cell potential* and the *total charge* that passes through a cell? Which of these is dependent on concentration? Which is dependent on the identity of the oxidant or the reductant? Which is dependent on the number of electrons transferred?

3.  In the equation *w*<sub>max</sub> = −*nFE*°<sub>cell</sub>, which quantities are extensive properties and which are intensive properties?

4.  For any spontaneous redox reaction, *E* is positive. Use thermodynamic arguments to explain why this is true.

5.  State whether you agree or disagree with this statement and explain your answer: Electrochemical methods are especially useful in determining the reversibility or irreversibility of reactions that take place in a cell.

6.  Although the sum of two half-reactions gives another half-reaction, the sum of the potentials of the two half-reactions cannot be used to obtain the potential of the net half-reaction. Why? When does the sum of two half-reactions correspond to the overall reaction? Why?

7.  Occasionally, you will find high-quality electronic equipment that has its electronic components plated in gold. What is the advantage of this?

8.  Blood analyzers, which measure pH, $P_{\text{CO}_{2}}\text{,}$ and $P_{\text{O}_{2}}\text{,}$ are frequently used in clinical emergencies. For example, blood $P_{\text{CO}_{2}}$ is measured with a pH electrode covered with a plastic membrane that is permeable to CO<sub>2</sub>. Based on your knowledge of how electrodes function, explain how such an electrode might work. Hint: CO<sub>2</sub>(g) + H<sub>2</sub>O(l) → HCO<sub>3</sub><sup>−</sup>(aq) + H<sup>+</sup>(aq).

9.  Concentration cells contain the same species in solution in two different compartments. Explain what produces a voltage in a concentration cell. When does V = 0 in such a cell?

10. Describe how an electrochemical cell can be used to measure the solubility of a sparingly soluble salt.

### Answers

1.  

2.  

3.  extensive: *w*<sub>max</sub> and *n*; intensive: *E*°<sub>cell</sub>

4.  

5.  

6.  

7.  Gold is highly resistant to corrosion because of its very positive reduction potential.

8.  

9.  

10. 

### Numerical Problems

1.  The chemical equation for the combustion of butane is as follows:

    $$\left. \text{C}_{4}\text{H}_{10}\text{(g)} + \frac{13}{2}\text{O}_{2}\text{(g)}\rightarrow 4\text{CO}_{2}\text{(g)} + 5\text{H}_{2}\text{O(g)} \right.$$

    This reaction has Δ*H*° = −2877 kJ/mol. Calculate *E*°<sub>cell</sub> and then determine Δ*G*°. Is this a spontaneous process? What is the change in entropy that accompanies this process at 298 K?

2.  How many electrons are transferred during the reaction Pb(s) + Hg<sub>2</sub>Cl<sub>2</sub>(s) → PbCl<sub>2</sub>(aq) + 2Hg(l)? What is the standard cell potential? Is the oxidation of Pb by Hg<sub>2</sub>Cl<sub>2</sub> spontaneous? Calculate Δ*G*° for this reaction.

3.  For the cell represented as Al(s)∣Al<sup>3+</sup>(aq)∥Sn<sup>2+</sup>(aq), Sn<sup>4+</sup>(aq)∣Pt(s), how many electrons are transferred in the redox reaction? What is the standard cell potential? Is this a spontaneous process? What is Δ*G*°?

4.  Explain why the sum of the potentials for the half-reactions Sn<sup>2+</sup>(aq) + 2e<sup>−</sup> → Sn(s) and Sn<sup>4+</sup>(aq) + 2e<sup>−</sup> → Sn<sup>2+</sup>(aq) does not equal the potential for the reaction Sn<sup>4+</sup>(aq) + 4e<sup>−</sup> → Sn(s). What is the net cell potential? Compare the values of Δ*G*° for the sum of the potentials and the actual net cell potential.

5.  Based on [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) and [Chapter 29 \"Appendix E: Standard Reduction Potentials at 25°C\"](/appendices/appendix-e-standard-reduction-.md#src-averill-1-0-ch96appe), do you agree with the proposed potentials for the following half-reactions? Why or why not?

    1.  Cu<sup>2+</sup>(aq) + 2e<sup>−</sup> → Cu(s), *E*° = 0.68 V
    2.  Ce<sup>4+</sup>(aq) + 4e<sup>−</sup> → Ce(s), *E*° = −0.62 V

6.  For each reaction, calculate *E*°<sub>cell</sub> and then determine Δ*G*°. Indicate whether each reaction is spontaneous.

    1.  2Na(s) + 2H<sub>2</sub>O(l) → 2NaOH(aq) + H<sub>2</sub>(g)
    2.  K<sub>2</sub>S<sub>2</sub>O<sub>6</sub>(aq) + I<sub>2</sub>(s) → 2KI(aq) + 2K<sub>2</sub>SO<sub>4</sub>(aq)
    3.  Sn(s) + CuSO<sub>4</sub>(aq) → Cu(s) + SnSO<sub>4</sub>(aq)

7.  What is the standard change in free energy for the reaction between Ca<sup>2+</sup> and Na(s) to give Ca(s) and Na<sup>+</sup>? Do the sign and magnitude of Δ*G*° agree with what you would expect based on the positions of these elements in the periodic table? Why or why not?

8.  In acidic solution, permanganate (MnO<sub>4</sub><sup>−</sup>) oxidizes Cl<sup>−</sup> to chlorine gas, and MnO<sub>4</sub><sup>−</sup> is reduced to Mn<sup>2+</sup>(aq).

    1.  Write the balanced chemical equation for this reaction.
    2.  Determine *E*°<sub>cell</sub>.
    3.  Calculate the equilibrium constant.

9.  Potentiometric titrations are an efficient method for determining the endpoint of a redox titration. In such a titration, the potential of the solution is monitored as measured volumes of an oxidant or a reductant are added. Data for a typical titration, the potentiometric titration of Fe(II) with a 0.1 M solution of Ce(IV), are given in the following table. The starting potential has been arbitrarily set equal to zero because it is the *change* in potential with the addition of the oxidant that is important.

    ````````{list-table}
    :header-rows: 1

    - - Titrant (mL)
      - *E* (mV)
    - - 2.00
      - 50
    - - 6.00
      - 100
    - - 9.00
      - 255
    - - 10.00
      - 960
    - - 11.00
      - 1325
    - - 12.00
      - 1625
    - - 14.00
      - 1875

    ````````

    1.  Write the balanced chemical equation for the oxidation of Fe<sup>2+</sup> by Ce<sup>4+</sup>.
    2.  Plot the data and then locate the endpoint.
    3.  How many millimoles of Fe<sup>2+</sup> did the solution being titrated originally contain?

10. The standard electrode potential (*E*°) for the half-reaction Ni<sup>2+</sup>(aq) + 2e<sup>−</sup> → Ni(s) is −0.257 V. What pH is needed for this reaction to take place in the presence of 1.00 atm H<sub>2</sub>(g) as the reductant if \[Ni<sup>2+</sup>\] is 1.00 M?

11. The reduction of Mn(VII) to Mn(s) by H<sub>2</sub>(g) proceeds in five steps that can be readily followed by changes in the color of the solution. Here is the redox chemistry:

    1.  MnO<sub>4</sub><sup>−</sup>(aq) + e<sup>−</sup> → MnO<sub>4</sub><sup>2−</sup>(aq); *E*° = +0.56 V (purple → dark green)
    2.  MnO<sub>4</sub><sup>2−</sup>(aq) + 2e<sup>−</sup> + 4H<sup>+</sup>(aq) → MnO<sub>2</sub>(s); *E*° = +2.26 V (dark green → dark brown solid)
    3.  MnO<sub>2</sub>(s) + e<sup>−</sup> + 4H<sup>+</sup>(aq) → Mn<sup>3+</sup>(aq); *E*° = +0.95 V (dark brown solid → red-violet)
    4.  Mn<sup>3+</sup>(aq) + e<sup>−</sup> → Mn<sup>2+</sup>(aq); *E*° = +1.51 V (red-violet → pale pink)
    5.  Mn<sup>2+</sup>(aq) + 2e<sup>−</sup> → Mn(s); *E*° = −1.18 V (pale pink → colorless)

    <!-- -->

    1.  Is the reduction of MnO<sub>4</sub><sup>−</sup> to Mn<sup>3+</sup>(aq) by H<sub>2</sub>(g) spontaneous under standard conditions? What is *E*°<sub>cell</sub>?
    2.  Is the reduction of Mn<sup>3+</sup>(aq) to Mn(s) by H<sub>2</sub>(g) spontaneous under standard conditions? What is *E*°<sub>cell</sub>?

12. Mn(III) can disproportionate (both oxidize and reduce itself) by means of the following half-reactions:

    $$\begin{array}{ll}
    \left. \text{Mn}^{3 +}\text{(aq)} + \text{e}^{-}\rightarrow\text{Mn}^{2 +}\text{(aq)} \right. & {E{^\circ} = 1.\text{51~V}}
    \end{array}$$

    $$\begin{array}{ll}
    \left. \text{Mn}^{3 +}\text{(aq)} + 2\text{H}_{2}\text{O(l)}\rightarrow\text{MnO}_{2}\text{(s)} + 4\text{H}^{+}\text{(aq)} + \text{e}^{-} \right. & {E{^\circ} = 0.95\text{~V}}
    \end{array}$$

    1.  What is *E*° for the disproportionation reaction?
    2.  Is disproportionation more or less thermodynamically favored at low pH than at pH 7.0? Explain your answer.
    3.  How could you prevent the disproportionation reaction from occurring?

13. For the reduction of oxygen to water, *E*° = 1.23 V. What is the potential for this half-reaction at pH 7.00? What is the potential in a 0.85 M solution of NaOH?

14. The biological molecule abbreviated as NADH (reduced nicotinamide adenine dinucleotide) can be formed by reduction of NAD<sup>+</sup> (nicotinamide adenine dinucleotide) via the half-reaction NAD<sup>+</sup> + H<sup>+</sup> + 2e<sup>−</sup> → NADH; *E*° = −0.32 V.

    1.  Would NADH be able to reduce acetate to pyruvate?
    2.  Would NADH be able to reduce pyruvate to lactate?
    3.  What potential is needed to convert acetate to lactate?

    $$\begin{array}{ll}
    \left. \text{acetate~} + \text{~CO}_{2} + \text{2H}^{+} + \text{2e}^{-}\rightarrow\text{pyruvate~} + \text{H}_{\text{2}}\text{O} \right. & {E{^\circ} = - 0.\text{70~V}}
    \end{array}$$

    $$\begin{array}{ll}
    \left. \text{pyruvate~} + \text{~2H}^{+} + \text{2e}^{-}\rightarrow\text{~lactate~} \right. & {E{^\circ} = - 0.\text{185~V}}
    \end{array}$$

15. Given the following biologically relevant half-reactions, will FAD (flavin adenine dinucleotide), a molecule used to transfer electrons whose reduced form is FADH<sub>2</sub>, be an effective oxidant for the conversion of acetaldehyde to acetate at pH 4.00?

    $$\begin{array}{ll}
    \left. \text{acetate~} + \text{~2H}^{+} + \text{2e}^{-}\rightarrow\text{acetaldehyde} + \text{H}_{\text{2}}\text{O} \right. & {E{^\circ} = - 0.\text{58~V}}
    \end{array}$$

    $$\begin{array}{ll}
    \left. \text{FAD~} + \text{~2H}^{+} + \text{2e}^{-}\rightarrow\text{FADH}_{\text{2}} \right. & {E{^\circ} = - 0.\text{18~V}}
    \end{array}$$

16. Ideally, any half-reaction with *E*° \> 1.23 V will oxidize water as a result of the half-reaction O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>−</sup> → 2H<sub>2</sub>O(l).

    1.  Will FeO<sub>4</sub><sup>2−</sup> oxidize water if the half-reaction for the reduction of Fe(VI) → Fe(III) is FeO<sub>4</sub><sup>2−</sup>(aq) + 8H<sup>+</sup>(aq) + 3e<sup>−</sup> → Fe<sup>3+</sup>(aq) + 4H<sub>2</sub>O; *E*° = 1.9 V?
    2.  What is the highest pH at which this reaction will proceed spontaneously if \[Fe<sup>3+</sup>\] = \[FeO<sub>4</sub><sup>2−</sup>\] = 1.0 M and $P_{\text{O}_{2}}$ = 1.0 atm?

17. Under acidic conditions, ideally any half-reaction with *E*° \> 1.23 V will oxidize water via the reaction O<sub>2</sub>(g) + 4H<sup>+</sup>(aq) + 4e<sup>−</sup> → 2H<sub>2</sub>O(l).

    1.  Will aqueous acidic KMnO<sub>4</sub> evolve oxygen with the formation of MnO<sub>2</sub>?
    2.  At pH 14.00, what is *E*° for the oxidation of water by aqueous KMnO<sub>4</sub> (1 M) with the formation of MnO<sub>2</sub>?
    3.  At pH 14.00, will water be oxidized if you are trying to form MnO<sub>2</sub> from MnO<sub>4</sub><sup>2−</sup> via the reaction 2MnO<sub>4</sub><sup>2−</sup>(aq) + 2H<sub>2</sub>O(l) → 2MnO<sub>2</sub>(s) + O<sub>2</sub>(g) + 4OH<sup>−</sup>(aq)?

18. Complexing agents can bind to metals and result in the net stabilization of the complexed species. What is the net thermodynamic stabilization energy that results from using CN<sup>−</sup> as a complexing agent for Mn<sup>3+</sup>/Mn<sup>2+</sup>?

    $$\begin{array}{ll}
    \left. \text{Mn}^{3 +}\text{(aq)} + \text{e}^{-}\rightarrow\text{Mn}^{2 +}\text{(aq)} \right. & {E{^\circ} = 1.\text{51~V}}
    \end{array}$$

    $$\begin{array}{ll}
    \left. \text{Mn(CN)}_{6}{}^{3 -}\text{(aq)} + \text{e}^{-}\rightarrow\text{Mn(CN)}_{6}{}^{4 -} \right. & {E{^\circ} = - 0.\text{24~V}}
    \end{array}$$

19. You have constructed a cell with zinc and lead amalgam electrodes described by the cell diagram Zn(Hg)(s)∣Zn(NO<sub>3</sub>)<sub>2</sub>(aq)∥Pb(NO<sub>3</sub>)<sub>2</sub>(aq)∣Pb(Hg)(s). If you vary the concentration of Zn(NO<sub>3</sub>)<sub>2</sub> and measure the potential at different concentrations, you obtain the following data:

    ````````{list-table}
    :header-rows: 1

    - - Zn(NO<sub>3</sub>)<sub>2</sub> (M)
      - *E*<sub>cell</sub> (V)
    - - 0.0005
      - 0.7398
    - - 0.002
      - 0.7221
    - - 0.01
      - 0.7014

    ````````

    1.  Write the half-reactions that occur in this cell.
    2.  What is the overall redox reaction?
    3.  What is *E*°<sub>cell</sub>? What is Δ*G*° for the overall reaction?
    4.  What is the equilibrium constant for this redox reaction?

20. Hydrogen gas reduces Ni<sup>2+</sup> according to the following reaction: Ni<sup>2+</sup>(aq) + H<sub>2</sub>(g) → Ni(s) + 2H<sup>+</sup>(aq); *E*°<sub>cell</sub> = −0.25 V; Δ*H* = 54 kJ/mol.

    1.  What is *K* for this redox reaction?
    2.  Is this reaction likely to occur?
    3.  What conditions can be changed to increase the likelihood that the reaction will occur as written?
    4.  Is the reaction more likely to occur at higher or lower pH?

21. The silver--silver bromide electrode has a standard potential of 0.07133 V. What is *K*<sub>sp</sub> of AgBr?

### Answers

1.  

2.  

3.  6e<sup>−</sup>; *E*°<sub>cell</sub> = 1.813 V; the reaction is spontaneous; Δ*G*° = −525 kJ/mol Al.

4.  

5.  

6.  

7.  

8.  

9.  

10. 

11. 

12. 

13. 

14. 

15. yes; *E*° = 0.40 V

16. 

17. 1.  yes; *E*° = 0.45 V
    2.  0.194 V
    3.  yes; *E*° = 0.20 V

18. 

19. 

20. 

21. 

(src-averill-1-0-ch19-s05)=

## 19.5 Commercial Galvanic Cells

````````````{note} Learning Objective

1.  To learn how commercial galvanic cells work.

````````````

Because galvanic cells can be self-contained and portable, they can be used as batteries and fuel cells. A battery (storage cell)[^chem-30] is a galvanic cell (or a series of galvanic cells) that contains all the reactants needed to produce electricity. In contrast, a fuel cell[^chem-31] is a galvanic cell that requires a constant external supply of one or more reactants to generate electricity. In this section, we describe the chemistry behind some of the more common types of batteries and fuel cells.

(src-averill-1-0-ch19-s05-s01)=

### Batteries

There are two basic kinds of batteries: *disposable*, or *primary*, batteries, in which the electrode reactions are effectively irreversible and which cannot be recharged; and *rechargeable*, or *secondary*, batteries, which form an insoluble product that adheres to the electrodes. These batteries can be recharged by applying an electrical potential in the reverse direction. The recharging process temporarily converts a rechargeable battery from a galvanic cell to an electrolytic cell.

Batteries are cleverly engineered devices that are based on the same fundamental laws as galvanic cells. The major difference between batteries and the galvanic cells we have previously described is that commercial batteries use solids or pastes rather than solutions as reactants to maximize the electrical output per unit mass. The use of highly concentrated or solid reactants has another beneficial effect: the concentrations of the reactants and the products do not change greatly as the battery is discharged; consequently, the output voltage remains remarkably constant during the discharge process. This behavior is in contrast to that of the Zn/Cu cell, whose output decreases logarithmically as the reaction proceeds ([Figure 19.11 \"The Variation of \"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-f01)). When a battery consists of more than one galvanic cell, the cells are usually connected in series---that is, with the positive (+) terminal of one cell connected to the negative (−) terminal of the next, and so forth. The overall voltage of the battery is therefore the sum of the voltages of the individual cells.

#### Leclanché Dry Cell

The dry cell, by far the most common type of battery, is used in flashlights, electronic devices such as the Walkman and Game Boy, and many other devices. Although the dry cell was patented in 1866 by the French chemist Georges Leclanché and more than 5 billion such cells are sold every year, the details of its electrode chemistry are still not completely understood. In spite of its name, the Leclanché dry cell[^chem-32] is actually a "wet cell": the electrolyte is an acidic water-based paste containing MnO<sub>2</sub>, NH<sub>4</sub>Cl, ZnCl<sub>2</sub>, graphite, and starch (part (a) in [Figure 19.13 \"Three Kinds of Primary (Nonrechargeable) Batteries\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s05-s01-s03-f01)). The half-reactions at the anode and the cathode can be summarized as follows:

Equation 19.74

cathode: 2MnO<sub>2</sub>(s) + 2NH<sub>4</sub><sup>+</sup>(aq) + 2e<sup>−</sup> → Mn<sub>2</sub>O<sub>3</sub>(s) + 2NH<sub>3</sub>(aq) + H<sub>2</sub>O(l)

Equation 19.75

anode: Zn(s) → Zn<sup>2+</sup>(aq) + 2e<sup>−</sup>

The Zn<sup>2+</sup> ions formed by the oxidation of Zn(s) at the anode react with NH<sub>3</sub> formed at the cathode and Cl<sup>−</sup> ions present in solution, so the overall cell reaction is as follows:

Equation 19.76

overall: 2MnO<sub>2</sub>(s) + 2NH<sub>4</sub>Cl(aq) + Zn(s) → Mn<sub>2</sub>O<sub>3</sub>(s) + Zn(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>(s) + H<sub>2</sub>O(l)

The dry cell produces about 1.55 V and is inexpensive to manufacture. It is not, however, very efficient in producing electrical energy because only the relatively small fraction of the MnO<sub>2</sub> that is near the cathode is actually reduced and only a small fraction of the zinc cathode is actually consumed as the cell discharges. In addition, dry cells have a limited shelf life because the Zn anode reacts spontaneously with NH<sub>4</sub>Cl in the electrolyte, causing the case to corrode and allowing the contents to leak out.

The alkaline battery[^chem-33] is essentially a Leclanché cell adapted to operate under alkaline, or basic, conditions. The half-reactions that occur in an alkaline battery are as follows:

Equation 19.77

cathode: 2MnO<sub>2</sub>(s) + H<sub>2</sub>O(l) + 2e<sup>−</sup> → Mn<sub>2</sub>O<sub>3</sub>(s) + 2OH<sup>−</sup>(aq)

Equation 19.78

anode: Zn(s) + 2OH<sup>−</sup>(aq) → ZnO(s) + H<sub>2</sub>O(l) + 2e<sup>−</sup>

Equation 19.79

$$\text{overall:~}\left. \text{Zn(s)~} + \text{~2MnO}_{\text{2}}\text{(s)}\rightarrow\text{ZnO(s)} + \text{Mn}_{\text{2}}\text{O}_{\text{3}}\text{(s)} \right.$$

This battery also produces about 1.5 V, but it has a longer shelf life and more constant output voltage as the cell is discharged than the Leclanché dry cell. Although the alkaline battery is more expensive to produce than the Leclanché dry cell, the improved performance makes this battery more cost-effective.

#### Button Batteries

Although some of the small *button* batteries used to power watches, calculators, and cameras are miniature alkaline cells, most are based on a completely different chemistry. In these batteries, the anode is a zinc--mercury amalgam rather than pure zinc, and the cathode uses either HgO or Ag<sub>2</sub>O as the oxidant rather than MnO<sub>2</sub> (part (b) in [Figure 19.13 \"Three Kinds of Primary (Nonrechargeable) Batteries\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s05-s01-s03-f01)). The cathode and overall reactions and cell output for these two types of button batteries are as follows:

Equation 19.80

cathode (Hg): HgO(s) + H<sub>2</sub>O(l) + 2e<sup>−</sup> → Hg(l) + 2OH<sup>−</sup>(aq)

Equation 19.81

$$\left. \text{overall~(Hg):~Zn(s)~} + \ 2\text{HgO(s)}\rightarrow\text{Hg(l)} + \text{ZnO(s)}\quad E_{\text{cell}} = 1.35\text{~V} \right.$$

Equation 19.82

cathode (Ag): Ag<sub>2</sub>O(s) + H<sub>2</sub>O(l) + 2e<sup>−</sup> → 2Ag(s) + 2OH<sup>−</sup>(aq)

Equation 19.83

$$\left. \text{overall~(Ag):~Zn(s)~} + \ 2\text{Ag}_{2}\text{O(s)}\rightarrow 2\text{Ag(s)} + \text{ZnO(s)}\quad E_{\text{cell}} = 1.6\text{~V} \right.$$

The major advantages of the mercury and silver cells are their reliability and their high output-to-mass ratio. These factors make them ideal for applications where small size is crucial, as in cameras and hearing aids. The disadvantages are the expense and the environmental problems caused by the disposal of heavy metals, such as Hg and Ag.

#### Lithium--Iodine Battery

None of the batteries described above is actually "dry." They all contain small amounts of liquid water, which adds significant mass and causes potential corrosion problems. Consequently, substantial effort has been expended to develop water-free batteries.

One of the few commercially successful water-free batteries is the lithium--iodine battery[^chem-34]. The anode is lithium metal, and the cathode is a solid complex of I<sub>2</sub>. Separating them is a layer of solid LiI, which acts as the electrolyte by allowing the diffusion of Li<sup>+</sup> ions. The electrode reactions are as follows:

Equation 19.84

cathode: I<sub>2</sub>(s) + 2e<sup>−</sup> → 2I<sup>−</sup>(LiI)

Equation 19.85

anode: 2Li(s) → 2Li<sup>+</sup>(LiI) + 2e<sup>−</sup>

Equation 19.86

$$\text{overall:~}\left. \text{2Li(s)~} + \text{~I}_{2}\text{(s)}\rightarrow 2\text{LiI(s)} \right.\quad E_{\text{cell}} = 3.5\text{~V}$$ ![Cardiac pacemaker. An x-ray of a patient showing the location and size of a pacemaker powered by a lithium--iodine battery.](/images/section_23/ad96c6b58f46a41eb574d4b699b2c5a5.jpg)

**Cardiac pacemaker.** An x-ray of a patient showing the location and size of a pacemaker powered by a lithium--iodine battery.

As shown in part (c) in [Figure 19.13 \"Three Kinds of Primary (Nonrechargeable) Batteries\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s05-s01-s03-f01), a typical lithium--iodine battery consists of two cells separated by a nickel metal mesh that collects charge from the anode. Because of the high internal resistance caused by the solid electrolyte, only a low current can be drawn. Nonetheless, such batteries have proven to be long-lived (up to 10 yr) and reliable. They are therefore used in applications where frequent replacement is difficult or undesirable, such as in cardiac pacemakers and other medical implants and in computers for memory protection. These batteries are also used in security transmitters and smoke alarms. Other batteries based on lithium anodes and solid electrolytes are under development, using TiS<sub>2</sub>, for example, for the cathode.

(src-averill-1-0-ch19-s05-s01-s03-f01)=

Figure 19.13 Three Kinds of Primary (Nonrechargeable) Batteries

![Figure 19.13 Three Kinds of Primary (Nonrechargeable) Batteries](/images/section_23/efb88aaf5493e18d3fd9bf19fe69bb22.jpg)

\(a\) A Leclanché dry cell is actually a "wet cell," in which the electrolyte is an acidic water-based paste containing MnO<sub>2</sub>, NH<sub>4</sub>Cl, ZnCl<sub>2</sub>, graphite, and starch. Though inexpensive to manufacture, the cell is not very efficient in producing electrical energy and has a limited shelf life. (b) In a button battery, the anode is a zinc--mercury amalgam, and the cathode can be either HgO (shown here) or Ag<sub>2</sub>O as the oxidant. Button batteries are reliable and have a high output-to-mass ratio, which allows them to be used in applications such as calculators and watches, where their small size is crucial. (c) A lithium--iodine battery consists of two cells separated by a metallic nickel mesh that collects charge from the anodes. The anode is lithium metal, and the cathode is a solid complex of I<sub>2</sub>. The electrolyte is a layer of solid LiI that allows Li<sup>+</sup> ions to diffuse from the cathode to the anode. Although this type of battery produces only a relatively small current, it is highly reliable and long-lived.

Dry cells, button batteries, and lithium--iodine batteries are disposable and cannot be recharged once they are discharged. Rechargeable batteries, in contrast, offer significant economic and environmental advantages because they can be recharged and discharged numerous times. As a result, manufacturing and disposal costs drop dramatically for a given number of hours of battery usage. Two common rechargeable batteries are the nickel--cadmium battery and the lead--acid battery, which we describe next.

#### Nickel--Cadmium (NiCad) Battery

The nickel--cadmium[^chem-35], or *NiCad*, battery is used in small electrical appliances and devices like drills, portable vacuum cleaners, and AM/FM digital tuners. It is a water-based cell with a cadmium anode and a highly oxidized nickel cathode that is usually described as the nickel(III) oxo-hydroxide, NiO(OH). As shown in [Figure 19.14 \"The Nickel--Cadmium (NiCad) Battery, a Rechargeable Battery\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s05-s01-s04-f01), the design maximizes the surface area of the electrodes and minimizes the distance between them, which decreases internal resistance and makes a rather high discharge current possible.

(src-averill-1-0-ch19-s05-s01-s04-f01)=

Figure 19.14 The Nickel--Cadmium (NiCad) Battery, a Rechargeable Battery

![Figure 19.14 The Nickel--Cadmium (NiCad) Battery, a Rechargeable Battery](/images/section_23/9027e68b61af042c56f8215265c08a09.jpg)

NiCad batteries contain a cadmium anode and a highly oxidized nickel cathode. This design maximizes the surface area of the electrodes and minimizes the distance between them, which gives the battery both a high discharge current and a high capacity.

The electrode reactions during the discharge of a NiCad battery are as follows:

Equation 19.87

cathode: 2NiO(OH)(s) + 2H<sub>2</sub>O(l) + 2e<sup>−</sup> → 2Ni(OH)<sub>2</sub>(s) + 2OH<sup>−</sup>(aq)

Equation 19.88

anode: Cd(s) + 2OH<sup>−</sup>(aq) → Cd(OH)<sub>2</sub>(s) + 2e<sup>−</sup>

Equation 19.89

$$\text{overall:~}\left. \text{Cd(s)} + 2\text{NiO(OH)(s)} + 2\text{H}_{2}\text{O(l)}\rightarrow\text{Cd(OH)}_{2}\text{(s)} + 2\text{Ni}{(\text{OH})}_{2}\text{(s)} \right.\quad E_{\text{cell}} = 1.4\text{~V}$$

Because the products of the discharge half-reactions are solids that adhere to the electrodes \[Cd(OH)<sub>2</sub> and 2Ni(OH)<sub>2</sub>\], the overall reaction is readily reversed when the cell is recharged. Although NiCad cells are lightweight, rechargeable, and high capacity, they have certain disadvantages. For example, they tend to lose capacity quickly if not allowed to discharge fully before recharging, they do not store well for long periods when fully charged, and they present significant environmental and disposal problems because of the toxicity of cadmium.

A variation on the NiCad battery is the nickel--metal hydride battery (NiMH) used in hybrid automobiles, wireless communication devices, and mobile computing. The overall chemical equation for this type of battery is as follows:

NiO(OH)(s) + MH → Ni(OH)<sub>2</sub>(s) + M(s)

The NiMH battery has a 30%--40% improvement in capacity over the NiCad battery; it is more environmentally friendly so storage, transportation, and disposal are not subject to environmental control; and it is not as sensitive to recharging memory. It is, however, subject to a 50% greater self-discharge rate, a limited service life, and higher maintenance, and it is more expensive than the NiCad battery.

#### Lead--Acid (Lead Storage) Battery

The lead--acid battery[^chem-36] is used to provide the starting power in virtually every automobile and marine engine on the market. Marine and car batteries typically consist of multiple cells connected in series. The total voltage generated by the battery is the potential per cell (*E*°<sub>cell</sub>) times the number of cells. As shown in [Figure 19.15 \"One Cell of a Lead--Acid Battery\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s05-s01-s05-f01), the anode of each cell in a lead storage battery is a plate or grid of spongy lead metal, and the cathode is a similar grid containing powdered lead dioxide (PbO<sub>2</sub>). The electrolyte is usually an approximately 37% solution (by mass) of sulfuric acid in water, with a density of 1.28 g/mL (about 4.5 M H<sub>2</sub>SO<sub>4</sub>). Because the redox active species are solids, there is no need to separate the electrodes. The electrode reactions in each cell during discharge are as follows:

Equation 19.90

$$\left. \text{cathode:~PbO}_{2}\text{(s)} + \text{HSO}_{4}{}^{-}\text{(aq)} + 3\text{H}^{+}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{PbSO}_{4}\text{(s)} + 2\text{H}_{2}\text{O(l)}\quad E_{\text{cathode}}^{{^\circ}} = 1.685\text{~V} \right.$$

Equation 19.91

$$\left. \text{anode:~Pb(s)~} + \text{~HSO}_{4}{}^{-}\text{(aq)}\rightarrow\text{PbSO}_{4}\text{(s)} + \text{H}^{+}\text{(aq)} + 2\text{e}^{-}\quad E_{\text{anode}}^{{^\circ}} = - 0.356\text{~V} \right.$$

Equation 19.92

$$\text{overall:~}\left. \text{Pb(s)~} + \text{~PbO}_{2}\text{(s)} + 2\text{HSO}_{4}{}^{-}\text{(aq)} + 2\text{H}^{+}\text{(aq)}\rightarrow 2\text{PbSO}_{4}(\text{s}) + 2\text{H}_{2}\text{O(l)} \right.\quad E_{\text{cell}}^{{^\circ}} = 2.041\text{~V}$$

(src-averill-1-0-ch19-s05-s01-s05-f01)=

Figure 19.15 One Cell of a Lead--Acid Battery

![Figure 19.15 One Cell of a Lead--Acid Battery](/images/section_23/78aa3b26627849dbff802309a826d49a.jpg)

The anodes in each cell of a rechargeable battery are plates or grids of lead containing spongy lead metal, while the cathodes are similar grids containing powdered lead dioxide (PbO<sub>2</sub>). The electrolyte is an aqueous solution of sulfuric acid. The value of *E*° for such a cell is about 2 V. Connecting three such cells in series produces a 6 V battery, whereas a typical 12 V car battery contains six cells in series. When treated properly, this type of high-capacity battery can be discharged and recharged many times over.

As the cell is discharged, a powder of PbSO<sub>4</sub> forms on the electrodes. Moreover, sulfuric acid is consumed and water is produced, decreasing the density of the electrolyte and providing a convenient way of monitoring the status of a battery by simply measuring the density of the electrolyte.

![Source: Photo courtesy of Mitchclanky2008, http://www.flickr.com/photos/25597837@N05/2422765479/ .](/images/section_23/17a1d3b4e4120c76f0e59d8673a48fe0.jpg)

Source: Photo courtesy of Mitchclanky2008, <http://www.flickr.com/photos/25597837@N05/2422765479/>.

When an external voltage in excess of 2.04 V per cell is applied to a lead--acid battery, the electrode reactions reverse, and PbSO<sub>4</sub> is converted back to metallic lead and PbO<sub>2</sub>. If the battery is recharged too vigorously, however, electrolysis of water can occur, resulting in the evolution of potentially explosive hydrogen gas. (For more information on electrolysis, see [Section 19.7 \"Electrolysis\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07).) The gas bubbles formed in this way can dislodge some of the PbSO<sub>4</sub> or PbO<sub>2</sub> particles from the grids, allowing them to fall to the bottom of the cell, where they can build up and cause an internal short circuit. Thus the recharging process must be carefully monitored to optimize the life of the battery. With proper care, however, a lead--acid battery can be discharged and recharged thousands of times. In automobiles, the alternator supplies the electric current that causes the discharge reaction to reverse.

### Fuel Cells

A fuel cell is a galvanic cell that requires a constant external supply of reactants because the products of the reaction are continuously removed. Unlike a battery, it does not store chemical or electrical energy; a fuel cell allows electrical energy to be extracted directly from a chemical reaction. In principle, this should be a more efficient process than, for example, burning the fuel to drive an internal combustion engine that turns a generator, which is typically less than 40% efficient, and in fact, the efficiency of a fuel cell is generally between 40% and 60%. Unfortunately, significant cost and reliability problems have hindered the wide-scale adoption of fuel cells. In practice, their use has been restricted to applications in which mass may be a significant cost factor, such as US manned space vehicles.

These space vehicles use a hydrogen/oxygen fuel cell that requires a continuous input of H<sub>2</sub>(g) and O<sub>2</sub>(g), as illustrated in [Figure 19.16 \"A Hydrogen Fuel Cell Produces Electrical Energy Directly from a Chemical Reaction\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s05-s02-f01). The electrode reactions are as follows:

Equation 19.93

cathode: O<sub>2</sub>(g) + 4H<sup>+</sup> + 4e<sup>−</sup> → 2H<sub>2</sub>O(g)

Equation 19.94

anode: 2H<sub>2</sub>(g) → 4H<sup>+</sup> + 4e<sup>−</sup>

Equation 19.95

$$\text{overall:~}\left. \text{2H}_{\text{2}}\text{(g)} + \text{O}_{\text{2}}\text{(g)}\rightarrow\text{2H}_{\text{2}}\text{O(g)} \right.$$

(src-averill-1-0-ch19-s05-s02-f01)=

Figure 19.16 A Hydrogen Fuel Cell Produces Electrical Energy Directly from a Chemical Reaction

![Figure 19.16 A Hydrogen Fuel Cell Produces Electrical Energy Directly from a Chemical Reaction](/images/section_23/e26f9d07bec9214ec1f9209bf81bc1d0.jpg)

Hydrogen is oxidized to protons at the anode, and the electrons are transferred through an external circuit to the cathode, where oxygen is reduced and combines with H<sup>+</sup> to form water. A solid electrolyte allows the protons to diffuse from the anode to the cathode. Although fuel cells are an essentially pollution-free means of obtaining electrical energy, their expense and technological complexity have thus far limited their applications.

The overall reaction represents an essentially pollution-free conversion of hydrogen and oxygen to water, which in space vehicles is then collected and used. Although this type of fuel cell should produce 1.23 V under standard conditions, in practice the device achieves only about 0.9 V. One of the major barriers to achieving greater efficiency is the fact that the four-electron reduction of O<sub>2</sub>(g) at the cathode is intrinsically rather slow, which limits current that can be achieved. All major automobile manufacturers have major research programs involving fuel cells: one of the most important goals is the development of a better catalyst for the reduction of O<sub>2</sub>.

````````````{important} Summary

A **battery** is a contained unit that produces electricity, whereas a **fuel cell** is a galvanic cell that requires a constant external supply of one or more reactants to generate electricity. One type of battery is the **Leclanché dry cell**, which contains an electrolyte in an acidic water-based paste. This battery is called an **alkaline battery** when adapted to operate under alkaline conditions. Button batteries have a high output-to-mass ratio; **lithium--iodine batteries** consist of a solid electrolyte; the **nickel--cadmium** (NiCad) battery is rechargeable; and the **lead--acid battery**, which is also rechargeable, does not require the electrodes to be in separate compartments. A fuel cell requires an external supply of reactants as the products of the reaction are continuously removed. In a fuel cell, energy is not stored; electrical energy is provided by a chemical reaction.

````````````

````````````{important} Key Takeaway

- Commercial batteries are galvanic cells that use solids or pastes as reactants to maximize the electrical output per unit mass.

````````````

### Conceptual Problems

1.  What advantage is there to using an alkaline battery rather than a Leclanché dry cell?

2.  Why does the density of the fluid in lead--acid batteries drop when the battery is discharged?

3.  What type of battery would you use for each application and why?

    1.  powering an electric motor scooter
    2.  a backup battery for a smartphone
    3.  powering an iPod

4.  Why are galvanic cells used as batteries and fuel cells? What is the difference between a battery and a fuel cell? What is the advantage to using highly concentrated or solid reactants in a battery?

### Answer

1.  
2.  
3.  1.  lead storage battery
    2.  lithium--iodine battery
    3.  NiCad, NiMH, or lithium ion battery (rechargeable)
4.  

### Numerical Problem

1.  This reaction is characteristic of a lead storage battery:

    Pb(s) + PbO<sub>2</sub>(s) + 2H<sub>2</sub>SO<sub>4</sub>(aq) → 2PbSO<sub>4</sub>(s) + 2H<sub>2</sub>O(l)

    If you have a battery with an electrolyte that has a density of 1.15 g/cm<sup>3</sup> and contains 30.0% sulfuric acid by mass, is the potential greater than or less than that of the standard cell?

### Answer

1.  \[H<sub>2</sub>SO<sub>4</sub>\] = 3.52 M; *E* \> *E*°

(src-averill-1-0-ch19-s06)=

## 19.6 Corrosion

````````````{note} Learning Objective

1.  To understand the process of corrosion.

````````````

Corrosion[^chem-37] is a galvanic process by which metals deteriorate through oxidation---usually but not always to their oxides. For example, when exposed to air, iron rusts, silver tarnishes, and copper and brass acquire a bluish-green surface called a *patina*. Of the various metals subject to corrosion, iron is by far the most important commercially. An estimated \$100 billion per year is spent in the United States alone to replace iron-containing objects destroyed by corrosion. Consequently, the development of methods for protecting metal surfaces from corrosion constitutes a very active area of industrial research. In this section, we describe some of the chemical and electrochemical processes responsible for corrosion. We also examine the chemical basis for some common methods for preventing corrosion and treating corroded metals.

````````````{important} Note the Pattern

Corrosion is a galvanic process.

````````````

Under ambient conditions, the oxidation of most metals is thermodynamically spontaneous, with the notable exception of gold and platinum. Hence it is actually somewhat surprising that any metals are useful at all in Earth's moist, oxygen-rich atmosphere. Some metals, however, are resistant to corrosion for kinetic reasons. For example, aluminum in soft-drink cans and airplanes is protected by a thin coating of metal oxide that forms on the surface of the metal and acts as an impenetrable barrier that prevents further destruction. Aluminum cans also have a thin plastic layer to prevent reaction of the oxide with acid in the soft drink. Chromium, magnesium, and nickel also form protective oxide films. Stainless steels are remarkably resistant to corrosion because they usually contain a significant proportion of chromium, nickel, or both.

In contrast to these metals, when iron corrodes, it forms a red-brown hydrated metal oxide (Fe<sub>2</sub>O<sub>3</sub>·*x*H<sub>2</sub>O), commonly known as *rust*, that does not provide a tight protective film ([Figure 19.17 \"Rust, the Result of Corrosion of Metallic Iron\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s06-f01)). Instead, the rust continually flakes off to expose a fresh metal surface vulnerable to reaction with oxygen and water. Because both oxygen and water are required for rust to form, an iron nail immersed in deoxygenated water will not rust---even over a period of several weeks. Similarly, a nail immersed in an organic solvent such as kerosene or mineral oil saturated with oxygen will not rust because of the absence of water.

(src-averill-1-0-ch19-s06-f01)=

Figure 19.17 Rust, the Result of Corrosion of Metallic Iron

![Figure 19.17 Rust, the Result of Corrosion of Metallic Iron](/images/section_23/28f7e127eabcc9de2916eefc451f6e03.jpg)

Iron is oxidized to Fe<sup>2+</sup>(aq) at an anodic site on the surface of the iron, which is often an impurity or a lattice defect. Oxygen is reduced to water at a different site on the surface of the iron, which acts as the cathode. Electrons are transferred from the anode to the cathode through the electrically conductive metal. Water is a solvent for the Fe<sup>2+</sup> that is produced initially and acts as a salt bridge. Rust (Fe<sub>2</sub>O<sub>3</sub>·*x*H<sub>2</sub>O) is formed by the subsequent oxidation of Fe<sup>2+</sup> by atmospheric oxygen.

In the corrosion process, iron metal acts as the anode in a galvanic cell and is oxidized to Fe<sup>2+</sup>; oxygen is reduced to water at the cathode. The relevant reactions are as follows:

Equation 19.96

$$\left. \text{cathode:~O}_{2}\text{(g)} + 4\text{H}^{+}\text{(aq)} + 4\text{e}^{-}\rightarrow 2\text{H}_{2}\text{O(l)}\quad E{^\circ} = 1.23\text{~V} \right.$$

Equation 19.97

$$\left. \text{anode:~Fe(s)}\rightarrow\text{Fe}^{2 +}\text{(aq)} + 2\text{e}^{-}\quad E{^\circ} = - 0.45\text{~V} \right.$$

(src-averill-1-0-ch19-s06-eq03)=

Equation 19.98

$$\text{overall:~}\left. \text{2Fe(s)~} + \text{~O}_{2}\text{(g)} + 4\text{H}^{+}\text{(aq)}\rightarrow 2\text{Fe}^{2 +}\text{(aq)} + \text{2H}_{2}\text{O(l)} \right.\quad E{^\circ} = 1.68\text{~V}$$

The Fe<sup>2+</sup> ions produced in the initial reaction are then oxidized by atmospheric oxygen to produce the insoluble hydrated oxide containing Fe<sup>3+</sup>, as represented in the following equation:

Equation 19.99

4Fe<sup>2+</sup>(aq) + O<sub>2</sub>(g) + (2 + 4*x*)H<sub>2</sub>O → 2Fe<sub>2</sub>O<sub>3</sub>·*x*H<sub>2</sub>O + 4H<sup>+</sup>(aq)

The sign and magnitude of *E*° for the corrosion process ([Equation 19.98](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s06-eq03)) indicate that there is a strong driving force for the oxidation of iron by O<sub>2</sub> under standard conditions (1 M H<sup>+</sup>). Under neutral conditions, the driving force is somewhat less but still appreciable (*E* = 1.25 V at pH 7.0). Normally, the reaction of atmospheric CO<sub>2</sub> with water to form H<sup>+</sup> and HCO<sub>3</sub><sup>−</sup> provides a low enough pH to enhance the reaction rate, as does acid rain. (For more information on acid rain, see [Chapter 4 \"Reactions in Aqueous Solution\"](/chapters/ch-04-reactions-in-aqueous-solution.md#src-averill-1-0-ch04), [Section 4.7 \"The Chemistry of Acid Rain\"](/chapters/ch-04-reactions-in-aqueous-solution.md#src-averill-1-0-ch04-s07).) Automobile manufacturers spend a great deal of time and money developing paints that adhere tightly to the car's metal surface to prevent oxygenated water, acid, and salt from coming into contact with the underlying metal. Unfortunately, even the best paint is subject to scratching or denting, and the electrochemical nature of the corrosion process means that two scratches relatively remote from each other can operate together as anode and cathode, leading to sudden mechanical failure ([Figure 19.18 \"Small Scratches in a Protective Paint Coating Can Lead to the Rapid Corrosion of Iron\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s06-f02)).

(src-averill-1-0-ch19-s06-f02)=

Figure 19.18 Small Scratches in a Protective Paint Coating Can Lead to the Rapid Corrosion of Iron

![Figure 19.18 Small Scratches in a Protective Paint Coating Can Lead to the Rapid Corrosion of Iron](/images/section_23/8e4c195ffca81016ecf39f948642121c.jpg)

Holes in a protective coating allow oxygen to be reduced at the surface with the greater exposure to air (the cathode), while metallic iron is oxidized to Fe<sup>2+</sup>(aq) at the less exposed site (the anode). Rust is formed when Fe<sup>2+</sup>(aq) diffuses to a location where it can react with atmospheric oxygen, which is often remote from the anode. The electrochemical interaction between cathodic and anodic sites can cause a large pit to form *under* a painted surface, eventually resulting in sudden failure with little visible warning that corrosion has occurred.

One of the most common techniques used to prevent the corrosion of iron is applying a protective coating of another metal that is more difficult to oxidize. Faucets and some external parts of automobiles, for example, are often coated with a thin layer of chromium using an electrolytic process that will be discussed in [Section 19.7 \"Electrolysis\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07). With the increased use of polymeric materials in cars, however, the use of chrome-plated steel has diminished in recent years. Similarly, the "tin cans" that hold soups and other foods are actually made of steel coated with a thin layer of tin. Neither chromium nor tin is intrinsically resistant to corrosion, but both form protective oxide coatings.

As with a protective paint, scratching a protective metal coating will allow corrosion to occur. In this case, however, the presence of the second metal can actually increase the rate of corrosion. The values of the standard electrode potentials for Sn<sup>2+</sup> (*E*° = −0.14 V) and Fe<sup>2+</sup> (*E*° = −0.45 V) in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) show that Fe is more easily oxidized than Sn. As a result, the more corrosion-resistant metal (in this case, tin) accelerates the corrosion of iron by acting as the cathode and providing a large surface area for the reduction of oxygen ([Figure 19.19 \"Galvanic Corrosion\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s06-f03)). This process is seen in some older homes where copper and iron pipes have been directly connected to each other. The less easily oxidized copper acts as the cathode, causing iron to dissolve rapidly near the connection and occasionally resulting in a catastrophic plumbing failure.

(src-averill-1-0-ch19-s06-f03)=

Figure 19.19 Galvanic Corrosion

![Figure 19.19 Galvanic Corrosion](/images/section_23/ce5bafdab1d1e4e0c8df22870f153136.jpg)

If iron is in contact with a more corrosion-resistant metal such as tin, copper, or lead, the other metal can act as a large cathode that greatly increases the rate of reduction of oxygen. Because the reduction of oxygen is coupled to the oxidation of iron, this can result in a dramatic increase in the rate at which iron is oxidized at the anode. Galvanic corrosion is likely to occur whenever two dissimilar metals are connected directly, allowing electrons to be transferred from one to the other.

One way to avoid these problems is to use a more easily oxidized metal to protect iron from corrosion. In this approach, called *cathodic protection*, a more reactive metal such as Zn (*E*° = −0.76 V for Zn<sup>2+</sup> + 2e<sup>−</sup> → Zn) becomes the anode, and iron becomes the cathode. This prevents oxidation of the iron and protects the iron object from corrosion. The reactions that occur under these conditions are as follows:

Equation 19.100

cathode: O<sub>2</sub>(g) + 4e<sup>−</sup> + 4H<sup>+</sup>(aq) → 2H<sub>2</sub>O(l)

Equation 19.101

anode: Zn(s) → Zn<sup>2+</sup>(aq) + 2e<sup>−</sup>

(src-averill-1-0-ch19-s06-eq07)=

Equation 19.102

$$\text{overall:~}\left. \text{2Zn(s)~} + \text{~O}_{\text{2}}\text{(g)} + \text{4H}^{+}\text{(aq)}\rightarrow\text{2Zn}^{\text{2+}}\text{(aq)} + \text{2H}_{\text{2}}\text{O(l)} \right.$$

The more reactive metal reacts with oxygen and will eventually dissolve, "sacrificing" itself to protect the iron object. Cathodic protection is the principle underlying *galvanized steel*, which is steel protected by a thin layer of zinc. Galvanized steel is used in objects ranging from nails to garbage cans. In a similar strategy, sacrificial electrodes[^chem-38] using magnesium, for example, are used to protect underground tanks or pipes ([Figure 19.20 \"The Use of a Sacrificial Electrode to Protect Against Corrosion\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s06-f04)). Replacing the sacrificial electrodes is more cost-effective than replacing the iron objects they are protecting.

(src-averill-1-0-ch19-s06-f04)=

Figure 19.20 The Use of a Sacrificial Electrode to Protect Against Corrosion

![Figure 19.20 The Use of a Sacrificial Electrode to Protect Against Corrosion](/images/section_23/06ebc176ac158067a2c4b8fdf423381a.jpg)

Connecting a magnesium rod to an underground steel pipeline protects the pipeline from corrosion. Because magnesium (*E*° = −2.37 V) is much more easily oxidized than iron (*E*° = −0.45 V), the Mg rod acts as the anode in a galvanic cell. The pipeline is therefore forced to act as the cathode at which oxygen is reduced. The soil between the anode and the cathode acts as a salt bridge that completes the electrical circuit and maintains electrical neutrality. As Mg(s) is oxidized to Mg<sup>2+</sup> at the anode, anions in the soil, such as nitrate, diffuse toward the anode to neutralize the positive charge. Simultaneously, cations in the soil, such as H<sup>+</sup> or NH<sub>4</sub><sup>+</sup>, diffuse toward the cathode, where they replenish the protons that are consumed as oxygen is reduced. A similar strategy uses many miles of somewhat less reactive zinc wire to protect the Alaska oil pipeline.

### Example 13

Suppose an old wooden sailboat, held together with iron screws, has a bronze propeller (recall that bronze is an alloy of copper containing about 7%--10% tin).

1.  If the boat is immersed in seawater, what corrosion reaction will occur? What is *E*°<sub>cell</sub>?
2.  How could you prevent this corrosion from occurring?

**Given:** identity of metals

**Asked for:** corrosion reaction, *E*°<sub>cell</sub>, and preventive measures

**Strategy:**

**A** Write the reactions that occur at the anode and the cathode. From these, write the overall cell reaction and calculate *E*°<sub>cell</sub>.

**B** Based on the relative redox activity of various substances, suggest possible preventive measures.

**Solution:**

1.  **A** According to [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01), both copper and tin are less active metals than iron (i.e., they have higher positive values of *E*° than iron). Thus if tin or copper is brought into electrical contact by seawater with iron in the presence of oxygen, corrosion will occur. We therefore anticipate that the bronze propeller will act as the cathode at which O<sub>2</sub> is reduced, and the iron screws will act as anodes at which iron dissolves:

    $$\begin{array}{lll}
    \text{cathode:} & \left. \text{O}_{2}\text{(s)} + \text{4H}^{+}\text{(aq)} + 4\text{e}^{-}\rightarrow 2\text{H}_{2}\text{O(l)} \right. & {E_{\text{cathode}}^{{^\circ}} = 1.23\text{~V}} \\
    \text{anode:} & \left. \text{Fe(s)}\rightarrow\text{Fe}^{2 +} + 2\text{e}^{-} \right. & {E_{\text{anode}}^{{^\circ}} = - 0.45\text{~V}} \\
    \text{overall:} & \left. \text{2Fe(s)~} + \text{~O}_{2}\text{(g)} + 4\text{H}^{+}\text{(aq)}\rightarrow 2\text{Fe}^{2 +}\text{(aq)} + 2\text{H}_{2}\text{O(l)} \right. & {E_{\text{cell}}^{{^\circ}} = 1.68\text{~V}}
    \end{array}$$

    Over time, the iron screws will dissolve, and the boat will fall apart.

2.  **B** Possible ways to prevent corrosion, in order of decreasing cost and inconvenience, are as follows: disassembling the boat and rebuilding it with bronze screws; removing the boat from the water and storing it in a dry place; or attaching an inexpensive piece of zinc metal to the propeller shaft to act as a sacrificial electrode and replacing it once or twice a year. Because zinc is a more active metal than iron, it will act as the sacrificial anode in the electrochemical cell and dissolve ([Equation 19.102](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s06-eq07)).

Exercise

Suppose the water pipes leading into your house are made of lead, while the rest of the plumbing in your house is iron. To eliminate the possibility of lead poisoning, you call a plumber to replace the lead pipes. He quotes you a very low price if he can use up his existing supply of copper pipe to do the job.

1.  Do you accept his proposal?
2.  What else should you have the plumber do while at your home?

**Answer:**

1.  Not unless you plan to sell the house very soon because the Cu/Fe pipe joints will lead to rapid corrosion.
2.  Any existing Pb/Fe joints should be examined carefully for corrosion of the iron pipes due to the Pb--Fe junction; the less active Pb will have served as the cathode for the reduction of O<sub>2</sub>, promoting oxidation of the more active Fe nearby.

````````````{important} Summary

The deterioration of metals through oxidation is a galvanic process called **corrosion**. Protective coatings consist of a second metal that is more difficult to oxidize than the metal being protected. Alternatively, a more easily oxidized metal can be applied to a metal surface, thus providing cathodic protection of the surface. A thin layer of zinc protects galvanized steel. **Sacrificial electrodes** can also be attached to an object to protect it.

````````````

````````````{important} Key Takeaway

- Corrosion is a galvanic process that can be prevented using cathodic protection.

````````````

### Conceptual Problems

1.  Do you expect a bent nail to corrode more or less rapidly than a straight nail? Why?

2.  What does it mean when a metal is described as being coated with a sacrificial layer? Is this different from galvanic protection?

3.  Why is it important for automobile manufacturers to apply paint to the metal surface of a car? Why is this process particularly important for vehicles in northern climates, where salt is used on icy roads?

### Answer

1.  

2.  

3.  Paint keeps oxygen and water from coming into direct contact with the metal, which prevents corrosion. Paint is more necessary because salt is an electrolyte that increases the conductivity of water and facilitates the flow of electric current between anodic and cathodic sites.

(src-averill-1-0-ch19-s07)=

## 19.7 Electrolysis

````````````{note} Learning Objective

1.  To understand electrolysis and describe it quantitatively.

````````````

In this chapter, we have described various galvanic cells in which a spontaneous chemical reaction is used to generate electrical energy. In an electrolytic cell, however, the opposite process, called electrolysis[^chem-39], occurs: an external voltage is applied to drive a nonspontaneous reaction ([Figure 19.1 \"Electrochemical Cells\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s01-f01)). In this section, we look at how electrolytic cells are constructed and explore some of their many commercial applications.

````````````{important} Note the Pattern

In an electrolytic cell, an external voltage is applied to drive a nonspontaneous reaction.

````````````

### Electrolytic Cells

If we construct an electrochemical cell in which one electrode is copper metal immersed in a 1 M Cu<sup>2+</sup> solution and the other electrode is cadmium metal immersed in a 1 M Cd<sup>2+</sup> solution and then close the circuit, the potential difference between the two compartments will be 0.74 V. The cadmium electrode will begin to dissolve (Cd is oxidized to Cd<sup>2+</sup>) and is the anode, while metallic copper will be deposited on the copper electrode (Cu<sup>2+</sup> is reduced to Cu), which is the cathode (part (a) in [Figure 19.21 \"An Applied Voltage Can Reverse the Flow of Electrons in a Galvanic Cd/Cu Cell\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07-s01-f01)). The overall reaction is as follows:

Equation 19.103

$$\begin{array}{ll}
\left. \text{Cd(s)} + \text{Cu}^{2 +}\text{(aq)}\rightarrow\text{Cd}^{2 +}\text{(aq)} + \text{Cu(s)} \right. & {E_{\text{cell}}^{{^\circ}} = 0.74\text{~V}}
\end{array}$$

This reaction is thermodynamically spontaneous as written (Δ*G*° \< 0):

Equation 19.104

$$\Delta G{^\circ} = - nFE_{\text{cell}}^{{^\circ}} = - (2\cancel{\text{mol}}\text{e}^{-})\lbrack 96,486\text{~J/}(\cancel{\text{V}} \cdot \cancel{\text{mol}})\rbrack(0.74\cancel{\text{V}}) = - 140\text{~kJ~(per~mole~Cd)}$$

In this direction, the system is acting as a galvanic cell.

(src-averill-1-0-ch19-s07-s01-f01)=

Figure 19.21 An Applied Voltage Can Reverse the Flow of Electrons in a Galvanic Cd/Cu Cell

![Figure 19.21 An Applied Voltage Can Reverse the Flow of Electrons in a Galvanic Cd/Cu Cell](/images/section_23/21422283a5bcc2908009993f6bbce8d1.jpg)

\(a\) When compartments that contain a Cd electrode immersed in 1 M Cd<sup>2+</sup>(aq) and a Cu electrode immersed in 1 M Cu<sup>2+</sup>(aq) are connected to create a galvanic cell, Cd(s) is spontaneously oxidized to Cd<sup>2+</sup>(aq) at the anode, and Cu<sup>2+</sup>(aq) is spontaneously reduced to Cu(s) at the cathode. The potential of the galvanic cell is 0.74 V. (b) Applying an external potential greater than 0.74 V in the reverse direction forces electrons to flow from the Cu electrode \[which is now the anode, at which metallic Cu(s) is oxidized to Cu<sup>2+</sup>(aq)\] and into the Cd electrode \[which is now the cathode, at which Cd<sup>2+</sup>(aq) is reduced to Cd(s)\]. The anode in an electrolytic cell is *positive* because electrons are flowing from it, whereas the cathode is *negative* because electrons are flowing into it.

The reverse reaction, the reduction of Cd<sup>2+</sup> by Cu, is thermodynamically nonspontaneous and will occur only with an *input* of 140 kJ. We can force the reaction to proceed in the reverse direction by applying an electrical potential greater than 0.74 V from an external power supply. The applied voltage forces electrons through the circuit in the reverse direction, converting a galvanic cell to an electrolytic cell. Thus the copper electrode is now the anode (Cu is oxidized), and the cadmium electrode is now the cathode (Cd<sup>2+</sup> is reduced) (part (b) in [Figure 19.21 \"An Applied Voltage Can Reverse the Flow of Electrons in a Galvanic Cd/Cu Cell\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07-s01-f01)). The signs of the cathode and the anode have switched to reflect the flow of electrons in the circuit. The half-reactions that occur at the cathode and the anode are as follows:

Equation 19.105

$$\left. \text{cathode:~Cd}^{2 +}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{Cd(s)}\quad E_{\text{cathode}}^{{^\circ}} = - 0.40\text{~V} \right.$$

Equation 19.106

$$\left. \text{anode:~Cu(s)}\rightarrow\text{Cu}^{2 +}\text{(aq)} + 2\text{e}^{-}\quad E_{\text{anode}}^{{^\circ}} = 0.34\text{~V} \right.$$

Equation 19.107

$$\begin{array}{lll}
\text{overall:} & \left. \text{Cd}^{2 +}\text{(aq)} + \text{Cu(s)}\rightarrow\text{Cd(s)} + \text{Cu}^{2 +}\text{(aq)} \right. & {E_{\text{cell}}^{{^\circ}} = - 0.74\text{~V}}
\end{array}$$

Because *E*°<sub>cell</sub> \< 0, the overall reaction---the reduction of Cd<sup>2+</sup> by Cu---clearly cannot occur spontaneously and proceeds only when sufficient electrical energy is applied. The differences between galvanic and electrolytic cells are summarized in [Table 19.3 \"Comparison of Galvanic and Electrolytic Cells\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07-s01-t01).

(src-averill-1-0-ch19-s07-s01-t01)=

Table 19.3 Comparison of Galvanic and Electrolytic Cells

````````{list-table}
:header-rows: 1

- - Property
  - Galvanic Cell
  - Electrolytic Cell
- - Δ*G*
  - \< 0
  - \> 0
- - *E* <sub>cell</sub>
  - \> 0
  - \< 0
- - **Electrode Process**
  -  
  -  
- - anode
  - oxidation
  - oxidation
- - cathode
  - reduction
  - reduction
- - **Sign of Electrode**
  -  
  -  
- - anode
  - −
  - \+
- - cathode
  - \+
  - −

````````

### Electrolytic Reactions

At sufficiently high temperatures, ionic solids melt to form liquids that conduct electricity extremely well due to the high concentrations of ions. If two inert electrodes are inserted into molten NaCl, for example, and an electrical potential is applied, Cl<sup>−</sup> is oxidized at the anode, and Na<sup>+</sup> is reduced at the cathode. The overall reaction is as follows:

Equation 19.108

2NaCl(l) → 2Na(l) + Cl<sub>2</sub>(g)

This is the reverse of the formation of NaCl from its elements. The product of the reduction reaction is *liquid* sodium because the melting point of sodium metal is 97.8°C, well below that of NaCl (801°C). Approximately 20,000 tons of sodium metal are produced commercially in the United States each year by the electrolysis of molten NaCl in a *Downs cell* ([Figure 19.22 \"A Downs Cell for the Electrolysis of Molten NaCl\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07-s02-f01)). In this specialized cell, CaCl<sub>2</sub> (melting point = 772°C) is first added to the NaCl to lower the melting point of the mixture to about 600°C, thereby lowering operating costs.

(src-averill-1-0-ch19-s07-s02-f01)=

Figure 19.22 A Downs Cell for the Electrolysis of Molten NaCl

![Figure 19.22 A Downs Cell for the Electrolysis of Molten NaCl](/images/section_23/b26ae4bda6a924adbb1d4b6bcba78cb1.jpg)

The electrolysis of a molten mixture of NaCl and CaCl<sub>2</sub> results in the formation of elemental sodium and chlorine gas. Because sodium is a liquid under these conditions and liquid sodium is less dense than molten sodium chloride, the sodium floats to the top of the melt and is collected in concentric capped iron cylinders surrounding the cathode. Gaseous chlorine collects in the inverted cone over the anode. An iron screen separating the cathode and anode compartments ensures that the molten sodium and gaseous chlorine do not come into contact.

Similarly, in the *Hall--Heroult process* used to produce aluminum commercially, a molten mixture of about 5% aluminum oxide (Al<sub>2</sub>O<sub>3</sub>; melting point = 2054°C) and 95% cryolite (Na<sub>3</sub>AlF<sub>6</sub>; melting point = 1012°C) is electrolyzed at about 1000°C, producing molten aluminum at the cathode and CO<sub>2</sub> gas at the carbon anode. The overall reaction is as follows:

Equation 19.109

2Al<sub>2</sub>O<sub>3</sub>(l) + 3C(s) → 4Al(l) + 3CO<sub>2</sub>(g)

Oxide ions react with oxidized carbon at the anode, producing CO<sub>2</sub>(g).

There are two important points to make about these two commercial processes and about the electrolysis of molten salts in general.

1.  The electrode potentials for molten salts are likely to be very different from the standard cell potentials listed in [Table 19.2 \"Standard Potentials for Selected Reduction Half-Reactions at 25°C\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s03-t01) and [Chapter 29 \"Appendix E: Standard Reduction Potentials at 25°C\"](/appendices/appendix-e-standard-reduction-.md#src-averill-1-0-ch96appe), which are compiled for the reduction of the hydrated ions in aqueous solutions under standard conditions.
2.  Using a mixed salt system means there is a possibility of competition between different electrolytic reactions. When a mixture of NaCl and CaCl<sub>2</sub> is electrolyzed, Cl<sup>−</sup> is oxidized because it is the only anion present, but either Na<sup>+</sup> or Ca<sup>2+</sup> can be reduced. Conversely, in the Hall--Heroult process, only one cation is present that can be reduced (Al<sup>3+</sup>), but there are three species that can be oxidized: C, O<sup>2−</sup>, and F<sup>−</sup>.

In the Hall--Heroult process, C is oxidized instead of O<sup>2−</sup> or F<sup>−</sup> because oxygen and fluorine are more electronegative than carbon, which means that C is a weaker oxidant than either O<sub>2</sub> or F<sub>2</sub>. Similarly, in the Downs cell, we might expect electrolysis of a NaCl/CaCl<sub>2</sub> mixture to produce calcium rather than sodium because Na is slightly less electronegative than Ca (χ = 0.93 versus 1.00, respectively), making Na easier to oxidize and, conversely, Na<sup>+</sup> more difficult to reduce. In fact, the reduction of Na<sup>+</sup> to Na is the observed reaction. In cases where the electronegativities of two species are similar, other factors, such as the formation of complex ions, become important and may determine the outcome.

### Example 14

If a molten mixture of MgCl<sub>2</sub> and KBr is electrolyzed, what products will form at the cathode and the anode, respectively?

**Given:** identity of salts

**Asked for:** electrolysis products

**Strategy:**

**A** List all the possible reduction and oxidation products. Based on the electronegativity values shown in [Figure 7.5 \"Definitions of the Atomic Radius\"](/chapters/ch-07-the-periodic-table-and-periodi.md#src-averill-1-0-ch07-s02-s01-f02), determine which species will be reduced and which species will be oxidized.

**B** Identify the products that will form at each electrode.

**Solution:**

**A** The possible reduction products are Mg and K, and the possible oxidation products are Cl<sub>2</sub> and Br<sub>2</sub>. Because Mg is more electronegative than K (χ = 1.31 versus 0.82), it is likely that Mg will be reduced rather than K. Because Cl is more electronegative than Br (3.16 versus 2.96), Cl<sub>2</sub> is a stronger oxidant than Br<sub>2</sub>.

**B** Electrolysis will therefore produce Br<sub>2</sub> at the anode and Mg at the cathode.

Exercise

Predict the products if a molten mixture of AlBr<sub>3</sub> and LiF is electrolyzed.

**Answer:** Br<sub>2</sub> and Al

Electrolysis can also be used to drive the thermodynamically nonspontaneous decomposition of water into its constituent elements: H<sub>2</sub> and O<sub>2</sub>. However, because pure water is a very poor electrical conductor, a small amount of an ionic solute (such as H<sub>2</sub>SO<sub>4</sub> or Na<sub>2</sub>SO<sub>4</sub>) must first be added to increase its electrical conductivity. Inserting inert electrodes into the solution and applying a voltage between them will result in the rapid evolution of bubbles of H<sub>2</sub> and O<sub>2</sub> ([Figure 19.23 \"The Electrolysis of Water\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07-s02-f02)). The reactions that occur are as follows:

Equation 19.110

$$\left. \text{cathode:~2H}^{+}\text{(aq)} + 2\text{e}^{-}\rightarrow\text{H}_{2}\text{(g)}\quad E_{\text{cathode}}^{{^\circ}} = 0\text{~V} \right.$$

Equation 19.111

$$\left. \text{anode:~2H}_{2}\text{O(l)}\rightarrow\text{O}_{2}\text{(g)} + 4\text{H}^{+}\text{(aq)} + 4\text{e}^{-}\quad E_{\text{anode}}^{{^\circ}} = 1.23\text{~V} \right.$$

Equation 19.112

$$\text{overall:~}\left. \text{2H}_{2}\text{O(l)}\rightarrow\text{O}_{2}\text{(g)} + 2\text{H}_{2}\text{(g)} \right.\quad E_{\text{cell}}^{{^\circ}} = - 1.23\text{~V}$$

(src-averill-1-0-ch19-s07-s02-f02)=

Figure 19.23 The Electrolysis of Water

![Figure 19.23 The Electrolysis of Water](/images/section_23/04cf6955d71f99d7e7b614709971d10c.jpg)

Applying an external potential of about 1.7--1.9 V to two inert electrodes immersed in an aqueous solution of an electrolyte such as H<sub>2</sub>SO<sub>4</sub> or Na<sub>2</sub>SO<sub>4</sub> drives the thermodynamically nonspontaneous decomposition of water into H<sub>2</sub> at the cathode and O<sub>2</sub> at the anode.

For a system that contains an electrolyte such as Na<sub>2</sub>SO<sub>4</sub>, which has a negligible effect on the ionization equilibrium of liquid water, the pH of the solution will be 7.00 and \[H<sup>+</sup>\] = \[OH<sup>−</sup>\] = 1.0 × 10<sup>−7</sup>. Assuming that $P_{\text{O}_{\text{2}}}$ = $P_{\text{H}_{\text{2}}}$ = 1 atm, we can use the standard potentials and [Equation 19.64](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s04-s04-eq04) to calculate *E* for the overall reaction:

Equation 19.113

$$\begin{array}{ll}
E_{\text{cell}} & {= E_{\text{cell}}^{{^\circ}} - \left( \frac{0.0591\text{~V}}{n} \right)\log\left( {P_{\text{O}_{2}}P_{\text{H}_{2}}^{2}} \right)} \\
E_{\text{cell}} & {= - 1.23\text{~V} - \left( \frac{0.0591\text{~V}}{4} \right)\log(1) = - 1.23\text{~V}}
\end{array}$$

Thus *E*<sub>cell</sub> is −1.23 V, which is the value of *E*°<sub>cell</sub> if the reaction is carried out in the presence of 1 M H<sup>+</sup> rather than at pH 7.0.

In practice, a voltage about 0.4--0.6 V greater than the calculated value is needed to electrolyze water. This added voltage, called an overvoltage[^chem-40], represents the additional driving force required to overcome barriers such as the large activation energy for the formation of a gas at a metal surface. Overvoltages are needed in all electrolytic processes, which explain why, for example, approximately 14 V must be applied to recharge the 12 V battery in your car.

In general, any metal that does *not* react readily with water to produce hydrogen can be produced by the electrolytic reduction of an aqueous solution that contains the metal cation. The *p*-block metals and most of the transition metals are in this category, but metals in high oxidation states, which form oxoanions, cannot be reduced to the metal by simple electrolysis. Active metals, such as aluminum and those of groups 1 and 2, react so readily with water that they can be prepared only by the electrolysis of molten salts. Similarly, any nonmetallic element that does not readily oxidize water to O<sub>2</sub> can be prepared by the electrolytic oxidation of an aqueous solution that contains an appropriate anion. In practice, among the nonmetals, only F<sub>2</sub> cannot be prepared using this method. Oxoanions of nonmetals in their highest oxidation states, such as NO<sub>3</sub><sup>−</sup>, SO<sub>4</sub><sup>2−</sup>, PO<sub>4</sub><sup>3−</sup>, are usually difficult to reduce electrochemically and usually behave like spectator ions that remain in solution during electrolysis.

````````````{important} Note the Pattern

In general, any metal that does not react readily with water to produce hydrogen can be produced by the electrolytic reduction of an aqueous solution that contains the metal cation.

````````````

### Electroplating

In a process called electroplating[^chem-41], a layer of a second metal is deposited on the metal electrode that acts as the cathode during electrolysis. Electroplating is used to enhance the appearance of metal objects and protect them from corrosion. Examples of electroplating include the chromium layer found on many bathroom fixtures or (in earlier days) on the bumpers and hubcaps of cars, as well as the thin layer of precious metal that coats silver-plated dinnerware or jewelry. In all cases, the basic concept is the same. A schematic view of an apparatus for electroplating silverware and a photograph of a commercial electroplating cell are shown in [Figure 19.24 \"Electroplating\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07-s03-f01).

(src-averill-1-0-ch19-s07-s03-f01)=

Figure 19.24 Electroplating

![Figure 19.24 Electroplating](/images/section_23/d6e7e7e35c7e541f54085d36d5a075e5.jpg)

\(a\) Electroplating uses an electrolytic cell in which the object to be plated, such as a fork, is immersed in a solution of the metal to be deposited. The object being plated acts as the cathode, on which the desired metal is deposited in a thin layer, while the anode usually consists of the metal that is being deposited (in this case, silver) that maintains the solution concentration as it dissolves. (b) In this commercial electroplating apparatus, a large number of objects can be plated simultaneously by lowering the rack into the Ag<sup>+</sup> solution and applying the correct potential.

The half-reactions in electroplating a fork, for example, with silver are as follows:

Equation 19.114

$$\left. \text{cathode~(fork):~Ag}^{+}\text{(aq)} + \text{e}^{-}\rightarrow\text{Ag(s)}\quad E_{\text{cathode}}^{{^\circ}} = 0.80\text{~V} \right.$$

Equation 19.115

$$\left. \text{anode~(silver~bar):~Ag(s)}\rightarrow\text{Ag}^{+}\text{(aq)}\quad E_{\text{anode}}^{{^\circ}} = 0.80\text{~V} \right.$$

The overall reaction is the transfer of silver metal from one electrode (a silver bar acting as the anode) to another (a fork acting as the cathode). Because *E*°<sub>cell</sub> = 0 V, it takes only a small applied voltage to drive the electroplating process. In practice, various other substances may be added to the plating solution to control its electrical conductivity and regulate the concentration of free metal ions, thus ensuring a smooth, even coating.

### Quantitative Considerations

If we know the stoichiometry of an electrolysis reaction, the amount of current passed, and the length of time, we can calculate the amount of material consumed or produced in a reaction. Conversely, we can use stoichiometry to determine the combination of current and time needed to produce a given amount of material.

The quantity of material that is oxidized or reduced at an electrode during an electrochemical reaction is determined by the stoichiometry of the reaction and the amount of charge that is transferred. For example, in the reaction Ag<sup>+</sup>(aq) + e<sup>−</sup> → Ag(s), 1 mol of electrons reduces 1 mol of Ag<sup>+</sup> to Ag metal. In contrast, in the reaction Cu<sup>2+</sup>(aq) + 2e<sup>−</sup> → Cu(s), 1 mol of electrons reduces only 0.5 mol of Cu<sup>2+</sup> to Cu metal. Recall that the charge on 1 mol of electrons is 1 faraday (1 *F*), which is equal to 96,486 C. We can therefore calculate the number of moles of electrons transferred when a known current is passed through a cell for a given period of time. The total charge (C) transferred is the product of the current (A) and the time (*t*, in seconds):

(src-averill-1-0-ch19-s07-s04-eq01)=

Equation 19.116

C = A × *t*

The stoichiometry of the reaction and the total charge transferred enable us to calculate the amount of product formed during an electrolysis reaction or the amount of metal deposited in an electroplating process.

For example, if a current of 0.60 A passes through an aqueous solution of CuSO<sub>4</sub> for 6.0 min, the total number of coulombs of charge that passes through the cell is as follows:

Equation 19.117

$$\text{charge} = (0.60\text{~A})(6.0\ \cancel{\text{min}})(60\text{~s/}\cancel{\min}) = 220\text{~A} \cdot \text{s} = 220\text{~C}$$

The number of moles of electrons transferred to Cu<sup>2+</sup> is therefore

Equation 19.118

$$\text{moles~e}^{-} = \frac{220\ \cancel{\text{C}}}{96,486\ \cancel{\text{C}}\text{/mol}} = 2.3 \times 10^{- 3}\text{~mol~e}^{-}$$

Because two electrons are required to reduce a single Cu<sup>2+</sup> ion, the total number of moles of Cu produced is half the number of moles of electrons transferred, or 1.2 × 10<sup>−3</sup> mol. This corresponds to 76 mg of Cu. In commercial electrorefining processes, much higher currents (greater than or equal to 50,000 A) are used, corresponding to approximately 0.5 *F*/s, and reaction times are on the order of 3--4 weeks.

### Example 15

A silver-plated spoon typically contains about 2.00 g of Ag. If 12.0 h are required to achieve the desired thickness of the Ag coating, what is the average current per spoon that must flow during the electroplating process, assuming an efficiency of 100%?

**Given:** mass of metal, time, and efficiency

**Asked for:** current required

**Strategy:**

**A** Calculate the number of moles of metal corresponding to the given mass transferred.

**B** Write the reaction and determine the number of moles of electrons required for the electroplating process.

**C** Use the definition of the faraday to calculate the number of coulombs required. Then convert coulombs to current in amperes.

**Solution:**

**A** We must first determine the number of moles of Ag corresponding to 2.00 g of Ag:

$$\text{moles~Ag} = \frac{\text{2}\text{.00~}\cancel{\text{g}}}{\text{107}\text{.868~}\cancel{\text{g}}\text{/mol}} = 1.85 \times 10^{- 2}\text{~mol~Ag}$$

**B** The reduction reaction is Ag<sup>+</sup>(aq) + e<sup>−</sup> → Ag(s), so 1 mol of electrons produces 1 mol of silver.

**C** Using the definition of the faraday,

$$\text{coulombs} = (1.85 \times 10^{- 2}\cancel{\text{mol}\text{e}^{-}})(96,486\text{~C/}\cancel{\text{mol}\text{e}^{-}}) = 1.78 \times 10^{3}\text{~C}$$

The current in amperes needed to deliver this amount of charge in 12.0 h is therefore

$$\begin{array}{ll}
\text{amperes} & {= \frac{1.78 \times 10^{3}\text{~C}}{(12.0\ \cancel{\text{h}})(60\cancel{\text{min}}\text{/}\cancel{\text{h}})(60\text{~s/}\cancel{\text{min}})}} \\
 & {= 4.12 \times 10^{- 2}\text{~C/s} = 4.12 \times 10^{- 2}\text{~A}}
\end{array}$$

Because the electroplating process is usually much less than 100% efficient (typical values are closer to 30%), the actual current necessary is greater than 0.1 A.

Exercise

A typical aluminum soft-drink can weighs about 29 g. How much time is needed to produce this amount of Al(s) in the Hall--Heroult process, using a current of 15 A to reduce a molten Al<sub>2</sub>O<sub>3/</sub>Na<sub>3</sub>AlF<sub>6</sub> mixture?

**Answer:** 5.8 h

````````````{important} Summary

In **electrolysis**, an external voltage is applied to drive a nonspontaneous reaction. A Downs cell is used to produce sodium metal from a mixture of salts, and the Hall--Heroult process is used to produce aluminum commercially. Electrolysis can also be used to produce H<sub>2</sub> and O<sub>2</sub> from water. In practice, an additional voltage, called an **overvoltage**, must be applied to overcome factors such as a large activation energy and a junction potential. **Electroplating** is the process by which a second metal is deposited on a metal surface, thereby enhancing an object's appearance or providing protection from corrosion. The amount of material consumed or produced in a reaction can be calculated from the stoichiometry of an electrolysis reaction, the amount of current passed, and the duration of the electrolytic reaction.

````````````

````````````{important} Key Takeaways

- In electrolysis, an external voltage is applied to drive a nonspontaneous reaction.
- The quantity of material oxidized or reduced can be calculated from the stoichiometry of the reaction and the amount of charge transferred.

````````````

````````````{important} Key Equation

**Relationship of charge, current and time**

[Equation 19.116](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07-s04-eq01): C = A × *t*

````````````

### Conceptual Problems

1.  Why might an electrochemical reaction that is thermodynamically favored require an overvoltage to occur?

2.  How could you use an electrolytic cell to make quantitative comparisons of the strengths of various oxidants and reductants?

3.  Why are mixtures of molten salts, rather than a pure salt, generally used during electrolysis?

4.  Two solutions, one containing Fe(NO<sub>3</sub>)<sub>2</sub>·6H<sub>2</sub>O and the other containing the same molar concentration of Fe(NO<sub>3</sub>)<sub>3</sub>·6H<sub>2</sub>O, were electrolyzed under identical conditions. Which solution produced the most metal? Justify your answer.

### Numerical Problems

1.  The electrolysis of molten salts is frequently used in industry to obtain pure metals. How many grams of metal are deposited from these salts for each mole of electrons?

    1.  AlCl<sub>3</sub>
    2.  MgCl<sub>2</sub>
    3.  FeCl<sub>3</sub>

2.  Electrolysis is the most direct way of recovering a metal from its ores. However, the Na<sup>+</sup>(aq)/Na(s), Mg<sup>2+</sup>(aq)/Mg(s), and Al<sup>3+</sup>(aq)/Al(s) couples all have standard electrode potentials (*E*°) more negative than the reduction potential of water at pH 7.0 (−0.42 V), indicating that these metals can never be obtained by electrolysis of aqueous solutions of their salts. Why? What reaction would occur instead?

3.  What volume of chlorine gas at standard temperature and pressure is evolved when a solution of MgCl<sub>2</sub> is electrolyzed using a current of 12.4 A for 1.0 h?

4.  What mass of copper metal is deposited if a 5.12 A current is passed through a Cu(NO<sub>3</sub>)<sub>2</sub> solution for 1.5 h.

5.  What mass of PbO<sub>2</sub> is reduced when a current of 5.0 A is withdrawn over a period of 2.0 h from a lead storage battery?

6.  Electrolysis of Cr<sup>3+</sup>(aq) produces Cr<sup>2+</sup>(aq). If you had 500 mL of a 0.15 M solution of Cr<sup>3+</sup>(aq), how long would it take to reduce the Cr<sup>3+</sup> to Cr<sup>2+</sup> using a 0.158 A current?

7.  Predict the products obtained at each electrode when aqueous solutions of the following are electrolyzed.

    1.  AgNO<sub>3</sub>
    2.  RbI

8.  Predict the products obtained at each electrode when aqueous solutions of the following are electrolyzed.

    1.  MgBr<sub>2</sub>
    2.  Hg(CH<sub>3</sub>CO<sub>2</sub>)<sub>2</sub>
    3.  Al<sub>2</sub>(SO<sub>4</sub>)<sub>3</sub>

### Answers

1.  

2.  

3.  5.2 L

4.  

5.  

6.  

7.  1.  cathode: Ag(s); anode: O<sub>2</sub>(g);
    2.  cathode: H<sub>2</sub>(g); anode: I<sub>2</sub>(s)

8.  

## 19.8 End-of-Chapter Material

### Application Problems

*Problems marked with a* ♦ *involve multiple concepts.*

1.  The percent efficiency of a fuel cell is defined as Δ*G*°/Δ*H*° × 100. If hydrogen gas were distributed for domestic and industrial use from a central electrolysis facility, the gas could be piped to consumers much as methane is piped today. Conventional nuclear power stations have an efficiency of 25%--30%. Use tabulated data to calculate the efficiency of a fuel cell in which the reaction H<sub>2</sub>(g) + 1/2O<sub>2</sub>(g) → H<sub>2</sub>O(g) occurs under standard conditions.

2.  ♦ You are about to run an organic reaction and need a strong oxidant. Although you have BrO<sub>3</sub><sup>−</sup> at your disposal, you prefer to use MnO<sub>4</sub><sup>−</sup>. You notice you also have MnO<sub>2</sub> in the lab.

    1.  Predict whether you will be able to synthesize MnO<sub>4</sub><sup>−</sup> using the materials available to you.
    2.  Write the overall reaction for the synthesis of MnO<sub>4</sub><sup>−</sup>.
    3.  What is Δ*G*° for this reaction?
    4.  What is the equilibrium constant?

3.  It is possible to construct a galvanic cell using amalgams as electrodes, each containing different concentrations of the same metal. One example is the Pb(Hg)(a<sub>1</sub>)∣PbSO<sub>4</sub>(soln)∣Pb(Hg)(a<sub>2</sub>) cell, in which a<sub>1</sub> and a<sub>2</sub> represent the concentrations of lead in the amalgams. No chemical change occurs; rather, the reaction transfers lead from one amalgam to the other, thus altering the Pb concentration in both amalgams. Write an equation for *E* for such a cell.

4.  ♦ The oldest known metallurgical artifacts are beads made from alloys of copper, produced in Egypt, Mesopotamia, and the Indus Valley around 3000 BC. To determine the copper content of alloys such as brass, a sample is dissolved in nitric acid to obtain Cu<sup>2+</sup>(aq), and then the pH is adjusted to 7.0. Excess KI is used to reduce the Cu<sup>2+</sup> to Cu<sup>+</sup> with concomitant oxidation of I<sup>−</sup> to I<sub>2</sub>. The iodine that is produced is then titrated with thiosulfate solution to determine the amount of Cu<sup>2+</sup> in the original solution. The following reactions are involved in the procedure:

    1.  Cu<sup>2+</sup>(aq) + I<sup>−</sup>(aq) + e<sup>−</sup> → CuI(s); *E*° = 0.86 V
    2.  S<sub>4</sub>O<sub>6</sub><sup>2−</sup>(aq) + 2e<sup>−</sup> → 2S<sub>2</sub>O<sub>3</sub><sup>2−</sup>(aq); *E*° = 0.08 V
    3.  NO<sub>3</sub><sup>−</sup>(aq) + 2H<sup>+</sup>(aq) + 2e<sup>−</sup> → NO<sub>2</sub><sup>−</sup>(aq) + H<sub>2</sub>O(l); *E*° = 0.94 V
    4.  I<sub>2</sub>(s) + 2e<sup>−</sup> → 2I<sup>−</sup>(aq); *E*° = 0.54 V

    <!-- -->

    1.  Write a balanced chemical equation for the reaction between nitric acid and Cu(s).
    2.  What is *E*°<sub>cell</sub> for this reaction?
    3.  What is *E*°<sub>cell</sub> for the reaction between thiosulfate and iodine?
    4.  When the pH of the copper(ll) solution is adjusted to 7.0, what is *E* for reduction of nitrate?
    5.  Why is it necessary to adjust the pH of the copper(II) solution before adding KI?
    6.  Use tabulated data to explain why rust (Fe<sub>2</sub>O<sub>3</sub>) is a contaminant that renders this method useless in determining Cu concentrations.

5.  The biological electron transport chain provides for an orderly, stepwise transfer of electrons. Both NADH (reduced nicotinamide adenine dinucleotide) and FADH<sub>2</sub> (reduced flavin adenine dinucleotide) are energy-rich molecules that liberate a large amount of energy during oxidation. Free energy released during the transfer of electrons from either of these molecules to oxygen drives the synthesis of ATP (adenosine triphosphate) formed during respiratory metabolism. The reactions are as follows:

    $$\begin{array}{rccl}
    {\text{NADH} + \text{H}^{+} + \frac{1}{2}\text{O}_{2}} & \left. \rightarrow\text{NAD}^{+} + \text{H}_{2}\text{O} \right. & {\Delta G{^\circ}'} & {= - 52.6\text{~kcal/mol}} \\
    {\text{FADH}_{2} + \frac{1}{2}\text{O}_{2}} & \left. \rightarrow\text{FAD} + \text{H}_{2}\text{O} \right. & {\Delta G{^\circ}'} & {= - 43.4\text{~kcal/mol}}
    \end{array}$$

    The standard potential (*E*°′) for a biological process is defined at pH = 7.0.

    1.  What is *E*°′<sub>cell</sub> for each reaction?
    2.  What is the reduction potential of NAD<sup>+</sup> at pH 7.0?
    3.  What is the reduction potential of FAD at pH 7.0?

6.  While working at a nuclear reactor site, you have been put in charge of reprocessing spent nuclear fuel elements. Your specific task is to reduce Pu(VI) to elemental Pu without reducing U(VI) to elemental U. You have the following information at your disposal:

    $$\begin{array}{rccccc}
    {E{^\circ}} & {\text{UO}_{2}{}^{2 +}} & {\overset{0.05}{\rightarrow}\text{UO}_{2}{}^{+}} & {\overset{0.62}{\rightarrow}\text{U}^{4 +}} & {\overset{- 0.61}{\rightarrow}\text{U}^{3 +}} & {\overset{- 1.85}{\rightarrow}\text{U}} \\
    {E{^\circ}} & {\text{PuO}_{2}{}^{2 +}} & {\overset{0.91}{\rightarrow}\text{PuO}_{2}{}^{+}} & {\overset{1.17}{\rightarrow}\text{Pu}^{4 +}} & {\overset{0.98}{\rightarrow}\text{Pu}^{3 +}} & {\overset{- 2.03}{\rightarrow}\text{Pu}}
    \end{array}$$

    Use tabulated data to decide what reductant will accomplish your task in an acidic solution containing 1.0 M concentrations of both UO<sub>2</sub><sup>2+</sup> and PuO<sub>2</sub><sup>2+</sup>.

7.  Stainless steels typically contain 11% Cr and are resistant to corrosion because of the formation of an oxide layer that can be approximately described as FeCr<sub>2</sub>O<sub>4</sub>, where the iron is Fe(II). The protective layer forms when Cr(II) is oxidized to Cr(III) and Fe is oxidized to Fe(II). Explain how this film prevents the corrosion of Fe to rust, which has the formula Fe<sub>2</sub>O<sub>3</sub>.

8.  ♦ Ion-selective electrodes are powerful tools for measuring specific concentrations of ions in solution. For example, they are used to measure iodide in milk, copper-ion levels in drinking water, fluoride concentrations in toothpastes, and the silver-ion concentration in photographic emulsions and spent fixing solutions. Describe how ion-selective electrodes work and then propose a design for an ion-selective electrode that can be used for measuring water hardness (Ca<sup>2+</sup>, Mg<sup>2+</sup>) in water-conditioning systems.

9.  ♦ Enzymes are proteins that catalyze a specific reaction with a high degree of specificity. An example is the hydrolysis of urea by urease:

    $$\text{NH}_{\text{2}}\text{CONH}_{\text{2}} + \text{2H}_{\text{2}}\text{O} + \text{H}^{+}\overset{\text{urease}}{\rightarrow}\text{2NH}_{\text{4}}{}^{+} + \text{HCO}_{\text{3}}{}^{-}$$

    An enzyme electrode for measuring urea concentrations can be made by coating the surface of a glass electrode with a gel that contains urease.

    1.  Explain what occurs when the electrode is placed in contact with a solution that contains urea.
    2.  What species diffuses through the gel?
    3.  What would be an effective reference electrode?

10. Gas-sensing electrodes can be constructed using a combination electrode that is surrounded by a gas-permeable membrane. For example, to measure CO<sub>2</sub>, a pH electrode and a reference electrode are placed in solution on the "inner" side of a CO<sub>2</sub>-permeable membrane, and the sample solution is placed on the "external" side. As CO<sub>2</sub> diffuses through the membrane, the pH of the internal solution changes due to the reaction CO<sub>2</sub>(g) + H<sub>2</sub>O(l) → HCO<sub>3</sub><sup>−</sup>(aq) + H<sup>+</sup>(aq). Thus the pH of the internal solution varies directly with the CO<sub>2</sub> pressure in the external sample. Ammonia electrodes operate in the same manner. Describe an electrode that would test for ammonia levels in seawater.

11. US submarines that are not nuclear powered use a combination of batteries and diesel engines for their power. When submerged, they are battery driven; when on the surface, they are diesel driven. Why are batteries not used when submarines are on the surface?

12. List some practical considerations in designing a battery to power an electric car.

13. ♦ It is possible to run a digital clock using the power supplied by two potatoes. The clock is connected to two wires: one is attached to a copper plate, and the other is attached to a zinc plate. Each plate is pushed into a different potato; when a wire connects the two potatoes, the clock begins to run as if it were connected to a battery.

    1.  Draw a cell diagram of the potato clock.
    2.  Explain why the clock runs.

14. ♦ The silver--zinc battery has the highest energy density of any rechargeable battery available today. Its use is presently limited to military applications, primarily in portable communications, aerospace, and torpedo-propulsion systems. The disadvantages of these cells are their limited life (they typically last no more than about 2 yr) and their high cost, which restricts their use to situations in which cost is only a minor factor. The generally accepted equations representing this type of battery are as follows:

    $$\left. 2\text{AgO(s)} + \text{Zn(s)} + \text{H}_{\text{2}}\text{O(l)}\rightarrow\text{Ag}_{\text{2}}\text{O(s)} + \text{Zn(OH)}_{\text{2}}\text{(aq)}\quad E{^\circ} = 1.85\text{~V} \right.$$

    $$\left. \text{Ag}_{2}\text{O(s)} + \text{Zn(s)} + \text{H}_{\text{2}}\text{O(l)}\rightarrow 2\text{Ag(s)} + \text{Zn(OH)}_{\text{2}}\text{(aq)}\quad E{^\circ} = 1.59\text{~V} \right.$$

    1.  Write the overall cell reaction and calculate *E*°<sub>cell</sub>.
    2.  If the cell is 75% efficient, what is the maximum amount of work that can be generated from this type of battery?
    3.  Use tabulated data to calculate the maximum work that can be generated by a lead storage cell. If a silver--zinc battery is operating at 100% efficiency, how do the two batteries compare?

15. All metals used in boats and ships are subject to corrosion, particularly when the vessels are operated in salt water, which is a good electrolyte. Based on the data in the following table, where potentials are measured using a glass electrode, explain why

    1.  iron or steel should not be used in bolts in a lead ballast keel.
    2.  ordinary brass should not be used as a structural fastening, particularly below the waterline.
    3.  an aluminum hull should not be painted with a copper-based antifouling paint.
    4.  magnesium sacrificial anodes are preferred over zinc when a vessel is kept in fresh water.
    5.  Monel (an alloy that contains mostly nickel and copper) is preferred over stainless steel for freshwater tanks.

    ````````{list-table}
    :header-rows: 1

    - - Metal
      - *E* versus Ag/AgCl (V)
    - - titanium
      - 0.02
    - - Monel \[Ni(Cu)\]
      - −0.06
    - - Ni(Al) bronze
      - −0.16
    - - lead
      - −0.20
    - - manganese bronze
      - −0.29
    - - brass
      - −0.30
    - - copper
      - −0.31
    - - tin
      - −0.31
    - - stainless steel
      - −0.49
    - - aluminum
      - −0.87
    - - zinc
      - −1.00
    - - magnesium
      - −1.60

    ````````

16. Parents often coat a baby's first shoes with copper to preserve them for posterity. A conducting powder, such as graphite, is rubbed on the shoe, and then copper is electroplated on the shoe. How much copper is deposited on a shoe if the electrolytic process is run for 60 min at 1.2 A from a 1.0 M solution of CuSO<sub>4</sub>?

17. Before 1886, metallic aluminum was so rare that a bar of it was displayed next to the Crown Jewels at the Paris Exposition of 1855. Today, aluminum is obtained commercially from aluminum oxide by the Hall--Heroult process, an electrolytic process that uses molten Al<sub>2</sub>O<sub>3</sub> and cryolite (Na<sub>3</sub>AlF<sub>6</sub>). As the operation proceeds, molten Al sinks to the bottom of the cell. The overall reaction is 2Al<sub>2</sub>O<sub>3</sub>(l) + 3C(s) → 4Al(l) + 3CO<sub>2</sub>(g); however, the process is only approximately 90% efficient.

    1.  Why is cryolite added to the Al<sub>2</sub>O<sub>3</sub>?
    2.  How much aluminum is deposited if electrodeposition occurs for 24 h at 1.8 A?

18. ♦ One of the most important electrolytic processes used in industry is the electrolytic reduction of acrylonitrile (CH<sub>2</sub>CHCN) to adiponitrile \[NC(CH<sub>2</sub>)<sub>4</sub>CN\]. The product is then hydrogenated to hexamethylenediamine \[H<sub>2</sub>N(CH<sub>2</sub>)<sub>6</sub>NH<sub>2</sub>\], a key component of one form of nylon. Using this process, Monsanto produces about 200,000 metric tons of adiponitrile annually. The cathode reaction in the electrochemical cell is as follows:

    2CH<sub>2</sub>CHCN + 2H<sup>+</sup> + 2e<sup>−</sup> → NC(CH<sub>2</sub>)<sub>4</sub>CN

    The cost of electricity makes this an expensive process. Calculate the total number of kilowatt-hours of electricity used by Monsanto each year in this process, assuming a continuous applied potential of 5.0 V and an electrochemical efficiency of 50%. (One kilowatt-hour equals 3.6 × 10<sup>3</sup> kJ.)

19. ♦ Compact discs (CDs) are manufactured by electroplating. Information is stored on a CD master in a pattern of "pits" (depressions, which correspond to an audio track) and "lands" (the raised areas between depressions). A laser beam cuts the pits into a plastic or glass material. The material is cleaned, sprayed with \[Ag(NH<sub>3</sub>)<sub>2</sub>\]<sup>+</sup>, and then washed with a formaldehyde solution that reduces the complex and leaves a thin silver coating. Nickel is electrodeposited on the disk and then peeled away to produce a master disk, which is used to stamp copies.

    1.  Write the half-reactions that correspond to the electrodeposition reaction.
    2.  If a CD has a radius of 12 cm and an interior hole with a diameter of 2.5 cm, how long does it take to deposit a 50 µm layer of nickel on one side of the CD using a 1.0 M solution of NiSO<sub>4</sub> and a current of 0.80 A?

20. ♦ Calculate the total amount of energy consumed in the electrolysis reaction used to make the 16 × 10<sup>6</sup> metric tons of aluminum produced annually worldwide, assuming a continuous applied potential of 5.0 V and an efficiency of 50%. Express your answer in kilojoules and in kilowatt-hours. (See Problem 19 for the conversion between kilowatt-hours and kilojoules.)

### Answers

1.  
2.  
3.  
4.  
5.  1.  *E*°<sub>cell</sub> = 1.14 V for NADH; 0.94 V for FADH<sub>2</sub>
    2.  −0.32 V
    3.  −0.12 V
6.  
7.  
8.  
9.  
10. 
11. 
12. 
13. 
14. 
15. 
16. 
17. 
18. 
19. 1.  Ni<sup>2+</sup>(aq) + 2e<sup>−</sup> → Ni(s); Ni(s) → Ni<sup>2+</sup>(aq) + 2e<sup>−</sup>
    2.  22 hrs
20. 

[^chem-1]: The study of the relationship between electricity and chemical reactions.

[^chem-2]: A substance that is capable of donating electrons and in the process is oxidized.

[^chem-3]: A substance that is capable of accepting electrons and in the process is reduced.

[^chem-4]: Reactions that represent either the oxidation half or the reduction half of an oxidation--reduction (redox) reaction.

[^chem-5]: An apparatus that generates electricity from a spontaneous oxidation--reduction (redox) reaction or, conversely, uses electricity to drive a nonspontaneous redox reaction.

[^chem-6]: An electrochemical cell that uses the energy released during a spontaneous oxidation--reduction (redox) reaction $\left( {\Delta G < 0} \right)$ to generate electricity.

[^chem-7]: Galvanic cells are named for the Italian physicist and physician Luigi Galvani (1737--1798), who observed that dissected frog leg muscles twitched when a small electric shock was applied, demonstrating the electrical nature of nerve impulses.

[^chem-8]: An electrochemical cell that consumes electrical energy from an external source to drive a nonspontaneous $\left( {\Delta G > 0} \right)$ oxidation--reduction (redox) reaction.

[^chem-9]: A solid metal connected by an electrolyte and an external circuit that provides an electrical connection between systems in an electrochemical cell (galvanic or electrolytic).

[^chem-10]: One of two electrodes in an electrochemical cell, it is the site of the oxidation half-reaction.

[^chem-11]: One of two electrodes in an electrochemical cell, it is the site of the reduction half-reaction.

[^chem-12]: A U-shaped tube inserted into both solutions of a galvanic cell that contains a concentrated liquid or gelled electrolyte and completes the circuit between the anode and the cathode.

[^chem-13]: Related to the energy needed to move a charged particle in an electric field, it is the difference in electrical potential beween two half-reactions.

[^chem-14]: The potential of an electrochemical cell measured under standard conditions (1 M for solutions, 1 atm for gases, and pure solids or pure liquids for other substances) and at a fixed temperature (usually 298 K).

[^chem-15]: Concentrated solutions of salts (about 1 M) generally do not exhibit ideal behavior, and the actual standard state corresponds to an *activity* of 1 rather than a concentration of 1 M. Corrections for nonideal behavior are important for precise quantitative work but not for the more qualitative approach that we are taking here.

[^chem-16]: The electrode chosen as the reference for all other electrodes, which has been assigned a standard potential of 0 V and consists of a Pt wire in contact with an aqueous solution that contains 1 M $\text{H}^{\text{~+~}}$ in equilibrium with $\text{H}_{2}$ gas at a pressure of 1 atm at the Pt-solution interface.

[^chem-17]: The potential of a half-reaction measured against the SHE under standard conditions.

[^chem-18]: As we shall see in [Section 19.7 \"Electrolysis\"](/chapters/ch-19-electrochemistry.md#src-averill-1-0-ch19-s07), this does not mean that the reaction cannot be made to occur at all under standard conditions. With a sufficient input of electrical energy, virtually any reaction can be forced to occur.

[^chem-19]: The electrode of a galvanic cell whose potential is related to the concentration of the substance being measured.

[^chem-20]: An electrode in an galvanic cell whose potential is unaffected by the properties of the solution.

[^chem-21]: A reference electrode that consists of a silver wire coated with a very thin layer of AgCl and dipped into a chloride ion solution with a fixed concentration.

[^chem-22]: A reference electrode that consists of a platinum wire inserted into a moist paste of liquid mercury (calomel; $\text{Hg}_{2}\text{Cl}_{2}$) and KCl in an interior cell, which is surrounded by an aqueous KCl solution.

[^chem-23]: An electrode used to measure the $\text{H}^{+}$ ion concentration of a solution and consisting of an internal Ag/AgCl electrode immersed in a 1 M HCl solution that is separated from the solution by a very thin glass membrane.

[^chem-24]: An electrode whose potential depends on only the concentration of a particular species in solution.

[^chem-25]: The SI unit of measure for the number of electrons that pass a given point in 1 second; it is defined as $6.25 \times 10^{18}\text{e}^{-}\text{/s}$ and relates electron potential (in volts) to energy (in joules): 1 J/1 V = 1 C.

[^chem-26]: The fundamental SI unit of electric current; it is defined as the flow of 1 C/s past a given point: 1A = 1 C/s.

[^chem-27]: The charge on 1 mol of electrons; it is obtained by multiplying the charge on the electron by Avogadro's number.

[^chem-28]: An equation for calculating cell potentials $\left( E_{\text{cell}} \right)$ under nonstandard conditions; it can be used to determine the direction of spontaneous reaction for any redox reaction under an conditions: $E_{\text{cell}} = E_{\text{cell}}^{{^\circ}} - \left( {RT/nF} \right)\text{ln~}Q\text{.}$

[^chem-29]: An electrochemical cell in which the anode and the cathode compartments are identical except for the concentration of a reactant.

[^chem-30]: A galvanic cell (or series of galvanic cells) that contains all the reactants needed to produce electricity.

[^chem-31]: A galvanic cell that requires a constant external supply of one or more reactants to generate electricity.

[^chem-32]: A battery consisting of an electrolyte that is an acidic water-based paste containing $\text{MnO}_{\text{2}},$ $\text{NH}_{\text{4}}\text{Cl},$ $\text{ZnCl}_{\text{2}}\text{,}$ graphite, and starch.

[^chem-33]: A battery that consists of a Leclanché cell adapted to operate under alkaline (basic) conditions.

[^chem-34]: A battery that consists of an anode of lithium metal and a cathode containing a solid complex of $\text{I}_{2}\text{,}$ with a layer of solid LiI in between that allows the diffusion of $\text{Li}^{+}$ ions.

[^chem-35]: A type of battery that consists of a water-based cell with a cadmium anode and a highly oxidized nickel cathode.

[^chem-36]: A battery consisting of a plate or grid of spongy lead metal, a cathode containing powdered $\text{PbO}_{\text{2}},$ and an electrolyte that is usually an aqueous solution of $\text{H}_{\text{2}}\text{SO}_{\text{4}}.$

[^chem-37]: A galvanic process by which metals deteriorate through oxidation---usually but not always to their oxides.

[^chem-38]: An electrode containing a more reactive metal that is attached to a metal object to inhibit that object's corrosion.

[^chem-39]: An electrochemical process in which an external voltage is applied to an electrolytic cell to drive a nonspontaneous reaction.

[^chem-40]: The voltage that must be applied in electrolysis in addition to the calculated (theoretical) value to overcome factors such as a high activation energy and the formation of bubbles on a surface.

[^chem-41]: A process in which a layer of a second metal is deposited on the metal electrode that acts as the cathode during electrolysis.
