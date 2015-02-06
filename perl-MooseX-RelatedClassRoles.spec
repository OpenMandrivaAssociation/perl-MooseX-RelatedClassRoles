%define upstream_name    MooseX-RelatedClassRoles
%define upstream_version 0.004

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Apply roles to a class related to yours
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::MOP)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildArch:	noarch

%description
Frequently, you have to use a class that provides some 'foo_class' accessor
or attribute as a method of dependency injection. Use this role when you'd
rather apply roles to make your custom 'foo_class' instead of manually
setting up a subclass.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.4.0-2mdv2011.0
+ Revision: 654259
- rebuild for updated spec-helper

* Tue Jul 27 2010 Shlomi Fish <shlomif@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 561845
- import perl-MooseX-RelatedClassRoles


* Fri Oct 09 2009 cpan2dist 0.004-1mdv
- initial mdv release, generated with cpan2dist
