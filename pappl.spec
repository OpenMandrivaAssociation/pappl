%define major 1
%define libname %mklibname pappl %{major}
%define devname %mklibname -d pappl

Summary:	Framework/Library for developing CUPS printer applications
Name:		pappl
Version:	1.3.0
Release:	1
Source0:	https://github.com/michaelrsweet/pappl/releases/download/v%{version}/pappl-%{version}.tar.gz
License:	Apache 2.0
BuildRequires:	pkgconfig(avahi-core)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	cups-devel
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng16)
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(zlib)
Requires:	%{libname} = %{EVRD}

%description
PAPPL is a simple C-based framework/library for developing CUPS Printer
Applications, which are the recommended replacement for printer drivers.

It was specifically developed to support LPrint and a future Gutenprint
Printer Application but is sufficiently general purpose to support any
kind of printer or driver that can be used on desktops, servers, and in
embedded environments.

%package -n %{libname}
Summary:	Library for the PAPPL printer application framework

%description -n %{libname}
Library for the PAPPL printer application framework

%package -n %{devname}
Summary:	Development files for the PAPPL printer application framework
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for the PAPPL printer application framework

%prep
%autosetup -p1
%configure --disable-static

%build
%make_build

%install
make install BUILDROOT=%{buildroot}
# We don't need the static lib
rm -f %{buildroot}%{_libdir}/*.a

%files
%{_bindir}/pappl-makeresheader
%{_datadir}/pappl
%{_docdir}/pappl
%{_mandir}/man1/*.1*

%files -n %{libname}
%{_includedir}/pappl
%{_libdir}/libpappl.so.%{major}
%{_libdir}/pkgconfig/pappl.pc
%{_mandir}/man3/*.3*

%files -n %{devname}
%{_libdir}/libpappl.so
