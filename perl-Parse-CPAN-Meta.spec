%define module   Parse-CPAN-Meta
%define version    1.38
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Parse META.yml and other similar CPAN metadata files
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Parse/%{module}-%{version}.tar.gz
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
*Parse::CPAN::Meta* is a parser for META.yml files, based on the parser
half of the YAML::Tiny manpage.

It supports a basic subset of the full YAML specification, enough to
implement parsing of typical META.yml files, and other similarly simple
YAML files.

If you need something with more power, move up to a full YAML parser such
as the YAML manpage, the YAML::Syck manpage or the YAML::LibYAML manpage.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/Parse

