Summary:	An Intel 8031/8051 assembler
Summary(pl):	Asembler dla procesorów Intel 8031/8051
Name:		as31
Version:	2.0
Release:	1.beta3
License:	GPL
Group:		Development/Languages
Source0:	http://www.pjrc.com/tech/8051/%{name}_beta3.tar.gz
URL:		http://www.pjrc.com/tech/8051/#as31_assembler
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Intel 8031/8051 assembler.

%description -l pl
Asembler dla procesorów Intel 8031/8051.

%prep
%setup -q -n %{name}

%build
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name}		$RPM_BUILD_ROOT%{_bindir}
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*.gz
