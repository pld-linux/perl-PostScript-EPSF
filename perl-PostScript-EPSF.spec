%include	/usr/lib/rpm/macros.perl
%define	pdir	PostScript
%define	pnam	EPSF
Summary:	PostScript::EPSF perl module
Summary(pl):	Modu� perla PostScript::EPSF
Name:		perl-PostScript-EPSF
Version:	0.01
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript::EPSF module provides the function include_epsf() that makes
it easy to include external EPSF files in your postscript output.

%description -l pl
PostScript::EPSF module udost�pnia funkcj� include_epsf(), kt�ra
u�atwia w��czanie plik�w EPSF do wyj�ciowego pliku postscriptowego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/PostScript/EPSF.pm
