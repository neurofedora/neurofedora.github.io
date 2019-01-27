NeuroFedora update: 2019 week 4
###############################
:date: 2019-01-27 14:09:10
:author: NeuroFedora
:category: News
:tags: Software, Blog
:slug: neurofedora-update-2019-week-4
:summary: An update on NeuroFedora_ in the 4th week of 2019: a new blog, and
          other software updates.


.. raw:: html

   <center>

.. figure:: {static}/images/NeuroFedoraLogo01.png
    :alt: NeuroFedora logo
    :width: 30%
    :class: img-responsive

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__

.. raw:: html

   </center>


Until now, I had been posting updates `on my personal blog under the
NeuroFedora tag <https://ankursinha.in/tag/neurofedora/>`__, but I thought it
was time we moved to a dedicated blog for NeuroFedora_. This will allow others
in the team to write posts, and, it'll ensure that all the information on
NeuroFedora_ is now disseminated by specific channels.

So, this week, apart from the new blog:

1. `neuron is in review <https://bugzilla.redhat.com/show_bug.cgi?id=1662526>`__
   and should be approved this week.
2. `python-tvb-data
   <https://bodhi.fedoraproject.org/updates/FEDORA-2019-872277e166>`__ is now in
   testing, so we can begin working on the main software for `The Virtual Brain
   simulator <https://www.thevirtualbrain.org/tvb/zwei>`__.
3. `SPM12 is now a WIP
   <https://github.com/sanjayankur31/rpm-specs/tree/spm12>`__. It bundles
   `FieldTrip <https://github.com/fieldtrip/fieldtrip>`__, so that will have to
   be packaged first.
4. the `STEPS simulator <https://github.com/CNS-OIST/STEPS>`__ is now `WIP
   <https://github.com/sanjayankur31/rpm-specs/tree/steps>`__. It bundles a few
   sources too, so they will have to be packaged first: `easyloggingpp
   <https://github.com/sanjayankur31/rpm-specs/tree/easyloggingpp>`__, and cvode
   are two major ones that need to be unbundled.
5. the `Arbor simulator
   <https://github.com/sanjayankur31/rpm-specs/tree/arbor>`__ is also a WIP. I
   ran into some trouble with CMake while trying to
   build it, but community members on the `devel list
   <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/UARN5KWBEMR22POWGDDF7WGCBAYT527X/>`__
   were quite quick to point out the issue.

----

We're going to continue packaging software one by one. We currently have 140
tools on our `list
<https://pagure.io/neuro-sig/NeuroFedora/issues?tags=S%3A+Needs+packaging>`__,
so it'll take some time before all of them are available in NeuroFedora_.

NeuroFedora_ is volunteer driven initiative and contributions in any form always
welcome.  You can get in touch with us `here
<https://docs.fedoraproject.org/en-US/neurofedora/overview/#_communicating_and_getting_help>`__.
We are happy to help you learn the skills needed to contribute to the project.
In fact, that is one of the major goals of the initiative---to spread technical
knowledge that is necessary to develop software for Neuroscience.

.. _NeuroFedora: https://neuro.fedoraproject.org
