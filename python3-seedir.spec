#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Package for creating, editing, and reading folder tree diagrams
Summary(pl.UTF-8):	Pakiet do tworzenia, edycji i czytania diagramów drzew folderów
Name:		python3-seedir
Version:	0.4.2
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/seedir/
Source0:	https://files.pythonhosted.org/packages/source/s/seedir/seedir-%{version}.tar.gz
# Source0-md5:	ce5aa308ec611280521c1cffdd82e885
URL:		https://pypi.org/project/seedir/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-natsort
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python package for creating, editing, and reading folder tree
diagrams.

%description -l pl.UTF-8
Pakiet do tworzenia, edycji i czytania diagramów drzew folderów.

%package apidocs
Summary:	Documentation for Python seedir module
Summary(pl.UTF-8):	Dokumentacja modułu Pythona seedir
Group:		Documentation

%description apidocs
Documentation for Python seedir module.

%description apidocs -l pl.UTF-8
Dokumentacja modułu Pythona seedir.

%prep
%setup -q -n seedir-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} tests/tests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%attr(755,root,root) %{_bindir}/seedir
%{py3_sitescriptdir}/seedir
%{py3_sitescriptdir}/seedir-%{version}-py*.egg-info

%files apidocs
%defattr(644,root,root,755)
%doc docs/*
