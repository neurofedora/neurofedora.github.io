NEST 2.18.0 (and 2.16.0) are ready for use on NeuroFedora
##########################################################
:date: 2019-08-13 09:27:17
:author: A: kur Sinha
:category: News
:tags: NEST, Computational Modelling, Modularity
:slug: nest-2-18-0-and-2-16-0-are-ready-for-use-on-neurofedora
:summary: NEST 2.18.0 and 2.16.0 are ready to use on NeuroFedora_!

.. raw:: html

   <center>

.. figure:: {static}/images/20190813-nest-logo.png
    :alt: The NEST simulator
    :width: 100%
    :class: img-responsive

.. raw:: html

   </center>

|
|

After a bit of work and testing, NEST 2.18.0 and 2.16.0 are now both available
for use on NeuroFedora_. The docs have also been updated to include complete
instructions on how to install and use these tools:
https://docs.fedoraproject.org/en-US/neurofedora/nest/

Here are a few quick FAQs for your convenience:

Q: How do I use NEST on NeuroFedora?

    It only takes two steps to install NEST using :code:`dnf` (the default package manager):

    - Download and run (optionally install) a "live" Fedora Workstation image from https://getfedora.org
    - Install NEST 2.18.0: Run :code:`sudo dnf install python3-nest` in a terminal.

Q: How do I use version 2.16.0?

    2.16.0 is provided as a "module". To install the 2.16.0 version:

    - Download and run (optionally install) a "live" Fedora Workstation image from https://getfedora.org
    - Install NEST 2.16.0: Run :code:`sudo dnf module install nest:2.16.0` in a terminal.

    Please note that only one version of NEST can be installed at once.

Q: Does NEST in NeuroFedora include MPI support?

    Yes---variants built with both MPICH and OpenMPI are available to use.

Q: Does NEST in NeuroFedora include libneurosim/MUSIC/CSA: support?

    Not all of them yet.

    - libneurosim: Yes
    - MUSIC: No (under review: https://pagure.io/neuro-sig/NeuroFedora/issue/28)
    - CSA:  No (WIP: https://pagure.io/neuro-sig/NeuroFedora/issue/33)

Q: Where do I get help?

    The NeuroFedora team maintains multiple communication channels for support and general discussion: https://docs.fedoraproject.org/en-US/neurofedora/communicating/

Q: What other tools does NeuroFedora provide?

    The complete list includes neuron, auryn, PyLEMS, NineML and lots more: https://src.fedoraproject.org/group/neuro-sig

    Fedora also includes more software that is not specific to computational neuroscience---such as productivity and development tools, a variety of desktop environments, server and container focussed editions, and other science related software:

    - https://getfedora.org/
    - https://labs.fedoraproject.org/
    - https://spins.fedoraproject.org/

.. include:: footer.txt

.. _NeuroFedora: https://neuro.fedoraproject.org
