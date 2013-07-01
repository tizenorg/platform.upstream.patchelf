Name:           patchelf
Version:        0.6
Release:        0
License:        GPL-3.0
Summary:        A utility for patching ELF binaries
Url:            http://nixos.org/patchelf.html
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
Source1001: 	patchelf.manifest
BuildRequires:  gcc-c++
# not working here
ExcludeArch:    ppc ppc64 %arm

%description
PatchELF is a simple utility for modifing existing ELF executables and
libraries.  It can change the dynamic loader ("ELF interpreter") of
executables and change the RPATH of executables and libraries.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
make

%check
make check

%install
%make_install
rm %{buildroot}/usr/share/doc/patchelf/README

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%doc README
/usr/bin/*
%{_mandir}/man*/patchelf.*

%changelog
