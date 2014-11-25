#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_with	ndf	# build package with NDF support
%bcond_with	gsd	# build package with GSD support

%define		pdir	Astro
%define		pnam	FITS-Header
%include	/usr/lib/rpm/macros.perl
Summary:	Astro::FITS::Header Perl module - a FITS header
Summary(pl.UTF-8):	Moduł Perla Astro::FITS::Header - nagłówek FITS
Name:		perl-Astro-FITS-Header
Version:	3.07
Release:	2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3a9795ecc74269419340e900018a5840
URL:		http://search.cpan.org/dist/Astro-FITS-Header/
%if %{with tests}
BuildRequires:	perl-Astro-FITS-CFITSIO >= 1.01
%endif
BuildRequires:	perl-devel >= 1:5.8.2
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-base >= 5.8.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Astro::FITS::Header and associated sub-classes are tools for reading,
modifying and then writing out FITS standard header blocks to FITS and
NDF files.

%description -l pl.UTF-8
Astro::FITS::Header i stowarzyszone z nim podklasy stanowią narzędzie
służące do odczytu bloków nagłówków zgodnych ze standardem FITS w
plikach FITS i NDF, a także do modyfikacji i zapisu tych bloków.

%package CFITSIO
Summary:	Astro::FITS::Header::CFITSIO - manipulates FITS headers from a FITS file
Summary(pl.UTF-8):	Astro::FITS::Header::CFITSIO - manipulowanie nagłówkami FITS pliku FITS
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl-Astro-FITS-CFITSIO >= 1.01

%description CFITSIO
Astro::FITS::Header::CFITSIO module makes use of the
Astro::FITS::CFITSIO module to read and write directly to a FITS HDU.

%description CFITSIO -l pl.UTF-8
Moduł Astro::FITS::Header::CFITSIO dokonuje bezpośredniego odczytu i
zapisu FITS HDU za pomocą modułu Astro::FITS::CFITSIO.

%package NDF
Summary:	Astro::FITS::Header::NDF - manipulate FITS headers from NDF files
Summary(pl.UTF-8):	Astro::FITS::Header::NDF - manipulowanie nagłówkami FITS plików NDF
Group:		Development/Languages/Perl
# only for install dirs ?
Requires:	%{name} = %{version}-%{release}
Requires:	perl-NDF >= 1.42

%description NDF
Astro::FITS::Header::NDF module makes use of the Starlink NDF module
to read and write to and NDF FITS extension or to a ".HEADER" block in
an HDS container file.

%description NDF -l pl.UTF-8
Moduł Astro::FITS::Header::NDF odczytuje i zapisuje rozszerzenie NDF
FITS lub blok ".HEADER" pliku pojemnika HDS za pomocą modułu Starlink
NDF.

%package GSD
Summary:	Astro::FITS::Header::GSD - manipulate FITS headers from GSD files
Summary(pl.UTF-8):	Astro::FITS::Header::GSD - manipulowanie nagłówkami FITS plików GSD
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description GSD
Astro::FITS::Header::GSD module makes use of the Starlink GSD module
to read from a GSD header.

%description GSD -l pl.UTF-8
Moduł Astro::FITS::Header::GSD odczytuje nagłówek GSD za pomocą modułu
Starlink GSD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	prefix=%{_prefix} \
	destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%dir %{perl_vendorlib}/Astro/FITS
%{perl_vendorlib}/Astro/FITS/Header.pm
%dir %{perl_vendorlib}/Astro/FITS/Header
%{perl_vendorlib}/Astro/FITS/Header/Item*
%{perl_vendorlib}/Astro/FITS/Header/AST.pm
%{_mandir}/man3/Astro::FITS::Header.*
%{_mandir}/man3/Astro::FITS::Header::Item*
%{_mandir}/man3/Astro::FITS::Header::AST.3pm*

%files CFITSIO
%defattr(644,root,root,755)
%{perl_vendorlib}/Astro/FITS/Header/CFITSIO.pm
%{_mandir}/man3/*CFITSIO*

%if %{with ndf}
%files NDF
%defattr(644,root,root,755)
%{perl_vendorlib}/Astro/FITS/Header/NDF.pm
%{_mandir}/man3/*NDF*
%endif

%if %{with gsd}
%files GSD
%defattr(644,root,root,755)
%{perl_vendorlib}/Astro/FITS/Header/GSD.pm
%{_mandir}/man3/*GSD*
%endif
