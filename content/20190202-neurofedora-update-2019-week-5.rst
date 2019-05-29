NeuroFedora update: 2019 week 5
###############################
:date: 2019-02-02 18:21:32
:slug: neurofedora-update-2019-week-5
:author: Ankur Sinha
:category: News
:tags: Software, Blog, Arbor, Neuron, Brian, PyNN, Python3
:summary: An update on NeuroFedora_ in the 5th week of 2019: more software
          updates.


.. include:: logo.txt

In the last week, we've continued to make progress on packages:

1. The neuron_ review should be done in a few days. We can then begin on the
   MPI versions, and Python bindings.
2. arbor_ is still a WIP. Here's a pre-print the developers published recently
   announcing it: https://arxiv.org/abs/1901.07454
3. Version 1 of the Brian Simulator is now available in the `NeuroFedora extras
   COPR repository`_. This version is in maintenance mode only and users should
   prefer the new Brian2_ simulator for their work. We only make version 1
   available because PyNN_ currently does not support version 2---that is a work
   in progress. Version 1 of the simulator will not be provided for Fedora
   releases after 29 since Fedora 30+ `are moving to Python3 only
   <https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal>`__.


.. include:: footer.txt


.. _NeuroFedora: https://neuro.fedoraproject.org
.. _neuron: https://bugzilla.redhat.com/show_bug.cgi?id=1662526
.. _arbor: https://pagure.io/neuro-sig/NeuroFedora/issue/190
.. _NeuroFedora extras COPR repository: https://docs.fedoraproject.org/en-US/neurofedora/copr/
.. _Brian2: https://apps.fedoraproject.org/packages/python-brian2
.. _PyNN: https://github.com/NeuralEnsemble/PyNN/pull/617
