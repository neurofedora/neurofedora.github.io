NeuroFedora update: 2019 week 7
###############################
:date: 2019-02-17 13:32:27
:author: Ankur Sinha
:slug: neurofedora-update-2019-week-7
:category: News
:tags: Software, Blog, Neuron, PyNN, Auryn
:summary: An update on NeuroFedora_ in the 7th week of 2019: more software
          updates.

.. raw:: html

   <center>

.. figure:: {static}/images/NeuroFedoraLogo01.png
    :alt: NeuroFedora logo
    :width: 30%
    :class: img-responsive

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__

.. raw:: html

   </center>


We continue to make progress on software that is to be included in
NeuroFedora_:

- neuron_ was approved for inclusion and is now in testing. This is without MPI
  support, and does not currently contain Python bindings. These are both being
  worked on now.
- auryn_ was approved for inclusion. While it builds fine on :code:`x86_64,
  i686, ppc64`, it does not build on other secondary architectures:
  :code:`armv7hl, aarch64, s390x`. So, we have filed a `ticket upstream
  <https://github.com/fzenke/auryn/issues/33>`__ to clarify if these are
  supported. You can read more about the architectures Fedora supports `here
  <https://fedoraproject.org/wiki/Architectures>`__.
- various other packages were updated to their latest versions: `fsleyes
  <https://bodhi.fedoraproject.org/updates/?packages=python-fsleyes>`__, `pydicom
  <https://bodhi.fedoraproject.org/updates/?packages=python-pydicom>`__, and
  `nibabel
  <https://bodhi.fedoraproject.org/updates/?packages=python-nibabel>`__. You
  can test them by enabling the updates-testing repository and give feedback on
  these updates (documented `here
  <https://fedoraproject.org/wiki/QA:Updates_Testing>`__).
- A number of packages need to be updated to their latest versions.
  Unfortunately, a few of these bundle software that must be removed, so it
  takes more time than simple updates: `InsightToolkit
  <https://bugzilla.redhat.com/show_bug.cgi?id=1674578>`__, `vxl
  <https://bugzilla.redhat.com/show_bug.cgi?id=1371436>`__, `gdcm
  <https://bugzilla.redhat.com/show_bug.cgi?id=1674946>`__.
- We announced NeuroFedora on `Neurostars
  <https://neurostars.org/t/neurofedora-free-software-for-free-neuroscience/3594>`__
  today also.

In other news, `PyNN is being considered as an INCF standard/best practice
<https://groups.google.com/forum/#!topic/neuralensemble/a4xnnPQ7dpM>`__. If you
do use it, please provide your comments.

---------

NeuroFedora_ is volunteer driven initiative and contributions in any form always
welcome.  You can get in touch with us `here
<https://docs.fedoraproject.org/en-US/neurofedora/overview/#_communicating_and_getting_help>`__.
We are happy to help you learn the skills needed to contribute to the project.
In fact, that is one of the major goals of the initiative---to spread technical
knowledge that is necessary to develop software for Neuroscience.


.. _NeuroFedora: https://neuro.fedoraproject.org
.. _neuron: https://src.fedoraproject.org/rpms/neuron
.. _auryn: https://src.fedoraproject.org/rpms/auryn
