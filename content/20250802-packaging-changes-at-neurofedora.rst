Packaging changes at NeuroFedora
################################
:date: 2025-08-02 14:02:06
:modified: 2025-08-02 14:02:06
:authors: Ankur
:category: News
:tags: Computational Modelling, Computational Neuroscience, Documentation, Fedora Lab, Neuroscience, FOSS, Fedora
:slug: packaging-changes-at-neurofedora
:summary: The NeuroFedora_ team has decided to make a couple of changes to the artefacts that we produce and maintain. Please read the post for details.

The NeuroFedora_ team has decided to make a couple of changes to the artefacts that we produce and maintain:

- The Comp Neuro Lab ISO image has been dropped.
- We are moving away from packaging Python software that is easily installable from PyPi_ into rpms for the Fedora repositories to testing it out on Fedora.

Over the years that the NeuroFedora_ team has been maintaining neuroscience rpm packages for the Fedora repositories, we have amassed a rather large number, `almost ~500 packages <https://src.fedoraproject.org/group/neuro-sig>`__.
That is great, and we are extremely pleased with our coverage of the neuroscience software ecosystem.
However, given that the team is composed of a few volunteers who can only dedicate limited amounts of their time to maintaining packages, we were beginning to find that we were unable to keep up with the increasing workload.

Further, we realised that the use case for including all neuroscience software in Fedora was no longer clear---was it really required for us to package all of it for users?

An example case is the Python ecosystem.
Usually, users/researchers/developers tend to install Python software directly from PyPi_ rather than relying on system packages that we provide.
The suggested use of virtual environments to isolate projects and their dependencies also requires the use of software directly from PyPi_, rather than using our system packages.
Therefore, for software that can be installed directly, we argue that it is less important that we package them.
Instead, it is more useful to our user base if we thoroughly test that this set of software can be properly installed and used on Fedora---on all the different versions of Python that a Fedora release supports.

So, a new guideline that we now follow is:

- prioritise packaging software that cannot be easily installed from upstream forges (such as PyPi_)

Following this, we have made a start on the Python packages that we maintain:

- we made a list of software that is easily installable from PyPi_
- we began dropping them from Fedora, and instead testing their usage from PyPi_

The testing involves:

- checking that the software and its extras can be successfully installed on Fedora using `pip`
- checking that the modules that the software include can be successfully imported

We `automate these tests using PyTest <https://pagure.io/neuro-sig/NeuroFedora/blob/main/f/python-package-usage-check>`__, and a daily report is published on `fedorapeople.org here <https://ankursinha.fedorapeople.org/neurofedora/package-status/>`__.

Our `documentation <https://https://docs.fedoraproject.org/en-US/neurofedora/>`__ has also been updated to reflect this change.
We now include two tables on each page.
One table provides information about the software that can be installed from PyPi_, and so is not included in rpm form in Fedora.
The other provides information about the software that continues to be included in Fedora, because it cannot be easily installed from PyPi_ directly.

We will continue reporting issues to upstream developers as we have done before.
The difference now is that we work directly with what they publish, rather than our rpm packaged versions of what they publish.

You can follow this discussion and progress `here <https://pagure.io/neuro-sig/NeuroFedora/issue/580>`__.
Please refer to the lists in the documentation for the up to date list of packages we include/test.


.. _NeuroFedora: https://neuro.fedoraproject.org
.. _PyPi: https://pypi.org
