Open Position: NeuroFedora is looking for a Spin/Lab master
###########################################################
:date: 2019-08-07 20:29:22
:author: NeuroFedora
:category: Community
:tags: Fedora Spin, Computational Neuroscience
:slug: open-position-neurofedora-is-looking-for-a-spin-lab-master
:summary: NeuroFedora_ is looking for a Spin/Lab master to manage a new installable ISO! Join us!

.. include:: logo.txt

Now that we are about a year into the project, we have `quite a bit of software
ready for users to use <https://src.fedoraproject.org/group/neuro-sig>`__. Here
is a dump of the complete list (find your tool!):

auryn, bionetgen, biosig4c++, calcium-calculator, COPASI, ctk, dcm2niix, dcmtk, DiffusionKurtosisFit, dlib, drawtk, gdcm, getdp, gifticlib, InsightToolkit, isis, libb64, liblsl, libminc, libneurosim, libsbml, nest, neuron, neurord, nipy-data, octave-metch, openigtlink, openmeeg, openvibe, petpvc, python-airspeed, python-amico, python-baker, python-bids-validator, python-biopython, python-brian2, python-chaospy, python-citeproc-py, python-dipy, python-duecredit, python-elephant, python-fastavro, python-fsleyes, python-fsleyes-props, python-fsleyes-widgets, python-fslpy, python-grabbit, python-gradunwarp, python-h5io, python-hdfs, python-hdmf, python-indexed_gzip, python-interfile, python-klusta, python-lazyarray, python-libNeuroML, python-matplotlib-scalebar, python-missingno, python-mne, python-mne-bids, python-moss, python-neo, python-neurosynth, python-nibabel, python-nilearn, python-nineml, python-nipy, python-nistats, python-nitime, python-nixio, python-num2words, python-patsy, python-petlink, python-pyactivetwo, python-pybids, python-pydicom, python-pydotplus, python-pyelectro, python-pyemd, python-pyfim, python-pygiftiio, python-pylatex, python-PyLEMS, python-PyLink, python-pymatreader, python-pynwb, python-pyoptical, python-pyphi, python-pyriemann, python-pysb, python-pyscaffold, python-pytest-lazy-fixture, python-pytest-sugar, python-pyxid, python-quantities, python-rangehttpserver, python-resumable-urlretrieve, python-simplewrap, python-tabulate, python-transforms3d, python-tvb-data, python-tvb-gdist, python-visionegg-quest, python-wxnatpy, python-xnat, rubygem-nifti, rudeconfig, smoldyn, teem, vrpn, vxl.

All of these tools can now be used in three simple steps:

1. Install a Fedora system. You can get the installable image from
   https://getfedora.org.
2. Install your software! For example: :code:`sudo dnf install python-fsleyes`.
3. Get to work!

Even though it is only three steps, it could still be made simpler. What if we
could have a Fedora Remix that you could simply download and use?

What is a Fedora Spin/Lab?
---------------------------

The Fedora community produces three "editions" that are featured on
https://getfedora.org. However, these are not all! The community is full of
volunteers with different interests, and so we also produce lots of secondary
products---Fedora Spins_ and Fedora Labs_. They are both downloadable images
like the Fedora editions, with the difference being that they are contain
different software sets.  The Spins_ for example, include different default
desktop environments: KDE, LXDE, LXQT, and so on. The Labs_ consist of
different "functional bundles", for different target audiences: Astronomy,
Design, Games, Security, and so on.

NeuroFedora Lab?
-----------------

So, the plan now is to have a similar downloadable image for NeuroFedora_. If
not a single image, maybe two: one each for the two main functional classes:
one for computational modelling, and one for neuroimaging. So, effectively that
will mean the process would become even simpler for users:

1. Download the image (and optionally install it).
2. Get to work!

Here's why installing is optional. All Fedora images are "Live". This means
that you don't really need to install them to use them. You can boot into them
off a USB drive and use them straight away---without installing them on a
computer.  This could be very very useful for tutorials and hackathons where
the organisers could have a bunch of these images ready for users to work on.


We are looking for a Spin/Lab master
-------------------------------------

So, we are looking for someone to manage the image. We have a small team
already, but we would like to keep the team focussed on including more
software---`there are still 160 tools in queue
<https://pagure.io/neuro-sig/NeuroFedora/issues?status=Open&tags=T%3A+Software>`__.


The Spin/Lab master shall:

- help decide what tools should be included in the image,
- lead the effort by using existing Fedora community infrastructure to create
  the images,
- ensure the images are always functional and ready to use,
- poke the rest of the team when needed to fix issues.

The time commitment would be: 2-3 hours a week.

What skills do you need for this? None---like all other tasks, you can learn on
the go. In general, you will use/learn:

- Git (since most things in Fedora now use Git),
- how to create a "kickstart" recipe---the configuration file that defines what
  the image contains. This is very well documented and mostly, you only have to
  copy paste the recipe off another image and tweak it.
- how to use the Fedora community infrastructure to build these images---this
  is also quite easy since there are helper tools for all of it. All you have
  to do is run the commands in the right order.

It is quite an easy role, and there are lots of people in the Fedora community
who would be happy to help when needed. There is a whole `Spins Special
Interest Group (SIG) <https://fedoraproject.org/wiki/Spins_SIG>`__, as a matter
of fact. The toughest bit would be learning the process that is to be followed.

Does that sound interesting? Do you want to learn new skills and help us make
NeuroFedora_ better and easier for neuroscience enthusiasts? Have any
questions? `Get in touch with us
<https://docs.fedoraproject.org/en-US/neurofedora/communicating/>`__!

.. include:: footer.txt
.. _NeuroFedora: https://neuro.fedoraproject.org
.. _Spins: https://spins.fedoraproject.org
.. _Labs: https://labs.fedoraproject.org
