Keeping software in NeuroFedora up to date
##########################################
:date: 2019-06-03 08:37:00
:author: Ankur Sinha
:category: Community
:tags: Software development, RPM, Packaging
:slug: keeping-software-in-neurofedora-up-to-date
:status: draft
:summary: This post summarises the process that the NeuroFedora_ package
          maintainers follow to keep the software set up to date.


.. include:: logo.txt

Given the large number of updates we published recently, we thought this is a
good chance to explain how the NeuroFedora_ team stays on top of all of this
software that is constantly being updated and improved.

Upstream releases a new version
-------------------------------

.. figure:: {static}/images/20190603-indexed-gzip.png
    :alt: Screenshot: upstream releases a new version of indexed-gzip on Github
    :width: 90%
    :class: img-responsive
    :target: {static}/images/20190603-indexed-gzip.png

|

It all starts with *upstream* releasing a new version.

*Upstream* are the developers of the software. We at NeuroFedora_ (and most
Linux distributions) are *downstream*: we take developed software, build and
integrate it all, and provide it in easily installable *packages* to users.

On Fedora, these packages are provided as :code:`rpm` archives via the
repositories. Other distributions may use other formats.

Anitya notifies us maintainers via Bugzilla
-------------------------------------------

.. figure:: {static}/images/20190603-indexed-gzip-anitya.png
    :alt: Screenshot: Anitya detects the new version.
    :width: 90%
    :class: img-responsive
    :target: {static}/images/20190603-indexed-gzip-anitya.png

|

**Anitya**  runs at https://release-monitoring.org and monitors upstream for
new versions.  `Anitya <https://github.com/release-monitoring/anitya>`__ is
able to monitor different upstream release methods such as Github, PyPi,
Sourceforge, Gitlab, and so on.  When Anitya detects a new version, it files a
bug on our community bug tracker at https://bugzilla.redhat.com notifying the
maintainers.


Maintainers test and update the Fedora package
----------------------------------------------

.. figure:: {static}/images/20190603-indexed-gzip-bugzilla.png
    :alt: Screenshot: Anitya files a bug notifying the maintainers
    :width: 90%
    :class: img-responsive
    :target: {static}/images/20190603-indexed-gzip-bugzilla.png

|

Once the bug has been filed, the next steps require manual work. There are
tools to make it all easier, but this is where we humans come in.

One of the `NeuroFedora package maintainers
<https://src.fedoraproject.org/group/neuro-sig>`__ notices the bug and begins
to work on it. All notifications from bugzilla are sent to the neuro-sig
mailing list, so the team is usually always aware of these.

First, we fetch the new source code and test it to see how it has changed in
the new release.

Sometimes, there are backward incompatible API/ABI changes. In such cases,
we have to see how *all* other software that depends on these is affected.
This is documented in the `community policy on updating software
<https://docs.fedoraproject.org/en-US/fesco/Updates_Policy/>`__. The idea is
that when new versions of software are released, as package maintainers, one
of our duties is to ensure that the new versions do not break existing
systems for our users.

Maintainers update the spec
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: {static}/images/20190603-indexed-gzip-sources.png
    :alt: Screenshot: A package maintainer updates the *spec* file.
    :width: 90%
    :class: img-responsive
    :target: {static}/images/20190603-indexed-gzip-sources.png

|

If everything seems to work fine, we begin to update the Fedora package. The
first step here is to update the *spec* file.

*spec* files provide instructions that tell the :code:`rpmbuild` tool how to
build the software, and where all its files should go in the :code:`rpm`
package. More information on the process can be found `here
<https://fedoraproject.org/wiki/Category:Package_Maintainers#Introduction_to_packaging>`__.

The spec file resides in the package's dist-git repository on
https://src.fedoraproject.org/rpms/ where other Fedora tools can access it.
When this has been updated to build the newest release, we queue up a new build
on the `Koji build system <https://koji.fedoraproject.org/koji/>`__.

.. figure:: {static}/images/20190603-indexed-gzip-koji.png
    :alt: Screenshot: A package maintainer queues up a new build.
    :width: 90%
    :class: img-responsive
    :target: {static}/images/20190603-indexed-gzip-koji.png

|


The build system handles all our supported arches unless told not to do so.
Currently, the Fedora community supports: :code:`x86_64, i686, armv7hl,
aarch64, ppc64le, s390x`. More information on these architectures can be found
`here <https://fedoraproject.org/wiki/Architectures>`__.

Quality assurance: the community tests the new packages
--------------------------------------------------------

Once the builds have completed successfully, we push the builds to our `Quality
Assurance <https://fedoraproject.org/wiki/QA>`__ pipeline for testing.

.. figure:: {static}/images/20190603-indexed-gzip-bodhi.png
    :alt: Screenshot: The Bodhi QA system manages our updates and their testing.
    :width: 90%
    :class: img-responsive
    :target: {static}/images/20190603-indexed-gzip-bodhi.png

|


It isn't enough to get the software to build correctly. We must also ensure
that it *works* correctly.  The pipeline lets community members (including
users) *test* these updated packages in a *staging repository*.

*You can help test these updates.* All you need to do is install them, and
provide feedback. This is all explained `here
<https://fedoraproject.org/wiki/QA:Updates_Testing>`__.

.. figure:: {static}/images/20190603-indexed-gzip-bodhi-ind.png
    :alt: Screenshot: An update on Bodhi that has been pushed to stable.
    :width: 90%
    :class: img-responsive
    :target: {static}/images/20190603-indexed-gzip-bodhi-ind.png

|

If the packages pass the community's battery of automated checks, and testers
provide positive feedback on their functioning, they are then moved from the
staging repositories to the *stable* repositories where they are available to
all users.


These general steps are not limited to the NeuroFedora_ team. They are followed
by all `Fedora community
<https://docs.fedoraproject.org/en-US/project/#_what_is_fedora_all_about>`__
`package maintainers
<https://fedoraproject.org/wiki/Join_the_package_collection_maintainers>`__


.. include:: footer.txt

.. _NeuroFedora: https://neuro.fedoraproject.org
.. _CNS*2019: https://www.cnsorg.org/cns-2019-quick
.. _Flock: https://flocktofedora.org/
