Summary:	A tool for gathering and displaying system information
Summary(de.UTF-8):	Informationen zum proc-Dateisystem
Summary(fr.UTF-8):	informations sur le système de fichiers proc
Summary(pl.UTF-8):	Informacje z filesystemu proc
Summary(tr.UTF-8):	proc dosya sistemi bilgileri
Name:		procinfo
Version:	18
Release:	3
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.cistron.nl/pub/people/svm/%{name}-%{version}.tar.gz
# Source0-md5:	27658d0a69040aca05a65b9888599d50
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-uptime.patch
Patch2:		%{name}-lsdev.patch
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The procinfo command gets system data from the /proc directory (the
kernel filesystem), formats it and displays it on standard output. You
can use procinfo to acquire information about your system from the
kernel as it is running.

%description -l de.UTF-8
Mit dem Paket procinfo können Sie nützliche Informationen aus /proc
abrufen. /proc ist das Kernel-Dateisystem, das Informationen über den
laufenden Kernel enthält.

%description -l fr.UTF-8
procinfo est un paquetage permettant d'obtenir des informations utiles
à partir de /proc. /proc est le système de fichiers du noyau. C'est
l'endroit où vous pouvez allez pour obtenir des informations sur le
noyau qui s'exécute.

%description -l pl.UTF-8
Procinfo jest programem, który przekazuje informacje wyczytane z
systemu plików jądra - /proc.

%description -l tr.UTF-8
procinfo, /proc dosya sisteminden bilgi almanıza izin veren bir
pakettir. /proc çekirdek dosya sistemini tutar ve koşan
çekirdeğinizden bilgi edinebileceğiniz bir dizin yapısı sunar.

%package perl
Summary:	procinfo perl helper scripts
Summary(pl.UTF-8):	Pomocnicze skrypty perlowe do procinfo
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description perl
Procinfo perl helper scripts.

%description perl -l pl.UTF-8
Pomocnicze skrypty perlowe do procinfo.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	LDLIBS="-lncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	prefix=%{_prefix} \
	bindir=%{_bindir} \
	mandir=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/procinfo
%{_mandir}/man8/procinfo*

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lsdev
%attr(755,root,root) %{_bindir}/socklist
%{_mandir}/man8/lsdev*
%{_mandir}/man8/socklist*
