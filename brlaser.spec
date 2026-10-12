Name:           brlaser
Version:        6.2.8
Release:        %mkrel 1
Summary:        Open-source CUPS driver for Brother laser printers
License:        GPLv2+
Group:          System/Printing
URL:            https://github.com/Owl-Maintain/brlaser
Source0:        https://github.com/Owl-Maintain/brlaser/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cups-devel

Requires:       cups

%description
brlaser is an open-source CUPS driver for Brother monochrome laser
printers and multifunction devices, including the Brother DCP-7055.

%prep
%autosetup -n brlaser-%{version}

%build
cmake -S . -B build \
    -DCMAKE_BUILD_TYPE=Release

cmake --build build -j%{?_smp_build_ncpus}

%check
ctest --test-dir build --output-on-failure

%install
DESTDIR=%{buildroot} cmake --install build

%files
%license COPYING
%doc README.md ChangeLog
/usr/lib/cups/filter/rastertobrlaser
/usr/share/cups/drv/brlaser.drv

%changelog
* Mon Oct 12 2026 Barbary <188488783+baba78300@users.noreply.github.com> 6.2.8-1
- Package Owl-Maintain brlaser 6.2.8 for Mageia 10
- Build directly from upstream sources
- Enable upstream test suite during RPM build
- Verified with Brother DCP-7055
