#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PerlIO
%define		pnam	eol
Summary:	PerlIO::eol -
Summary(pl):	PerlIO::eol -
Name:		perl-PerlIO-eol
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7e11fb1cc3b2a65678714877ae361823
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

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
%{perl_vendorarch}/PerlIO/eol.pm
%dir %{perl_vendorarch}/auto/PerlIO/eol
%{perl_vendorarch}/auto/PerlIO/eol/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PerlIO/eol/*.so
%{_mandir}/man3/*
