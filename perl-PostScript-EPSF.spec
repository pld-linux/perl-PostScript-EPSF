%include	/usr/lib/rpm/macros.perl
Summary:	PostScript-EPSF perl module
Summary(pl):	Modu� perla PostScript-EPSF
Name:		perl-PostScript-EPSF
Version:	0.01
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/PostScript/PostScript-EPSF-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/PostScript/EPSF
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/PostScript/EPSF.pm
%{perl_sitearch}/auto/PostScript/EPSF
