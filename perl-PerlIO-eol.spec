#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	PerlIO
%define		pnam	eol
Summary:	PerlIO::eol - PerlIO layer for normalizing line endings
Summary(pl.UTF-8):	PerlIO::eol - warstwa PerlIO do normalizacji końców wierszy
Name:		perl-PerlIO-eol
Version:	0.17
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/PerlIO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	da9c763968374de47a49942d35689f00
URL:		http://search.cpan.org/dist/PerlIO-eol/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PerlIO::eol Perl module normalizes any of "CR", "LF", "CRLF" and
"Native" into the designated line ending. It works for both input and
output handles.

%description -l pl.UTF-8
Moduł Perla PerlIO::eol służy do normalizacji dowolnych spośród
następujących zakończeń wierszy: "CR", "LF", "CRLF" do zadanej
postaci. Działa zarówno dla plików wejściowych, jak i dla wyjściowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/PerlIO/eol/*.so
%{_mandir}/man3/*
