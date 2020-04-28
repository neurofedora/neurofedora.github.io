Fedora 32 Computational Neuroscience ready-to-install ISO image is now available!
#################################################################################
:date: 2020-04-28 15:05:00
:author: Ankur Sinha
:category: News
:tags: Computational Modelling, Fedora Lab, GENESIS, Julia, NEST, Neuron, Python,  Software
:slug: fedora-32-computational-neuroscience-ready-to-install-iso-image-is-now-available
:summary: Fedora 32 was released today, and so was the NeuroFedora
          Computational Neuroscience ISO image! Download, install, and get to
          work!


.. raw:: html

   <center>

.. figure:: {static}/images/20200428-Comp-neuro-website.png
    :alt: Download the Fedora 32 Computational Neuroscience image from labs.fedoraproject.org
    :width: 80%
    :class: img-responsive
    :target: https://labs.fedoraproject.org/en/comp-neuro

.. raw:: html

   </center>
   <br />

`Fedora 32 <https://getfedora.org>`__ was released today after a full six
months of development. There are a lot of improvements and new changes included
in this release. You can read the `announcement here
<https://fedoramagazine.org/announcing-fedora-32-2/>`__ and the complete
release notes `here <https://docs.fedoraproject.org/en-US/fedora/f32>`__.

This release is particularly exciting for the NeuroFedora team. It also marks
the first release of our first deliverable: the CompNeuro Lab ISO image! The
aim of developing such ready to install ISO images that are packed with the
necessary tools is to enable users to quickly set up their computers and get
down to work, instead of wasting precious time and effort on installing tools
individually by hand. While we hope that this will enable researchers by
providing them easy access to Free/Open Source research tools, we also hope
that the platform will serve as a teaching aid in Computational Neuroscience
courses.

.. raw:: html

   <center>

.. figure:: {static}/images/20200428-neurofedora-featured.png
    :alt: Applications featured in the CompNeuro ISO image.
    :width: 80%
    :class: img-responsive
    :target: https://labs.fedoraproject.org/en/comp-neuro

.. raw:: html

   </center>
   <br />


This CompNeuro release includes a number of modelling related tools that we
were able to package over the release:

- `Auryn <https://fzenke.net/auryn/doku.php>`__,
- `Bionetgen <https://www.csb.pitt.edu/Faculty/Faeder/?page_id=409>`__,
- `Calc: calcium-calculator <https://web.njit.edu/~matveev/calc.html>`__,
- `COPASI <http://copasi.org/>`__,
- `GetDP <http://getdp.info//>`__,
- `GENESIS <http://genesis-sim.org/GENESIS/genesis.html>`__,
- `MOOSE <https://moose.ncbs.res.in/>`__,
- `NEST simulator <https://www.nest-simulator.org/>`__,
- `NEURON <https://neuron.yale.edu/neuron/>`__,
- `PyLEMS <http://lems.github.io/LEMS/>`__,
- `Smoldyn <http://www.smoldyn.org/>`__,

All of these tools have been built with the current best practices in Software
Development in mind---this is mandated by the `Fedora community's software
packaging guidelines
<https://docs.fedoraproject.org/en-US/packaging-guidelines/>`__. In addition to
modelling tools, the ISO image also includes multiple tools used in analysis of
data:

- the complete `Python science stack <https://www.scipy.org/>`__: NumPy, SciPy, Matplotlib, IPython, SymPy, and Pandas,
- `R <https://www.r-project.org/>`__,
- `Julia <https://julialang.org/>`__.
- `GNU Octave <https://www.gnu.org/software/octave/>`__,
- `GNUPlot <http://gnuplot.info/>`__,
- `Paraview <https://www.paraview.org/>`__,

This is not all, though! There's `even more Neuroscience software
<https://docs.fedoraproject.org/en-US/neurofedora/software/>`__ that can be
installed from the repositories. Also, since this edition is derived from
Fedora, users have access to the *complete* set of packages that are included
in Fedora: all the `desktop environments <https://spins.fedoraproject.org/>`__,
productivity tools, development tools, and libraries that you can choose from.

The CompNeuro ISO image is based on the `Fedora Workstation
<https://getfedora.org/en/workstation/>`__ product that uses the modern `GNOME
desktop environment <https://www.gnome.org/>`__.  It provides a clean interface
integrated with a plethora of daily use productivity and development tools:

.. raw:: html

   <center>

.. figure:: {static}/images/20200427-gnome.png
    :alt: Screenshot of the GNOME desktop environment.
    :width: 80%
    :class: img-responsive
    :target: {static}/images/20200427-gnome.png

|

.. figure:: {static}/images/20200427-gnome-applications.png
    :alt: Screenshot of the GNOME desktop environment with applications.
    :width: 80%
    :class: img-responsive
    :target: {static}/images/20200427-gnome-applications.png

.. raw:: html

   </center>
   <br />


If GNOME isn't to your liking, though, there are other options. You can install
any `Fedora "spin" <https://spins.fedoraproject.org>`__ and install the
software you need there also. Whatever you choose, you'll be ready to work in
no time:

- download a Fedora image,
- install the tools you need,
- get to work!

Feedback is welcome
--------------------

This is the team's first deliverable. There is a lot of Free/Open Source
software out there that still needs to be included in NeuroFedora. If you use a
tool that's not on our `list
<https://pagure.io/neuro-sig/NeuroFedora/issues?status=Open&tags=T%3A+Software>`__,
please let us know. If you experience any issues or have ideas for improvement,
please do let us know. You can contact the team using any of our `communication
channels <https://docs.fedoraproject.org/en-US/neurofedora/communicating/>`__.

Developing NeuroFedora is also a great learning experience, especially for
students. As a volunteer based community project, we learn skills and tools
together and share knowledge freely with each other. No skills or experience
are necessary to join the community. You can find what you want to do, and
gather the required knowledge as you go at your own pace. We strongly encourage
students to join the team, contribute their bit, and learn more about the tools
use in Neuroscience while they do it.

We'd love to hear from you. Please get in touch.
