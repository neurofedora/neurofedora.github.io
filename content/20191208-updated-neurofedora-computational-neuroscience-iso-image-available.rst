Updated NeuroFedora Computational Neuroscience ISO image available
##################################################################
:date: 2019-12-08 12:14:11
:author: Ankur Sinha
:category: News
:tags: Computational Modelling, GENESIS,  NEST, Neuron, Julia, R
:slug: updated-neurofedora-computational-neuroscience-iso-image-available
:summary: An updated ready to use ISO image with Computational Neuroscience
          software is now available. It now includes Julia and R.


.. include:: logo.txt


We've been working on making more software available in NeuroFedora_. Neuron_
is now built with IV_ support, so models from ModelDB_ that use these should
now be runnable using NeuroFedora_.

The `Computational Neuroscience ISO image
<{filename}/20191105-neurofedora-computational-neuroscience-iso-image-is-now-available.rst>`__
has been updated to include these improvements. After receiving some feedback,
we've also added Julia and R to the image. The new version, 20191201, is
available for download `here <https://fedorapeople.org/groups/neuro-sig/>`__.
The checksum file is also provided. So please test your download for
correctness before you proceed to use it.

On a Linux system, please download both files (ISO and CHECKSUM), and run the
following command in a terminal, in the directory where the files were
downloaded, to verify the downloaded ISO:

.. code:: bash

    sha256sum -c Fedora-31-Comp-Neuro-20191201-1-x86_64-CHECKSUM



Other updates
--------------

In the meantime, we continue to package more software from our (rather long)
`list <https://pagure.io/neuro-sig/NeuroFedora/issues?status=Open&tags=F%3A+Computational+neuroscience>`__.
jLEMS_ is now in testing; Arbor_ is in ready for `review
<https://bugzilla.redhat.com/show_bug.cgi?id=1780906>`__; Napari_ is being
`worked upon <https://pagure.io/neuro-sig/NeuroFedora/issue/305>`__; along with
a bunch of other tools. Help is always welcome. So if you'd have the software
development skills required to build tools from source or would like to
develop these, please get in touch with us!


NeuroFedora at FOSDEM
---------------------

We've submitted an abstract to the `Open Research Tools and Technologies
Devroom
<https://fosdem.org/2020/schedule/track/open_research_tools_and_technologies/>`__
at FOSDEM which will be held Brussels on February 1 and 2. There will also be
general Fedora presence at the event, with a booth too. You can learn more
about Fedora at FOSDEM `here <https://fedoraproject.org/wiki/FOSDEM_2020>`__.

Please get in touch with the people listed on the event page for more
information on Fedora at FOSDEM. For NeuroFedora_ specific inquiries, you can
contact `major <https://fedoraproject.org/wiki/User:Major>`__ who is the
NeuroFedora_ team member organising our presence at the event (or ping the team
on our communication channels).

Where we need help
------------------

There's always lots to do. Here's a short list of where we need help:

- including new software: https://pagure.io/neuro-sig/NeuroFedora/issues,
- using and testing the software, to ensure that it works correctly: just
  download the ISO or install tools and use them, and `file bugs if (when,
  rather) you find them
  <https://docs.fedoraproject.org/en-US/quick-docs/howto-file-a-bug/>`__,
- keeping our `documentation <https://neuro.fedoraproject.org>`__ up to date:
  documentation is paramount, so we need to keep it up to date,


I won't list the skills that these tasks need, because we're not simply looking
for people who have them already. We are looking for people who'd like to
promote Open Science, and we will help them learn the skills.


.. include:: footer.txt

.. _NeuroFedora: https://neuro.fedoraproject.org
.. _Neuron: https://src.fedoraproject.org/rpms/neuron
.. _IV: https://src.fedoraproject.org/rpms/iv
.. _jLEMS: https://src.fedoraproject.org/rpms/jlems
.. _ModelDB: https://senselab.med.yale.edu/ModelDB/
.. _Arbor: https://github.com/arbor-sim/arbor
.. _Napari: http://napari.org/
