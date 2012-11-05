#
# spec file for package patchelf
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           patchelf
Version:        0.6
Release:        0
License:        GPL-3.0
Summary:        A utility for patching ELF binaries
Url:            http://nixos.org/patchelf.html
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
# not working here
ExcludeArch:    ppc ppc64 %arm

%description
PatchELF is a simple utility for modifing existing ELF executables and
libraries.  It can change the dynamic loader ("ELF interpreter") of
executables and change the RPATH of executables and libraries.

%prep
%setup -q

%build
%configure
make

%check
make check

%install
%make_install
rm %{buildroot}/usr/share/doc/patchelf/README

%files
%defattr(-,root,root)
%doc README
/usr/bin/*
%{_mandir}/man*/patchelf.*

%changelog
