#
# Conditional build:
# _without_tests - do not perform "make test"
# _with_ndf      - generate package with NDF support
# _with_gsd      - generate package with GSD support
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Astro
%define		pnam	FITS-Header
Summary:	Astro::FITS::Header Perl module - a FITS header
Summary(pl):	Modu³ Perla Astro::FITS::Header - nag³ówek FITS
Name:		perl-Astro-FITS-Header
Version:	2.6.1
Release:	3
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64e8a0c677ff02188a1784b5b27bcff9
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Astro::FITS::Header and associated sub-classes are tools for reading,
modifying and then writing out FITS standard header blocks to FITS and
NDF files.

%description -l pl
Astro::FITS::Header i stowarzyszone z nim podklasy stanowi± narzêdzie
s³u¿±ce do odczytu bloków nag³ówków zgodnych ze standardem FITS w
plikach FITS i NDF, a tak¿e do modyfikacji i zapisu tych bloków.

%package CFITSIO
Summary:	Astro::FITS::Header::CFITSIO - manipulates FITS headers from a FITS file
Summary(pl):	Astro::FITS::Header::CFITSIO - manipulowanie nag³ówkami FITS pliku FITS
Group:		Development/Languages/Perl
Requires:	%{name}

%description CFITSIO
Astro::FITS::Header::CFITSIO module makes use of the
Astro::FITS::CFITSIO module to read and write directly to a FITS HDU.

%description CFITSIO -l pl
Modu³ Astro::FITS::Header::CFITSIO dokonuje bezpo¶redniego odczytu i
zapisu FITS HDU za pomoc± modu³u Astro::FITS::CFITSIO.

%package NDF
Summary:	Astro::FITS::Header::NDF - manipulate FITS headers from NDF files
Summary(pl):	Astro::FITS::Header::NDF - manipulowanie nag³ówkami FITS plików NDF
Group:		Development/Languages/Perl
# only for install dirs ?
Requires:	%{name}

%description NDF
Astro::FITS::Header::NDF module makes use of the Starlink NDF module
to read and write to and NDF FITS extension or to a ".HEADER" block
in an HDS container file.

%description NDF -l pl
Modu³ Astro::FITS::Header::NDF odczytuje i zapisuje rozszerzenie NDF
FITS lub blok ".HEADER" pliku pojemnika HDS za pomoc± modu³u Starlink
NDF.

%package GSD
Summary:	Astro::FITS::Header::GSD - manipulate FITS headers from GSD files
Summary(pl):	Astro::FITS::Header::GSD - manipulowanie nag³ówkami FITS plików GSD
Group:		Development/Languages/Perl
Requires:	%{name}

%description GSD
Astro::FITS::Header::GSD module makes use of the Starlink GSD module
to read from a GSD header.

%description GSD -l pl
Modu³ Astro::FITS::Header::GSD odczytuje nag³ówek GSD za pomoc± modu³u
Starlink GSD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%dir %{perl_vendorlib}/Astro/FITS
%{perl_vendorlib}/Astro/FITS/Header.pm
%dir %{perl_vendorlib}/Astro/FITS/Header
%{perl_vendorlib}/Astro/FITS/Header/Item*
%{_mandir}/man3/Astro::FITS::Header.*
%{_mandir}/man3/Astro::FITS::Header::Item*

%files CFITSIO
%defattr(644,root,root,755)
%{perl_vendorlib}/Astro/FITS/Header/CFITSIO.pm
%{_mandir}/man3/*CFITSIO*

%if 0%{?_with_ndf:1}
%files NDF
%defattr(644,root,root,755)
%{perl_vendorlib}/Astro/FITS/Header/NDF.pm
%{_mandir}/man3/*NDF*
%endif

%if 0%{?_with_gsd:1}
%files GSD
%defattr(644,root,root,755)
%{perl_vendorlib}/Astro/FITS/Header/GSD.pm
%{_mandir}/man3/*GSD*
%endif
