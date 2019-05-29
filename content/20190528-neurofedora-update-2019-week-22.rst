NeuroFedora update: 2019 week 22
################################
:date: 2019-05-28 11:29:33
:author: Ankur Sinha
:slug: neurofedora-update-2019-week-22
:category: News
:tags: Software
:summary: An update on NeuroFedora_ in the 22nd week of 2019: more software
          updates.


.. include:: logo.txt

An update on what we have been up to at NeuroFedora_ is long `overdue
<https://pagure.io/neuro-sig/NeuroFedora/issue/232>`__!
In the last few weeks, all of these were updated to their latest versions and
are now available to NeuroFedora_ users:

- `python-missingno <https://src.fedoraproject.org/rpms/python-missingno>`__
- `python-nineml <https://src.fedoraproject.org/rpms/python-nineml>`__
- `python-dipy <https://src.fedoraproject.org/rpms/python-dipy>`__
- `python-pybids <https://src.fedoraproject.org/rpms/python-pybids>`__
- `python-brian2 <https://src.fedoraproject.org/rpms/python-brian2>`__
- `python-pymatreader <https://src.fedoraproject.org/rpms/python-pymatreader>`__
- `python-pysb <https://src.fedoraproject.org/rpms/python-pysb>`__
- `python-libNeuroML <https://src.fedoraproject.org/rpms/python-libNeuroML>`__
- `python-efel <https://src.fedoraproject.org/rpms/python-efel>`__
- `python-petlink <https://src.fedoraproject.org/rpms/python-petlink>`__
- `python-grabbit <https://src.fedoraproject.org/rpms/python-grabbit>`__
- `python-xnat <https://src.fedoraproject.org/rpms/python-xnat>`__
- `python-chaospy <https://src.fedoraproject.org/rpms/python-chaospy>`__
- `python-nilearn <https://src.fedoraproject.org/rpms/python-nilearn>`__
- `python-pynwb- <https://src.fedoraproject.org/rpms/python-pynwb->`__
- `python-hdfs <https://src.fedoraproject.org/rpms/python-hdfs>`__

The contain various bug fixes and enhancements. Please update your system to
the latest versions using `dnf`. You can also use the graphical package manager
that you prefer. `dnf`, however, will work on all installations (apart from
`Silverblue <https://silverblue.fedoraproject.org/>`__ which is rpm-ostree based.).

.. code:: bash

    sudo dnf update --refresh



As I write this post, the newest version of `VXL
<https://src.fedoraproject.org/rpms/vxl>`__ is building on the system. This
took quite a bit of work to update but that is a story for another day :)

.. include:: footer.txt

.. _NeuroFedora: https://neuro.fedoraproject.org
