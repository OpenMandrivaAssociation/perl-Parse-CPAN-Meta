%define upstream_name    Parse-CPAN-Meta
%define upstream_version 1.4409

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Parse META.yml and other similar CPAN metadata files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/Parse-CPAN-Meta-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(CPAN::Meta::YAML)
BuildArch:	noarch

%description
*Parse::CPAN::Meta* is a parser for META.yml files, based on the parser
half of the YAML::Tiny manpage.

It supports a basic subset of the full YAML specification, enough to
implement parsing of typical META.yml files, and other similarly simple
YAML files.

If you need something with more power, move up to a full YAML parser such
as the YAML manpage, the YAML::Syck manpage or the YAML::LibYAML manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Parse

%changelog
* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 1.440.100-2mdv2011.0
+ Revision: 640777
- rebuild to obsolete old packages

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.440.100-1
+ Revision: 638934
- update to new version 1.4401

* Fri Feb 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.440.0-1
+ Revision: 635800
- update to new version 1.4400

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.420.0-1
+ Revision: 635444
- new version

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-2mdv2010.0
+ Revision: 420981
- rebuild

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-1mdv2010.0
+ Revision: 408838
- update to 1.40

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.390.0-1mdv2010.0
+ Revision: 404284
- rebuild using %%perl_convert_version

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.39-1mdv2010.0
+ Revision: 378236
- update to new version 1.39

* Sun May 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.38-1mdv2010.0
+ Revision: 376728
- update to new version 1.38

* Thu Mar 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.1
+ Revision: 354172
- update to new version 0.05

* Fri Feb 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.1
+ Revision: 343257
- import perl-Parse-CPAN-Meta


* Fri Feb 20 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist



