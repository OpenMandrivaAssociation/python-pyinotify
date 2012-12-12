%define oname pyinotify

Summary:	Python module for monitoring filesystems changes
Name:		python-%{oname}
Version:	0.9.4
Release:	1
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

%description
Pyinotify is a pure Python module for monitoring filesystems changes.
Pyinotify relies on inotify, a Linux Kernel functionality (since 
kernel 2.6.13). inotify is an event-driven notification mechanism, its 
notifications are exported to user space through three system calls. 
Pyinotify binds these system calls and provides an implementation on 
top of them.

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

%files
%doc README* ACKS COPYING
%{py_puresitedir}/*


%changelog
* Tue Feb 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.3-1
+ Revision: 771611
- version update 0.9.3

* Mon Oct 17 2011 Alexandre Lissy <alissy@mandriva.com> 0.9.2-1
+ Revision: 705039
- Updating to latest 0.9.2

* Sun Oct 31 2010 Jani Välimaa <wally@mandriva.org> 0.9.1-1mdv2011.0
+ Revision: 591120
- new version 0.9.1
- fix url & license
- drop py_requires macro

* Sat Jul 10 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-1mdv2011.0
+ Revision: 550143
- update to new version 0.9.0

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.9-1mdv2010.1
+ Revision: 489190
- update to new version 0.8.9

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 0.8.9

* Sat Nov 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.8-1mdv2010.1
+ Revision: 462260
- update to new version 0.8.8

* Fri Sep 25 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.7-1mdv2010.0
+ Revision: 449203
- Update to new version 0.8.7
- Remove libc version check patch integrated upstream

* Sun Jun 07 2009 Jérôme Brenier <incubusss@mandriva.org> 0.8.6-2mdv2010.0
+ Revision: 383771
- fix libc version check

* Sun Jun 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.6-1mdv2010.0
+ Revision: 383755
- do some speac file cleaning

  + Jérôme Brenier <incubusss@mandriva.org>
    - initial package python-pyinotify
    - Created package structure for python-pyinotify.

