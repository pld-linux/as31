#
# Conditional build:
%bcond_with	gtk	# with GTK+ interface (you probably don't want this)
#
Summary:	An Intel 8031/8051 assembler
Summary(pl):	Asembler dla procesorów Intel 8031/8051
Name:		as31
Version:	2.0
Release:	1.beta3
License:	GPL
Group:		Development/Languages
Source0:	http://www.pjrc.com/tech/8051/%{name}_beta3.tar.gz
# Source0-md5:	24e2d74747e0b3672cdb581138e50d8f
Patch0:		%{name}-nostrip.patch
URL:		http://www.pjrc.com/tech/8051/#as31_assembler
BuildRequires:	bison
%{?with_gtk:BuildRequires:	gtk+-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Intel 8031/8051 assembler.

%description -l pl
Asembler dla procesorów Intel 8031/8051.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	as31 %{?with_gtk:as31_gtk}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name}		$RPM_BUILD_ROOT%{_bindir}
%{?with_gtk:install %{name}_gtk	$RPM_BUILD_ROOT%{_bindir}}
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
