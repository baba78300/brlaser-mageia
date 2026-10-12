# brlaser for Mageia

Unofficial Mageia packaging for
[Owl-Maintain/brlaser](https://github.com/Owl-Maintain/brlaser),
an open-source CUPS driver for Brother laser printers and multifunction devices.

## Tested configuration

This package has been built and tested on:

- Mageia 10 x86_64
- Owl-Maintain/brlaser 6.2.8
- Brother DCP-7055
- CUPS 2.4.x

The Brother DCP-7055 is detected by CUPS as:

    Brother DCP-7055, using Owl-Maintain/brlaser v6.2.8

A real print test was successfully completed on the DCP-7055.

## Package contents

The RPM installs:

    /usr/lib/cups/filter/rastertobrlaser
    /usr/share/cups/drv/brlaser.drv

The package is built directly from the official upstream source code and runs
the upstream test suite during the RPM build.

## Build

Required packages include:

    rpm-build
    cmake
    gcc-c++
    cups-devel

Place the upstream source archive specified by Source0 in:

    ~/rpmbuild/SOURCES/

Then build the binary RPM and source RPM with:

    rpmbuild -ba brlaser.spec

On Mageia 10 x86_64 this produces packages similar to:

    brlaser-6.2.8-1.mga10.x86_64.rpm
    brlaser-6.2.8-1.mga10.src.rpm

## Installation

Install the generated RPM as root:

    dnf install brlaser-6.2.8-1.mga10.x86_64.rpm

For the DCP-7055, verify CUPS detection with:

    lpinfo -m | grep -i DCP-7055

## Upstream project

Driver development is maintained by Owl-Maintain:

https://github.com/Owl-Maintain/brlaser

This repository only provides Mageia packaging and is not an official
Mageia or Owl-Maintain project.
