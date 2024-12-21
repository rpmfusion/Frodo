Summary: Commodore 64 emulator
Name: Frodo
Version: 4.5
Release: 1%{?dist}
License: GPL-2.0-or-later
URL: http://frodo.cebix.net/
Source0: https://github.com/cebix/frodo4/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool
BuildRequires: SDL2-devel
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils
Requires: hicolor-icon-theme

Obsoletes: %{name}-gui <= 4.1b

%description
Frodo is a free, portable Commodore 64 emulator that runs on a variety
of platforms, with a focus on the exact reproduction of special graphical
effects possible on the C64.

Frodo comes in two flavors: The regular "Frodo" which uses a cycle-exact
emulation, and the simplified "Frodo Lite" which is less compatible but runs
better on slower machines.


%prep
%autosetup -n frodo4-%{version}


%build
autoreconf -fvi
%configure
%make_build


%install
%make_install

# Validate desktop files
desktop-file-validate \
   %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate \
   %{buildroot}%{_datadir}/applications/%{name}Lite.desktop


%files
%{_bindir}/Frodo
%{_bindir}/FrodoLite
%{_datadir}/Frodo
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}Lite.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/mime/packages/vnd.cbm-%{name}.xml
%doc %{_docdir}/%{name}
%exclude %{_docdir}/%{name}/COPYING
%license COPYING


%changelog
* Mon Dec 16 2024 Andrea Musuruane <musuruan@gmail.com> - 4.5-1
- Updated to new upstream release

* Mon Nov 04 2024 Andrea Musuruane <musuruan@gmail.com> - 4.4-1
- Updated to new upstream release

* Sun Oct 13 2024 Andrea Musuruane <musuruan@gmail.com> - 4.3-1
- Updated to new upstream release

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1b-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1b-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1b-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1b-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1b-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1b-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1b-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1b-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1b-16
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 4.1b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 4.1b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.1b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.1b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul  7 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 4.1b-11
- Fix building with gcc6 / fix FTBFS

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 4.1b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 4.1b-9
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Mar 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.1b-8
- Rebuilt for c++ ABI breakage

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.1b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 4.1b-6
- rebuild for new F11 features

* Fri Nov 02 2007 Andrea Musuruane <musuruan@gmail.com> 4.1b-5
- removed %%{?dist} tag from changelog
- updated icon cache scriptlets to be compliant to new guidelines

* Sun Mar 25 2007 Andrea Musuruane <musuruan@gmail.com> 4.1b-4
- moved preference editor in a subpackage
- changed desktop categories to Game;Emulator

* Tue Feb 27 2007 Andrea Musuruane <musuruan@gmail.com> 4.1b-3
- added libXt-devel to BR to fix building on FC5

* Sat Feb 24 2007 Andrea Musuruane <musuruan@gmail.com> 4.1b-2
- changed desktop files to open terminal otherwise SAM cannot be run

* Sat Feb 10 2007 Andrea Musuruane <musuruan@gmail.com> 4.1b-1
- first release for Dribble based on current PLD package
- fixed License tag
- updated URL tag
- updated Source tag
- fixed patch names to meet Fedora guidelines
- added a patch based on the current OpenBSD port to fix SAM
- updated Build Requires
- fixed BuildRoot to meet Fedora guidelines
- added %%{?_smp_mflags} to make invocation to speed up SMP builds
- fixed %%files
- used Frodo icon made by Christian Rosentreter. 
  Downloaded from http://www.christianrosentreter.com/
- added desktop files
- minor changes

