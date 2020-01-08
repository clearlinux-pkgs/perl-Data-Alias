#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Alias
Version  : 1.21
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Data-Alias-1.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Data-Alias-1.21.tar.gz
Summary  : Comprehensive set of aliasing operations
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Data-Alias-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)

%description
NAME
Data::Alias - Comprehensive set of aliasing operations
DESCRIPTION
Aliasing is the phenomenon where two different expressions actually
refer to the same thing.  Modifying one will modify the other, and if
you take a reference to both, the two values are the same.

%package dev
Summary: dev components for the perl-Data-Alias package.
Group: Development
Provides: perl-Data-Alias-devel = %{version}-%{release}
Requires: perl-Data-Alias = %{version}-%{release}

%description dev
dev components for the perl-Data-Alias package.


%package perl
Summary: perl components for the perl-Data-Alias package.
Group: Default
Requires: perl-Data-Alias = %{version}-%{release}

%description perl
perl components for the perl-Data-Alias package.


%prep
%setup -q -n Data-Alias-1.21
cd %{_builddir}/Data-Alias-1.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Alias.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/Data/Alias.pm
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/auto/Data/Alias/Alias.so
