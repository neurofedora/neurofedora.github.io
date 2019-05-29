How NeuroFedora provides software to its users
##############################################
:date: 2019-05-28 12:32:39
:author: Ankur Sinha
:category: Community
:tags: Software development, RPM, Packaging
:slug: how-neurofedora-provides-software-to-its-users
:status: draft
:summary: This post summarises the process that the NeuroFedora_ package
          maintainers follow to keep the software set up to date.


.. include:: logo.txt

Given the large chunk of updates that we published recently, we thought this is
a good chance to explain how the NeuroFedora_ team stays on top of all of this
software that is constantly being updated and improved.

#. It all starts with *upstream* releasing a new version.

   *Upstream* are the developers of the software. We at NeuroFedora_ (and most
   Linux distributions) are *downstream*: we take developed software, build and
   integrate it all, and provide it in easily installable *packages* to users.

   On Fedora, these packages are :code:`rpm` archives, while other
   distributions use other file formats.

#. The awesome `Anitya <https://github.com/release-monitoring/anitya>`__ tool
   that runs at https://release-monitoring.org detects an update, and files a
   bug notifying us of the new version.

   Here is an example bug that it filed to let us know that a new version of
   python-efel was now available:
   https://bugzilla.redhat.com/show_bug.cgi?id=1702573

The next steps require manual work. There are tools to make it all easier, but
this is where we humans come in.

3. One of the `NeuroFedora package maintainers
   <https://src.fedoraproject.org/group/neuro-sig>`__ notices the bug and
   begins to work on it.

#. We fetch the new source code and test to see how it has changed in the new
   release.

   Sometimes, there are backward incompatible API/ABI changes. In such cases,
   we have to see how *all* other software that depends on these is affected.
   This is documented in the `community policy on updating software
   <https://docs.fedoraproject.org/en-US/fesco/Updates_Policy/>`__. The idea is
   that when new versions of software are released, as package maintainers, one
   of our duties is to ensure that the new versions do not break existing
   systems for our users.

#. If everything seems to work fine, we update the spec file.

   *spec* files include instructions that tell the :code:`rpmbuild` tool how
   to build the software, and where all its files should go in the :code:`rpm`
   package. More information on the process can be found `here
   <https://fedoraproject.org/wiki/Category:Package_Maintainers#Introduction_to_packaging>`__.

#. We push the updated spec file to the package's dist-git repository on
   https://src.fedoraproject.org/rpms/.

#. We then queue up a new build on the `Koji build system
   <https://koji.fedoraproject.org/koji/>`__.

   The build system handles all our supported arches unless told not to do so.
   Currently, the Fedora community supports: :code:`x86_64, i686, armv7hl,
   aarch64, ppc64le, s390x`. More information on these architectures can be
   found `here <https://fedoraproject.org/wiki/Architectures>`__.

#. Once the builds have completed successfully, we push the builds to our
   `Quality Assurance <https://fedoraproject.org/wiki/QA>`__ pipeline for
   testing.

   It isn't enough to get the software to build correctly. We must
   also ensure that it *works* correctly.  The pipeline lets community members
   (including users) *test* these updated packages in a *staging repository*.

   *You can help test these updates.* All you need to do is install them, and
   provide feedback. This is all explained `here
   <https://fedoraproject.org/wiki/QA:Updates_Testing>`__.

#.  If the packages pass the community's battery of automated checks, and
    testers provide positive feedback on their functioning, they are then moved
    from the staging repositories to the *stable* repositories where they are
    available to all users.


.. include:: footer.txt

.. _NeuroFedora: https://neuro.fedoraproject.org
.. _CNS*2019: https://www.cnsorg.org/cns-2019-quick
.. _Flock: https://flocktofedora.org/
