%include	/usr/lib/rpm/macros.perl
Summary:	PostScript-EPSF perl module
Summary(pl):	Modu³ perla PostScript-EPSF
Name:		perl-PostScript-EPSF
Version:	0.01
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/PostScript/PostScript-EPSF-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript-EPSF module provides the function include_epsf() that makes
it easy to include external EPSF files in your postscript output.

%description -l pl
PostScript-EPSF module udostêpnia funkcjê include_epsf(), która
u³atwia w³±czanie plików EPSF do wyj¶ciowego pliku postscriptowego.

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
