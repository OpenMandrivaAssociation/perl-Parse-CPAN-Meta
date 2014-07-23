%define upstream_name    Parse-CPAN-Meta
%define upstream_version 1.4414

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Parse META.yml and other similar CPAN metadata files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

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
