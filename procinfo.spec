Summary:	proc filesystem information
Summary(de):	Informationen zum proc-Dateisystem 
Summary(fr):	informations sur le système de fichiers proc
Summary(pl):	Informacje z filesystemu proc 
Summary(tr):	proc dosya sistemi bilgileri
Name:		procinfo
Version:	17
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	U¿ytki/System
URL:		ftp://sunsite.unc.edu/pub/Linux/system/status/ps
Source:		ftp.cistron.nl:/pub/people/svm/%{name}-%{version}.tar.gz
Patch:		procinfo-DESTDIR.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
procinfo is a package to allow you to get useful information
from /proc.  /proc is the kernel filesystem.  This is a place
you can go to acquire information from your running kernel.

%description -l pl
Procinfo jest programem, który przekazuje informacje wyczytane z systemu 
plików j±dra - /proc.

%description -l de
Mit dem Paket procinfo können Sie nützliche Informationen aus
/proc abrufen. /proc ist das Kernel-Dateisystem, das Informationen
über den laufenden Kernel enthält.

%description -l fr
procinfo est un paquetage permettant d'obtenir des informations
utiles à partir de /proc. /proc est le système de fichiers du noyau.
C'est l'endroit où vous pouvez allez pour obtenir des informations
sur le noyau qui s'exécute.

%description -l tr
procinfo, /proc dosya sisteminden bilgi almanýza izin veren bir pakettir.
/proc çekirdek dosya sistemini tutar ve koþan çekirdeðinizden bilgi
edinebileceðiniz bir dizin yapýsý sunar.

%prep
%setup -q
%patch -p1

%build
make \
	CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/ncurses" \
	LDLIBS="-lncurses"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_prefix},%{_bindir},%{_mandir}/man8}

make install \
	DESTDIR="$RPM_BUILD_ROOT" \
	prefix=%{_prefix} \
	bindir=%{_bindir} \
	mandir=%{_mandir}


gzip -9fn README $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%attr(755,root,root) %{_bindir}/procinfo
%attr(755,root,root) %{_bindir}/lsdev
%attr(755,root,root) %{_bindir}/socklist
%{_mandir}/man8/*

%changelog
* Sun May 16 1999 Artur Frysiak <wiget@pld.org.pl>
  [17-1]
- recompiled on new rpm

* Tue Oct 06 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [15-1d]
- translation modified for pl,
- updated to procinfo-14,
- minor modificatons of the spec file.
- added ncurses patch prepared 
  by M. Ró¿ycki <macro@ds2.pg.gda.pl>.

* Wed Jun 17 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [13-3]
- build against glibc-2.1.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- updated to version 0.11

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
