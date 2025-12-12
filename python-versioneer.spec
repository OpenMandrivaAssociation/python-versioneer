Name:		python-versioneer
Version:	0.29
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/v/versioneer/versioneer-%{version}.tar.gz
Summary:	Easy VCS-based management of project version strings
URL:		https://pypi.org/project/versioneer/
License:	Unlicense
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Easy VCS-based management of project version strings

%files
%{_bindir}/*
%{py_sitedir}/__pycache__/*
%{py_sitedir}/versioneer.py
%{py_sitedir}/versioneer-*.*-info
