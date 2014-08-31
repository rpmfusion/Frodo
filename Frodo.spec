%define pkgversion %(echo %version|sed s/\\\\\./\\_/)

Summary: Commodore 64 emulator
Name: Frodo
Version: 4.1b
Release: 10%{?dist}
License: Distributable
Group: Applications/Emulators
URL: http://frodo.cebix.net/
Source0: http://frodo.cebix.net/downloads/%{name}V%{pkgversion}.Src.tar.gz
Source1: Frodo.png
Source2: Frodo.desktop
Source3: FrodoPC.desktop
Source4: FrodoSC.desktop
Patch0: Frodo-4.1b-paths.patch
Patch1: Frodo-4.1b-opt.patch
Patch2: Frodo-4.1b-alpha.patch
Patch3: Frodo-4.1b-SAM.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: autoconf
BuildRequires: SDL-devel >= 1.2.0
BuildRequires: libXt-devel 
BuildRequires: desktop-file-utils
Requires: hicolor-icon-theme

%package gui
Summary: Preferences editor for Frodo
Group: Applications/Emulators
Requires: %{name}
Requires: tk

%description
Frodo V4.1 is a free, portable C64 emulator for BeOS, Unix, MacOS,
AmigaOS, RiscOS and WinNT/95 systems.

This emulator focuses on the exact reproduction of special graphical
effects possible on the C64, and has therefore relatively high system
requirements. It should only be run on systems with at least a
PowerPC/Pentium/68060. Frodo is capable of running most games and
demos correctly, even those with FLI, FLD, DYCP, open borders,
multiplexed sprites, timing dependent decoders, fast loaders etc. 6510
emulation: All undocumented opcodes, 100 percent correct decimal mode,
instruction/cycle exact emulation. VIC emulation: Line-/cycle-based
emulation, all display modes, sprites with collisions/priorities, DMA
cycles, open borders, all $d011/$d016 effects. SID emulation:
Real-time digital emulation (16 bit, 44.1kHz), including filters (only
under BeOS, Linux, HP-UX, MacOS and AmigaOS). 1541 emulation: Drive
simulation in directories, .d64/x64 or .t64/LYNX files, or
processor-level 1541 emulation that works with about 95 percent of all
fast loaders and even some copy protection schemes. Other peripherals:
Keyboard and joystick (real joysticks (only under BeOS, Linux and
AmigaOS) or keyboard emulation). The full source code in C++ is
available. Frodo is freeware.

%description gui
An enhanced Tcl/Tk preferences GUI for Frodo written by Gerard Decatrel

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

%build
cd Src
autoconf
%configure
make %{?_smp_mflags} all FRODOHOME="\\\"%{_datadir}/Frodo/\\\""

%install
rm -rf %{buildroot}
install -d 755 %{buildroot}%{_bindir}
install -d 755 %{buildroot}%{_datadir}/Frodo/{64prgs,64imgs}
install -m 755 Src/Frodo Src/FrodoPC Src/FrodoSC %{buildroot}%{_bindir}
install -m 755 TkGui.tcl %{buildroot}%{_datadir}/Frodo
install -m 644 "Frodo Logo" "1541 ROM" "Basic ROM" "Char ROM" "Kernal ROM" \
  %{buildroot}%{_datadir}/Frodo
install -m 644 64prgs/* %{buildroot}%{_datadir}/Frodo/64prgs

#install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/

#install desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor dribble        \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE2}
desktop-file-install --vendor dribble        \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE3}
desktop-file-install --vendor dribble        \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE4}

%clean
rm -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%defattr(-,root,root)
%{_bindir}/Frodo
%{_bindir}/FrodoPC
%{_bindir}/FrodoSC
%{_datadir}/Frodo
%{_datadir}/applications/dribble-%{name}.desktop
%{_datadir}/applications/dribble-%{name}PC.desktop
%{_datadir}/applications/dribble-%{name}SC.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%doc CHANGES Docs/*
%exclude %{_datadir}/Frodo/TkGui.tcl

%files gui
%defattr(-,root,root)
%{_datadir}/Frodo/TkGui.tcl

%changelog
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

