---
title: Are Protein Forcefields Getting Better?


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
- Semiquantitative prediction based on machine-learning and physical approaches

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


---
title: A Brief History of NMR-based FF development

$$\chi^2 = \sum_i \frac{1}{n} \frac{(x_k^{expt} - x_k^{model})^2}{\sigma_k^2}$$

---

<center>
<img width=850 src=figures/best_hummer_title.png />


<img height=450 src=figures/best_triangles.png />
</center>

---
<center>
<img width=850 src=figures/gordon_title.png />


<img height=400 src=figures/gordon_rama.png />
</center>

---
<center>
<img width=850 src=figures/shaw_title.png />


<img height=400 src=figures/shaw_ff_time.png />
</center>

---
<center>
<img width=850 src=figures/kb_title.png />


<img height=400 src=figures/ChiSquared_All.png />
</center>

