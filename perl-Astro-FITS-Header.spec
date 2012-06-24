%include	/usr/lib/rpm/macros.perl
%define		pdir	Astro
%define		pnam	FITS-Header
Summary:	Astro::FITS::Header Perl module
Summary(cs):	Modul Astro::FITS::Header pro Perl
Summary(da):	Perlmodul Astro::FITS::Header
Summary(de):	Astro::FITS::Header Perl Modul
Summary(es):	M�dulo de Perl Astro::FITS::Header
Summary(fr):	Module Perl Astro::FITS::Header
Summary(it):	Modulo di Perl Astro::FITS::Header
Summary(ja):	Astro::FITS::Header Perl �⥸�塼��
Summary(ko):	Astro::FITS::Header �� ����
Summary(no):	Perlmodul Astro::FITS::Header
Summary(pl):	Modu� Perla Astro::FITS::Header
Summary(pt):	M�dulo de Perl Astro::FITS::Header
Summary(pt_BR):	M�dulo Perl Astro::FITS::Header
Summary(ru):	������ ��� Perl Astro::FITS::Header
Summary(sv):	Astro::FITS::Header Perlmodul
Summary(uk):	������ ��� Perl Astro::FITS::Header
Summary(zh_CN):	Astro::FITS::Header Perl ģ��
Name:		perl-Astro-FITS-Header
Version:	2.2
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-CFITSIO.diff
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Astro::FITS::Header and associated sub-classes are tools for reading,
modifying and then writing out FITS standard header blocks to FITS and
NDF files.

%description -l cs
Modul Astro::FITS::Header pro Perl.

%description -l da
Perlmodul Astro::FITS::Header.

%description -l de
Astro::FITS::Header Perl Modul.

%description -l es
M�dulo de Perl Astro::FITS::Header.

%description -l fr
Module Perl Astro::FITS::Header.

%description -l it
Modulo di Perl Astro::FITS::Header.

%description -l ja
Astro::FITS::Header Perl �⥸�塼��

%description -l ko
Astro::FITS::Header �� ����.

%description -l no
Perlmodul Astro::FITS::Header.

%description -l pl
Astro::FITS::Header i stowarzyszone z nim podklasy stanowi� narz�dzie
s�u��ce do odczytu blok�w nag��wk�w zgodnych ze standardem FITS w
plikach FITS i NDF, a tak�e do modyfikacji i zapisu tych blok�w.

%description -l pt
M�dulo de Perl Astro::FITS::Header.

%description -l pt_BR
M�dulo Perl Astro::FITS::Header.

%description -l ru
������ ��� Perl Astro::FITS::Header.

%description -l sv
Astro::FITS::Header Perlmodul.

%description -l uk
������ ��� Perl Astro::FITS::Header.

%description -l zh_CN
Astro::FITS::Header Perl ģ��

%package CFITSIO
Summary:	Astro::FITS::Header::CFITSIO Perl module
Summary(cs):	Modul Astro::FITS::Header::CFITSIO pro Perl
Summary(da):	Perlmodul Astro::FITS::Header::CFITSIO
Summary(de):	Astro::FITS::Header::CFITSIO Perl Modul
Summary(es):	M�dulo de Perl Astro::FITS::Header::CFITSIO
Summary(fr):	Module Perl Astro::FITS::Header::CFITSIO
Summary(it):	Modulo di Perl Astro::FITS::Header::CFITSIO
Summary(ja):	Astro::FITS::Header::CFITSIO Perl �⥸�塼��
Summary(ko):	Astro::FITS::Header::CFITSIO �� ����
Summary(no):	Perlmodul Astro::FITS::Header::CFITSIO
Summary(pl):	Modu� Perla Astro::FITS::Header::CFITSIO
Summary(pt):	M�dulo de Perl Astro::FITS::Header::CFITSIO
Summary(pt_BR):	M�dulo Perl Astro::FITS::Header::CFITSIO
Summary(ru):	������ ��� Perl Astro::FITS::Header::CFITSIO
Summary(sv):	Astro::FITS::Header::CFITSIO Perlmodul
Summary(uk):	������ ��� Perl Astro::FITS::Header::CFITSIO
Summary(zh_CN):	Astro::FITS::Header::CFITSIO Perl ģ��
Group:		Development/Languages/Perl
Requires:	%{name}

%description CFITSIO
Astro::FITS::Header::CFITSIO module makes use of the
Astro::FITS::CFITSIO module to read and write directly to a FITS HDU.

%description CFITSIO -l pl
Modu� Astro::FITS::Header::CFITSIO dokonuje bezpo�redniego odczytu i
zapisu FITS HDU za pomoc� modu�u Astro::FITS::CFITSIO.

%package NDF
Summary:	Astro::FITS::Header::NDF Perl module
Summary(cs):	Modul Astro::FITS::Header::NDF pro Perl
Summary(da):	Perlmodul Astro::FITS::Header::NDF
Summary(de):	Astro::FITS::Header::NDF Perl Modul
Summary(es):	M�dulo de Perl Astro::FITS::Header::NDF
Summary(fr):	Module Perl Astro::FITS::Header::NDF
Summary(it):	Modulo di Perl Astro::FITS::Header::NDF
Summary(ja):	Astro::FITS::Header::NDF Perl �⥸�塼��
Summary(ko):	Astro::FITS::Header::NDF �� ����
Summary(no):	Perlmodul Astro::FITS::Header::NDF
Summary(pl):	Modu� Perla Astro::FITS::Header::NDF
Summary(pt):	M�dulo de Perl Astro::FITS::Header::NDF
Summary(pt_BR):	M�dulo Perl Astro::FITS::Header::NDF
Summary(ru):	������ ��� Perl Astro::FITS::Header::NDF
Summary(sv):	Astro::FITS::Header::NDF Perlmodul
Summary(uk):	������ ��� Perl Astro::FITS::Header::NDF
Summary(zh_CN):	Astro::FITS::Header::NDF Perl ģ��
Group:		Development/Languages/Perl
# only for install dirs ?
Requires:	%{name}

%description NDF
Astro::FITS::Header::NDF module makes use of the Starlink NDF module
to read and write to and NDF FITS extension or to a ".HEADER" block
in an HDS container file.

%description NDF -l pl
Modu� Astro::FITS::Header::NDF odczytuje i zapisuje rozszerzenie NDF
FITS lub blok ".HEADER" pliku pojemnika HDS za pomoc� modu�u Starlink
NDF.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}
#%{__make} test

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

%files NDF
%defattr(644,root,root,755)
%{perl_sitelib}/Astro/FITS/Header/NDF.pm
%{_mandir}/man3/*NDF*
