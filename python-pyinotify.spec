%define oname pyinotify
%define version 0.8.6
%define release %mkrel 1

Summary: Python module for monitoring filesystems changes
Name: python-%{oname}
Version: %{version}
Release: %{release}
Source0: http://seb.dbzteam.org/pub/pyinotify/releases/%{oname}-%{version}.tar.gz
License: GPLv2+
Group: Development/Python
Url: http://trac.dbzteam.org/pyinotify
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides: %{oname} = %{version}-%{release}
BuildRequires: epydoc
%py_requires -d

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
%{__make} doc

%install
rm -rf %{buildroot}
%{__python} setup.py install  --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog COPYING NEWS TODO
%doc docstrings
%{py_puresitedir}/*


