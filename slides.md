---
title: The Atomistic Basis of Disease

...EVKMD<b><font color="black">A</font></b>EFRHDS...  ...EVKMD<b><font color="black">T</font></b>EFRHDS...  ...EVKMD<b><font color="black">V</font></b>EFRHDS...

<img width=300 src=figures/alanine.png />  <img width=300 src=figures/threonine.png />   <img width=300 src=figures/valine.png />

<footer class="source"> 
Jonsson, 2012  A673 T673 V673
</footer>

---
title: Molecular Dynamics: Biophysical Models at the nanoscale

- Generate atomic-scale hypotheses
- Predict the outcome of biophysical measurements
- Interpret experimental observables 


---
title: Molecular Dynamics Forcefield Error 

<img height=500 src=figures/elephant.jpg />

<footer class="source">
http://newh2o.com/2012/11/02/gemstones-elephant-in-the-room-free-project/
</footer>


---
title: How to Evaluate and Refine Forcefields with NMR
class: segue dark nobackground


---
title: Why NMR?

- Probe individual or pairs of atoms
- Solution phase, ensemble averages
- Direct geometric map from simulation to observable

<center>
<img height=350 src=figures/noesy.jpg />
</center>

<footer class="source"> 
http://www.acornnmr.com/codeine/noesy.htms
</footer>

---
title: NMR Observables: Chemical Shifts

- Sensitive to local environment
- Easy to obtain
- Semiquantitative prediction: PPM, ShiftX2, Sparta+

<center>
<img height=300 src=figures/1D_NMR.png />
</center>

<footer class="source"> 
http://publications.nigms.nih.gov/structlife/chapter3.html
</footer>


---
title: NMR Observables: Chemical Shifts

- Complex machine learning models
- Unknown error bars

<center>
<img height=450 src=figures/shiftx2_features.png />
</center>


<footer class="source"> 
Bax, 2010.  Wishart, 2011.  Bruschweiler, 2012.
</footer>

---
title: Conclusion: Chemical Shifts are great for semiquantitative FF Evaluation


---
title: NMR Observables: NOE

- Probe pairs of nonbonded atoms
- Sensitive to $\langle r^{-\frac{1}{k}}\rangle$ for $k = 3, 6$
- Key experiment in NMR structure determination

<center>
<img height=350 src=figures/noesy.jpg />
</center>

---
title: NMR Observables: NOE


- Complex modulation by dynamics
- Typically treated non-quantitatively
- Weak, medium, or strong restraints on a single structure

---
title: Conclusion: NOEs are information rich but non-quantitative under current treatments


---
title: NMR Observables: Structure


<center>
<img width=300 src=figures/hp35.png /> 
</center>

- Assumes single structure, not equilibrium
- Discards quantitative experimental measurements

---
title: Conclusion: Structure is an important sanity check, but a qualitative, derived quantity

---
title: NMR Observables: Scalar Couplings

- Probe pairs of atoms separated by 1-3 bonds

<center>
<img height=550 src=figures/ALA3.png />
</center>

---
title: NMR Observables: Scalar Couplings


- Sensitive to geometry via Karplus curve

<center>
<img height=425 src=figures/karplus_ala3.png />
</center>

---
title: NMR Observables: Scalar Couplings

- Uncertainties of ~0.4 Hz for $^3J H_N H_\alpha $
- Poor models for other classes of JC

<center>
<img height=400 src=figures/wangbax1996.png />
</center>

---
title: Conclusion: JCs are currently the most direct comparisons available for FF evaluation



---
title: A Brief History of NMR-based FF development

$$\chi^2 = \frac{1}{n} \sum_k  \frac{(x_k^{expt} - x_k^{model})^2}{\sigma_k^2}$$

---

<center>
<img width=850 src=figures/schwalbe_title.png /> 

</center>

- Studied ALA2 through ALA8

<center>
<img height=350 src=figures/ALA3.png />
</center>


---

<center>
<img width=850 src=figures/schwalbe_title.png /> 
</center>

- Chemical shift and scalar couplings

<center>
<img width=450 src=figures/schwalbe_figure.png />

</center>

---

<center>
<img width=850 src=figures/schwalbe_title.png /> 
</center>

- PPII conformation dominates short ALA peptides

<center>
<img width=650 src=figures/schwalbe_chi2.png />

</center>


---

<center>
<img width=850 src=figures/best_hummer_title.png />
</center>

- Evaluate scalar couplings ($^3J H_N H_\alpha $) on ALA5
- Modern force fields too helical
- ALA5 has *some* helical content

---

<center>
<img width=850 src=figures/best_hummer_title.png />



<img height=450 src=figures/best_triangles.png />
</center>

---
<center>
<img width=850 src=figures/gordon_title.png />

</center>

- Idea: adjust dihedral terms to better fit JC data
- Similar work also done by R. Best (ff99sb*, ff03*), Bruschweiler

---
<center>
<img width=850 src=figures/gordon_title.png />


<img height=400 src=figures/gordon_rama.png />
</center>

---
<center>
<img width=850 src=figures/shaw_title.png />
</center>

- Folded proteins: GB3, Ubiquitin
- $\alpha$ and $\beta$ peptides: AAQAA, CLN025
- Folding / Unfolding : HP35, WW FiP35
---
<center>
<img width=850 src=figures/shaw_title.png />


<img height=400 src=figures/shaw_ff_time.png />
</center>

---
<center>
<img width=850 src=figures/kb_title.png />
</center>

- 11 force fields, 5 water models
- Ace-X-NME, homotripeptides, tetrapeptides, ubiquitin
- Scalar couplings, chemical shifts

---
<center>
<img width=850 src=figures/kb_title.png />
</center>

<img height=400 src=figures/ChiSquared_All.png />
</center>


---
title: $\chi^2$ robust to system sizes

<center>
<img height=230 src=figures/ChiSquared_1UBQ.png />
<img height=230 src=figures/ChiSquared_Tripeptides.png />

<img height=230 src=figures/ChiSquared_Dipeptides.png />

</center>


---
title: Takeaways

- NMR probes ensemble average properties with atomic resolution
- MD and simple models yield semi-quantitative predictions of NMR observables (CS, JC, NOE)
- Recent forcefields are (by design) more consistent with NMR measurements

---
title: Future Work

- Beyond "manual" adjustment of FFs: Forcebalance, Bayesian FFs?
- Using experiments to fit more than just dihedrals
- Designing experiments to improve force fields

---
title: Related work

- Combining MD and experiment to infer conformational ensembles (with TJ Lane and Christian Schwantes; based on work by John and Pitera)
- Improved Karplus relations (with TJ Lane)

---
title: Towards quantitative structural biology
subtitle: Going beyond static NOEs

- MD$\rightarrow$Correlation function$\rightarrow$Spectral Density$\rightarrow$Relaxation Matrix$\rightarrow$NOE
- What is ultimate information content of a NOE experiment?
- Overhauser: a toolbox for quantitative NOE spectroscopy


---
title: How NOE Works (1)

$C(t) = \langle \frac{P_2(\mathbf{u}(0) \cdot \mathbf{u}(t))}{r^3(0)r^3(t)} \rangle$

$C(0) = \langle r^{-6} \rangle$

$C(\infty) \approx S^2 \langle r^{-3} \rangle^2$

$J(\omega) = \mathcal{F}[C(t)]$


---
title: How NOE Works (2)

Relaxation matrix:

---
title: Scalar Couplings

<center>
<img height=500 src=figures/3JHNHA.png />
</center>

---
title: Dipeptide Populations

<center>
<img height=500 src=figures/PopulationTriangle.png />
</center>
