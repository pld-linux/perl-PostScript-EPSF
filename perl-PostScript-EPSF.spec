%define	pdir	PostScript
%define	pnam	EPSF
%include	/usr/lib/rpm/macros.perl
Summary:	PostScript-EPSF perl module
Summary(pl):	Modu� perla PostScript-EPSF
Name:		perl-PostScript-EPSF
Version:	0.01
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript-EPSF module provides the function include_epsf() that makes
it easy to include external EPSF files in your postscript output.

%description -l pl
PostScript-EPSF module udost�pnia funkcj� include_epsf(), kt�ra
u�atwia w��czanie plik�w EPSF do wyj�ciowego pliku postscriptowego.

%prep
%setup -q -n PostScript-EPSF-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/PostScript/EPSF.pm
