%define upstream_name    MooseX-RelatedClassRoles
%define upstream_version 0.004

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Apply roles to a class related to yours
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::MOP)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Role::Parameterized)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Frequently, you have to use a class that provides some 'foo_class' accessor
or attribute as a method of dependency injection. Use this role when you'd
rather apply roles to make your custom 'foo_class' instead of manually
setting up a subclass.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


