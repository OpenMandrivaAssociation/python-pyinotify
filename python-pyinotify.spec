%define oname pyinotify

Summary:	Python module for monitoring filesystems changes
Name:		python-%{oname}
Version:	0.9.6
Release:	2
License:	MIT
Group:		Development/Python
Url:		http://github.com/seb-m/pyinotify
Source0:	http://pypi.python.org/packages/source/p/pyinotify/%{oname}-%{version}.tar.gz
BuildArch:	noarch
Provides:	%{oname} = %{version}-%{release}
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
# pyinotify can use psyco to speed things up, unfortunaltely,
# psyco does not work under x86_64
#Suggests:	python-psyco

%description
Pyinotify is a pure Python module for monitoring filesystems changes.
Pyinotify relies on inotify, a Linux Kernel functionality (since 
kernel 2.6.13). inotify is an event-driven notification mechanism, its 
notifications are exported to user space through three system calls. 
Pyinotify binds these system calls and provides an implementation on 
top of them.

%prep
%setup -qn %{oname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

%files
%doc README* ACKS COPYING
%{py_puresitedir}/pyinotify-%{version}-*.egg-info
%{py_puresitedir}/pyinotify.py*
