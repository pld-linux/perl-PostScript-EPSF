%include	/usr/lib/rpm/macros.perl
%define	pdir	PostScript
%define	pnam	EPSF
Summary:	PostScript::EPSF perl module
Summary(pl):	Modu³ perla PostScript::EPSF
Name:		perl-PostScript-EPSF
Version:	0.01
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript::EPSF module provides the function include_epsf() that makes
it easy to include external EPSF files in your postscript output.

%description -l pl
PostScript::EPSF module udostêpnia funkcjê include_epsf(), która
u³atwia w³±czanie plików EPSF do wyj¶ciowego pliku postscriptowego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/PostScript/EPSF.pm
