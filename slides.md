---
title: The Atomistic Basis of Disease

...EVKMD<b><font color="black">A</font></b>EFRHDS...  ...EVKMD<b><font color="black">T</font></b>EFRHDS...  ...EVKMD<b><font color="black">V</font></b>EFRHDS...

<img width=300 src=figures/alanine.png />  <img width=300 src=figures/threonine.png />   <img width=300 src=figures/valine.png />

<footer class="source"> 
Jonsson, 2012  A673 T673 V673
</footer>

---
title: Why Molecular Dynamics?

- Predict the outcome of biophysical measurements
- Generate atomic-scale hypotheses
- Interpret experimental obervables 


---
title: Molecular Dynamics Forcefield Error 

<img height=500 src=figures/elephant.jpg />

<footer class="source">
http://newh2o.com/2012/11/02/gemstones-elephant-in-the-room-free-project/
</footer>


---
title: Why NMR?

- Probe individual or pairs of atoms
- Solution phase, ensemble averages
- Direct map from simulation to observable

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

- Complex predictors with unknown error bars

<center>
<img height=450 src=figures/shiftx2_features.png />
</center>


<footer class="source"> 
Bax, 2010.  Wishart, 2011.  Bruschweiler, 2012.
</footer>

---
title: NMR Observables: Scalar Couplings

- Probe pairs of atoms separated by 1-3 bonds
- Sensitive to geometry via Karplus curve

<center>
<img height=425 src=figures/karplus_ala3.png />
</center>

---
title: NMR Observables: Scalar Couplings

- Uncertainties of ~0.4 Hz for $^3J H_N H_\alpha $
- Poor models for other classes of JC

<center>
<img height=425 src=figures/karplus_ala3.png />
</center>

---
title: NMR Observables: NOE

- Probe pairs of nonbonded atoms
- Sensitive to $\langle r^{-\frac{1}{6}}\rangle$
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
title: A Brief History of NMR-based FF development

$$\chi^2 = \frac{1}{n} \sum_k  \frac{(x_k^{expt} - x_k^{model})^2}{\sigma_k^2}$$

---

<center>
<img width=850 src=figures/schwalbe_title.png /> 

</center>

- Chemical shift and scalar couplings
- Studied ALA2 through ALA8
- PPII structure dominates

---

<center>
<img width=850 src=figures/schwalbe_title.png /> 

<img width=450 src=figures/schwalbe_figure.png />

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
title: Takeaways

- NMR probes ensemble average properties with atomic resolution
- MD and simple models yield semi-quantitative predictions of NMR observables (CS, JC, NOE)
- Recent forcefields are (by design) more consistent with NMR measurements

---
title: Future Work

- Beyond "manual" adjustment of FFs: Forcebalance, Bayesian FFs?
- Using experiments to fit more than just dihedrals

