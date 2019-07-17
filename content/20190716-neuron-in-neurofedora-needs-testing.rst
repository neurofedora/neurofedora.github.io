NEURON in NeuroFedora needs testing
###################################
:date: 2019-07-17 08:52:51
:author: Ankur Sinha
:category: News
:tags: NEURON, Quality Assurance, Bodhi
:slug: neuron-in-neurofedora-needs-testing
:summary: The NEURON_ simulator in NeuroFedora_ requires testing


.. include:: logo.txt

We have been working on including the NEURON_ simulator in NeuroFedora_ for a
while now. The build process that NEURON_ uses has certain peculiarities that
make it a little harder to build.

For those that are interested in the technical details, while the main NEURON_
core is built using the standard :code:`./configure; make ; make install`
process that cleanly differentiates the "build" and "install" phases, the
Python bits are built as a "post-install hook". That is to say, they are built
after the other bits in the "install" step instead of the "build" step. This
implies that the build is not quite straightforward and must be slightly
tweaked to ensure that the `Fedora packaging guidelines
<https://docs.fedoraproject.org/en-US/packaging-guidelines/>`__ are met.

After discussing things on this `Github issue
<https://github.com/neuronsimulator/nrn/issues/238>`__, the developers,
`@nrnhines <https://github.com/nrnhines>`__ (Michael Hines) and `@ramcdougal
<https://ramcdougal.com/>`__ (Robert A McDougal) helped me understand the
complexities of the build process and get it done. They have also mentioned
that NEURON_ is now moving to a CMake_ based build system and should be simpler
to work with in the future. CMake_ is generally nicer for projects that include
different languages and build systems.

After a few hours of work, NEURON_ is now ready to use in NeuroFedora_. It is
built with Python 3, and does not currently provide IV and MPI bits. These will
be worked upon later. Since MUSIC_ is not yet in NeuroFedora_, NEURON_ does not
support MUSIC_ either currently. This is also a `work in progress
<https://pagure.io/neuro-sig/NeuroFedora/issue/28>`__.

I have tested the NEURON_ build on my machine with a few example simulations
and it works well, but this cannot be considered exhaustive testing of the
package. If you have a Fedora_ system, please test NEURON_ and let us know if
you notice any issues. Here's how.

Step 1: Set up a Fedora installation
------------------------------------

NeuroFedora_ is based on Fedora_, so the simplest way to use it is to install a
Fedora Workstation using the live images available on https://getfedora.org.
You can either install it on a system or use a virtual machine if you wish.
NeuroFedora_ includes lots of other software for neuroscience also. You can
learn more in our `documentation
<https://docs.fedoraproject.org/en-US/neurofedora/software/>`__.  Fedora_, in
general, provides lots of other software too. You can search them using the
`Fedora Packages web application
<https://apps.fedoraproject.org/packages/s/>`__.


Step 2: Install NEURON
-----------------------

I would recommend updating your system before proceeding using :code:`dnf` in a
terminal:

.. code:: bash

    sudo dnf update --refresh


Then, you can install NEURON_. It is currently in the testing repositories, so
they will need to be enabled for the command:


.. code:: bash

    sudo dnf --enablerepo=updates-testing install neuron python3-neuron


Step 3: Test it out
--------------------

Test it out with your models. Hopefully, everything will work fine. The NEURON_
documentation is here for those that would like to tinker with it too:
https://www.neuron.yale.edu/neuron/docs

Step 4: Give feedback
----------------------

.. raw:: html

   <center>

.. figure:: {static}/images/20190716-Bodhi.png
    :alt: Bodhi logo
    :width: 30%
    :class: img-responsive

    Bodhi_, the Fedora Quality Assurance web application.

.. raw:: html

   </center>

This step is optional, especially if everything works fine. If you experience
any issues, please do get in touch with us. You can either contact us directly
using one of our `communication channels
<https://docs.fedoraproject.org/en-US/neurofedora/communicating/>`__, or you
can **give karma** to the update on Bodhi_. The latter is preferred.

Bodhi_ is the system Fedora_ uses for pushing updates to users. In a nutshell:

- a new version of software is released
- the Fedora_ maintainer updates the Fedora_ package.
- the maintainer submits the new Fedora_ package to Bodhi_
- the package remains in the :code:`updates-testing` repositories while users
  test it out and provide feedback.
- if the update receives positive feedback (positive karma), it is
  automatically pushed to the :code:`updates` repository for all users to
  receive the new version.
- if the update receives negative feedback, the new version is not sent out to
  users and the maintainer must fix the reported issues and submit a new
  version of the package for testing again.

This workflow applies to all Fedora_ packages, thus ensuring that there's
plenty of time for issues to be flagged before the software reaches users.  So,
if you have a few minutes to spare, please help us by testing these packages
out. The updates for Fedora 29 and Fedora 30 are both here:
https://bodhi.fedoraproject.org/updates/?packages=neuron

Please note that this requires an Fedora_ account, since that's the account
system that links all Fedora_ community infrastructure. This Fedora Magazine
post provides an excellent resource on setting up a Fedora_ Account:
https://fedoramagazine.org/getting-set-up-with-fedora-project-services/

Detailed information on testing updates in Fedora_ can be found here on the
Quality Assurance (QA) team's documentation:
https://fedoraproject.org/wiki/QA:Updates_Testing



.. include:: footer.txt

.. _NeuroFedora: https://neuro.fedoraproject.org
.. _NEURON: https://www.neuron.yale.edu/neuron/
.. _CMake: https://cmake.org/
.. _Fedora: https://getfedora.org
.. _MUSIC: https://github.com/INCF/MUSIC
.. _Bodhi: https://bodhi.fedoraproject.org
