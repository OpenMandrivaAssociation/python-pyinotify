%define oname pyinotify

Summary:	Python module for monitoring filesystems changes
Name:		python-%{oname}
Version:	0.9.1
Release:	%mkrel 1
License:	MIT
Group:		Development/Python
Url:		http://github.com/seb-m/pyinotify
Source0:	http://seb.dbzteam.org/pub/pyinotify/releases/%{oname}-%{version}.tar.gz
BuildArch:	noarch
Provides:	%{oname} = %{version}-%{release}
BuildRequires:	epydoc
BuildRequires:	python-devel
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

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* ACKS COPYING
%{py_puresitedir}/*
