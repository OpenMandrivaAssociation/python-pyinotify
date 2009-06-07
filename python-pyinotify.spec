%define oname pyinotify

Summary:	Python module for monitoring filesystems changes
Name:		python-%{oname}
Version:	0.8.6
Release:	%mkrel 2
License:	GPLv2+
Group:		Development/Python
Url:		http://pyinotify.sourceforge.net/
Source0:	http://seb.dbzteam.org/pub/pyinotify/releases/%{oname}-%{version}.tar.gz
# fix libc version check, picked from upstream
Patch0:		%{name}-0.8.6-fix-libc-version-check.patch
BuildArch:	noarch
Provides:	%{oname} = %{version}-%{release}
BuildRequires:	epydoc
%py_requires -d
# pyinotify can use psyco to speed things up, unfortunaltely,
# psyco does not work under x86_64
#Suggests:	python-psyco
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Pyinotify is a pure Python module for monitoring filesystems changes.
Pyinotify relies on inotify, a Linux Kernel functionality (since 
kernel 2.6.13). inotify is an event-driven notification mechanism, its 
notifications are exported to user space through three system calls. 
Pyinotify binds these system calls and provides an implementation on 
top of them.

%prep
%setup -q -n %{oname}
%patch0 -p1

%build
%{__python} setup.py build
%make doc

%install
rm -rf %{buildroot}
%{__python} setup.py install  --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog NEWS TODO
%doc docstrings
%{py_puresitedir}/*
