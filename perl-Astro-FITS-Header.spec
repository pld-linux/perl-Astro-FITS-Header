#
# Conditional build:
# _without_tests - do not perform "make test"
# _with_ndf      - generate package with NDF support
%include	/usr/lib/rpm/macros.perl
%define		pdir	Astro
%define		pnam	FITS-Header
Summary:	Astro::FITS::Header Perl module
Summary(cs):	Modul Astro::FITS::Header pro Perl
Summary(da):	Perlmodul Astro::FITS::Header
Summary(de):	Astro::FITS::Header Perl Modul
Summary(es):	Módulo de Perl Astro::FITS::Header
Summary(fr):	Module Perl Astro::FITS::Header
Summary(it):	Modulo di Perl Astro::FITS::Header
Summary(ja):	Astro::FITS::Header Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Astro::FITS::Header ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Astro::FITS::Header
Summary(pl):	Modu³ Perla Astro::FITS::Header
Summary(pt):	Módulo de Perl Astro::FITS::Header
Summary(pt_BR):	Módulo Perl Astro::FITS::Header
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Astro::FITS::Header
Summary(sv):	Astro::FITS::Header Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Astro::FITS::Header
Summary(zh_CN):	Astro::FITS::Header Perl Ä£¿é
Name:		perl-Astro-FITS-Header
Version:	2.4
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
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
Summary:	Astro::FITS::Header::CFITSIO Perl module
Summary(cs):	Modul Astro::FITS::Header::CFITSIO pro Perl
Summary(da):	Perlmodul Astro::FITS::Header::CFITSIO
Summary(de):	Astro::FITS::Header::CFITSIO Perl Modul
Summary(es):	Módulo de Perl Astro::FITS::Header::CFITSIO
Summary(fr):	Module Perl Astro::FITS::Header::CFITSIO
Summary(it):	Modulo di Perl Astro::FITS::Header::CFITSIO
Summary(ja):	Astro::FITS::Header::CFITSIO Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Astro::FITS::Header::CFITSIO ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Astro::FITS::Header::CFITSIO
Summary(pl):	Modu³ Perla Astro::FITS::Header::CFITSIO
Summary(pt):	Módulo de Perl Astro::FITS::Header::CFITSIO
Summary(pt_BR):	Módulo Perl Astro::FITS::Header::CFITSIO
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Astro::FITS::Header::CFITSIO
Summary(sv):	Astro::FITS::Header::CFITSIO Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Astro::FITS::Header::CFITSIO
Summary(zh_CN):	Astro::FITS::Header::CFITSIO Perl Ä£¿é
Group:		Development/Languages/Perl
Requires:	%{name}

%description CFITSIO
Astro::FITS::Header::CFITSIO module makes use of the
Astro::FITS::CFITSIO module to read and write directly to a FITS HDU.

%description CFITSIO -l pl
Modu³ Astro::FITS::Header::CFITSIO dokonuje bezpo¶redniego odczytu i
zapisu FITS HDU za pomoc± modu³u Astro::FITS::CFITSIO.

%if %{?_with_ndf:1}%{!?_with_ndf:0}
%package NDF
Summary:	Astro::FITS::Header::NDF Perl module
Summary(cs):	Modul Astro::FITS::Header::NDF pro Perl
Summary(da):	Perlmodul Astro::FITS::Header::NDF
Summary(de):	Astro::FITS::Header::NDF Perl Modul
Summary(es):	Módulo de Perl Astro::FITS::Header::NDF
Summary(fr):	Module Perl Astro::FITS::Header::NDF
Summary(it):	Modulo di Perl Astro::FITS::Header::NDF
Summary(ja):	Astro::FITS::Header::NDF Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Astro::FITS::Header::NDF ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Astro::FITS::Header::NDF
Summary(pl):	Modu³ Perla Astro::FITS::Header::NDF
Summary(pt):	Módulo de Perl Astro::FITS::Header::NDF
Summary(pt_BR):	Módulo Perl Astro::FITS::Header::NDF
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Astro::FITS::Header::NDF
Summary(sv):	Astro::FITS::Header::NDF Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Astro::FITS::Header::NDF
Summary(zh_CN):	Astro::FITS::Header::NDF Perl Ä£¿é
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
%endif

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
%dir %{perl_sitelib}/Astro/FITS
%{perl_sitelib}/Astro/FITS/Header.pm
%dir %{perl_sitelib}/Astro/FITS/Header
%{perl_sitelib}/Astro/FITS/Header/[^CN]*
%{_mandir}/man3/Astro::FITS::Header.*
%{_mandir}/man3/Astro::FITS::Header::[^CN]*

%files CFITSIO
%defattr(644,root,root,755)
%{perl_sitelib}/Astro/FITS/Header/CFITSIO.pm
%{_mandir}/man3/*CFITSIO*

%if %{?_with_ndf:1}%{!?_with_ndf:0}
%files NDF
%defattr(644,root,root,755)
%{perl_sitelib}/Astro/FITS/Header/NDF.pm
%{_mandir}/man3/*NDF*
%endif
