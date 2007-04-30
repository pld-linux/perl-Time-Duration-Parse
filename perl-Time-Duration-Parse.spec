#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Time
%define	pnam	Duration-Parse
Summary:	Time::Duration::Parse - Parse string that represents time duration
#Summary(pl.UTF-8):	
Name:		perl-Time-Duration-Parse
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Time/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	56e1c1674a5180d32927a130fd739d96
URL:		http://search.cpan.org/dist/Time-Duration-Parse/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Exporter-Lite
BuildRequires:	perl(Time::Duration)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time::Duration::Parse is a module to parse human readable duration
strings like 2 minutes and 3 seconds to seconds.

It does the opposite of duration_exact function in Time::Duration
and is roundtrip safe.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Time/Duration/*.pm
%{_mandir}/man3/*
